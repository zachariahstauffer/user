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
