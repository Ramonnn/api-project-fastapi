from typing import Optional
from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

my_posts = [{"title": "favorite hobbies", "content": "I like videogames", "id": 1}, {
    "title": "favorite foods", "content": "I like pizza", "id": 2}]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_details": post}
