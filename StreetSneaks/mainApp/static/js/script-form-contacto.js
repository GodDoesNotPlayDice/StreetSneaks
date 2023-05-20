

$(document).ready(function() {

    $('#contactanos-form').submit(function(e) {
      e.preventDefault();
      var name = $('#name').val();
      var email = $('#email').val();
      var order = $('#order').val();
      var subject = $('#subject').val();
      var mensage = $('#mensage').val();
  
      $(".error").remove();

      if (name.length == 0) {
        $('#name').after('<span class="error">Este campo es obligatorio</span>');
      }else if (name.length < 3) {
        $(".error").remove();
        $('#name').after('<span class="error">Este campo debe tener mínimo 3 caracteres</span>');
      }else{
        var regEx = /^[a-zA-ZÀ-ÿ\s]{3,15}$/
        var validname = regEx.test(name);
        if (!validname) {
          $('#name').after('<span class="error">Ingrese un nombre válido</span>');
        }
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
      }else{
        var regEx = /^.{2,100}$/
        var validsubject = regEx.test(subject);
        if (!validsubject) {
          $('#subject').after('<span class="error">Ingrese el asunto</span>');
      }}
      if (mensage.length == 0) {
        $('#mensage').after('<span class="error">El mensage es obligatorio.</span>');
      }else{
        var regEx = /^.{20,1000}$/
        var validmensage = regEx.test(mensage);
        if (!validmensage) {
          $('#mensage').after('<span class="error">Ingrese un mínimo de 50 caracteres</span>');
      }}
    });
  
  });




