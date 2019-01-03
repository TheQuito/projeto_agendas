$(document).ready(function(){
	//###################################################
	$("#button").click(function(){
		var peso = $("#peso").val();
		var altura = $("#altura").val();
		var sexo = $("#sexo").val();
		$.ajax({
		    type: "GET",
		    url: "http://localhost:9090/rest/api/services/getimc?peso="+peso+"&altura="+altura+"&sexo="+sexo,  
		    async: false,
		    dataType: 'json',
		    success: function(data) {
		       $("#div").html("<b>Imc: </b>" + data.imc);
		       $("#situacao").html("<b>Situação:</b> " + data.situacao);
		       $("#idPeso").html("<b>Peso(kg): </b>" + data.peso);
		       
		    }
		});
	});

});

//###################################################
function requestPage(url, target) {
	$.ajax({
		type: "GET",
		url: url,
		dataType: "html",
		success: function(data) {
			$(target).html(data);
		}
	});
}
//###################################################