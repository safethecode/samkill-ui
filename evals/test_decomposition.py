import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from reference_json_fixture import binding, decomposition_fixture, write


SCRIPT = Path(os.environ.get("DESIGN_GATE_SCRIPT", str(
    Path(__file__).resolve().parents[1] / "skills/reference-review/scripts/design_gate.py"))).with_name("reference_check.py")


class DecompositionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.doc, self.interpretation = decomposition_fixture(self.root)

    def check(self, expected=0):
        write(self.root, "decomposition.json", self.doc)
        self.interpretation["decomposition_sha256"] = binding(self.root, "decomposition.json")["sha256"]
        write(self.root, "interpretation.json", self.interpretation)
        result = subprocess.run([sys.executable, str(SCRIPT), "decompose", "--root", str(self.root),
            "--decomposition", "decomposition.json", "--interpretation", "interpretation.json"], capture_output=True, text=True)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def test_valid_extensible_bundle_is_read_only(self):
        self.check()
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        self.check()
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir()})

    def test_hex_requires_explicit_srgb_and_alpha(self):
        for value in [{"hex": "white", "alpha": 1, "color_space": "srgb"},
                      {"hex": "#FFF", "alpha": 1, "color_space": "srgb"},
                      {"hex": "#FFFFFF80", "alpha": 1, "color_space": "srgb"},
                      {"hex": "#FFFFFF", "alpha": True, "color_space": "srgb"},
                      {"hex": "#FFFFFF", "alpha": 1.2, "color_space": "srgb"},
                      {"hex": "#FFFFFF", "alpha": 1, "color_space": "display-p3"}]:
            with self.subTest(value=value):
                self.doc["elements"][0]["properties"]["background"]["value"] = value
                self.check(2)

    def test_unknown_color_does_not_fabricate_hex(self):
        prop = self.doc["elements"][0]["properties"]["background"]
        prop.update(status="unknown", value=None, unknown_reason="No reliable pixel or CSS access")
        self.doc["required"].remove("O2")
        self.interpretation["coverage"][2]["status"] = "unknown"
        self.check()

    def test_gradient_stops_keep_color_and_position(self):
        prop = self.doc["elements"][0]["properties"]["background"]
        prop.update(kind="gradient", value={"type": "linear", "direction": "90deg", "stops": [
            {"position": 0, "color": {"hex": "#FFFFFF", "alpha": 1, "color_space": "srgb"}},
            {"position": 1, "color": {"hex": "#000000", "alpha": 0, "color_space": "srgb"}}]})
        self.check()
        prop["value"]["stops"][1]["color"]["hex"] = "transparent"
        self.check(2)

    def test_source_or_raw_hash_change_blocks_readiness(self):
        (self.root / "reference.svg").write_text("changed source")
        self.check(2)

    def test_raw_text_and_references_cannot_be_dropped(self):
        self.doc["raw"] = []
        self.check(2)

    def test_parent_cycle_and_dangling_relation_are_rejected(self):
        self.doc["elements"][0]["parent_id"] = "E1"
        self.check(2)
        self.doc["elements"][0]["parent_id"] = None
        self.doc["relations"] = [{"id": "L1", "kind": "align", "from": "E1", "to": "missing", "raw_refs": ["RAW1"]}]
        self.check(2)

    def test_coordinate_units_and_bounds_are_validated(self):
        prop = self.doc["elements"][0]["properties"]["width"]
        prop["unit"] = "CSS-px"
        self.check(2)
        prop.update(kind="bounds", unit="image-px", value={"x": -5, "y": 0, "width": 464, "height": 400})
        self.check()
        prop["value"]["height"] = -1
        self.check(2)

    def test_required_unknown_is_not_implementation_ready(self):
        self.doc["required"].append("O3")
        self.check(2)

    def test_missing_extension_treatment_is_rejected(self):
        self.interpretation["coverage"].pop()
        self.check(2)

    def test_custom_fields_require_treatment_and_are_preserved(self):
        self.doc["product_specific"] = {"shape": "freeform", "unstructured": [1, "raw", None]}
        self.check(2)
        self.interpretation["coverage"].append({"ref": "/product_specific", "status": "unsupported",
            "target": "report", "interpretation": "Retain the custom data; no renderer supports it yet"})
        self.check()
        self.assertEqual(json.loads((self.root / "decomposition.json").read_text())["product_specific"], self.doc["product_specific"])

    def test_non_json_numbers_cannot_hide_in_extensions(self):
        self.doc["extensions"]["custom:number"] = float("nan")
        self.check(2)

    def test_interpretation_must_cover_each_property_once(self):
        self.interpretation["coverage"].append(copy.deepcopy(self.interpretation["coverage"][0]))
        self.check(2)

    def test_export_includes_complete_json_and_external_raw_without_truncation(self):
        raw = "Raw analysis with custom geometry and original color notation.\n" * 500
        (self.root / "raw.md").write_text(raw)
        self.doc["raw"][0] = {"id": "RAW1", "artifact": binding(self.root, "raw.md")}
        self.check()
        handoff = {"schema_version": 2, "decomposition": binding(self.root, "decomposition.json"),
            "interpretation": binding(self.root, "interpretation.json"), "anchors": [{
                "id": "Q1", "observation_id": "O1", "feature": "width", "target": ".panel",
                "source": binding(self.root, "reference.svg"),
                "observed": {"value": 464, "unit": "image-px", "basis": "measured", "method": "synthetic source"},
                "expected": {"value": 464, "unit": "image-px", "tolerance": 0}}]}
        write(self.root, "handoff.json", handoff)
        result = subprocess.run([sys.executable, str(SCRIPT), "export", "--root", str(self.root),
            "--handoff", "handoff.json"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)["payload"]
        self.assertEqual(payload["decomposition"], self.doc)
        self.assertEqual(payload["raw_artifacts"][0]["text"], raw)
        self.assertEqual(payload["source_bindings"], handoff)


if __name__ == "__main__":
    unittest.main()
