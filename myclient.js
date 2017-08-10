window.onload = function() {
	var url, jqchr;

	for ( var i = 0; i < 2; i++ ) {
		url = document.URL + 'inputs/' + i;
		jqxhr = $.getJSON(url, function(data) {
			console.log('API response received');
			$('#input').append('<p>input gpio port ' + data['gpio'] + ' on pin ' +
			  data['pin'] + ' has a current value ' + data['value'] + '</p');
		});
	}
};