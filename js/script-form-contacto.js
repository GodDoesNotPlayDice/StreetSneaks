

$(document).ready(function() {

    $('#contactanos-form').submit(function(e) {
      e.preventDefault();
      var name = $('#name').val();
      var email = $('#email').val();
      var order = $('#order').val();
      var subject = $('#subject').val();
  
      $(".error").remove();

      if (name.length == 0) {
        $('#name').after('<span class="error">Este campo es obligatorio</span>');
      }else if (name.length < 3) {
        $(".error").remove();
        $('#name').after('<span class="error">Este campo debe tener mínimo 3 caracteres</span>');
      }
      if (email.length == 0) {
        $('#email').after('<span class="error">Este campo es obligatorio</span>');
      } else {
        var regEx = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
        var validEmail = regEx.test(email);
        if (!validEmail) {
          $('#email').after('<span class="error">Ingrese un Email válido</span>');
        }
      }
      if (order.length == 0) {
        $('#order').after('<span class="error">Este campo es obligatorio.</span>');
      }else if (order.length < 6) {
        $('#order').after('<span class="error">El número de orden es de mínimo 6 caracteres.</span>');
      }
      if (subject.length == 0) {
        $('#subject').after('<span class="error">El asunto es obligatorio.</span>');
      }
    });
  
  });