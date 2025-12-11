from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

import uvicorn


from CoreFunctions import SignUpClass, LoginClass, UserClass, AdminSettingsClass, DataClass

app = FastAPI()
templates = Jinja2Templates(directory="Templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="foot")


signupc = SignUpClass()
loginc = LoginClass()
adminsettings = AdminSettingsClass()
data = DataClass()


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse(request=request, name="HomePage.html", context={"message": "Login or Sign Up"})

@app.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse(request=request, name="SignUp.html", context={"content": "This is Page 1."})

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(request=request, name="Login.html")

@app.get("/usersettings", response_class=HTMLResponse)
def usersettings(request: Request):
    username = request.session.get("username")
    messages = request.session.get("messages")
    succeed = request.session.get("succeed")
    return templates.TemplateResponse(request=request, name="UserSettings.html", context={"user": username, "messages": messages, "succeed": succeed})

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")

@app.post("/signup", response_class=HTMLResponse)
def submitsignup(request: Request, username = Form(), password = Form()):

    print(f'{username} and {password}')

    messages, passed = signupc.sign_up(username, password)

    if not passed:
        for i in messages:
            print(i)
        return templates.TemplateResponse(request=request, name="SignUp.html", context={"success": passed, "messages": messages})

    print(f'{username} has signed up')
    return templates.TemplateResponse(request=request, name="SignUp.html", context={"success": passed, "messages": messages})

@app.post("/login", response_class=HTMLResponse)
def submitlogin(request: Request, username = Form(), password = Form()):

    print(f'{username} and {password}')

    messages, passed, _ = loginc.login(username, password)

    if not passed:
        return templates.TemplateResponse(request=request, name="Login.html", context={'messages': messages, "success": passed})


    request.session['username'] = username
    return RedirectResponse(url="/usersettings", status_code=303)

@app.post("/deleteuser")
def deleteuser(request: Request):

    username = request.session.get("username")

    id, admin, _ = data.load(username)



    user = make_user_object(request=request)

    if user is None:
        return RedirectResponse(url="/login", status_code=303)
    
    user.delete_account()

    return RedirectResponse(url='/', status_code=303)
    
@app.post("/change_password")
def change_password(request: Request, password = Form(), confirm = Form()):
    
    user = make_user_object(request=request)
    messages = []
    
    if user is None:
        return RedirectResponse(url="/login", status_code=303)
    
    if password == confirm:
        passed, messages = user.change_password(password)
        request.session["messages"] = messages
        request.session["succeed"] = passed
        return RedirectResponse(url='/usersettings', status_code=303)


    messages.append("Password does not match")


    request.session["messages"] = messages
    request.session["succeed"] = False
    return RedirectResponse(url='/usersettings', status_code=303)

@app.post("/promote-demote")
def promote_demote(request: Request, id = Form()):
    pass

@app.post("/wipe")
def wipe(request: Request):
    data.wipe()

def make_user_object(request: Request):
    username = request.session.get("username")
    id, admin, _,  =data.load(username)

    if username is None or admin is None:
        return None

    user = UserClass(id, username, admin)

    return user

if __name__=='__main__':
    uvicorn.run("WebApp:app", host="localhost", port=8000, reload=True)