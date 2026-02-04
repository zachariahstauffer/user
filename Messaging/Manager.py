

class connection_manager:
    def __init__(self):
        self.active_users: dict = {}

    async def connect(self, UserId, websocket):
        
        self.active_users[UserId] = websocket

    def disconnect(self, UserId):
        if UserId in self.active_users:
            del self.active_users[UserId]

    async def send_to_user(self, message, UserId):
        if UserId in self.active_users:
            socket = self.active_users[UserId]
            await socket.send(message)
