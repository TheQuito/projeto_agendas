

// Instancia um gráfico de pizza e retorna o mesmo para quem chamou esta função
function pieChart(dados, container, tema='light1'){
	var chart = new CanvasJS.Chart(container, {
		theme: tema, // "light2", "dark1", "dark2"
		animationEnabled: true, // change to true		
		title:{
			text: ""
		},
		data: [
			{
				innerRadius: "80%",
				radius: "90%",
				legendMarkerType: "square",
				showInLegend: true,
				startAngle: 90,
				// Change type to "bar", "area", "spline", "pie",etc.
				type: 'pie',
				dataPoints: dados
			}
		]
	})
	return chart;
};




// Instancia um gráfico de barras e retorna o mesmo para quem chamou esta função
function barChart(dados, container, tema='light1'){
	var chart = new CanvasJS.Chart(container, {
		theme: tema, // "light2", "dark1", "dark2"
		animationEnabled: true, // change to true		
		title:{
			text: ""
		},
		data: [
			{
				innerRadius: "80%",
				radius: "90%",
				legendMarkerType: "square",
				showInLegend: true,
				startAngle: 90,
				// Change type to "bar", "area", "spline", "pie",etc.
				type: 'bar',
				dataPoints: dados
			}
		]
	})
	return chart;
};


// Instancia um gráfico de area e retorna o mesmo para quem chamou esta função
function areaChart(dados, container, tema='light1'){
	var chart = new CanvasJS.Chart(container, {
		theme: tema, // "light2", "dark1", "dark2"
		animationEnabled: true, // change to true		
		title:{
			text: ""
		},
		data: [
			{
				innerRadius: "80%",
				radius: "90%",
				legendMarkerType: "square",
				showInLegend: true,
				startAngle: 90,
				// Change type to "bar", "area", "spline", "pie",etc.
				type: 'area',
				dataPoints: dados
			}
		]
	})
	return chart;
};



// Instancia um gráfico de spline e retorna o mesmo para quem chamou esta função
function splineChart(dados, container, tema='light1'){
	var chart = new CanvasJS.Chart(container, {
		theme: tema, // "light2", "dark1", "dark2"
		animationEnabled: true, // change to true		
		title:{
			text: ""
		},
		data: [
			{
				innerRadius: "80%",
				radius: "90%",
				legendMarkerType: "square",
				showInLegend: true,
				startAngle: 90,
				// Change type to "bar", "area", "spline", "pie",etc.
				type: 'spline',
				dataPoints: dados
			}
		]
	})
	return chart;
};



