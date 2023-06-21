$(document).ready(function() {
    $('#nro-credit').on('input', function() {
      validateCardNumber();
    });
  
    $('#fecha-card').on('input', function() {
      validateExpiryDate();
    });
  
    $('#cvv-card').on('input', function() {
      validateCVV();
    });
  
    $('form').on('submit', function(event) {
      if (!isFormValid()) {
        event.preventDefault();
      } else {
        Swal.fire(
            '¡Gracias por su compra!',
            'Será redirigido a sus pedidos',
            'success'
        );
      }
    });
  
    function isFormValid() {
      var isValid = true;
      var cardNumber = $('#nro-credit').val();
      var expiryDate = $('#fecha-card').val();
      var cvv = $('#cvv-card').val();
  
      if (cardNumber === '' || !/^\d+$/.test(cardNumber) || !isCardTypeValid(cardNumber)) {
        showError('#nro-credit', 'Por favor, ingrese un número de tarjeta válido.');
        isValid = false;
      } else {
        clearError('#nro-credit');
      }
  
      if (expiryDate === '' || !/^(0[1-9]|1[0-2])\/\d{2}$/.test(expiryDate)) {
        showError('#fecha-card', 'Por favor, ingrese una fecha de caducidad válida (MM/AA).');
        isValid = false;
      } else {
        clearError('#fecha-card');
      }
  
      if (cvv === '' || !/^\d{3}$/.test(cvv)) {
        showError('#cvv-card', 'Por favor, ingrese un CVV válido (3 dígitos numéricos).');
        isValid = false;
      } else {
        clearError('#cvv-card');
      }
  
      return isValid;
    }
  
    function isCardTypeValid(cardNumber) {
      var cardType = getCardType(cardNumber);
      return cardType === 'mastercard' || cardType === 'visa';
    }
  
    function validateCardNumber() {
      var cardNumber = $('#nro-credit').val();
      var cardType = getCardType(cardNumber);
  

      if (cardNumber === '') {
        showError('#nro-credit', 'El número de tarjeta es obligatorio.');
      } else if (!/^\d+$/.test(cardNumber)) {
        showError('#nro-credit', 'El número de tarjeta solo debe contener números.');
      } else if (!isCardTypeValid(cardNumber)) {
        showError('#nro-credit', 'Solo se aceptan tarjetas Mastercard o Visa.');
      } else if (cardNumber.length !== getCardNumberLength(cardType)) {
        showError('#nro-credit', 'El número de tarjeta debe tener ' + getCardNumberLength(cardType) + ' dígitos.');
      } else {
        clearError('#nro-credit');
      }
    }
  
    function getCardType(cardNumber) {
      var visaPattern = /^4/;
      var mastercardPattern = /^5[1-5]/;
  
      if (visaPattern.test(cardNumber)) {
        return 'visa';
      } else if (mastercardPattern.test(cardNumber)) {
        return 'mastercard';
      } else {
        return '';
      }
    }
  
    function getCardNumberLength(cardType) {
      if (cardType === 'visa') {
        return 16;
      } else if (cardType === 'mastercard') {
        return 16;
      } else {
        return 0;
      }
    }
  
    function validateExpiryDate() {
      var expiryDate = $('#fecha-card').val();
  
      if (expiryDate === '') {
        showError('#fecha-card', 'La fecha de caducidad es obligatoria.');
      } else if (!/^(0[1-9]|1[0-2])\/\d{2}$/.test(expiryDate)) {
        showError('#fecha-card', 'El formato de fecha de caducidad debe ser MM/AA.');
      } else {
        clearError('#fecha-card');
      }
    }
  
    function validateCVV() {
      var cvv = $('#cvv-card').val();
  
      if (cvv === '') {
        showError('#cvv-card', 'El CVV es obligatorio.');
      } else if (!/^\d{3}$/.test(cvv)) {
        showError('#cvv-card', 'El CVV debe contener 3 dígitos numéricos.');
      } else {
        clearError('#cvv-card');
      }
    }
  
    function showError(fieldId, errorMessage) {
        $(fieldId).addClass('is-invalid');
        $(fieldId).next('.text-danger').text(errorMessage);
        $(fieldId).next('.text-danger').show();
      }
    
      function clearError(fieldId) {
        $(fieldId).removeClass('is-invalid');
        $(fieldId).next('.text-danger').text('');
        $(fieldId).next('.text-danger').hide();
      }
      
  });
  