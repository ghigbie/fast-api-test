from typing import Optional
from pydantic import BaseModel

class BlogModel(BaseModel):
  title: str
  content: str
  nb_comments: Optional[int]
  published: Optional[bool]