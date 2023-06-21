$(".btn-pagar").click(function (event) {
    var direccionSeleccionada = $("#direccion").val();
    if (direccionSeleccionada !== "nan") {
       console.log("no valido")
    } else {
        event.preventDefault();
        Swal.fire(
            'Error',
            'Debes seleccionar una dirección válida',
            'error'
        );
    }
});
