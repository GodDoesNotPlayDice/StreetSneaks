$('#decenso').click(function(e) {        
    Swal.fire(
      'Usuario Degradado!',
      'El Usuario dejó de ser vendedor',
      'success'
    );
  });
  $('#acenso').click(function(e) {
    Swal.fire(
      'Usuario ascendido!',
      'El usuario ahora es vendedor',
      'success'
    );
  });
  