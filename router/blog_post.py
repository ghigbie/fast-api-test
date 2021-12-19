from typing import Optional
from fastapi import APIRouter
from models.blog import BlogModel

router = APIRouter(
  prefix='/blog',
  tags=['blog', 'post']
)

@router.post('/new')
def create_blog(blog: BlogModel):
  return {'message': 'blog created', 
          'blog': blog}