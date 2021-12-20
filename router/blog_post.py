from typing import Optional
from fastapi import APIRouter, Query
from models.blog import BlogModel

router = APIRouter(
  prefix='/blog',
  tags=['blog', 'post']
)

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int=1):
  return {'message': 'blog created', 
          'id': id,
          'version': version, 
          'blog': blog
          }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, comment_id: 
                  int = Query(None, title='Id of the comment', description="Description of a comment")):
  return {
    'blog': blog,
    'id': id,
    'comment_id': comment_id
  }
