from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication
from mangum import Mangum

models.Base.metadata.create_all(engine)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ok!"}


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

handler = Mangum(app)
