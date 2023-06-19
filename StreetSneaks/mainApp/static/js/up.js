$(document).ready(function() {
    // Función de validación del formulario
    $("form").submit(function(event) {
      // Obtener los valores de los campos de nombre y precio
      var name = $("#name").val().trim();
      var precio = $("#precio").val().trim();
      
      // Reiniciar los mensajes de error
      $("#name-error").text("");
      $("#precio-error").text("");
      
      // Validar el campo de nombre
      if (name === "") {
        $("#name-error").text("El nombre no puede estar vacío");
        event.preventDefault(); // Prevenir el envío del formulario
      } else if (/[^a-zA-Z0-9\s]/.test(name)) {
        $("#name-error").text("El nombre no puede contener caracteres especiales");
        event.preventDefault(); // Prevenir el envío del formulario
      }
      
      // Validar el campo de precio
      if (precio === "") {
        $("#precio-error").text("El precio no puede estar vacío");
        event.preventDefault(); // Prevenir el envío del formulario
      } else if (isNaN(precio)) {
        $("#precio-error").text("El precio debe ser un número válido");
        event.preventDefault(); // Prevenir el envío del formulario
      }
    });
  });