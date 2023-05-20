$(document).ready(function() {
    $('#register-form').submit(function(event) {
      event.preventDefault();
      var name = $('#name').val();
      var apellido = $('#apellido').val();
      var email = $('#email').val();
      var password = $('#password').val();
      var checkbox = $('#checkbox-form').val();
      
      $(".error").remove();
      
      if (name.length == 0) {
        $('#name').after('<span class="error">Este campo es obligatorio.</span>');
      }else if (name.length < 3) {
        $(".error").remove();
        $('#name').after('<span class="error">Este campo debe tener mínimo 3 caracteres.</span>');
      }else{
        var regEx = /^[a-zA-ZÀ-ÿ\s]{3,15}$/
        var validname = regEx.test(name);
        if (!validname) {
          $('#name').after('<span class="error">Ingrese un nombre válido</span>');
        }
      }

      if (apellido.length == 0) {
        $('#apellido').after('<span class="error">Este campo es obligatorio.</span>');
      }else if (apellido.length < 3) {
        $(".error").remove();
        $('#apellido').after('<span class="error">Este campo debe tener mínimo 3 caracteres.</span>');
      }else{
        var regEx = /^[a-zA-ZÀ-ÿ\s]{3,15}$/
        var validapellido = regEx.test(apellido);
        if (!validapellido) {
          $('#apellido').after('<span class="error">Ingrese un apellido válido.</span>');
        }
      }

      if (email.length == 0) {
        $('#email').after('<span class="error">Este campo es obligatorio.</span>');
      } else {
        var regEx = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
        var validEmail = regEx.test(email);
        if (!validEmail) {
          $('#email').after('<span class="error">Ingrese un Email válido.</span>');
        }
      }
      if (password.length == 0) {
        
        $('#password').after('<span class="error">Este campo es obligatorio.</span>');
      } else{
        var regEx =/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/
        var validapassword = regEx.test(password);
        if (!validapassword) {
          $('#password').after('<span class="error">Ingrese una contraseña válida.</span>');
        }
      }

      if (!$(checkbox).is(":checked"))  {
        $('#checkbox-form').after('<span class="error"> <br> debe leer y aceptar nuestros terminos y condiciones para continuar.</span>');
      }
    });
  });


