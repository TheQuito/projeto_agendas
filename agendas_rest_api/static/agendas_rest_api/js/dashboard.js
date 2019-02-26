
/* Executa uma requisição ajax na api restFul em busca dos dados de vagas para o aplicativo.
	   Na sequência executa as funções barChart() e pieChart() passando os dados obtidos
	   na requisição ajax, e o id do container onde o gráfico deve ser plotado	
	*/
	function loadChart() {
		$.get('http://localhost:9191/agendas_rest_api/getVagasApp/', function (data) {	
			var labels = [];
			var dados = [];
			for (var i = 0; i < data.vagas.length; i++) {
				labels[i] = data.vagas[i][0];
				dados[i] = data.vagas[i][1];
			};
			var ctx1 = document.getElementById('chartContainer0').getContext('2d');
			var ctx2 = document.getElementById('chartContainer1').getContext('2d');
			var ctx5 = document.getElementById('chartContainer5').getContext('2d');
			
			chartPie(ctx1, labels, dados);
			chartBar(ctx2, labels, dados);
			chartPie(ctx5, labels, dados);
			
		}, 'json');
	};
	
	function obterDadosEsperaExame(){
		$.get('http://localhost:9191/agendas_rest_api/atrasoMedioExames', function(data){
			var labels = [];
			var dados = [];
			for(var i=0; i< data.listaExames.length; i++){
				labels[i] = data.listaExames[i][0];
				dados[i] = data.listaExames[i][1];
			}
			var ctx3 = document.getElementById('chartContainer3').getContext('2d');
			chartBar(ctx3, labels, dados);
			var ctx6 = document.getElementById('chartContainer6').getContext('2d');
			chartBar(ctx6, labels, dados);
		})
	}
    


    // FUNÇÃO QUE GERA UMA INSTÂNCIA DE CHART PASSANDO O ID DO CONTAINER, ARRAY DE LABELS E ARRAY DE DATASETS
	function loadChartAgendamentosApp(myChart, labels, datasets){
		var ctx = document.getElementById(myChart).getContext('2d');
		chartLine(ctx, labels, datasets);
    }
    

    // FUNÇÃO QUE PREPARA OS DADOS E EM SEGUIDA CHAMA A FUNÇÃO QUE CARREGA O GRÁFICO
	function loadDataAgendamentosApp(myChart, estabelecimento, dataInicio, dataFim){
		var labels = [];
		var estabelecimento = estabelecimento;
		var dataInicio = dataInicio;
		var dataFim = dataFim;
		var url = 'http://localhost:9191/agendas_rest_api/agendamentosApp'
		var parametros = '?estabelecimento='+estabelecimento+'&dataInicio='+dataInicio+'&dataFim='+dataFim
		$.get(url + parametros, function (dados) {		
			for(var i = 0; i < dados.listaDeDatas.length; i++){
				labels[i] = dados.listaDeDatas[i];	
			}
			var datasets = []
			for(var i = 0; i < dados.agendamentos.length; i++){
				qtds = [];
				for(var j=0, k=0; j < labels.length; j++){
					if(k < dados.agendamentos[i].length){
						if(labels[j] == dados.agendamentos[i][k].data){
							qtds[j] =  dados.agendamentos[i][k].qtd;
							k++
						}else{
							qtds[j] = 0;
						}
					}else{
						qtds[j] = 0;
					}					
				}
				datasets[i] = {
					label : dados.agendamentos[i][i].especialidade,
					borderColor: cores[i],
					backgroundColor : 'rgba(0,0,0,0)',
					data : qtds,
				};
			}
			loadChartAgendamentosApp(myChart, labels, datasets);
		}, 'json');
	}