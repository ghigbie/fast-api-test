from os import stat
from fastapi import FastAPI, status, Response
from typing import Optional
from enum import Enum

from starlette.responses import Response

app = FastAPI()
base = "/v1/api/"

@app.get("/")
def root():
  return {"message": "Root api route"}

# @app.get('/blog/all/')
# def get_all_blogs():
#   return {"message": "These are all blogs"}

# querey parameters 
@app.get('/blog/all', tags=['blog'], summary='Retrieve all blogs', description='This API calls simulates retrieving all blogs')
def get_all_blogs(page=1, page_size: Optional[int]=10):
  return {'message': f'All {page_size} blogs on page {page}'}

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

@app.get('/blog/type/{type}', tags=['blog'], summary='Retreives all blogs of specific type')
def get_blog_type(type: BlogType):
  return {'message': f'Blogs with type: {type}'}

@app.get('/blog/{id}/comment/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  """
  Simulates retrieving a comment of a specified blog
  """
  return {'message': f'blog: {id}, comment: {comment_id}, valid: {valid}, username: {username}'}

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'], response_description='Responds with a specific blog' )
def get_blog(id: int, response: Response):
  if id < 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f'Blog with id {id} not found. Error code {response.status_code}'}
  else:
    response.status_code = status.HTTP_200_OK
    return {"message": f'Blog with id: {id}'}
