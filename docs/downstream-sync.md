# 종속 프로젝트 동기화

사용자 요구(2026-10-21): samkill-ui 변경이 이를 호출하거나 참고한 세 프로젝트에 영향을 주면 해당 부분도 수정한다. 원본만 커밋하고 후속 프로젝트를 놓치지 않는다.

## 관리 대상

| 프로젝트 | 확인한 관계 | 변경 시 확인할 실제 사용처 |
|---|---|---|
| [samkill-pdp-design](https://github.com/safethecode/samkill-pdp-design) | samkill-ui의 PDP 라우팅, 분해/검수 스킬 복사본, PDP 전용 제작 절차 | `skills/pdp-design/`, `skills/reference-decompose/`, `skills/reference-review/`, README·DESIGN, 별도 개인 pdp-design 설치본 |
| [qwen3.6-35b-a3b-coding-samkill-ui](https://github.com/safethecode/qwen3.6-35b-a3b-coding-samkill-ui) | 8개 공통 스킬을 guide.md로 가공한 스냅샷과 로컬 Qwen 실행 계약 | `skills/qwen-samkill-ui/`, `scripts/skill-context.mjs`의 실제 전달 경로, AGENTS·UPSTREAM·출처 해시, 설치기 소비 경로 |
| [samkill-goodnotes-diary](https://github.com/safethecode/samkill-goodnotes-diary) | reference-decompose 사용 기록과 자체 PDF 조사·분해·제작·검수에 반영한 원칙 | `skills/samkill-goodnotes-design/`의 해당 본문/참고 기준, DESIGN·README·맥락 기록 |

프로젝트는 각각 별도 저장소다. 개인 설치본과 저장소 원본, 과거 실험 산출물을 구별한다. 찾을 수 없는 프로젝트는 접근 가능 여부를 확인하고 남은 일로 기록한다. 수정 권한을 푸시·배포·새 설치 권한으로 확대하지 않는다.

## 변경 시 수행

1. 원본의 변경 경로·이전/현재 커밋과 변경 의미를 확인한다. 각 대상의 AGENTS·DESIGN·관련 맥락, Git 상태와 해당 사용처를 읽는다.
2. 직접 호출, 복사, 변환, 원칙만 반영한 관계를 실제 파일로 대조한다. 변경에 영향받는 진입점·필수 참고 기준·활성 프롬프트를 수정한다. 원칙 반영은 제품별 단계에 대응하고 모든 스킬의 일괄 복사로 바꾸지 않는다.
3. 기존 사용자 요구·제품별 예외와 과거 실패를 보존한다. 과거 출력이나 고정 해시·설치 영수증을 조용히 덮어쓰지 않는다. 이번에 새 설치/릴리스하지 않은 복사본은 자동 최신화됐다고 하지 않는다.
4. 문서·링크·메타데이터와 실제 전달 경로를 검사한다. 코드·판독기 변경 시 해당 프로젝트 검사를 실행한다. 문서 검사로 제품 렌더·행동·실기기 게이트를 통과시키지 않는다.
5. 원본 버전, 실제 수정 경로, 대상 커밋, 설치본 대조, 검증·미실행과 후속 작업을 기록한다. 목적별 커밋에서 기존 무관한 변경을 제외하고 현재 승인 범위로만 원격에 반영한다.

## 2026-10-21 실행 순서 반영

원본 기준 커밋은 `ad3f8110df2522d72150831e99429744861ce8a5`다. `uibowl-research → reference-decompose → reference-to-ui → reference-review` 순서, 단계별 기존 자료 재사용, 검색만·국소 수정·접근 실패의 범위를 다뤘다.

- PDP: 실제 전용 진입점과 Gen 인계에 원본 확인 → 분해 → 콘셉트/Gen → 렌더 비교를 반영했다. 상품 조사에 UIbowl을 강제하지 않았다. 이번에 변경한 원본3개 파일은 PDP 복사본에 없으므로 전체 스킬 묶음을 추가하지 않았다. 기존 분해/검수 복사본 전체가 최신이라는 인증은 아니다. 기록은 대상 `docs/upstream-sync.md`다.
- Qwen: 원본3개 파일의 기존 변환 바이트를 확인한 뒤 갱신하고 source/adapted SHA-256을 남겼다. 로컬 진입점과 모든 direct stage/컴포넌트에 실제 전달하는 `decomposed-layout.md`도 맞췄다. 기존 가이드 전달 코드·로컬 Python 잠금 방식은 보존했다. 기록은 대상 `UPSTREAM.md`, `docs/upstream-sync-20261021.md`, `evals/results/upstream-20261021/sync.json`이다.
- Goodnotes: 직접 호출/복사본은 없고 자체 조사·분해 절차가 원칙을 반영한다. 진입점에 단계별 재사용·부재 구분을 명시하고 PDF 전용 의미와 최신 빈 서식 요구를 보존했다. 기존 PDF·고정 해시·설치 릴리스를 바꾸지 않았다. 기록은 대상 `docs/context/upstream-sync-2026-10-21.md`다.

DOWNSTREAM-SYNC-01 수동 대조: 세 관계를 실제 파일에서 구별했고, upstream 버전 문서만 수정하는 데서 끝내지 않고 각 활성 진입점·공통 프롬프트의 해당 부분을 수정했다. 제품별 기존 출력은 그대로 두었다. 신규 UI/PDF 품질 실험으로 확대하지 않는다.

| 대상 | 반영 커밋 | 실행한 검증 |
|---|---|---|
| 원본 실행 순서 | `ad3f811` | 2개 스킬 형식·YAML·스테이징 로컬 링크193개·공백 검사 |
| PDP | `9a9e387` | 프로젝트/개인 설치본 스킬 형식·로컬 링크25개·공백 검사, 개인 설치8파일 전체 바이트 일치 |
| Qwen | `bf372d7` | 스킬 형식·로컬 링크63개/앵커4개·3개 원본/가공 해시·공백 검사, Node213개와 Python게이트2개 |
| Goodnotes | `32bacde` | 스킬 형식·로컬 링크56개·공백 검사, PDF/엔진/설치 릴리스 변경 없음 |

Qwen 첫 Node 검사는 macOS 임시 폴더의 symlink/realpath 표기 차이로212/213이었다. 테스트를 바꾸지 않고 `TMPDIR=/private/tmp npm test`로 전체를 재실행해213/213을 확인했다. 첫 실패와 환경별 결과는 대상 `validation.json`에 보존했다. 실제 모델 생성·새 UI/PDF 렌더·시각/행동·Goodnotes 실기기 시험은 수행하지 않았다. 개인 samkill-ui/reference-to-ui는 원본 심볼릭 링크를, PDP는 이번에 갱신한 별도 복사본을 확인했다. 다른 프로젝트의 기존 외부 설치본까지 새로 설치/갱신한 것은 아니다.

세 대상은 모두 기존 origin/main보다1커밋 앞선 로컬 상태다. 이번 작업은 푸시하지 않았다. 원본의 기존 screen-spec·Round07/11·output 및 PDP의 기존 미추적 수집 파일은 커밋에서 제외했다.

## 후속 푸시 승인과 실제 반영

사용자가 같은 날 네 저장소의 푸시를 승인했다. 위 미푸시 상태는 승인 전 이력이다. samkill-ui는 `70b70ab`, Qwen은 `bf372d7`, Goodnotes는 `32bacde`까지 원격 main 반영을 확인했다.

PDP는 원격 `da89a39`에190개 선행 커밋이 있어 첫 푸시가 거절됐다. 기존 원격 이력과 이번 `9a9e387`을 `35595f7`로 충돌 없이 병합하고 승인·검증 기록을 추가한 `8944165`를 원격 main으로 푸시했다. 두 이력이 모두 최종 결과에 포함됨을 확인했다. 통합 후 스킬 형식·audit-links(missing없음)·변경 문서 링크28개(Git tree 기준)·공백을 검증했다. 추가된 원격 스킬 보완과 제품 기록은 보존했고 실제 상품 제작이나 새 품질 승인은 수행하지 않았다.

PDP의 원래 main 작업 폴더와 미추적 파일은 그대로이며 통합 반영본은 별도 worktree의 `codex/pdp-samkill-ui-sync` 브랜치다. 후속 작업은 원래 로컬 main을 최신 원격이라고 가정하지 말고 실제 브랜치·원격·사용처를 다시 확인한다. 앞선 개인 설치8파일 검증은 당시 버전의 결과이며 최신 원격 전체 패키지의 재설치를 뜻하지 않는다. 원본의 이번 푸시 결과 기록은 별도 문서 커밋으로 반영한다.

## 2026-10-22 수치 인계·원본 비교의 실행 검사

원본 기준은 `cde9efbc116bd6a64bb27020ee27c2a9294b84d1` 위의 **미커밋 작업 변경**이다. 신규 원본 커밋이나 원격 반영으로 기록하지 않는다. [yoch 재현과 검증](../evals/results/reference-evidence-2026-10-22/README.md), [검증 기록](../evals/results/reference-evidence-2026-10-22/validation.json)에 변경과 한계를 연결한다.

| 대상 | 실제 로컬 반영 | 검증·기록 |
|---|---|---|
| Qwen (`bf372d7` 위) | 가공 가이드6개·수치 helper·prepare/최종 check, 로컬 진입점·공통 전달 프롬프트·AGENTS. 기존 Windows/sidecar 잠금 보존 | 원본 회귀38개·Node213개·Python2개. `docs/upstream-sync-20261022.md`, `evals/results/reference-evidence-20261022/sync.json`에 원본/가공 해시 |
| PDP (`8944165` 위 통합 worktree) | 전용 Gen 인계·handoff, 기존 분해/검수의 관련 문단, 수치 helper·prepare/최종 check. 제품별 내용·플랫폼/동시기록 보존 | 원본 회귀38개·플랫폼/동시기록8개·audit-links missing없음. 대상 `docs/upstream-sync.md`, `docs/session-context.md` |
| Goodnotes (`32bacde` 위) | 자체 PDF 조사/분해·품질 검수와 전용 측정 안내, 독립 prepare helper. 앱75규칙과 최종 게이트를 PDF에 강제하지 않음 | prepare 유효/정성만/단위혼용3경우. `docs/context/upstream-sync-2026-10-22.md`. PDF·설치 릴리스·고정 영수증 변경 없음 |

개인 samkill-ui/reference-review 등은 원본 심볼릭 링크다. 별도 개인 pdp-design 복사본에는 이번 진입점/handoff 문단만 반영했고 최신 원격 패키지 전체를 설치하지 않았다. 신규 Goodnotes 설치는 하지 않았다. 생성 전 prepare는 작업 절차이며 모든 모델 추론을 자동 가로채는 기능이 아니다. Qwen/PDP의 기존 최종 check는 갱신한 판독기를 사용한다.

세 대상과 원본 모두 이번 변경은 로컬 상태이며 커밋·푸시하지 않았다. 새 모델 추론·제품 렌더/행동·PDF/실기기 검증으로 확대하지 않는다. yoch의 진행 중인 교정 코드는 읽기 전용으로 확인했고 수정하지 않았다.
