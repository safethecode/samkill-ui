# 분해 JSON의 실제 수신·재현 검증 — 2026-10-23

JSON만으로 이해가 보장되지는 않았다. 같은 핵심 수치를 전달한 텍스트·JSON 수신자가 모두 비슷한 치수를 재현했고, 둘 다 분석자가 빠뜨린 관계를 놓쳤다. 구현 전 해석 검토와 원본–첫 렌더 비교에서 실제 오류를 찾았고, 입력·해석·구현을 교정한 뒤 다시 검증했다. 이 결과로 JSON의 일반적인 성능 우월이나 생성 성공률 개선을 주장하지 않는다.

현재 판정은 **두 정적 재현 사례의 인계·교정 경로 확인**이다. Qwen 추론과 전체 제품 게이트는 미검증이다. 원본 날짜색의 낮은 대비도 아래에 보존한다.

## 방법과 고정 조건

독립 Codex 수신자 두 개를 새 대화 맥락으로 실행했다. 한 수신자는 수치·HEX·문구·관계가 포함된 prose, 다른 수신자는 같은 핵심 정보의 확장 JSON과 전체 raw를 받았다. 수신자는 자기 작업 폴더만 읽고 먼저 해석을 작성한 뒤, 별도 인계 후 HTML/CSS를 만들었다. 실제 원본 픽셀·다른 수신자 결과·네트워크 접근은 작업 지시로 제한했다. 별도 OS 보안 격리나 완전한 블라인드 실험을 주장하지 않는다.

이 실험은 **이미지를 의도적으로 감춘 전달 경로 시험**이다. 실제 스킬 워크플로에서는 원본 이미지·에셋도 함께 전달해야 한다. 새 레퍼런스 조사나 전체 분해 스킬의 독립 블라인드 평가, Qwen 실행을 대신하지 않는다. 로컬 Qwen/Ollama 실행 환경은 없었고 현재 기본 Codex 수신자를 사용했다. 표본은 형식당 한 수신자·두 사례이며 무작위 배정·반복 실험은 하지 않았다.

| 사례 | 실제 자료 | 실험의 표시 조건 |
|---|---|---|
| 폼 | 저장된 Toss 담당자 정보 영역 [원본 crop](analyst/form/source.png) | 464×501 image-px → 464×501 CSS-px, DPR1 렌더 |
| 카드 | 저장된 UIbowl Jumpit 이력서 목록 [원본 crop](analyst/cards/source.png) | 1908×568 image-px ×0.625 → 1193×355 CSS-px, DPR1 렌더 |

배율은 실험의 재구성 선택이다. 원본 CSS·서체·DPR을 복원한 값으로 부르지 않는다. 기존 DOM 근거가 있는 원래 Toss 진단과 이번 raster-only 전달 시험을 구별한다. 본래 진단은 [별도 기록](../reference-evidence-2026-10-22/README.md)에 있다.

[구현 전 계획](plan.json)과 최초 [입력 해시](input-freeze.json)를 보존했다. 구현 후 원래 치수 허용값을 넓히지 않았다. 첫 비교에서 새로 발견한 관계·색 역할·강조도 검사는 후속 교정 항목이며 최초 형식 비교의 사전 등록 항목으로 소급하지 않는다.

## 실제로 발견한 문제와 교정

