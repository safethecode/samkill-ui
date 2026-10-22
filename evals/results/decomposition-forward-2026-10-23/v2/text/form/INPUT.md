Reconstruct only the saved contact-info section, excluding the brand header and separator lines. The source crop is464x501 image-px. At test viewport464x501 use1image-px per CSS-px. The heading starts at(0,0). All five fields share the left edge and full464 width. Labels and examples are above/below their field; a required red dot follows the first four labels, not the phone. Preserve the first example and final phone hint. Field top coordinates are70,181,267,353,439; each outer field height40 and radius10. Text may slightly extend the crop after our14px hint adaptation; preserve all content instead of clipping it. Use normal vertical flow with local spacing, not five absolutely positioned fields. All new reading text is at least14px and500. No logos, divider lines, extra title, footer, submit action or decorations. Source screenshots do not reveal focus; use an inset field-wrapper focus ring while real focus remains on input.



Coordinate system: image-px, top-left. 464 by 501.

Rendering decisions: {'scale': 1, 'viewport_width': 464, 'viewport_height': 501, 'mapping': 'test reconstruction choice: CSS-px = image-px * scale; not recovered source CSS', 'source_image_available_to_receiver': False, 'font': 'Arial, Apple SD Gothic Neo, sans-serif', 'default_text_weight': 500, 'no_javascript': True, 'assets': ['assets/icons/Plus.svg', 'assets/icons/EllipsisVertical.svg', 'assets/icons/CircleHelp.svg']}

Element E-panel, role contact-info-section, parent None.

Observation O1 / bounds: {'x': 0, 'y': 0, 'width': 464, 'height': 501}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O2 / width: 464. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O3 / layout: {'flow': 'vertical', 'background_role': 'canvas', 'render_font_sizes_css': {'heading': 16, 'label': 15, 'hint': 14, 'input': 15}, 'heading_weight': 700, 'other_weight': 500, 'heading_line_height': 24, 'label_line_height': 22, 'hint_line_height': 20, 'field_outer_height': 40, 'field_inner_padding': {'block': 7, 'inline': 12}, 'field_radius': 10, 'label_to_field_gap': 6, 'field_to_hint_gap': 4}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O21 / canvas: {'hex': '#FFFFFF', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O22 / heading_color: {'hex': '#36383A', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O23 / label_color: {'hex': '#515359', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O24 / hint_color: {'hex': '#72777D', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O25 / field_border: {'hex': '#E9EBED', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O26 / required_dot: {'hex': '#EF3846', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O27 / original_font: None. Status unknown. Font family and source hint CSS are not established; use shared system family and14px/500 minimum.

Element E-heading, role section-heading, parent E-panel.

Observation O4 / bounds: {'x': 0, 'y': 0, 'width': 464, 'height': 24}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O5 / content: '담당자 정보를 알려주세요.'. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-company, role label-field-and-example, parent E-panel.

Observation O6 / bounds: {'x': 0, 'y': 42, 'width': 464, 'height': 90}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O7 / content: {'label': '고객사명', 'required': True, 'hint': '예) 토스페이먼츠', 'input_type': 'text'}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O8 / layout: {'label_top': 42, 'field_top': 70, 'hint_top': 114, 'label_width': 'auto', 'input_full_width': True}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-business, role label-and-field, parent E-panel.

Observation O9 / bounds: {'x': 0, 'y': 153, 'width': 464, 'height': 68}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O10 / content: {'label': '사업자번호', 'required': True, 'input_type': 'text'}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O11 / layout: {'label_top': 153, 'field_top': 181}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-person, role label-and-field, parent E-panel.

Observation O12 / bounds: {'x': 0, 'y': 239, 'width': 464, 'height': 68}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O13 / content: {'label': '담당자명', 'required': True, 'input_type': 'text'}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O14 / layout: {'label_top': 239, 'field_top': 267}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-email, role label-and-field, parent E-panel.

Observation O15 / bounds: {'x': 0, 'y': 325, 'width': 464, 'height': 68}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O16 / content: {'label': 'e-mail', 'required': True, 'input_type': 'email'}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O17 / layout: {'label_top': 325, 'field_top': 353}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-phone, role label-field-and-hint, parent E-panel.

Observation O18 / bounds: {'x': 0, 'y': 411, 'width': 464, 'height': 90}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O19 / content: {'label': '연락처', 'required': False, 'hint': '담당자 연락처 또는 회사 대표 번호를 입력해 주세요.', 'input_type': 'tel'}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O20 / layout: {'label_top': 411, 'field_top': 439, 'hint_top': 483}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Relation L1: E-company -> E-phone. All outer fields share full464 width and x=0; hints belong to their field, not the following field.

Relation L2: E-company -> E-business. Example hint comes before the second label; second-to-fifth field pitch86image-px.

Adaptation D1: ['E-company', 'E-phone']: User text minimum14px/500; Raise small helper text for this experiment; keep geometry and content as close as possible

Implementation-critical refs: O1, O2, O3, E-panel, O4, O5, E-heading, O6, O7, O8, E-company, O9, O10, O11, E-business, O12, O13, O14, E-person, O15, O16, O17, E-email, O18, O19, O20, E-phone, O21, O22, O23, O24, O25, O26, L1, L2, D1, /extensions/experiment:rendering


Analyst correction after independent readback: use a 6 CSS-px gap after the 22px label line box to preserve the observed field-top anchors (70,181,267,353,439). The earlier 8px gap was inconsistent. This 6px flow resolution is a reconstruction decision. Original estimated company/phone group bounds stay90 image-px; the declared14px helper adaptation makes final content height92px and final content end503px. Preserve the full hints rather than clipping. Do not claim90px contains the adapted92px content.
