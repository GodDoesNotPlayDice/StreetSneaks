// En el archivo validacion.js
$(document).ready(function() {
  $("#direccionForm").submit(function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Obtén el valor del campo de dirección
    var direccion = $("#direccion").val();

    // Expresión regular para verificar caracteres especiales
    var specialChars = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;

    // Verifica si la dirección está vacía o contiene caracteres especiales
    if (direccion === "" || specialChars.test(direccion)) {
      $("#err").text("La dirección es inválida.");
    } else {
      // Si la validación es exitosa, envía el formulario
      $("#direccionForm").unbind("submit").submit();
    }
  });
});
