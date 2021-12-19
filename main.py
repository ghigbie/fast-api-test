from fastapi import FastAPI
from enum import Enum

app = FastAPI()
base = "/v1/api/"

@app.get("/")
def root():
  return {"message": "Root api route"}

# @app.get('/blog/all/')
# def get_all_blogs():
#   return {"message": "These are all blogs"}

# querey parameters 
@app.get('/blog/all')
def get_all_blogs(page=1, page_size=10):
  return {'message': f'All {page_size} blogs on page {page}'}

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
  return {'message': f'Blog with type: {type}'}

@app.get('/blog/{id}')
def get_blog(id: int):
  return {"message": f'Blog with id: {id}'}
