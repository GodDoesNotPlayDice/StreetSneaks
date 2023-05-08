const expresiones = {
	nombre: /^[a-zA-ZÀ-ÿ\s]{5,15}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{5,15}$/,
	email: /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/,
	telefono: /^[0-9]{9}$/, // Expresion para el numero de chile de 9 digitos.
    textArea: /^.{500,1000}$/
}

const campos = {
    first_name:false,
    last_name:false,
    number:false,
    email:false,
    text:false,
}

const form = document.getElementById('form');
const inputs = document.querySelectorAll('#form input,textarea');

const first_name = document.getElementById('w_user');
const last_name = document.getElementById('w_last');
const number = document.getElementById('w_cel');
const email = document.getElementById('w_email');
const text = document.getElementById('w_text');

const n_error = document.getElementById('fn-warn')
const a_error = document.getElementById('fa-warn')
const e_error = document.getElementById('fe-warn')
const c_error = document.getElementById('fc-warn')
const p_error = document.getElementById('fp-warn')

const id_name = document.getElementById('name')
const id_apellido = document.getElementById('apellido')
const id_celular = document.getElementById('numero')
const id_email = document.getElementById('email')
const id_propuesta = document.getElementById('propuesta')


const finalWarn = document.getElementById('warning');

const validarFormulario = (e) => { // Funcion
    switch (e.target.name) {
        case 'name':
            if(expresiones.nombre.test(e.target.value)){
                id_name.classList.add('cv_enable_input_check')
                first_name.classList.remove('enable')
                id_name.classList.remove('cv_enable_input')
                campos['first_name'] = true
            } else {
                campos['first_name'] = false
                id_name.classList.remove('cv_enable_input_check')
                id_name.classList.add('cv_enable_input')
                first_name.classList.add('enable')
                if (e.target.value.length > 15)
                first_name.innerHTML = 'El nombre ingresado es muy largo.'
                else if (e.target.value.length < 5)  {
                    if (e.target.value.length == 0){
                        first_name.classList.remove('enable')
                    } else {
                        first_name.innerHTML = 'El nombre ingresado es muy corto.'
                    }

                }
                else{
                    first_name.innerHTML = 'Nombre invalido.'
                }
            }
            break;
        case 'surname':
            if(expresiones.apellido.test(e.target.value)){
                id_apellido.classList.add('cv_enable_input_check')
                last_name.classList.remove('enable')
                id_apellido.classList.remove('cv_enable_input')
                campos['last_name'] = true
            } else {
                id_apellido.classList.remove('cv_enable_input_check')
                id_apellido.classList.add('cv_enable_input')
                campos['last_name'] = false
                last_name.classList.add('enable')
                if (e.target.value.length > 15)
                last_name.innerHTML = 'El apellido ingresado es muy largo.'
                else if (e.target.value.length < 5)  {
                    if (e.target.value.length == 0){
                        last_name.classList.remove('enable')
                    } else {
                        last_name.innerHTML = 'El apellido ingresado es muy corto.'
                    }
                }
                else{
                    last_name.innerHTML = 'Apellido invalido.'
                }
            }
            break;
        case 'email':
            if(expresiones.email.test(e.target.value)){
                id_email.classList.add('cv_enable_input_check')
                email.classList.remove('enable')
                id_email.classList.remove('cv_enable_input')
                campos['email'] = true
            } else {
                id_email.classList.remove('cv_enable_input_check')
                id_email.classList.add('cv_enable_input')
                campos['email'] = false
                email.classList.add('enable')
                if (e.target.value.length > 25)
                email.innerHTML = 'El email ingresado es muy largo.'
                else if (e.target.value.length < 5)  {
                    if (e.target.value.length == 0){
                        email.classList.remove('enable')
                    } else {
                        email.innerHTML = 'El email ingresado es muy corto.'
                    }
                }
                else{
                    email.innerHTML = 'Email invalido.'
                }
            }
            break;
        case 'numero':
            if(expresiones.telefono.test(e.target.value)){
                id_celular.classList.add('cv_enable_input_check')
                id_celular.classList.remove('cv_enable_input')
                number.classList.remove('enable')
                campos['number'] = true
            } else {
                id_celular.classList.remove('cv_enable_input_check')
                id_celular.classList.add('cv_enable_input')
                campos['number'] = false
                if (e.target.value.length == 0){
                    number.classList.remove('enable')
                }else{
                    number.classList.add('enable')
                    number.innerHTML = 'Numero invalido.'
                }
            }

            break;
        case 'propuesta':
            if(expresiones.textArea.test(e.target.value)){
                text.classList.remove('enable')
                campos['text'] = true
            } else {
                campos['text'] = false
                text.classList.add('enable')
                if (e.target.value.length > 1000)
                text.innerHTML = 'El Texto ingresado es muy largo.'
                else if (e.target.value.length < 500)  {
                    if (e.target.value.length == 0){
                        text.classList.remove('enable')
                    } else {
                        text.innerHTML = `Recuerda que es minimo 500 caracteres: ${e.target.value.length}`
                    }
                }
                else{
                    text.innerHTML = 'Texto invalido.'
                }
            }
            break;
        default:
            break;
    }
};


inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario); // Ejecutar la funcion

});
form.addEventListener('submit', e => {
    e.preventDefault() // Prevengo el comportamiento por defecto del formulario
    if (campos.email === true && campos.first_name === true && campos.last_name === true && campos.number === true && campos.text === true ){
        finalWarn.classList.remove('enable');
        form.reset();
    } else {
        console.log(campos.email, campos.first_name, campos.last_name, campos.number, campos.text)
        finalWarn.classList.add('enable');
        if (campos.email === false){
            e_error.classList.add('enable');
        } else {
            e_error.classList.remove('enable');
        }
        if (campos.first_name === false) {
            n_error.classList.add('enable');
        } else {
            n_error.classList.remove('enable');
        }
        if (campos.last_name === false) {
            a_error.classList.add('enable');
        } else {
            a_error.classList.remove('enable');
        }
        if (campos.number === false) {
            c_error.classList.add('enable');
        } else {
            c_error.classList.remove('enable');
        }
        if (campos.text === false) {
            p_error.classList.add('enable')

        }
    }

});



