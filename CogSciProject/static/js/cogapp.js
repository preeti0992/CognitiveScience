//handles data popultaion and server request and response

$(function () {
	
	//define arrays same as backend
	var emotions = ['Rage', 'Anger', 'Desperation', 'Fear'];
	var emo_codes = ['rage', 'anger', 'desperation', 'fear'];

	var situations = ['Psychological Issues', 'Relationship issues', 'Trauma or Abuse'];
	var sit_codes = ['psychological', 'relationship', 'trauma'];

	//var factors =['Rage', 'Anger','Desperation','Fear','Psychological Issues','Relationship issues','Trauma or Abuse'];
	//var factor_codes = ['rage', 'anger', 'desperation', 'fear','psychological', 'relationship', 'trauma'];

	var sel_emo = [];
	var sel_sit = [];

	//data for heatmap
	var heatmapData = [];
	//exp count
	var expCnt = 0;

	//add empty options
	var op = new Option("", "");
	$(op).html("");
	$("#sel_emotions").append(op);
	op = new Option("", "");
	$(op).html("");
	$("#sel_situations").append(op);

	//add options
	for (var i = 0; i < emotions.length; i++) {
		op = new Option(emotions[i], i);
		//use jquery to select the html object 'o'
		$(op).html(emotions[i]);
		$("#sel_emotions").append(op);
	}
	//add options
	for (var i = 0; i < situations.length; i++) {
		op = new Option(situations[i], i);
		//use jquery to select the html object 'o'
		$(op).html(situations[i]);
		$("#sel_situations").append(op);
	}

	//on change event of options
	$("#sel_emotions").change(function () {
		var id = $("#sel_emotions").val();

		if (!sel_emo.includes(id)&&id!="") {
			sel_emo.push(id);
			var parent = $('#div_emotions');
			var inputs = parent.find('input');
			$('<input />', {
				type: 'checkbox',
				id: 'cb_emo' + id,
				value: emotions[id]
			}).prop('checked', true).change(factor_selector).appendTo(parent);
			$('<label />', {
				id: 'lcb_emo' + id,
				text: emotions[id]
			}).appendTo(parent);
		}

	});

	//on change event of options
	$("#sel_situations").change(function () {
		
		var id = $("#sel_situations").val();
		if (!sel_sit.includes(id)&&id!="") {
			sel_sit.push(id);
			var parent = $('#div_situations');
			var inputs = parent.find('input');

			$('<input />', {
				type: 'checkbox',
				id: 'cb_sit' + id,
				value: situations[id]
			}).prop('checked', true).change(factor_selector).appendTo(parent);
			$('<label />', {
				id: 'lcb_sit' + id,
				text: situations[id]
			}).appendTo(parent);
		}
	});
	
    //select factor
	var factor_selector = function () {
		//alert('checked');
		var id = this.id;
		if (id.indexOf('emo') != -1) {
			var index = sel_emo.indexOf(id.match(/\d+/)[0]);
			if (index > -1) {
				sel_emo.splice(index, 1);
			}
			$('#' + id).remove();
			//$("#div_emotions").remove('#'+id);
			$('#l' + id).remove();
		}
		if (id.indexOf('sit') != -1) {
			var index = sel_sit.indexOf(id.match(/\d+/)[0]);
			if (index > -1) {
				sel_sit.splice(index, 1);
			}
			$('#' + id).remove();
			//$("#div_emotions").remove('#'+id);
			$('#l' + id).remove();
		}
	};
    
    //get selected options
	var selected_list = function (index_list, target_list) {
		var selection = [];
		for (var i = 0; i < index_list.length; i++) {
			selection.push(target_list[index_list[i]]);
		}
		return selection;
	};

    //probability calculation button click
	$('#inputBtn').click(function () {
		if (sel_emo.length == 0 ) {
			alert("Please select a factor to see its probability");
			return;
		}
		$.ajax({
			url: '/getProb',
			data: JSON.stringify({
				'emotions': selected_list(sel_emo, emo_codes),
				'situations': selected_list(sel_sit, sit_codes)
			}),
			dataType: 'json',
			type: 'POST',
			success: function (response) {
				//var responseObj = JSON.parse(response);
				var status = response.status;
				var errorMsg = '';

				if (status === 'BAD') {
					errorMsg += 'Error. Please try again!';
					$('#errorMsg').text(errorMsg);
				} else {
					$('#errorMsg').text('');
					//console.log($('#outputMsg').text());
					//console.log(response);

					$('#outputMsg').text('Probabilities of selected factors: '); // + JSON.stringify(response.result));
					//console.log($('#outputMsg').text());
					
					//clear charts
					$(".chart").empty();
					$(".heatmap").empty();
					
					//create data to display in charts
					var chartData = [];
					var keys = Object.keys(response.result);
					expCnt++;
					var evidence_str = "";
					/*
					for(var i=0;i<sel_sit.length;i++){
    					evidence_str += selected_list(sel_sit[i], situations)+", ";
					}
					evidence_str=evidence_str.slice(0, -2); //remove extra space and ','
					*/
					//create a string of evidence names
					evidence_str += selected_list(sel_sit, situations);
					evidence_str = evidence_str.replace(',',', ')
					
					for (var i = 0; i < keys.length; i++) {
						var emo = emotions[emo_codes.indexOf(keys[i])],
							pc = Math.round(response.result[keys[i]] * 10000) / 100;
    						chartData.push({
							emo: emo,
							pc: pc
						});
						heatmapData.push({
							exp: 'Experiment ' + expCnt,
							emo: emo,
							pc: pc,
							evi:evidence_str
						});
					}
					
					//display charts
					createChart(chartData);
					createHeatmap(heatmapData,expCnt);
				}
			},
			error: function (error) {
				console.log(error);
			}
		});
	});
	
});