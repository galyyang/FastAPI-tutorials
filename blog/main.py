from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication
from blog.core import config
from mangum import Mangum

models.Base.metadata.create_all(engine)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is our secret key", "Key": f"{config.settings.secret_key}"}


app.include_router(authentication.router, prefix=config.settings.prefix)
app.include_router(blog.router, prefix=config.settings.prefix)
app.include_router(user.router, prefix=config.settings.prefix)

handler = Mangum(app)
