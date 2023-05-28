$(document).ready(function() {
  $('form').submit(function(event) {
    event.preventDefault();
    var usuario = $('#usuario').val();
    var password = $('#Contrasenna').val();
    
    if (usuario.length == 0) {
      $('#usuario_group').children('span').addClass('enable');
    } else {
      var regEx = /^[a-zA-Z0-9_]+$/;
      var validUsuario = regEx.test(usuario);
      if (!validUsuario) {
          $('#usuario_group').children('span').addClass('enable');
      } else {
          $('#usuario_group').children('span').removeClass('enable');
          var val_usuario = true;
      }
    }
    if (password.length == 0) {
      $('#password_group').children('span').addClass('enable');
    } else {
      $('#password_group').children('span').removeClass('enable');
      var val_pass = true;
    }
    if (val_pass && val_usuario) {
      this.submit();
    }
  });
});
