

$(document).ready(function() {

    $('#contactanos-form').submit(function(e) {
      e.preventDefault();
      var name = $('#name').val();
      var email = $('#email').val();
      var order = $('#order').val();
      var subject = $('#subject').val();
  
      $(".error").remove();

      if (name.length < 3) {
        $('#name').after('<span class="error">Este campo es obligatorio</span>');
      }
      if (email.length < 1) {
        $('#email').after('<span class="error">este campo es obligatorio</span>');
      } else {
        var regEx = /^[A-Z0-9][A-Z0-9._%+-]{0,63}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/;
        var validEmail = regEx.test(email);
        if (!validEmail) {
          $('#email').after('<span class="error">Enter a valid email</span>');
        }
      }
      if (order.length < 6) {
        $('#order').after('<span class="error">El número de orden es de mínimo 6 caracteres.</span>');
      }
      if (subject.length < 1) {
        $('#subject').after('<span class="error">El asunto es obligatorio.</span>');
      }
    });
  
  });