jQuery(document).ready(function(){

	//Hide (Collapse) the toggle containers on load
	jQuery(".toggle_container").hide();

	//Switch the "Open" and "Close" state per click
	jQuery(".trigger").toggle(function(){
		jQuery(this).addClass("active");
		}, function () {
		jQuery(this).removeClass("active");
	});


	//Slide up and down on click
	jQuery(".trigger").click(function(){
		jQuery(this).next(".toggle_container").slideToggle("medium");
        });

});
