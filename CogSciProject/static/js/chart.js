var createChart = function (data) {
	//sample data
	/*
	var data=[
	    {emo:"rage", pc:12},
	    {emo:"anger", pc:14},
	    {emo:"fear", pc:4},
	    {emo:"desperation", pc:2}
	];
	*/
	
	//console.log("before");
	//console.log(data);
	
	data = data.sort(function (x, y) {
		return d3.ascending(x.pc, y.pc);
	});

    
	//console.log(data);

	//set up margins
	var margin = {
		top: 10,
		right: 10,
		bottom: 10,
		left: 100
	};
	
	
	var n=data.length;
	
	//chart height and width
	var width = 360,
    	height = n * 40;
    
    //parent svg height and width
    /*
	var w = 600,
		h = 300;
	*/
	var w = width + margin.left + margin.right + 100,
		h = height + margin.top + margin.bottom + 100;

	var svg = d3.select(".chart").append("svg")
		.attr("width", w)
		.attr("height", h)
		.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	var xScale = d3.scale.linear()
		.domain([0, d3.max(data, function (d) {
			return d.pc;
		})])
		.range([margin.left, width + margin.left]);

	var yScale = d3.scale.ordinal()
		.domain(data.map(function (d) {
			return d.emo;
		}))
		.rangeRoundBands([height + margin.top, margin.top], .2);
    	//.range([height+margin.top, margin.top]);

	//create y axis with names
	var yAxis = d3.svg.axis()
		.scale(yScale)
		.tickSize(0)
		.orient("left");

	svg.append("g")
		.attr("class", "axis")
		.call(yAxis)

	var bars = svg.selectAll(".bar")
		.data(data)
		.enter()
		.append("g")

	var colorScale = d3.scale.quantile()
		.domain([0, d3.max(data, function (d) {
			return d.pc;
		})])
		//.range(["#b3e0ff","#99d6ff","#80ccff","#66c2ff","#4db8ff","#33adff","#1aa3ff","#0099ff","#008ae6","#007acc","#006bb3","#005c99"]);
		.range(["#009532", "#00a050", "#00aa72", "#00b597", "#00c0c0", "#00a8ca", "#008ed5", "#0070df", "#004eea"]);
    	//.range(["#bfdfbf","#aad5aa","#95ca95","#80c080","#6ab56a","#55aa55","#40a040","#2b952b"]);

	//append rects
	bars.append("rect")
		.attr("fill", function (d) {
			return colorScale(d.pc);
		})
		.attr("y", function (d) {
			return yScale(d.emo);
		})
		.attr("height", yScale.rangeBand())
		.attr("x", 0)
		.attr("width", function (d) {
			return xScale(d.pc);
		});

	//add a label to each bar
	bars.append("text")
		.attr("class", "label")
		.attr("y", function (d) {
			return yScale(d.emo) + yScale.rangeBand() / 2 + 4;// adjsted position
		})
		.attr("x", 10)
		.style("fill", "white")
		.text(function (d) {
			return d3.format(",")(d.pc)+"%";
		});
};