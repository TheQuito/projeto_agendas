$('#btn2').on('click', function(e){
	alert(e.clientX +' x '+ e.clientY)
	$.get('http://localhost:9191/agendas_rest_api/getjson/', function(data){
		if(data.success){
			alert('tudo certo' + ' -' + data.message + ' - ' + data.valor)
			$("#conteudo").html('Sucesso: ' + data.success);
			$("#conteudo").append('<br>Mensagem: ' + data.message);
			$("#conteudo").append('<br>Valor: ' + data.valor);
		}else{
			alert(data.message);
		}
	}, 'json')
});

$('#btn3').on('click', function(e){
	$.get('http://localhost:9191/agendas_rest_api/obterVagas', function(data){
		alert(data.vagas[2].estabelecimento + ' - ' + data.vagas[2].vagas)
		$("#conteudo").append(data.vagas[2].estabelecimento + ' - ' + data.vagas[2].vagas);
	}, 'json')
});