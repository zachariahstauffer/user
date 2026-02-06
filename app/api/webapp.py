from fastapi import FastAPI, Form, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware


#all @app.post functions down here











@app.websocket('/ws/{userID}')
async def websocket_endpoint(websocket: WebSocket, userID: int):
    try:
        await socket_endpoint(websocket=websocket, UserId=userID)

        

    except Exception as e:
        print(e)

#app js get/post requests below here




#non @app function below here
