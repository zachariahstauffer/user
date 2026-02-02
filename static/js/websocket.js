let host = window.location.hostname;

let port = host === "localhost" ? '8000' : "8080"

console.log(`ws://${host}:${port}`)

let socket = new WebSocket(`ws://${host}:${port}`);

socket.onmessage = (event) => {
    data = JSON.parse(event.data)


}
