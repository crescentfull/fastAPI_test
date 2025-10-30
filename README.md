# Realworld FastAPI로 구현하기
- FastAPI를 활용하여 Layered Architecture 로 구성


```bash
app/
 ├── api/                        # Presentation Layer (FastAPI endpoints)
 │   ├── routers/
 │   │   ├── article_router.py
 │   │   ├── user_router.py
 │   │   └── auth_router.py
 │   └── dependencies.py         # 공통 DI (Session, Service 주입 등)
 │
 ├── services/                   # Service Layer (Business Logic)
 │   ├── article_service.py
 │   ├── user_service.py
 │   └── auth_service.py
 │
 ├── repositories/               # Repository Layer (DB Access)
 │   ├── article_repository.py
 │   ├── user_repository.py
 │   └── base_repository.py
 │
 ├── models/                     # Domain Model (SQLModel / ORM Entities)
 │   ├── article.py
 │   ├── user.py
 │   └── __init__.py
 │
 ├── schemas/                    # Data Transfer Objects (DTO)
 │   ├── article.py
 │   ├── user.py
 │   ├── auth.py
 │   └── common.py
 │
 ├── db/                         # Infrastructure (DB Engine, Session)
 │   ├── base.py
 │   ├── session.py
 │   ├── init_db.py
 │   └── migrations/
 │
 ├── core/                       # Core Utilities (Config, Security, JWT)
 │   ├── config.py
 │   ├── security.py
 │   ├── jwt.py
 │   └── hashing.py
 │
 ├── tests/                      # Unit + Integration Tests
 │   ├── unit/
 │   │   ├── test_article_service.py
 │   │   ├── test_user_service.py
 │   ├── integration/
 │   │   ├── test_article_api.py
 │   │   ├── test_auth_api.py
 │   └── conftest.py
 │
 └── main.py                     # FastAPI Entry Point
```