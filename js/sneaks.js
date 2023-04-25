const settings = {
	async: true,
	crossDomain: true,
	url: 'https://shoes-collections.p.rapidapi.com/shoes',
	method: 'GET',
	headers: {
		'content-type': 'application/octet-stream',
		'X-RapidAPI-Key': 'e124f90510msh45761f5572f2521p1c2a8ejsna1db582243af',
		'X-RapidAPI-Host': 'shoes-collections.p.rapidapi.com'
	}
};

$.ajax(settings).done(function (response) {
	$.each()
});