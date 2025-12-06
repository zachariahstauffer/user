from fastapi import FastAPI, Form, Request
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from CoreFunctions import SignUpClass, LoginClass, UserClass, AdminSettingsClass

app = FastAPI()
templates = Jinja2Templates(directory="Templates")
signupc = SignUpClass()
loginc = LoginClass()
user = None
adminsettings = AdminSettingsClass

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse(request=request, name="HomePage.html", context={"message": "Hello from FastAPI!"})

@app.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse(request=request, name="SignUp.html", context={"content": "This is Page 1."})

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(request=request, name="Login.html")

@app.post("/signup", response_class=HTMLResponse)
def submitsignup(request: Request, username = Form(), password = Form()):

    print(f'{username} and {password}')

    val, flags = signupc.sign_up(username, password)

    if not val:
        for i in flags:
            print(i)
        return templates.TemplateResponse(request=request, name="SignUp.html")

    print(f'{username} has signed up')

    return templates.TemplateResponse(request=request, name="HomePage.html")

@app.post("/login", response_class=HTMLResponse)
def submitlogin(request: Request, username = Form(), password = Form()):

    print(f'{username} and {password}')

    message, passed, user = loginc.login(username, password)

    if not passed:
        for i in message:
            print(i)

        return templates.TemplateResponse(request=request, name="login.html")
        

    print(f'{username} has logged in')
    return templates.TemplateResponse(request=request, name='HomePage.html')



if __name__=='__main__':
    uvicorn.run("WebApp:app", host="0.0.0.0", port=8000, reload=True)