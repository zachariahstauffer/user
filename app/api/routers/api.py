from fastapi import APIRouter


router = APIRouter(prefix='/api')



@router.get('/check-login')
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
