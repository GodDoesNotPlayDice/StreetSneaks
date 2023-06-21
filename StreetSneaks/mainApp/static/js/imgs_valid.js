$(document).ready(function() {
    $("#up-form").submit(function(event) {
      var fileInput1 = $("#file_input").get(0).files[0];
      var fileInput2 = $("#file_input1").get(0).files[0];
      var fileInput3 = $("#file_input2").get(0).files[0];
      var imagesError = $("#images-error");
      
      // Reiniciar el mensaje de error
      imagesError.text("");
      
      if (!fileInput1 || !fileInput2 || !fileInput3) {
        imagesError.text("Debes cargar las tres imágenes.");
        event.preventDefault(); // Prevenir el envío del formulario
      }
    });
  });