1. 첫 해석에서 두 수신자 모두 폼의 22px label/28px 좌표 차이와 gap8의 모순, 작은 힌트의 새 높이, 카드1192/1193 폭과 추정 박스/동일 열의 충돌을 짚었다. 구조 검사기는 이를 READY로 처리했다. 이는 해시·형식 준비 판정이며 의미 모순의 자동 판정이 아니다. [첫 기록](v1/integrity-checks.json), [입력 교정](readback-corrections.json)을 보존했다.
2. v2 입력으로 만든 첫 화면에서는 입력칸·3열 치수와 초기 상태가 맞았다. 그러나 두 수신자 모두 필수 점을 label 위쪽보다9px 낮게 놓고, 상태 점을 label 앞에 놓았다. 분석자가 위치 관계를 쓰지 않은 탓이었다. JSON 수신자의 가져오기/추가 글자·비공개 track 색 선택도 원본과 달랐다. 전역 팔레트만 주고 요소별 역할 연결을 충분히 하지 않은 문제였다. [첫 판독](first/review.json), [첫 측정](first/measurements.json), [교정 내용](visual-corrections.json)을 보존했다.
3. v3에서 사용자 지정 `marker-layout` 속성과 요소별 HEX 역할을 추가했다. 수신자 해석40/48항목을 다시 묶고 실제 export를 전달했다. 원본과 재비교하며 가져오기 버튼의 강조도도500으로 평평해진 것을 확인했다. [v3 판독](v3/review.json)을 보존하고, v4는 그 버튼만16px/700으로 재구성했다. 원본의 정확한 font-weight를 알아냈다는 뜻은 아니다. [강조 교정](emphasis-correction.json).
4. 마지막 해석·export 이후 각각 필요한 CSS만 수정했다. 원본·분해·해석·HTML·캡처·처리 기록을 연결해 재검증했다. 분석자의 자체 설명을 독립 수신자 해석이라고 부르지 않았다. [수신 기록](receipts.json), [최종 준비 검사](preflight-v4.json), [처음/최종 비교 실행](core-comparison-results.json).

[폼 전후](iteration-form.png) · [카드 전후](iteration-cards.png) · [원본/텍스트/JSON 폼](comparison-form.png) · [원본/텍스트/JSON 카드](comparison-cards.png)

## 최종 관찰

| 검사 | 텍스트 수신 | JSON/raw 수신 |
|---|---|---|
| 폼 입력칸5개 | 모두464×40px, y=70/181/267/353/439 | 동일 |
| 카드3개 | y=106.875, 높이203.125, 폭 차이<0.016px | 동일 |
| 고정한 치수 측정 | 30/30 허용값 이내 | 30/30 허용값 이내 |
| 필수 점/상태 점 관계 | 10/10 충족 | 10/10 충족 |
| 측정한 역할별 색 | 선언 HEX와 일치 | 선언 HEX와 일치 |
| 읽는 글자 | 최소14px/500, 제목·버튼의 상위 굵기 보존 | 동일 |
| 기본/390px/글자200% | 가로 넘침0, 판독한 내용의 잘림·겹침 없음 | 동일 |
| 실제 입력·키보드 | label/type/required, 입력 유지, wrapper inset focus 확인; native toggle Space/복귀 | 동일 |

[전체 측정](measurements.json)과 [브라우저 관찰](browser-observations.json)은 실제 Chrome155.0.8059.85 headless에서 얻었다. 글자200%는 각 요소의 계산된 font-size를 먼저 저장하고 두 배로 적용한 검사이며, 브라우저 줌이나 실제 모바일 기기 검사가 아니다. 정상 캡처 후 폼에 `테스트 입력`을 채웠으므로 스트레스 캡처에는 그 값과 실제 초점이 보인다.

JSON 최종 인계88항목 중86항목은 실제 처리 결과와 연결했고, 두 사례의 원본 서체 미확인은 optional `unverified`로 보존했다. [폼 해석](analyst/form/interpretation.json)·[처리/비교](analyst/form/comparison.json), [카드 해석](analyst/cards/interpretation.json)·[처리/비교](analyst/cards/comparison.json)을 볼 수 있다. export의 전체 decomposition/raw가 보존됐는지도 비교했다. 새로운 `marker-layout` 종류를 삭제하거나 기존 종류에 억지 변환하지 않았다.

