# 확장 JSON·raw·해석·핵심 화면 인계

사용자는 분해 결과의 좌표·색·레이아웃 형태를 확장 가능한 JSON으로 전달하고, 규격 밖 정보와 전체 raw도 보존하도록 요청했다. 색은 가능한 HEX로 전달하고 실제 이해를 확인하는 절차까지 반영·커밋·푸시하도록 승인했다.

## 실제 변경

- [전체 분해 형식](../../../skills/reference-decompose/references/decomposition-json.md): sources/spaces/raw/elements/properties/relations/adaptations/required/extensions. 관찰 근거·미확인과 각색을 분리한다.
- [실행 가능한 합성 예제](../../../skills/reference-decompose/references/json-example/decomposition.json): 좌표·HEX/alpha·원문·unknown·제품 확장과 [받은 쪽 해석](../../../skills/reference-decompose/references/json-example/interpretation.json). 가상 SVG이며 실제 제품 재현/미관 평가가 아니다.
- [실제 export](example-export.json): JSON 전체와 원문/해석을 전달하고 외부 raw artifact도 UTF-8 전체 내용으로 포함한다. 추가 필드를 삭제하거나 원문을 자르지 않는다. 실제 생성 입력에 이 payload와 원본/에셋을 넣는 것은 작업 담당의 의무다.
- handoff/comparison v2: 전체 분해/해석 해시·관찰ID, 첫 핵심 화면의 소스 snapshot/캡처·판독, 최종 원문/확장 처리 기록을 연결한다. catalog/contract/report 버전1과75규칙은 유지했다.

## 검증

새 CLI가 없던 원본·Qwen·PDP에서 초기12개 사례를 실행해 실패3개/하위 오류14개를 확인한 뒤 구현했다. 첫 구현은12개가 통과했고 이후 export 원문 보존·비JSON숫자 거절을 더해14개가 됐다. 판독기 회귀는38→46개다.

원본46+14개, Qwen/PDP 복사본 각60개, Goodnotes 독립 helper14개가 통과했다. 기존 Qwen Node213개·Python2개, PDP 전체69개도 통과했다. macOS 임시 경로는 canonical TMPDIR로 실행했으며 테스트나 판정을 완화하지 않았다. [별도 거절 사례](diagnostics.json)는 HEX 대신 색 이름, 확장 처리 누락을 UNVERIFIED로 확인했다. [검증 기록](validation.json)에 범위를 남겼다.

최종 check의 누락/구버전/다른 분해 관찰·다른 해석·빠진 확장·핵심 미지원·없어진 핵심 화면 증거는 통과하지 않는다. 첫 핵심 화면의 실제 퇴보 선언은 FAIL이다. 숫자·해시·상태 문자열을 검사하는 범위와 실제 판독을 구별한다.

## 한계

새 모델 추론·서비스 UI·상품 전체·Goodnotes PDF/기기 검증은 수행하지 않았다. 해석 문장의 정확성이나 관찰자의 진실성, 올바른 영역 선택, 미관과 실제 이해를 자동 증명하지 않는다. 구조 통과만으로 신규 제품이나 일반적인 이해도 향상을 승인하지 않는다. 실제 핵심 화면과 전체 결과 비교가 필요하다. 기존 실패·입력·제품별 제약은 보존했다.
