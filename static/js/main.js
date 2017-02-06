$(document).ready(function() {
	$("form").submit(function(event){
		event.preventDefault();

		$.ajax({
			type: "POST",
			url: "/changecurrency",
			data: {
				number: 1,
				price: 3000,
				originalCurrency: "usd",
				newCurrency: "sgd"
			},
			success: function(data){
				console.log(data);
			}
		})
	});
});