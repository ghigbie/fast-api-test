from fastapi import FastAPI

app = FastAPI()
base = "/v1/api/"

@app.get("/")
def root():
  return {"message": "Root api route"}

@app.get('/blog/{id}')
def get_blog(id: int):
  return {"message": f"blog with id: {id}"}

@app.get('/blog/all/')
def get_all_blogs():
  return {"message": "These are all blogs"}