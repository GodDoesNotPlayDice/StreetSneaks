$(document).ready(function () {
	let title = $("#title").text();
	function card(valueOfElement){
		let card = `<div class="sneaks__card zoom"><div class="sneaks__card__img"><a class="sneaks__card__img__link" href="#"><img class="sneaks__card__img__img" src="${valueOfElement.imagen}" alt="${valueOfElement.nombre}"></a></div><div class="sneaks__card__details"><div class="sneaks__card__details__name-price"><p>${valueOfElement.nombre}</p><p>${valueOfElement.precio} CLP</p></div><div class="sneaks__card__details__desc"><p>${valueOfElement.tipo}</p><p>1 Color</p></div></div></div>`
		$('#sneaks').append(card)
	}

    $.get("https://sneaksstore-66c63-default-rtdb.firebaseio.com/Sneaks.json", function(data, status){
        console.log(status)
        $.each(data, function (indexInArray, valueOfElement) {
				if(valueOfElement.tipo === "Mujer" && title === "Mujer"){
					card(valueOfElement)
				} else if (valueOfElement.tipo === "Hombre" && title === "Hombre"){
					card(valueOfElement)
				} else if (title != "Hombre" && title != "Mujer") {
					card(valueOfElement)
				}

        });
  });
});