from fastapi import WebSocket, WebSocketDisconnect
import json
from .Manager import connection_mannager

cm = connection_mannager()

async def socket_endpoint(websocket: WebSocket, UserId):
    await cm.connect(UserId, websocket)
    
    try:

        while True:
            raw_data = await websocket.receive_text()
            data = json.loads(raw_data)

            to_user = data['to']
            message = data['message']

            await cm.send_to_user(message, to_user)

    except WebSocketDisconnect:
        cm.disconnect(UserId)
