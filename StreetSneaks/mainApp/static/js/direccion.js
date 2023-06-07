$(document).ready(function () {
    const direccionElement = $('#direccion');
    const token = document.getElementsByName('csrfmiddlewaretoken')[0];

    direccionElement.on('blur', function (e) {
        const formData = new FormData();
        formData.append('csrfmiddlewaretoken', token.value);
        formData.append('direccion', direccionElement.val()); // Obtener el valor seleccionado

        const peticion = $.ajax({
            async: true,
            crossDomain: true,
            url: 'http://127.0.0.1:8000/venta/api/validar_direccion',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false
        });

        peticion.done(function (response) {
            console.log('done');
            console.log(direccionElement.val()); // Mostrar el valor seleccionado
        });

        peticion.fail(function (response) {
            console.log('fail');
            console.log(response);
        });
    });
});
