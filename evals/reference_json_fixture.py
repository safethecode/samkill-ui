import hashlib
import json


def write(root, name, value):
    (root / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def binding(root, name):
    return {"path": name, "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest()}


def decomposition_fixture(root):
    (root / "reference.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600"><rect x="168" y="80" width="464" height="400" fill="#FFFFFF"/></svg>\n')
    doc = {"schema_version": 1, "document_id": "synthetic-form", "revision": "1",
        "sources": [{"id": "R1", "kind": "image", "artifact": binding(root, "reference.svg")}],
        "spaces": [{"id": "S1", "source_id": "R1", "unit": "image-px", "width": 800, "height": 600,
                    "origin": "top-left", "dpr": None}],
        "raw": [{"id": "RAW1", "text": "Synthetic rectangle only. White panel, width464 image-px; no CSS or behavior inferred."}],
        "elements": [{"id": "E1", "parent_id": None, "role": "form-panel", "source_ids": ["R1"], "raw_refs": ["RAW1"],
            "properties": {
                "width": {"id": "O1", "kind": "length", "status": "measured", "value": 464, "unit": "image-px",
                    "space_id": "S1", "source_ids": ["R1"], "raw_refs": ["RAW1"], "method": "Synthetic SVG rectangle width"},
                "background": {"id": "O2", "kind": "color", "status": "measured",
                    "value": {"hex": "#FFFFFF", "alpha": 1, "color_space": "srgb"},
                    "source_ids": ["R1"], "raw_refs": ["RAW1"], "method": "Synthetic SVG fill attribute"},
                "flow": {"id": "O3", "kind": "layout", "status": "unknown", "value": None,
                    "unknown_reason": "Static rectangle has no original CSS flow", "source_ids": ["R1"], "raw_refs": ["RAW1"]}},
            "extensions": {"product:surface": {"description": "Synthetic optional extension"}}}],
        "relations": [], "adaptations": [], "required": ["E1", "O1", "O2"], "extensions": {}}
    write(root, "decomposition.json", doc)
    refs = ["E1", "O1", "O2", "O3", "RAW1", "/elements/0/extensions/product:surface"]
    interpretation = {"schema_version": 1, "decomposition_sha256": binding(root, "decomposition.json")["sha256"],
        "coverage": [{"ref": ref, "status": "planned" if ref != "O3" else "unknown", "target": ".panel",
            "interpretation": "Preserve the source rectangle and its white fill; choose CSS flow separately"} for ref in refs]}
    write(root, "interpretation.json", interpretation)
    return doc, interpretation
