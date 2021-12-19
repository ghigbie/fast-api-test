from fastapi import APIRouter

router = APIRouter(
  prefix = '',
  tags = ['base']
)

@router.get('/')
def index():
  return {'message': 'Root API route'}