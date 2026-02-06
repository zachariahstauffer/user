document.addEventListener('DOMContentLoaded', function(){

    const input = document.getElementById("password")
    const length = document.getElementById("length")
    const num = document.getElementById("number")
    const lower = document.getElementById("lower")
    const upper = document.getElementById("upper")
    const special = document.getElementById("special")

    input.addEventListener('focus', function() {
        document.getElementById('password_requirements').style.display = 'block'
    })

    input.addEventListener('blur', function () {
        document.getElementById('password_requirements').style.display = 'none'
    })

    input.addEventListener('keyup', function() {
        var numbers = /[1-9]/g
        var lowerCase = /[a-z]/g
        var upperCase = /[A-Z]/g
        var specials = /[!@#$%^&]/g

        console.log(input.value, input.value.length)

        if(input.value.length >= 6) {
            length.classList.remove('invalid')
            length.classList.add('valid')
        } else {
            length.classList.remove('valid')
            length.classList.add("invalid")
        }

        if(input.value.match(numbers)){
            num.classList.remove('invalid')
            num.classList.add('valid')
        } else {
            num.classList.remove('valid')
            num.classList.add('invalid')
        }

        if(input.value.match(upperCase)){
            upper.classList.remove('invalid')
            upper.classList.add('valid')
        } else {
            upper.classList.remove('valid')
            upper.classList.add('invalid')
        }

        if(input.value.match(lowerCase)){
            lower.classList.remove('invalid')
            lower.classList.add('valid')
        } else {
            lower.classList.remove('valid')
            lower.classList.add('invalid')
        }

                if(input.value.match(specials)){
            special.classList.remove('invalid')
            special.classList.add('valid')
        } else {
            special.classList.remove('valid')
            special.classList.add('invalid')
        }
    })


    
})