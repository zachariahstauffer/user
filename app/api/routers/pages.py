

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
