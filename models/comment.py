from typing import Optional
from pydantic import BaseModel

class CommentModel(BaseModel):
  title: str
  body: str
  published: Optional[bool]