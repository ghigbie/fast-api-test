from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import base_get


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(base_get.router)


