$(document).ready(function() {
    $('#register-form').submit(function(event) {
      event.preventDefault();
      var name = $('#name').val();
      var apellido = $('#apellido').val();
      var email = $('#email').val();
      var password1 = $('#password1').val();
      var password2 = $('#password2').val();
      var celular = $('#celular').val();
      
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
        var regEx = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
        var validEmail = regEx.test(email);
        if (!validEmail) {
          $('#email').after('<span class="error">Ingrese un Email válido.</span>');
        } else if (email.length >= 50) {
          $('#email').after('<span class="error">El Email debe tener menos de 50 caracteres.</span>');
        }
      }

      if (celular.length == 0) {
        $('#celular').after('<span class="error">Este campo es obligatorio.</span>');
      } else {
        var regEx = /^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$/;
        var validCelular = regEx.test(celular);
        if (!validCelular) {
          console.log('Error')
          $('#celular').after('<span class="error">Ingrese un número de celular válido.</span>');
        }
      }   

      if (password1.length == 0) {
        $('#password1').after('<span class="error">Este campo es obligatorio.</span>');
      } else {
        var regEx = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;
        var validPassword1 = regEx.test(password1);
        if (!validPassword1) {
          $('#password1').after('<span class="error">Ingrese una contraseña válida.</span>');
        } else if (password1 !== password2) {
          $('#password2').after('<span class="error">Las contraseñas no coinciden.</span>');
        }
      }
      if (!$('#checkbox-form').is(":checked")) {
        $('#checkbox-form').after('<span class="error"> <br> Debe leer y aceptar nuestros términos y condiciones para continuar.</span>');
      }
      if ($(".error").length === 0) {
        $('#register-form').unbind('submit').submit();
      }
    });
  });


