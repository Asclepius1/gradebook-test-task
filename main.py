from fastapi import FastAPI

from api.v1.endpoints import api_router
from db.base import engine
from db.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gradebook")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)


