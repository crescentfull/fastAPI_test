from fastapi import FastAPI
from app.api.routers import article_router, user_router, auth_router
from app.db.session import init_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}
