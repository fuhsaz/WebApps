$(document).ready(function(){

	/* Deal with the CSRF stuff */

	function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');
	function csrfSafeMethod(method) {
    	// these HTTP methods do not require CSRF protection
    	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
	});

	$('#difficulty-select').change(function(){
		var newSort = $(this).val();
		var data = {"difficulty":newSort};
		$.ajax({
			type:"POST",
			url:"../filterPuzzles/",
			data:data,
			dataType:"JSON",
		})
		.done(function(data){
			$('.expendable').each(function(){
				$(this).remove()
			});
			$.each(data.data, function(i, each){
				var newTr = '<tr class="expendable"><td class="td-id">'
				newTr += each.id;
				newTr += '</td><td class="td-difficulty">';
				newTr += each.difficulty;
				newTr += '</td><td class="td-button"><button type="button" class="preview-button" value="';
				newTr += each.id;
				newTr += '">Click Me</button></td></tr>';
			    $('#puzzles').append(newTr)
			})
		})
		.fail(function(xhr, status, error) {
			console.log(xhr.responseText);
		});
	});

	$('.preview-button').on('click', function () {
		var id = $(this).val();
		var data = {"id":id};
	    $.ajax({
	        type: 'POST',
	        url: '../preview',
	        data:data,
	        dataType:"JSON",
	    })
	    .done(function (data, textStatus, jqXHR) {
	            $('#foo_modal').find('.modal-body').html(data);
	            $('#foo_modal').modal('show');
	    })
	    .fail(function(xhr, status, error) {
			console.log(xhr.responseText);
		});
	});
});