$(function() {

$("#f1").on('submit', function(event) {

	$.ajax({
		data : {
			name : $('#nameInput').val(),
			email : $('#emailInput').val(),
			password : $('#emailInput').val()
		},
		type : 'POST',
		url : '/admin/process'
	})
	.done(function(data) {

		if (data.error) {
			$('#errorAlert').text(data.error).show();
			$('#successAlert').hide();
		}
		else {
			$('#successAlert').text(data.name).show();
			$('#errorAlert').hide();
		}

	});

	event.preventDefault();

});
	$("#f2").on('submit', function(event) {

	$.ajax({
		data : {
			name : $('#nameInput1').val(),
			email : $('#emailInput1').val(),
			password : $('#passInput1').val()
		},
		type : 'POST',
		url : '/admin/process'
	})
	.done(function(data) {

		if (data.error) {
			$('#errorAlert').text(data.error).show();
			$('#successAlert').hide();
		}
		else {
			$('#successAlert').text(data.name).show();
			$('#errorAlert').hide();
		}
		var ul = $('<ul>').appendTo('#ct');
		$(data.items).each(function(index, item) {
    	ul.append(
        	$(document.createElement('li')).text(item)
    	);
    });

	});

	event.preventDefault();

});
	$("#f3").on('submit', function(event) {

	$.ajax({
		data : {
			name : $('#nameInput2').val(),
			email : $('#emailInput2').val(),
			password : $('#passInput2').val(),
			keywords : $('#getInput2').val()
		},
		type : 'POST',
		url : '/admin/process'
	})
	.done(function(data) {

		if (data.error) {
			$('#errorAlert').text(data.error).show();
			$('#successAlert').hide();
		}
		else {
			$('#successAlert').text(data.name).show();
			$('#errorAlert').hide();
		}
		var ul = $('<ul>').appendTo('#ct1');
		$(data.items).each(function(index, item) {
    	ul.append(
        	$(document.createElement('li')).text(item)
    	);
    });

	});

	event.preventDefault();

});
	$("#f4").on('submit', function(event) {

	$.ajax({
		data : {
			name : $('#nameInput3').val(),
			email : $('#emailInput3').val(),
			password : $('#passInput3').val()
		},
		type : 'POST',
		url : '/admin/process'
	})
	.done(function(data) {

		if (data.error) {
			$('#errorAlert').text(data.error).show();
			$('#successAlert').hide();
		}
		else {
			$('#successAlert').text(data.name).show();
			$('#errorAlert').hide();
		}
		var ul = $('<ul>').appendTo('#ct2');
		$(data.items).each(function(index, item) {
    	ul.append(
        	$(document.createElement('li')).text(item)
    	);
    });

	});

	event.preventDefault();

});


});
