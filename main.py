from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get('/about/{id}')
def demo(id:int, limit:int,publish:bool):
    if publish:
        return("Hello World ",id,limit, "Published")
    else:
        return("Hello World ",id,limit,"Unpublished")


class demo1(BaseModel):
    Name:str
    add:str
    phno:int

@app.post('/post')
def post_demo(demo:demo1):
    return({'data':(f'The name is {demo.Name} and The add is {demo.add} and phone number is {demo.phno}')})


if __name__ == "__main__":
    uvicorn.run(app,host= "127.0.0.1", port=8000)

