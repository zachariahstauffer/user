function getWebSocketURL(userId) {
    let protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
    let hostname = window.location.hostname
    let port = window.location.port || (window.location.protocol === 'https:' ? '443' : '80')

    let adjustedPort = port;

    if (host === 'localhost' && port === '80') {
        adjustedPort = '8000'
    } else if (host !== 'localhost' && port === '80') {
        adjustedPort = '8080'
    }

    return `${protocol}//${host}:${adjustedPort}/ws/${userID}`

}


const userID = fetch("/api/get_userID")
const socket = new WebSocket(getWebSocketURL(userID))


