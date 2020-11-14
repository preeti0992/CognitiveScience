var createHeatmap = function (data,expCnt) {
    //sample data
    /*
    var data =[
        {
            exp:"Experiment 1",
            emo:"rage",
            pc:10,
            evi:"Rage"
        }
    };
    */
    
	var blockSize = 30,
		cellSize = blockSize - 1,
		margin = {
			top: 100,
			right: 20,
			bottom: 20,
			left: 100
		};
    	
	//chart height and width with hotizontal legend
	var width = 400,
    	height = (expCnt+1.5) * blockSize;//extra 1.5 for legend 
    	
    //chart height and width with vertical legend but height insufficient
    /*var width = 500,
    	height = expCnt * blockSize;//extra 1.5 for legend*/
    
    //parent svg height and width
	var w = width + margin.left + margin.right,
		h = height + margin.top + margin.bottom;
		
	var svg = d3.select('.heatmap')
		.append("svg")
		.attr("width", w)
		.attr("height", h)
		.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	var xValues = d3.set(data.map(function (item) {
			return item.emo;
		})).values();

	var xScale = d3.scale.ordinal()
		.domain(xValues)
		.rangeBands([0, xValues.length * blockSize]);

	var xAxis = d3.svg.axis()
		.scale(xScale)
		.tickFormat(function (d) {
			return d;
		})
		.orient("top");
		
	var yValues = d3.set(data.map(function (item) {
			return item.exp;
		})).values();

	var yScale = d3.scale.ordinal()
		.domain(yValues)
		.rangeBands([0, yValues.length * blockSize]);

	var yAxis = d3.svg.axis()
		.scale(yScale)
		.tickFormat(function (d) {
			return d;
		})
		.orient("left");

	var max = d3.max(data, function (d) {
		return d.pc;
	});
	
	var colorScale = d3.scale.quantile()
		.domain([0, max])
		//.range(["#b3e0ff","#99d6ff","#80ccff","#66c2ff","#4db8ff","#33adff","#1aa3ff","#0099ff","#008ae6","#007acc","#006bb3","#005c99"]);
		.range(["#ffcc33", "#ffbf00", "#f29f00", "#e67f00", "#d95f00", "#cc4000", "#c02000", "#b30000", "#800000"]);
    	//.range(["#ffffe5","#f7fcb9","#d9f0a3","#addd8e","#78c679","#41ab5d","#238443","#006837","#004529"]);

	var tip = d3.tip()
		.attr('class', 'd3-tip')
		.html(function (d) {
			return "<div><span class='light'>" + d.emo + ": " + d.pc + "% <br />" + d.evi + "</span></div>";
		});

	var cells = svg.selectAll('rect')
		.data(data)
		.enter()
		.append('g')
		.append('rect')
		.attr('class', 'cell')
		.attr('width', cellSize)
		.attr('height', cellSize)
		.attr('y', function (d) {
			return yScale(d.exp);
		})
		.attr('x', function (d) {
			return xScale(d.emo);
		})
		.attr('fill', function (d) {
			return colorScale(d.pc);
		})
		.on('mouseover', function (d) {
			tip.show(d)
		})
		.on('mouseout', tip.hide);

	// Invoke tooltip for each cell
	cells.call(tip);

    //add y axis labels
	svg.append("g")
		.attr("class", "y axis")
		.call(yAxis)
		.selectAll('text')
		.attr('font-weight', 'normal');

    //add x axis labels
	svg.append("g")
		.attr("class", "x axis")
		.call(xAxis)
		.selectAll('text')
		.attr('font-weight', 'normal')
		.style("text-anchor", "start")
		.attr("dx", ".8em")
		.attr("dy", ".5em")
		.attr("transform", function (d) {
			return "rotate(-60)";
		});


	var legendCellWidth = blockSize;

	var legend = svg.selectAll(".legend")
		//.data(colorScale.quantiles(9));
		.data([0].concat(colorScale.quantiles()), function (d) {
			return d;
		});

    //create legend group
	legend.enter()
    	.append("g")
		.attr("class", "legend");

    //create legend rects horizontal
	legend.append("rect")
		.attr("x", function (d, i) {
			return legendCellWidth * i;
		})
		.attr("y", height - blockSize)
		.attr("width", legendCellWidth)
		.attr("height", blockSize * .5)
		.style("fill", function (d, i) {
			return colorScale.range()[i];
		});
	
	/*	
    //create legend rects vertical but height is insufficient here
	legend.append("rect")
		.attr("x", width - blockSize)
		.attr("y", function (d, i) {
			return legendCellWidth * i;
		})
		.attr("height", legendCellWidth)
		.attr("width", blockSize * .5)
		.style("fill", function (d, i) {
			return colorScale.range()[i];
		});

    */
    
    //add legend text
	legend.append("text")
		.attr("class", "legend")
		.text(function (d) {
			return Math.round(d);
		})
		.attr("x", function (d, i) {
			return legendCellWidth * i;
		})
		.attr("y", height );//+ blockSize * .5);

	legend.exit().remove();
	
};