

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
