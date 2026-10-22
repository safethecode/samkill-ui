# yoch.cc 인계·판독 실패와 실행 검사 보완

사용자 교정: 이미 있는 기준을 못 지키는 일이 계속되는데 ‘기준에 못 미친다’는 설명으로 끝내지 않는다. 실패 프로젝트로 yoch.cc를 지정했다.

## 실제 확인한 실패

- 기존 reference-brief는 CMS의 좁은 열과 넉넉한 공백만 관찰하고, design-contract에서640px/질문32px/입력48px를 chosen으로 정했다. 첫 리뷰는 원본 약460 image-px와 구현640px를 언급하면서 adapted-and-verified로 판정했다.
- 저장된 gate-report의 RUI-16/17은 pass다. 전체 게이트는 외부 인증/실기기 unknown 때문에 당시에도 UNVERIFIED였으므로 전체 PASS였다고 바꾸어 기록하지 않는다. 문제는 시각 판정 두 항목이 퇴보를 통과시킨 것이다.
- 현재 공용 CMS 페이지를 읽기 전용 브라우저1440×900/DPR1로 다시 확인했다. 제목 박스464 CSS-px, 제목24px/700, input 내용440×24px/15px였다. input 내용 박스와 외곽 필드 박스를 혼동하지 않는다. 이 관찰은 현재 페이지의 측정이며 당시 미수행 실측을 소급 보완한 증거가 아니다.
- 저장된 초기 구현의 dom-metrics는 본문640px, input 내용638×49.59375px다. 초기 public.css의 폭640px 선언도 원래 커밋1881bf5에서 보존했다. 현재 교정 브랜치의 변경은 수정하지 않았다.
- Lovable의 원본320px 썸네일과 초기 랜딩도 직접 읽었다. 원본의 색 면적/흰 입력 패널 표현이 초기 결과에서 사라졌다. 이 작은 이미지는 정확한 CSS·메인 화면 전체의 규격을 증명하지 않으며, ‘메인’과 ‘기획하기’의 화면 목적 확인이 필요한 점도 프로젝트 교정 기록에 남아 있다.

측정과 처음 결과는 [원본 DOM](source-toss-current.json), [원본1440px](source-toss-current.png), [초기 공개 폼](yoch-before-public-1440.png), [초기 랜딩](yoch-before-landing-1440.png), [당시 Lovable 자료](yoch-before-source-lovable.jpg), [파일 해시와 초기 판정](yoch-baseline.json)에 보존했다.

## 같은 입력으로 확인한 판독기 차이

RUI-16만 분리한 **진단용 카탈로그**로 원본464/초기640 CSS-px와 이전 pass 선언을 재생했다. 제품의75규칙을 줄여 통과시키는 실행이 아니며 yoch 전체의 새 게이트 결과도 아니다. 인계는 구현 후 진단으로 작성했으므로 최초 프롬프트의 충분성·독립 재현 증거로 사용하지 않는다. 허용8px 역시 이 진단의 선택값이다.

| 실행 | 결과 |
|---|---|
| [기존 판독기](diagnostic/before-result.json) | PASS/exit0. 연결된 파일과 해시는 확인했지만176px 차이를 검사하지 않음 |
| [수정 판독기](diagnostic/check-result.json) | FAIL/exit1. expected464/actual640/delta176/tolerance8을 RUI-16 실패로 판정 |
| [수치 인계 준비](diagnostic/prepare-result.json) | READY/exit0. 구현/시각 품질 승인이 아님 |
| [‘좁은 열’만 기록](diagnostic/vague-result.json) | UNVERIFIED/exit2 |
| [image-px/CSS-px 혼용](diagnostic/unit-mismatch-result.json) | UNVERIFIED/exit2 |

게이트 계약의 reference_handoff, 보고서의 reference_comparison과 실제 비교 파일을 연결했다. 원본/인계/캡처 변경, 구현 변경 뒤 비교 재사용, 관찰을 chosen으로 대체, 누락된 비교, 숫자가 같아도 regressed/unverified인 시각 판정도 회귀에 포함한다. 기존 실패나 입력을 덮어쓰지 않는다.

## 검증 범위와 한계

판독기 회귀38개를 원본·Qwen 가공본·PDP 복사본에 각각 실행해 통과했다. 기존 Qwen Node213개와 Python잠금2개, PDP 플랫폼/동시기록8개도 통과했다. Goodnotes의 동봉된 독립 prepare CLI는 유효/정성만/단위혼용 입력에서 각각 READY/UNVERIFIED/UNVERIFIED였으며 PDF를 생성하지 않았다.

측정자가 실제로 원본을 읽었는지, 영역이 정확한지, 중요 특징을 모두 골랐는지나 미관까지 도구가 자동 증명하지 않는다. 실제 시각 판독은 별도로 필요하다. 새 서비스 생성·독립 모델 실행·교정 중인 yoch 화면의 최종 승인·Goodnotes 실기기 검증은 수행하지 않았다. 이번 결과로 장기 재발이 해결됐다고 주장하지 않는다.
