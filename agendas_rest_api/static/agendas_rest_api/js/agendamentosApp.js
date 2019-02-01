// FUNÇÃO QUE PREPARA OS DADOS E EM SEGUIDA CHAMA A FUNÇÃO QUE CARREGA O GRÁFICO
function loadData(myChart, estabelecimento, dataInicio, dataFim){
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
        loadChart(myChart, labels, datasets);
    }, 'json');
}



    

// FUNÇÃO QUE GERA UMA INSTÂNCIA DE CHART PASSANDO O ID DO CONTAINER, ARRAY DE LABELS E ARRAY DE DATASETS
function loadChart(myChart, labels, datasets){
    var ctx = document.getElementById(myChart).getContext('2d');
    chartLine(ctx, labels, datasets);
}

// CAPTURA O EVENTO DE CLICK DO BOTÃO DIREITO DO MOUSE SOBRE O GRÁFICO E ABRE UM MODAL COM CAMPOS PARA ESPECIFICAR FILTROS
function detectRightButton(event){
    button = event.which;
    if(button == 3){
        document.body.oncontextmenu = function() {return false;};  //desabilita o menu de contexto do botão direito
        $("#myModal-sm").modal();
    }
}