원본과 결과의 시각 판독은 직접 수행했다. `reference_check.compare_reference`는 그 판독·파일 해시·폭 연결을 확인했다. 첫 화면은 실제 차이를 regressed로 기록해 실패를 유지했고, 교정본은 비교 범위 안에서 차단 항목이 없었다. 단일 HTML 해시로 실행한 독립 helper 검사이며, 전체 제품의 design_gate fingerprint/75개 활성 규칙 PASS가 아니다.

## 남은 한계와 알려진 제품 문제

원본의 날짜색#A2A2A2와 카드색#F5F5F8은 계산 대비2.346:1로 읽는 글자4.5:1 기준에 미달한다. 이번에는 원본 색 전달을 시험하므로 그대로 남겼으며 **제품 접근성 통과로 처리하지 않는다**. 원본 색을 정확히 옮겼다는 사실로 품질 문제를 면제하지 않는다.

정적 재현 범위에는 import/add/menu/help의 실제 서비스 흐름, 서버 제출, 비동기·빈/오류 상태, 실제 기기·스크린리더 음성 검증이 없다. native toggle의 상태 변경 확인은 서비스 상태와 문구 갱신까지 구현했다는 뜻이 아니다. [한계 기록](limitations.json).

첫 JSON 좁은 화면의 fullPage 캡처에 resize 직후의 오래된 타일이 반복되는 문제가 있었다. 원본 캡처를 남기고 새 페이지·긴 viewport로 재현을 확인했다. 두 animation frame 뒤 캡처하도록 고쳤고, HTML 해시가 같은 상태에서 다시 확인했다. 시각 결함을 숨긴 제품 CSS 수정으로 처리하지 않았다. [캡처 기록](capture-note.json), [처음 캡처](first/json/cards/narrow-render.png), [안정화 캡처](first/json/cards/stable-narrow-render.png).

## 검증과 재실행

판독기46개·분해14개 회귀 검사를 실제 실행해60개가 통과했다. [기록](regression-results.json). 평가 harness의 Node 문법·anti-slop 일반15규칙/정확성 lint·checkJs, Python compile도 통과했다. [코드 검사](code-validation.json). Python 검사를 anti-slop lint 통과라고 부르지 않는다. 스킬 코드·원본 계약·세 종속 프로젝트의 실행 코드는 이번 검증에서 추가 변경하지 않았다.

저장소 루트에서:

```sh
python3 -m unittest discover -s evals -p 'test_design_gate.py' -v
python3 -m unittest discover -s evals -p 'test_decomposition.py' -v
python3 evals/results/decomposition-forward-2026-10-23/verify_evidence.py evals/results/decomposition-forward-2026-10-23
python3 skills/reference-review/scripts/reference_check.py decompose --root evals/results/decomposition-forward-2026-10-23/analyst/cards --decomposition decomposition.json --interpretation interpretation.json
```

렌더 재실행은 `browser.mjs <증거 디렉터리>`에 설치된 Playwright와 Chrome이 필요하다. Playwright를 로컬에서 해석하거나 `SAMKILL_PLAYWRIGHT_MODULE`에 설치된 모듈 경로를 지정한다. 캡처를 덮어쓰므로 디렉터리 복사본에서 실행한다. `measure.py <복사본>`·`make_boards.py <복사본>`은 측정·비교판을 다시 만든다. `compare.py <저장소 루트> <복사본>`은 첫/최종 bound comparison을 재실행한다.

freeze 파일의 경로는 각 단계 작성 당시의 상대 경로다. 최초는 `v1/`, 첫 구현은 `first/`, v2/v3는 해당 보존 디렉터리에서 확인하며 별도 보존하지 않은 공통 TASK·에셋은 현재 파일의 동일 해시로 확인한다. 최종 입력·구현은 현재 `analyst/`·`text/`·`json/`에 있다. `verify_evidence.py`가 이 매핑과 고정된 허용값의 원래 계획을 검사한다. 공식 Lucide 에셋·LICENSE·[출처](icon-provenance.json)를 함께 보존했다.
