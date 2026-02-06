









def make_user_object(request: Request):
    username = request.session.get("username")
    id, admin, _, = data.load(username)

    if username is None or admin is None:
        return None

    user = UserClass(id, username, admin)

    return user
