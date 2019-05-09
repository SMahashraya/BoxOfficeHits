var width = parseInt(d3.select("#scatter").style("width"));
var height = width - width / 4;
var margin = 15;

var labelArea = 100;

var textPadBot = 30;
var textPadLeft = 30;

var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", width)
  .attr("height", height)
  .attr("class", "chart");

  var markerRadius;
  function crGet() {
      if (width <= 1000) {
          markerRadius = 10;
      }
      else {
          markerRadius = 12;
      }
  }
  crGet();

  svg.append("g").attr("class", "xText");
  var xText = d3.select(".xText");

  function xTextRefresh() {
    xText.attr(
      "transform",
      "translate(" +
        ((width - labelArea) / 2 + labelArea) +
        ", " +
        (height - margin - textPadBot) +
        ")"
    );
  }
  xTextRefresh();
// 1. IMDb Rating
  xText
  .append("text")
  .attr("y", -26)
  .attr("data-name", "imdbrating")
  .attr("data-axis", "x")
  .attr("class", "aText active x")
  .text("IMDb Rating");
// 2. MetaScore
xText
  .append("text")
  .attr("y", 0)
  .attr("data-name", "metascore")
  .attr("data-axis", "x")
  .attr("class", "aText inactive x")
  .text("Metascore");
// 3. Rotten Tomatoes Score
xText
  .append("text")
  .attr("y", 26)
  .attr("data-name", "rotten_tomatoes_score")
  .attr("data-axis", "x")
  .attr("class", "aText inactive x")
  .text("Rotten Tomatoes Score");

var leftTextX = margin + textPadLeft;
var leftTextY = (height + labelArea) / 2 - labelArea;

svg.append("g").attr("class", "yText");

var yText = d3.select(".yText");

function yTextRefresh() {
    yText
    .attr(
      "transform",
      "translate(" + leftTextX + ", " + leftTextY + ")rotate(-90)"
    );
  }
yTextRefresh();

yText
.append("text")
.attr("y", -26)
.attr("data-name", "total_gross")
.attr("data-axis", "y")
.attr("class", "aText active y")
.text("Total Gross");

d3.csv("assets/data/movies.csv", function(data) {
    visualize(data)
    console.log(data);
});

d3.csv("assets/data/movies.csv", function(error, data) {
  console.log(error)
  data.forEach(function(d) {
    d.imdbrating = +d.imdbrating;
    d.rotten_tomatoes_score = +d.rotten_tomatoes_score;
    d.year = +d.year;
    d.metascore = +d.metascore;
  });
  var allYears = d3.map(data, function(d){return(d.year)}).keys()
  d3.select("#selectButton") 
    .selectAll("myYears")
    .data(allYears)
    .enter()
    .append('year')
    .text(function (d) { return d; })
    .attr("value", function (d) { return d; })

  function update(selectedData) {
    var dataFilter = data.filter(function(d){return d.year == selectedData})
    theCircles
      .datum(dataFilter)
      .transition()
      .duration(1000)
    }
  }
)

