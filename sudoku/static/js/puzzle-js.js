$(document).ready(function() {
		/* 
		This will make cells that were filled in from the beginning green, so that
	   	the user knows they shouldn't change them. 
	   	At the same time, thicken the outlines of the 3x3 boxes to make them clearer 
	   	*/
	var counter = 1;
	$('.cell').each(function(){
		var cur = $(this).text().trim();
		if (cur.localeCompare("") != 0) {
			$(this).css("background-color", "#cff2a2");
		}
		if (1 <= counter && counter <= 9) {
			$(this).parent().css("border-top-width", "3px");
		}
		if (73 <= counter && counter <= 81) {
			$(this).parent().css("border-bottom-width", "3px");
		}
		if (19 <= counter && counter <= 27) {
			$(this).parent().css("border-bottom-width", "3px");
		}
		if (28 <= counter && counter <= 36) {
			$(this).parent().css("border-top-width", "3px");
		}
		if (46 <= counter && counter <= 54) {
			$(this).parent().css("border-bottom-width", "3px");
		}
		if (55 <= counter && counter <= 63) {
			$(this).parent().css("border-top-width", "3px");
		}
		if (counter % 9 == 1 || counter % 9 == 4 || counter % 9 == 7) {
			$(this).parent().css("border-left-width", "3px");
		}
		if (counter % 9 == 3 || counter % 9 == 6 || counter % 9 == 0) {
			$(this).parent().css("border-right-width", "3px");
		}
		
		counter += 1;
	});
	
	/* This will make it so the user can click a cell and fill in a value */
	$(document).on('click', '.cell', function(){
		var cur = $(this).text().trim()
		var toAdd = "<input type='text' value='"
		toAdd += cur;
		toAdd += "' style='width:100%' id='newInput'/>";
		$(this).html(toAdd);
		$('#newInput').focus();
		$('#newInput').select();
		$(this).focusout(function(){
			var newVal = $('#newInput').val();
			$('#newInput').remove();
			$(this).text(newVal);
		});
	});
});