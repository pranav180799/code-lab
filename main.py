
from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def home():
#     return {"Hello": "World"}
#
# @app.get("/about")
# def about():
#     data= {
#         "name":"Pranav",
#         "Age":25,
#         "hobby":"riding"
#     }
#     return data

@app.get("/blog/{user_name}")
def page(user_name: str):
    return {"page":"blog_page","user_name":user_name}
