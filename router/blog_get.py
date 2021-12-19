from fastapi import APIRouter, status, Response
from typing import Optional
from enum import Enum

router = APIRouter(
  prefix='/blog',
  tags=['blog']
)

# querey parameters 
@router.get('/all', tags=['blog'], summary='Retrieve all blogs', description='This API calls simulates retrieving all blogs')
def get_all_blogs(page=1, page_size: Optional[int]=10):
  return {'message': f'All {page_size} blogs on page {page}'}

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

@router.get('/type/{type}', tags=['blog'], summary='Retreives all blogs of specific type')
def get_blog_type(type: BlogType):
  return {'message': f'Blogs with type: {type}'}

@router.get('/{id}/comment/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  """
  Simulates retrieving a comment of a specified blog
  """
  return {'message': f'blog: {id}, comment: {comment_id}, valid: {valid}, username: {username}'}

@router.get('/{id}', status_code=status.HTTP_200_OK, tags=['blog'], response_description='Responds with a specific blog' )
def get_blog(id: int, response: Response):
  if id < 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f'Blog with id {id} not found. Error code {response.status_code}'}
  else:
    response.status_code = status.HTTP_200_OK
    return {"message": f'Blog with id: {id}'}