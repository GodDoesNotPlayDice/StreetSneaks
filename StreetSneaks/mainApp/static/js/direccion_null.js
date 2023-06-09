// validacion.js

document.getElementById("direccion").addEventListener("blur", function(event) {
    validarDireccion(event);
  });
  
  function validarDireccion(event) {
    event.preventDefault(); // Evitar envío del formulario por defecto
  
    var direccionInput = document.getElementById("direccion");
    var direccion = direccionInput.value.trim(); // Eliminar espacios en blanco al principio y al final
  
    var caracteresEspeciales = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
    var hayError = false; // Variable para rastrear si hay errores
  
    if (direccion === "") {
      document.getElementById("err").textContent = "Dirección vacía. Por favor, ingresa tu dirección.";
      hayError = true;
    } else if (caracteresEspeciales.test(direccion)) {
      document.getElementById("err").textContent = "Dirección inválida. No se permiten caracteres especiales.";
      hayError = true;
    } else {
      document.getElementById("err").textContent = ""; // Limpiar el mensaje de error si la dirección es válida
    }
  
    if (!hayError) {
      // Si no hay errores, permitir el envío del formulario
      document.getElementById("direccion").form.submit();
    }
  }
  