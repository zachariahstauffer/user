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

    sidebar_toggle.addEventListener('click', (_) => {
        sidebar.classList.toggle('collapsed');
    });
}

sidebar_functions();