from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
 
app = FastAPI()
app.mount('/',StaticFiles(directory='templates',html=True))


# @app.get("/")
# def main():
#     html_content = "<h2>Hello METANIT.COM!</h2>"
#     return HTMLResponse(content=html_content)