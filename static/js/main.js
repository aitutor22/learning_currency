$(document).ready(function() {
	$("form").submit(function(event){
		event.preventDefault();

		$.ajax({
			type: "POST",
			url: "/changecurrency",
			data: {
				number: $("#numberBags")[0].value,
				price: $("#price")[0].value,
				originalCurrency: $("#originalCurrency")[0].value,
				newCurrency: $("#newCurrency")[0].value
			},
			success: function(data){
				if (data.status == 200) {
					alert("Total price is " + data.total_price)
				}
			}
		})
	});
});