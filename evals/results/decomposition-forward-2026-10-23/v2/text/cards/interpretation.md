# Resume-management panel interpretation

## Evidence boundary

This refreshed plan uses only TASK.md, this case's revised INPUT.md, INTERPRETATION-TASK.md, and REVISION.md. I have no original image and have not inspected source pixels. Evidence labels and raster colors are reported by the supplied handoff. Original CSS, font, and DPR remain unknown. The original readback is preserved outside this receiving workspace by the parent; this file states the corrected current plan.

## Supplied facts and relationships

- The saved panel crop is 1908 × 568 image-px. The declared comparison scale is 0.625 CSS-px per image-px, an experimental choice rather than recovered CSS. This yields 1192.5 × 355 CSS-px before viewport rounding.
- E-panel is white. E-heading (“이력서 관리”) sits at the left of a shared header region; E-import (“사람인 이력서 가져오기”) sits at its right. The import action has a white background, supplied border color, and estimated 8px CSS radius.
- E-heading's estimated bounds are (72, 72, 500, 64) image-px. E-import's estimated bounds are (1547, 59, 290, 70).
- E-grid's estimated bounds are (72, 171, 1765, 325). It contains three equal-height, equal-width columns in one row, with an estimated 29 image-px gap. The shared estimated card dimensions are 569 × 325 image-px.
- E-card1's estimated bounds are (72, 171, 569, 325). Its title is “유아이볼이력서_1차”; its three status labels are “기술스택”, “학력”, “경력/프로젝트”, each with a green dot. Its native toggle starts checked, its visibility text is “공개”, and its date is “2026.06.02 등록”.
- E-card2's estimated bounds are (670, 171, 568, 325). Its title is “유아이볼이력서_2차”; the same three status labels have red dots. Its native toggle starts unchecked, its visibility text is “비공개”, and its date is “2026.06.02 등록”. Its structure and owned padding match E-card1.
- Each resume card has title then right ellipsis in a top row, a status row whose supplied CSS top is 70px, and a footer 24 CSS-px from its bottom. Toggle, public/private text, and help icon belong together at footer left; the date belongs at footer right. Supplied toggle size is 30 × 18 CSS-px.
- E-add's estimated bounds are (1267, 171, 569, 325). It contains the exact label “새로운 이력서를 추가해보세요!” and a green 36px CSS circle containing a white supplied Plus icon. Circle and label are one vertically centered group with a 12px gap.
- Declared CSS choices include heading 32px/700, card title 20px/600, metadata 14px/500, import action 16px/500, card padding 24px, and card radius 15px. These values already use CSS units and will not be multiplied by 0.625 again.
- The analyst's revision fixes the comparison viewport at 1193 × 355 CSS-px, explicitly rounding the scaled 1192.5px width upward. It declares panel width 100%, 45px inline padding, three equal tracks, 18.125px column gaps, grid top 106.875px, and card height 203.125px. The equal-track width is (1193 − 90 − 2 × 18.125) / 3 = 355.583333 CSS-px. Original estimated one-image-pixel card differences do not override these equal-column relations.

The handoff supplies opaque sRGB raster colors, alpha 1 throughout: canvas #FFFFFF, card backgrounds #F5F5F8, green #02DD6D, red #FE5467, main text #111112, supporting text #444445, muted text #A2A2A2, and border #E2E4E3. They are composited samples, not recovered source CSS tokens.

## Concrete reconstruction choices

Use a white, margin-free, 100%-width panel and the corrected comparison viewport of 1193 × 355 CSS-px. The earlier rendering-object width of 1192 has been corrected. The 1193px target is now a supplied experimental decision, not a provisional receiver choice.

Use normal grid/flex flow, not three independently positioned cards. Apply the corrected 45px inline panel padding, the scaled equivalent of the supplied 72 image-px. At the 1193px viewport the grid's available width is 1103px. Use three equal fractional columns of 355.583333 CSS-px with the corrected 18.125px gap. Preserve the original 1103.125px scaled estimated grid width and one-image-pixel card differences as source estimates only; do not use them to perturb the now-declared equal-track assembly.

Place the header flow region at y=36.875px, the scaled import-action top. Give the heading an 8.125px local top offset within that region to place its line box at y=45px, the scaled heading top. Use heading line-height 40px. The heading then determines a header bottom of y=85px. Follow it with 21.875px of space so the card row starts at the corrected y=106.875px. The import button will be 181.25 × 43.75px and align at the header's right edge; a 1px border is a local choice. These dimensions preserve the handoff's estimated source anchors through flow and local spacing. The original small right-edge estimate difference remains in the evidence record, while the corrected symmetric 45px panel padding governs assembly.

