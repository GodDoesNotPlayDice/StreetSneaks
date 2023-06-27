$(document).ready(function() {
  $('#contactanos-form').submit(function(event) {
    event.preventDefault(); // Evita que se envíe el formulario automáticamente

    var orderValue = $('select').val();
    var subjectValue = $('#subject').val();
    var messageValue = $('#mensage').val();

    // Elimina los mensajes de error anteriores
    $('.error-message').remove();

    // Validación del campo "Número de pedido"
    if (orderValue === 'nan') {
      $('<p class="error-message" style="color: red;">Seleccione un número de pedido válido</p>').insertAfter('select');
    }

    // Validación del campo "Asunto"
    if (subjectValue === '') {
      $('<p class="error-message" style="color: red;">Ingrese el asunto</p>').insertAfter('#subject');
    }

    // Validación del campo "Mensaje"
    if (messageValue === '') {
      $('<p class="error-message" style="color: red;">Ingrese el mensaje</p>').insertAfter('#mensage');
    }

    // Validación de la longitud máxima de caracteres
    var maxLength = 1000;
    if (subjectValue.length > maxLength) {
      $('<p class="error-message" style="color: red;">El campo "Asunto" excede el límite de caracteres</p>').insertAfter('#subject');
    }
    if (messageValue.length > maxLength) {
      $('<p class="error-message" style="color: red;">El campo "Mensaje" excede el límite de caracteres</p>').insertAfter('#mensage');
    }

    // Si hay mensajes de error, detener el envío del formulario
    if ($('.error-message').length > 0) {
      return;
    }

    // Si pasa todas las validaciones, puedes enviar el formulario
    // Aquí puedes agregar tu lógica para enviar los datos del formulario
    // al servidor o realizar cualquier otra acción necesaria

    // Mostrar notificación de éxito

    // Reiniciar el formulario después del envío (opcional)
    $('#contactanos-form').unbind('submit').submit();

    Swal.fire(
      'Completado Enviado',
      'Se envió el formulario correctamente',
      'success'
    );

  });
});
