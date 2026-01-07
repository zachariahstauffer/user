function toggle_password() {
    var x = document.getElementById("password")

    if (x.type === "password") {

        x.type = "text"

    } else {
        x.type = "password"
    }
}

function toggle_useroptions() {
    var x = document.getElementById("options_toggles")

    if (x.style.display === 'none'){
        x.style.display = 'block'
    } else {
        x.style.display = 'none'
    }
}

function toggle_sidebar() {
    var x = document.getElementById("sidebar")
    var y = document.getElementById('toggle-sidebar-container')
    console.log('called')

    if (x.style.display === 'block') {
        console.log('first if')
        x.style.display = 'none'

    } else {
        console.log('else')
        x.style.display = 'block'

    }
    console.log('done')
    y.style.display = 'flex'
}