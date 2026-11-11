# Samkill 스킬 호출 이름 — 2026-11-11

사용자는 목록의 제목은 영어로 `Samkill`로 시작하고 설명은 한국어로 유지하며 `$` 호출 이름과 다른 스킬의 호출도 함께 바꾸도록 요청했다. `name`·폴더·기본 호출 프롬프트와 설치 연결을 같은 ID로 맞췄다.

| 이전 호출 | 새 호출 | 표시 제목 |
|---|---|---|
| `$samkill-ui` | `$samkill-ui` | Samkill UI |
| `$uibowl-research` | `$samkill-uibowl-research` | Samkill UIbowl Research |
| `$reference-decompose` | `$samkill-reference-decompose` | Samkill Reference Decompose |
| `$reference-to-ui` | `$samkill-reference-to-ui` | Samkill Reference to UI |
| `$reference-review` | `$samkill-reference-review` | Samkill Reference Review |
| `$design-md` | `$samkill-design-md` | Samkill Design MD |
| `$ux-copy` | `$samkill-ux-copy` | Samkill UX Copy |
| `$onboarding-flow` | `$samkill-onboarding-flow` | Samkill Onboarding |

이전 이름의 중복 설치 별칭은 남기지 않았다. 이미 열린 세션의 목록 갱신은 실제 메뉴에서 확인하지 않았으므로 새 이름이 즉시 표시된다고 단정하지 않는다.

원본 진입점·하위 스킬·템플릿·현재 기준과 Qwen의 실제 stage/component loader, PDP의 복사본/의존 경로와 전용 인계, Goodnotes의 호출, 개인 PDP 설치본 및 별도 화면설계서 스킬의 기술 참조를 갱신했다. Qwen 가공본은 `guide.md`를 유지해 별도 스킬로 중복 등록하지 않는다. PDP의 기존 제품별 본문과 의존 리소스 출처를 보존했고 전체 패키지 갱신으로 기록하지 않는다.

과거 평가·frozen manifest·입력/출력 해시는 당시 이름과 버전에 묶인 증거다. 과거 실행을 재현하려면 그 기록에 고정된 커밋을 사용한다. 현재 경로를 안내하는 문서 링크는 갱신하되 과거 해시나 결과를 새 이름의 결과로 다시 쓰지 않는다.

[검증 기록](../evals/results/samkill-skill-namespace-2026-11-11.json): 원본46+14개, Qwen213+2개, PDP69개, Goodnotes helper14개를 통과했다. 독립 검토의 활성 미해결 항목은0개다. Qwen의 lint3건·CheckJS14건은 변경 전후 동일한 실패이며 PASS가 아니다. 실제 메뉴 갱신·모델 추론·새 제품 화면/PDF 품질은 미검증이다. [종속 반영](downstream-sync.md)에 원본 버전과 반영 커밋을 연결한다.
