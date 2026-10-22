# Contact-info section interpretation

## Evidence boundary

This plan uses only TASK.md, this case's INPUT.md, and INTERPRETATION-TASK.md. I have no original image and have not inspected source pixels. “Measured” and “estimated” below describe the handoff's evidence labels, not measurements I made. Source image coordinates do not establish original CSS or DPR.

## Supplied facts and relationships

- The saved section is 464 × 501 image-px. Its heading starts at (0, 0). The experiment declares scale 1, so the comparison viewport is 464 × 501 CSS-px.
- The canvas is white. All five fields have x=0, width 464, outer height 40, and radius 10. Their supplied field-top anchors are 70, 181, 267, 353, and 439 image-px.
- E-panel owns E-heading and five vertically ordered field groups: E-company, E-business, E-person, E-email, E-phone. Each group's label belongs above its own input. The company example and phone hint belong below their own inputs.
- E-heading contains exactly “담당자 정보를 알려주세요.” Its supplied estimated bounds are (0, 0, 464, 24).
- E-company has label “고객사명”, a required red dot, type text, and example “예) 토스페이먼츠”. Label top is 42, field top 70, hint top 114. Its supplied estimated group bounds are (0, 42, 464, 90).
- E-business has label “사업자번호”, a required red dot, and type text. Label top is 153 and field top 181. Its supplied estimated group bounds are (0, 153, 464, 68).
- E-person has label “담당자명”, a required red dot, and type text. Label top is 239 and field top 267. Its supplied estimated group bounds are (0, 239, 464, 68).
- E-email has label “e-mail”, a required red dot, and type email. Label top is 325 and field top 353. Its supplied estimated group bounds are (0, 325, 464, 68).
- E-phone has label “연락처”, no required dot, type tel, and hint “담당자 연락처 또는 회사 대표 번호를 입력해 주세요.” Label top is 411, field top 439, and hint top 483. Its supplied estimated group bounds are (0, 411, 464, 90).
- The company example precedes the second label. The second through fifth field-top anchors repeat at a pitch of 86 image-px.

The handoff supplies these opaque sRGB raster colors, each alpha 1: canvas #FFFFFF, heading #36383A, labels #515359, hints #72777D, field border #E9EBED, required dot #EF3846. These are supplied composited samples, not recovered CSS tokens.

## Concrete reconstruction choices

Use normal document flow. The section will start at the viewport origin with no body margin or section padding and will fill the available 464-px width. It will have intrinsic content height with at least the comparison crop height; the final hint will remain visible even if it extends beyond y=501.

Use the declared family Arial, Apple SD Gothic Neo, sans-serif. Heading: 16px, weight 700, line-height 24px. Labels and inputs: 15px, weight 500. Labels: 22px line-height. Hints: 14px, weight 500, line-height 20px. Input outer boxes will use border-box sizing, a 40px height, a 1px supplied border color, 10px radius, 12px inline padding, and nominal 7px block padding. Input line-height 24px makes that declared padding fit the 40px box including its borders. Fields and their parent groups will share the left edge and available width.

The following local flow values reproduce the supplied anchor sequence without absolute-positioning the groups:

1. Heading line box: y=0–24; then an 18px gap to the company label at y=42.
2. Each 22px label line box is followed by a 6px gap, placing the first field at y=70 and the later fields at the supplied anchors.
3. The company field ends at y=110; a 4px gap places its 20px example at y=114–134. A 19px group gap places the business label at y=153.
4. The business field ends at y=221; an 18px gap places the next label at y=239. The same 18px gap after the person and email fields places subsequent labels at y=325 and y=411.
5. The phone field ends at y=479; a 4px gap places its 20px hint at y=483–503. This 2px extension is allowed by the supplied helper-text adaptation. No clipping or helper-text reduction will hide it.

The 6px label-to-field gap is an explicit reconstruction resolution: the handoff also declares an estimated 8px gap, but 22px label line-height plus 8px cannot retain its specified label and field anchors, which are 28px apart. I will preserve the anchors and declared label line-height, and record the difference instead of silently presenting 6px as observed.

Use a semantic section, a heading, labelled native inputs, and helper-text associations. Apply data-eid exactly to the named source elements: E-panel, E-heading, E-company, E-business, E-person, E-email, E-phone. The first four inputs will carry required semantics; phone will not. No input values or placeholders are supplied, so they will start empty with no invented placeholder. Required dots are visual markers, not new copy; their exact size and label spacing are unspecified, so a 4px dot with a 4px inline gap is a declared local choice.

Use the supplied colors for their named roles and white input backgrounds. Input text will use #515359 as a local role assignment because no separate input-value color is supplied. Focus will remain on the actual input; the field wrapper will receive an inset shadow on focus-within, with no size or text-position change and no inner duplicate ring. A 2px inset shadow in the existing #515359 label color is a local keyboard-focus choice, not a source observation. Provide a forced-colors outline fallback on the wrapper. No focus appearance is evidenced by the handoff.

## Intentional constraints

- Keep all text and punctuation exactly as supplied, including “e-mail”, the example, and the final phone hint.
- Keep all reading text at least 14px and weight 500; the heading retains weight 700.
- Reconstruct this section only. Omit brand header, separators, extra title, footer, submit action, and decoration.
- Use no JavaScript, code comments, external URLs, inline SVG, canvas, or image-based UI painting. This case needs no icon asset.
- Use flow layout rather than five absolutely positioned fields. This is a static reconstruction experiment, with native input behavior, not a production or design-gate approval.

## Unknowns and tensions retained for review

- Original font, CSS, DPR, native input appearance, input text color, required-dot dimensions, and focus appearance are unknown.
- Estimated 8px label-to-field spacing conflicts with the supplied 22px label line-height and 28px anchor difference; the implementation choice above favors the anchors.
- Estimated 90px company/phone bounds do not contain a full adapted 20px hint beginning 72px into the group. The resulting 92px content height and final y=503 are intentional reconstruction consequences, not revised source measurements.
- The 1px border, 24px input line-height, empty initial input state, dot size/gap, and focus treatment are local implementation choices where exact source details were not supplied.
- I cannot verify source resemblance or pixel accuracy without the unavailable original image. No HTML has been created at this stage.
