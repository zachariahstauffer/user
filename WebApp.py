from fastapi import FastAPI, Form, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

import uvicorn
import argparse

from Auth import SignUpClass, LoginClass, UserClass, AdminSettingsClass, SqliteClass
from Messaging.ws import socket_endpoint


app = FastAPI()
templates = Jinja2Templates(directory=["Templates", 'Templates/auth', 'Templates/settings'])

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key="foot")

signupc = SignUpClass()
loginc = LoginClass()
adminsettings = AdminSettingsClass()
data = SqliteClass()

active_users = {}


#all @app.get function below here

@app.get("/sidebar", response_class=HTMLResponse)
def sidebar(request: Request):
    print("sidebar")
    return templates.TemplateResponse(request=request, name="Sidebar.html")

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    print("homepage")
    return templates.TemplateResponse(request=request, name="HomePage.html")

@app.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    print("sign up page")
    messages = request.session.get("messages")
    succeed = request.session.get("succeed")
    request.session.clear()
    return templates.TemplateResponse(request=request, name="SignUp.html", context={"messages": messages, "success": succeed})

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    print('login page')
    messages = request.session.get("messages")
    succeed = request.session.get("succeed")
    request.session.clear()
    return templates.TemplateResponse(request=request, name="Login.html", context={"messages": messages, "succeed": succeed})

@app.get("/usersettings", response_class=HTMLResponse)
def usersettings(request: Request):
    print('user settings page')
    username = request.session.get("username")

    return templates.TemplateResponse(request=request, name="UserSettings.html")

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    print('logged out')
    return RedirectResponse(url="/")

@app.get("/messaging", response_class=HTMLResponse)
def messaging(request: Request):
    username = request.session.get("username")
    return templates.TemplateResponse(request=request, name='Messaging.html', context={"username": username})


#all @app.post functions down here

@app.post("/signup")
def submitsignup(request: Request, username = Form(), password = Form()):

    print(f'{username} and {password}')

    messages, passed = signupc.sign_up(username, password)

    if not passed:
        for i in messages:
            print(i)
        request.session["messages"] = messages
        request.session["succeed"] = passed
        return RedirectResponse(url="/signup", status_code=303)
    
    request.session["messages"] = messages
    request.session["succeed"] = passed
    
    print(f'{username} has signed up')
    return RedirectResponse(url="/signup", status_code=303)

@app.post("/login")
def submitlogin(request: Request, username = Form(), password = Form()):

    print(f'{username} and {password}')

    messages, passed, _ = loginc.login(username, password)

    if not passed:
        request.session["messages"] = messages
        request.session["passed"] = passed
        return RedirectResponse(url="/login", status_code=303)
    
    request.session['username'] = username


    return RedirectResponse(url="/", status_code=303)

@app.post("/deleteuser")
def deleteuser(request: Request):

    username = request.session.get("username")

    id, admin, _ = data.load(username)

    user = make_user_object(request=request)

    if user is None:
        return RedirectResponse(url="/login", status_code=303)
    
    user.delete_account()

    request.session.clear()

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


@app.websocket('ws/{userID}')
async def websocket_endpoint(websocket: WebSocket, userID: int):
    try:
        await socket_endpoint(websocket=websocket, UserId=userID)

        

    except Exception as e:
        print(e)

#app js get/post requests below here

@app.get('/api/check-login')
def check_login(request: Request):
    username = request.session.get('username')

    if username:
        id, admin, _ = data.load(username)
        return JSONResponse({
            "login": True,
            "username": username,
            "admin": bool(admin)
        })
    
    return JSONResponse({'login': False})



#non @app function below here

def make_user_object(request: Request):
    username = request.session.get("username")
    id, admin, _, = data.load(username)

    if username is None or admin is None:
        return None

    user = UserClass(id, username, admin)

    return user




if __name__=='__main__':
    try:
        parser = argparse.ArgumentParser(description="web app")

        valid_true_args = ["T", 't', 'True', 'true']
        valid_false_args = ['F', 'f', 'False', 'false']

        parser.add_argument(
            '--host',
            type=str,
            help="Chose a valid host",
            default='localhost'
        )

        parser.add_argument(
            '--port',
            help="chose an available port",
            type=int,
            default=8000
        )

        parser.add_argument(
            "--reload",
            type=str,
            default="f"
        )

        parser.add_argument(
            "--workers",
            type=int,
            help="number of threads uvicorn can use"
        )


        args = parser.parse_args()

        host = args.host
        port = args.port
        reload = args.reload

        if reload in valid_true_args:
            reload = True

        elif reload in valid_false_args:
            reload = False

        else:
            reload = False



        """
            If you want to connect multiple devices
            Set host to 0.0.0.0
            set port to 8080
            Make sure you have port forwarding for 8080
            Have someone type your ip shown in network settings + : + port
            ie.: http://10.0.0.1:8080
            both devices must be on the same wifi
        """

        uvicorn.run(
            "WebApp:app",
            host=host,
            port=port,
            reload=reload,
            workers=4,
            limit_concurrency=100,
            timeout_keep_alive=5
        )

    except Exception as e:
        print(e)
