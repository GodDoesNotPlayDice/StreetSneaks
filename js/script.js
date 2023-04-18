const nombre = document.getElementById('name');
const apellido = document.getElementById('appaterno');
const email = document.getElementById('email');
const propuesta = document.getElementById('propuesta');
const form = document.getElementById('form');
const warning = document.getElementById('warning');


form.addEventListener("submit", e => {
    e.preventDefault();
    let warningText = ""
    let val = false
    let regex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
    if (nombre.value.length < 5){
        warningText = `Nombre muy corto`
        val = true
    }
    if (apellido.value.length < 5){
        warningText = `Apellido muy corto`
        val = true
    }
    if (!regex.test(email.value)){
        warningText = `El email no es valido`
        val = true
    }

    if (propuesta.value.length < 500){
        warningText = `El Porque quieres trabajar con nosotros? es muy corto`
        val = true
    }
    
    if(val){
        alert(warningText)
    }
})