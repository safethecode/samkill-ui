Reconstruct the cropped resume-management panel only, not the site header, navigation or attachment section. Source crop1908x568 image-px; render at scale0.625 into1193x355 CSS-px. Original CSS/DPR are unknown; this scale is an experimental choice. The white panel has a heading at upper left and a bordered import button at upper right. Below is one row of three equal gray panels: two resume cards and one new-resume action. Card1 has three green status dots, checked/public toggle and date; card2 has three red status dots, unchecked/private toggle and same date. Card titles end1차 and2차. Toggle/public/help belong together at bottom left, date at bottom right. The last card has a green circle plus and label centered as one group. Preserve these relations in grid/flex flow. Card backgrounds are#F5F5F8, green#02DD6D, red#FE5467, main text#111112, supporting text#444445, muted text#A2A2A2 and border#E2E4E3. Remove the source decorative horizontal rules inside the first two cards under the user rule, preserving the footer gap. Use provided official Lucide SVGs only; do not draw replacement icons. Minimum text14px/500. No extra service title, KPI, footer or brand logo. This is a static specimen with native input/toggle initial states, not a functional resume app.



Coordinate system: image-px, top-left. 1908 by 568.

Rendering decisions: {'scale': 0.625, 'viewport_width': 1192, 'viewport_height': 355, 'mapping': 'test reconstruction choice: CSS-px = image-px * scale; not recovered source CSS', 'source_image_available_to_receiver': False, 'font': 'Arial, Apple SD Gothic Neo, sans-serif', 'default_text_weight': 500, 'no_javascript': True, 'assets': ['assets/icons/Plus.svg', 'assets/icons/EllipsisVertical.svg', 'assets/icons/CircleHelp.svg']}

Element E-panel, role resume-management-panel, parent None.

Observation O1 / bounds: {'x': 0, 'y': 0, 'width': 1908, 'height': 568}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O2 / width: 1908. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O3 / layout: {'canvas': 'white', 'comparison_scale': 0.625, 'padding_inline_image_px': 72, 'font_sizes_css': {'heading': 32, 'card_title': 20, 'metadata': 14, 'import_button': 16}, 'heading_weight': 700, 'card_title_weight': 600, 'other_weight': 500, 'card_padding_css': 24, 'card_radius_css': 15, 'grid_gap_image_px': 29, 'header_to_grid': 'grid y=171image-px'}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O20 / canvas: {'hex': '#FFFFFF', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O21 / card_background: {'hex': '#F5F5F8', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O22 / green: {'hex': '#02DD6D', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O23 / red: {'hex': '#FE5467', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O24 / main_text: {'hex': '#111112', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O25 / support_text: {'hex': '#444445', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O26 / muted_text: {'hex': '#A2A2A2', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O27 / border_color: {'hex': '#E2E4E3', 'alpha': 1, 'color_space': 'srgb'}. Status measured. Repeated flat raster RGB sample; composited raster color, not recovered original CSS token

Observation O28 / original_font: None. Status unknown. Native font/CSS/DPR unknown; raster dimensions known. Role font sizes are declared reconstruction choices, not measured source CSS.

Element E-heading, role panel-heading, parent E-panel.

Observation O4 / bounds: {'x': 72, 'y': 72, 'width': 500, 'height': 64}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O5 / content: '이력서 관리'. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-import, role secondary-action, parent E-panel.

Observation O6 / bounds: {'x': 1547, 'y': 59, 'width': 290, 'height': 70}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O7 / content: '사람인 이력서 가져오기'. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O8 / layout: {'button_border': 'border color token', 'button_background': 'canvas', 'radius_css': 8}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-grid, role three-equal-columns, parent E-panel.

Observation O9 / bounds: {'x': 72, 'y': 171, 'width': 1765, 'height': 325}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O10 / layout: {'display': 'grid', 'columns': 3, 'gap_image_px': 29, 'each_width_image_px': 569, 'each_height_image_px': 325}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-card1, role public-resume-card, parent E-grid.

Observation O11 / bounds: {'x': 72, 'y': 171, 'width': 569, 'height': 325}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O12 / content: {'title': '유아이볼이력서_1차', 'status_items': ['기술스택', '학력', '경력/프로젝트'], 'status_color': 'green', 'public': True, 'public_text': '공개', 'date': '2026.06.02 등록'}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O13 / layout: {'title_row': 'title then right ellipsis', 'status_row_top_css': 70, 'footer': 'bottom row24px from bottom; toggle/public/help left, date right', 'toggle_size_css': [30, 18], 'ellipsis_asset': 'assets/icons/EllipsisVertical.svg', 'help_asset': 'assets/icons/CircleHelp.svg'}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-card2, role private-resume-card, parent E-grid.

Observation O14 / bounds: {'x': 670, 'y': 171, 'width': 568, 'height': 325}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O15 / content: {'title': '유아이볼이력서_2차', 'status_items': ['기술스택', '학력', '경력/프로젝트'], 'status_color': 'red', 'public': False, 'public_text': '비공개', 'date': '2026.06.02 등록'}. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O16 / layout: {'same_as': 'E-card1 except content and toggle state'}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Element E-add, role new-resume-action, parent E-grid.

Observation O17 / bounds: {'x': 1267, 'y': 171, 'width': 569, 'height': 325}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O18 / content: '새로운 이력서를 추가해보세요!'. Status measured. Inspect stored raster region/visible text; visual relationship inference for layout

Observation O19 / layout: {'alignment': 'centered as one vertical group', 'circle_diameter_css': 36, 'circle_fill': 'green', 'plus_asset': 'assets/icons/Plus.svg', 'plus_color': 'white', 'icon_to_label_gap_css': 12}. Status estimated. Inspect stored raster region/visible text; visual relationship inference for layout

Relation L1: E-card1 -> E-card2. Equal height, shared top edge, same owned padding; visual variants differ only by content/status.

Relation L2: E-card2 -> E-add. Three equally sized cards in one row at comparison width.

Relation L3: E-heading -> E-import. Heading left and import right share one header region, not separate sections.

Adaptation D1: ['E-card1', 'E-card2']: User prohibits decorative dividers; Remove only the two internal horizontal rules, keep footer hierarchy and gap

Adaptation D2: ['E-panel']: Default screen background is#FFFFFF; Crop outer gray page and omit external gray corner pixels; preserve gray internal cards

Implementation-critical refs: O1, O2, O3, E-panel, O4, O5, E-heading, O6, O7, O8, E-import, O9, O10, E-grid, O11, O12, O13, E-card1, O14, O15, O16, E-card2, O17, O18, O19, E-add, O20, O21, O22, O23, O24, O25, O26, O27, L1, L2, L3, D1, D2, /extensions/experiment:rendering
