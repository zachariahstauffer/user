let activeUserId = null;

function open_chat(userId){
    activeUserId = userId;
}

async function send_message_watcher() {
    let textarea = document.getElementById('composer');
    let counter = document.getElementById('char-count');
    let send = document.getElementById('send');


    textarea.addEventListener('keydown', (event) => {
        if(event.key == 'Enter' && !event.shiftKey){
            event.preventDefault();

            let text = textarea.value;

            if(!text.trim()){
                return;
            };

            create_message_element(text, 'message');

            textarea.value = '';
            counter.innerHTML = 280;
        };
    });

    send.addEventListener('click', (_) => {

        let text = textarea.value;

        create_message_element(text, "message")


        textarea.value = ''
        counter.innerHTML = 280
    });
};


function create_message_element(message, classes) {
    let parent_element = document.getElementById('messages-container');

    let div = document.createElement('div');
    let pre = document.createElement('pre')

    if (!message){
        return
    }

    pre.textContent = message



    div.appendChild(pre)

    if(classes){
        div.classList.add(classes);
    }
    
    parent_element.prepend(div);
};


document.addEventListener("DOMContentLoaded",  (_) => {
    send_message_watcher()
});


