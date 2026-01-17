// Grabbing the sidebar
async function set_sidebar() {
    try {
        const sidebar_url = '/sidebar';
        const response = await fetch(sidebar_url);

        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }

        const html = await response.text();
        // Got the html data, assign it
        document.getElementById('sidebar').innerHTML = html;
    } catch (err) {
        alert('Fetch failed: ' + err.message);
        console.error(err);
        return undefined;
    }
}

async function sidebar_functions() {
    await set_sidebar();

    // Functionality goes here
    let sidebar_toggle = document.getElementById('toggle-sidebar-container');
    let sidebar = document.getElementById('sidebar');

    let dropdown = document.getElementById('dropdown-btn-container');
    let dropdown_hide = document.getElementById('sidebar-dropdown-hide')



    sidebar_toggle.addEventListener('click', (_) => {
        sidebar.classList.toggle('collapsed');
    });

    dropdown.addEventListener('click', (_) => {
        dropdown_hide.classList.toggle('collapsed');
    });
}

async function check_login_status(){
    try{

    let response = await fetch('/api/check-login')
    let data = await response.json()

    let sidebar_signup = document.getElementById('sidebar_signup')
    let sidebar_login = document.getElementById('sidebar_login')


    let sidebar_profile = document.getElementById('sidebar_profile')
    let sidebar_logout = document.getElementById('sidebar_logout')

    if (data.login){
        sidebar_signup.classList.add('hidden')
        sidebar_login.classList.add('hidden')


        sidebar_profile.classList.remove('hidden')
        sidebar_logout.classList.remove('hidden')
    } else {
        sidebar_signup.classList.remove('hidden')
        sidebar_login.classList.remove('hidden')


        sidebar_profile.classList.add('hidden')
        sidebar_logout.classList.add('hidden')


    }

    } catch (err) {
        console.error(err)
    }
}


document.addEventListener('DOMContentLoaded', (_) => {
    sidebar_functions();
    check_login_status();   
})