function visualize(theData) {
    var curX = "imdbrating";
    var curY = "total_gross";

    var xMin;
    var xMax;
    var yMin;
    var yMax;

    var toolTip = d3
    .tip()
    .attr("class", "d3-tip")
    .offset([40, -60])
    .html(function(d) {
        var theX;
        var theTitle = "<div>" + d.title + "</div>";
        var theY = "<div>" + curY + ": " + d[curY] + "%</div>";
        if (curX === "imdbrating") {
            theX = "<div>" + curX + ": " + d[curX] + "%</div>";
        }
        else {
            theX = "<div>" + curX + ": " + parseFloat(d[curX]).toLocaleString("en") + "</div>";
        }
        return theTitle + theX + theY;
    });
    svg.call(toolTip);

    function xMinMax() {
        xMin = d3.min(theData, function(d) {
            return parseFloat(d[curX]) * 0.50;
        });

        xMax = d3.max(theData, function(d) {
            return parseFloat(d[curX]) * 1.00;
        });
    }

    function yMinMax() {
        yMin = d3.min(theData, function(d) {
            return parseFloat(d[curY]) * 0.50;
        });
        yMax = d3.max(theData, function(d) {
            return parseFloat(d[curY]) * 1.00;
        });
    }
    function labelChange(axis, clickedText) {
        d3
        .selectAll(".aText")
        .filter("." + axis)
        .filter(".active")
        .classed("active", false)
        .classed("inactive", true);
    
    clickedText.classed("inactive", false).classed("active", true);
    }

    xMinMax();
    yMinMax();

    var xScale = d3
    .scaleLinear()
    .domain([xMin, xMax])
    .range([margin + labelArea, width - margin]);
    var yScale = d3
    .scaleLinear()
    .domain([yMin, yMax])
    .range([height - margin - labelArea, margin]);

    var xAxis = d3.axisBottom(xScale);
    var yAxis = d3.axisLeft(yScale);

    function tickCount() {
        if (width <= 500) {
          xAxis.ticks(5);
          yAxis.ticks(5);
        }
        else {
          xAxis.ticks(10);
          yAxis.ticks(10);
        }
      }
      tickCount();

    svg
    .append("g")
    .call(xAxis)
    .attr("class", "xAxis")
    .attr("transform", "translate(0," + (height - margin - labelArea) + ")");
    
    svg
    .append("g")
    .call(yAxis)
    .attr("class", "yAxis")
    .attr("transform", "translate(" + (margin + labelArea) + ", 0)");

    var theCircles = svg.selectAll("g theCircles").data(theData).enter();
    
    var posterColors = d3.scaleOrdinal()
    .domain(["Black", "White", "Gray", "NaN", "Cyan", "Magenta", "Yellow", "Red", "Blue"])
    .range(["#000000", "#FFFFFF", "#808080", "#E9967A", "##00FFFF", "#FF00FF", "#FFE933", "#FF3333", "#4933FF" ])
    theCircles
    .append("circle")
    
    // These attr's specify location, size and class.
    .attr("cx", function(d) {
      return xScale(d[curX]);
    })
    .attr("cy", function(d) {
      return yScale(d[curY]);
    })
    .attr("r", markerRadius)
    .attr("class", function(d) {
      return "titleCircle ";
    })
    // Hover rules
    .on("mouseover", function(d) {
      // Show the tooltip
      toolTip.show(d, this);
      // Highlight the state circle's border
      d3.select(this).style("stroke", "#323232");
    })
    .on("mouseout", function(d) {
      // Remove the tooltip
      toolTip.hide(d);
      // Remove highlight
      d3.select(this).style("stroke", "#e3e3e3");
    });
    d3.selectAll(".aText").on("click", function() {
        // Make sure we save a selection of the clicked text,
        // so we can reference it without typing out the invoker each time.
        var self = d3.select(this);
    
        // We only want to run this on inactive labels.
        // It's a waste of the processor to execute the function
        // if the data is already displayed on the graph.
        if (self.classed("inactive")) {
          // Grab the name and axis saved in label.
          var axis = self.attr("data-axis");
          var name = self.attr("data-name");
    
          // When x is the saved axis, execute this:
          if (axis === "x") {
            // Make curX the same as the data name.
            curX = name;
    
            // Change the min and max of the x-axis
            xMinMax();
    
            // Update the domain of x.
            xScale.domain([xMin, xMax]);
    
            // Now use a transition when we update the xAxis.
            svg.select(".xAxis").transition().duration(1000).call(xAxis);
    
            // With the axis changed, let's update the location of the state circles.
            d3.selectAll("circle").each(function() {
              // Each state circle gets a transition for it's new attribute.
              // This will lend the circle a motion tween
              // from it's original spot to the new location.
              d3
                .select(this)
                .transition()
                .attr("cx", function(d) {
                  return xScale(d[curX]);
                })
                .duration(1000);
            });
    
            // We need change the location of the state texts, too.
            d3.selectAll(".titleText").each(function() {
              // We give each state text the same motion tween as the matching circle.
              d3
                .select(this)
                .transition()
                .attr("dx", function(d) {
                  return xScale(d[curX]);
                })
                .duration(300);
            });
    
            // Finally, change the classes of the last active label and the clicked label.
            labelChange(axis, self);
          }
          else {
            // When y is the saved axis, execute this:
            // Make curY the same as the data name.
            curY = name;
    
            // Change the min and max of the y-axis.
            yMinMax();
    
            // Update the domain of y.
            yScale.domain([yMin, yMax]);
    
            // Update Y Axis
            svg.select(".yAxis").transition().duration(300).call(yAxis);
            labelChange(axis, self);
          }
        }
    });
}