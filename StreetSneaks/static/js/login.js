$(document).ready(function() {
    $('form').submit(function(event) {
      event.preventDefault();
      var email = $('#email').val();
      var password = $('#Contrasenna').val();
      
      if (email.length == 0) {
        $('#email_group').children('span').addClass('enable');
      } else {
        var regEx = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
        var validEmail = regEx.test(email);
        if (!validEmail) {
            $('#email_group').children('span').addClass('enable');
        } else {
            $('#email_group').children('span').removeClass('enable');
            var val_email = true
        }
      }
      if (password.length == 0) {
        $('#password_group').children('span').addClass('enable');
      } else{
        $('#password_group').children('span').removeClass('enable');
        var val_pass = true
      }
      if (val_pass && val_email) {
        this.submit();
      }
    });
  });