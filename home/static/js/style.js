$(document).ready(function () {
	//dropdown hover
	$('ul.nav li.dropdown').hover(function() {
	  $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeIn(500);
	}, function() {
	  $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeOut(500);
	});
	//end dropdown hover
});