The grid cards will be 203.125px tall, with 24px owned padding, 15px radius, and #F5F5F8 backgrounds. They end at y=310px, leaving 45px of white canvas to the crop bottom. Use Arial, Apple SD Gothic Neo, sans-serif as declared. Main headings and card titles use #111112. Import text also uses #111112. Metadata and visibility text use #444445; dates use #A2A2A2. These semantic mappings are reconstruction decisions where the handoff lists a palette without identifying every individual text run.

For each resume card:

1. Use a top flex row containing a 20px/600 title with a 28px line-height and an official EllipsisVertical asset at its right. Use a 20px icon box as a local choice; the exact source icon size is unspecified. Do not add menu content.
2. Start the status row 70px below the card's top. With 24px padding and a 28px title line, this uses an 18px local gap. Keep all three status items in one flex row in supplied order. Use 14px/500 text with a 20px line-height, a 6px colored status dot, 6px dot-to-label gap, and 16px between status items. Dot diameter and row subspacing are local choices, not observed values. These dots are supplied status geometry, not replacement icon drawings.
3. Let the remaining vertical space expand before the footer. Use a 20px footer line box ending 24px above the card bottom. The left cluster is a 30 × 18px native checkbox styled as a switch, its supplied visibility text, and the official CircleHelp asset. The date remains at the right on the same row. Local gaps are 8px between switch and visibility text and 4px before help; use a 14px help icon. Keep the two left clusters' distinct text widths without moving the dates out of their shared alignment.
4. The checked switch track will use the supplied green and its thumb white. The unchecked track will use the supplied border color and its thumb white. Exact source switch-track colors and thumb dimensions were not supplied; these are local choices. Native checked/unchecked state, keyboard focus, and label association will remain real. This specimen's visibility labels describe its supplied initial states; no JavaScript or app state model is added.
5. Remove the two internal decorative horizontal rules explicitly mentioned in the handoff. Preserve the generous footer gap through layout rather than replacing the rules with another visual separator.

E-add will share the same card surface, size, and radius. Center its 36px green circle and label as a single vertical flex group with the supplied 12px gap. Use the official Plus asset in white, with a provisionally 20px icon box. Use a 16px/500 label with a 24px line-height and #444445, because no distinct label size or role color is specified. The entire card can be a native type=button action with its supplied label; no destination or functional add flow will be invented.

Apply data-eid exactly to E-panel, E-heading, E-import, E-grid, E-card1, E-card2, and E-add. Use native buttons for import/menu/add and labelled native checkbox inputs for the switches. Help-icon accessibility text can identify its supplied role without adding visible tooltip copy. Use only the supplied local Plus.svg, EllipsisVertical.svg, and CircleHelp.svg assets, through external image references or CSS masks for the needed colors. Do not redraw these icons or inline their SVG markup.

## Intentional constraints

- Preserve all supplied titles, Korean strings, slash, underscore, date punctuation, and initial visibility states.
- Keep reading text at least 14px/500 while retaining heading and title hierarchy.
- Reconstruct only the cropped panel. Omit site header, navigation, attachment section, service title, KPI, footer, logo, and outside gray pixels. Internal gray cards remain.
- Use no decorative separator lines, including replacement borders, shadows, or pseudo-element rules between card sections. Preserve functional import-button borders and keyboard focus.
- Use no JavaScript, code comments, external URLs, inline SVG, canvas, or UI-as-image painting. Buttons are static specimen controls; no resume application behavior is claimed.
- No original-image, visual-similarity, production-readiness, or design-gate approval claim is possible from this handoff alone. No HTML has been created at this stage.

## Resolved corrections and remaining unknowns

- Viewport width is settled at 1193 CSS-px. Do not use 1192 or derive a different comparison viewport from the unrounded 1192.5 value.
- Equal columns are settled at 355.583333 CSS-px at the comparison width. Card2's original estimated 568px width and E-add's x=1267 remain source estimates; the corrected equal-grid contract governs implementation.
- Symmetric 45px inline padding is settled by the revision. The original estimated grid's right-edge difference does not require an asymmetric padding adjustment.
- Original font, CSS, DPR, exact line metrics, icon sizes, status-dot size/spacing, add-label size/color, switch off-state styling, menu behavior, import behavior, help content, and focus appearance are unknown. Local choices above do not convert these into source facts.
- No source pixels are available to verify the palette mappings, density, line wrapping, visual resemblance, or precise icon placement.
