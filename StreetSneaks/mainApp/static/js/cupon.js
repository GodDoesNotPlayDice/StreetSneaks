$(document).ready(function () {
    const cuponElement = $('#name')
    const totalTextElement = $('#total-text')
    const cuponTextElement = $('#cupon-text')
	const token = document.getElementsByName( 'csrfmiddlewaretoken' )[0]

	cuponElement.on('blur', function (e) {
		const formData = new FormData()

		formData.append('csrfmiddlewaretoken', token.value)
		formData.append('name', cuponElement.val())

		const peticion = $.ajax({
				async: true,
				crossDomain: true,
				url: 'http://127.0.0.1:8000/venta/api/validar_cupon',
				method: 'POST',
				data: formData,
				processData: false,
				contentType: false
			}
		)

		peticion.done(function (response) {
			console.log('done')
			const total = response.total
			totalTextElement.text("$" + total)	
			cuponTextElement.text('(Cupon Aplicado)')
		})

		peticion.fail(function (response) {
			console.log('fail')
			console.log(response)
		})
	})


})