$(document).ready(function() {
  $('#editUserForm').submit(function(e) {
    e.preventDefault();
    // Obtener los valores de los campos
    var username = $('#username').val().trim();
    var lastname = $('#lastname').val().trim();
    var email = $('#email').val().trim();
    var celular = $('#celular').val().trim();

    // Validar la longitud y los símbolos especiales en cada campo
    var isValid = true;

    if (username !== '') {
      if (username.length > 20 || hasSpecialSymbols(username)) {
        Swal.fire({
          icon: 'error',
          title: 'Error de validación',
          text: 'El nombre de usuario no debe exceder los 20 caracteres y no debe contener símbolos especiales.',
        });
        isValid = false;
      }
    }

    if (lastname !== '') {
      if (lastname.length > 20 || hasSpecialSymbols(lastname)) {
        Swal.fire({
          icon: 'error',
          title: 'Error de validación',
          text: 'El apellido no debe exceder los 20 caracteres y no debe contener símbolos especiales.',
        });
        isValid = false;
      }
    }

    if (email !== '') {
      if (!isValidEmail(email)) {
        Swal.fire({
          icon: 'error',
          title: 'Error de validación',
          text: 'Por favor, ingrese un correo electrónico válido y sin símbolos especiales.',
        });
        isValid = false;
      }
    }

    if (celular !== '') {
      if (celular.length > 20 || hasSpecialSymbols(celular)) {
        Swal.fire({
          icon: 'error',
          title: 'Error de validación',
          text: 'El número de celular no debe exceder los 20 caracteres y no debe contener símbolos especiales.',
        });
        isValid = false;
      }
    }

    if (isValid) {
      Swal.fire({
        icon: 'success',
        title: 'Usuario Actualizado con éxito',
        text: 'Su usuario se ha editado con éxito.',
      });

      // Aquí puedes enviar el formulario o realizar otras acciones necesarias
      $('#editUserForm').off('submit').submit(); // Desactivar el evento submit y enviar el formulario
    }
  });

  function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  function hasSpecialSymbols(text) {
    var specialSymbolsRegex = /[!@#$%^&*(),.?":{}|<>]/;
    return specialSymbolsRegex.test(text);
  }
});
