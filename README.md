# FastAPI 기반 RealWorld 백엔드 API 구현 프로젝트 (개인)

---

- **기간:** 2025-11-01 ~ 현재
- **기술 스택:** Python, FastAPI, SQLModel, PyJWT, Argon2, pytest, uv
- **GitHub:** https://github.com/youngroknroll/fastAPI_test

---

## 기획 배경
단순 CRUD 구현을 넘어, **변경에 유연한 비동기 아키텍처**를 직접 설계하고 검증하고자 RealWorld API 명세를 기반으로 개발했습니다. FastAPI와 SQLModel을 통해 비동기 처리 효율을 극대화했으며, 특히 **TDD(Test-Driven Development)**를 전면 도입하여 코드의 책임 분리와 유지보수성을 실무 수준으로 끌어올리는 데 집중했습니다.

## 주요 성과 및 해결 방법
- ✔️ **계층형 아키텍처 설계:** API, Service, Repository 계층을 엄격히 분리하여 Router의 비대화를 방지하고, 비즈니스 로직만 독립적으로 테스트 가능한 구조를 확립했습니다.
- ✔️ **TDD 기반 기능 구현 및 안정성 확보:** pytest-asyncio를 활용한 Red-Green-Refactor 사이클을 준수하여, 기능 추가 시 발생할 수 있는 사이드 이펙트를 차단하고 도메인 간 정합성을 검증했습니다.
- ✔️ **SQLModel을 통한 데이터 모델링 최적화:** Pydantic과 SQLAlchemy의 장점을 결합한 SQLModel을 도입하여 데이터 정의 중복을 제거하고, 정적 타입 검사를 통해 런타임 에러를 최소화했습니다.
- ✔️ **비동기 N+1 문제 해결:** Repository 계층에서 selectinload 전략을 통한 Eager Loading을 적용하여 관계 데이터 조회 시 발생하는 쿼리 폭증 문제를 해결하고 응답 지연 시간을 단축했습니다.

## 결과와 배운 점
기술적 화려함보다 중요한 것은 *'예측 가능한 시스템'* 을 구축하는 것임을 깨달았습니다. TDD를 통해 확보한 테스트 커버리지가 리팩토링의 심리적 안전 장치가 되어주었으며, 이는 결과적으로 더 과감한 성능 개선과 코드 간결화로 이어졌습니다. 앞으로도 무분별한 기술 도입보다는 문제의 본질을 파악하고 최적의 추상화 수준을 결정하는 실용주의적 개발자로 성장하겠습니다.

---

## Quick Start (uv 기반)
```bash
# 의존성 설치
uv sync

# 테스트 실행
uv run pytest

# 서버 실행
uv run uvicorn app.main:app --reload
