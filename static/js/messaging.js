async function update_message_field() {
    let textarea = document.getElementById("composer");
    let submit = document.getElementById("send");
    let counter = document.getElementById("char-count");
    let text = textarea.value;


    textarea.addEventListener("input", (_) => {
        text = textarea.value
    })


    submit.addEventListener("click", (_) => {

        create_message_element(text, 'user')


        textarea.value = "";
        text = ''
        counter.innerHTML = 280;
    })
}

async function websocket_handler() {
    let ws = new WebSocket();

    ws.onmessage = function(event){}
}












function create_message_element(message, classes) {
    let parent_element = document.getElementById('messages-container');

    let div = document.createElement('div');
    let p = document.createElement('p')

    p.textContent = message

    div.appendChild(p)

    if(classes){
        div.classList.add(classes);
    }
    
    parent_element.prepend(div);
}


// add new deamon functions here
document.addEventListener("DOMContentLoaded",  (_) => {
    update_message_field();
    websocket_handler();
})


