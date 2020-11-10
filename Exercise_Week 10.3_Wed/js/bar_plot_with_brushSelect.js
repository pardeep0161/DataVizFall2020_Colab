function bar_plot(values, beans, ax,
                  title = "",
                  xLabel = "",
                  yLabel = "",
                  margin = 100) {


    let axis = d3.select(`${ax}`);

    let xScale = d3.scaleBand().domain(beans).range([margin, 1000 - margin]);
    xScale.padding(0.4);
    console.log(xScale)
    let yScale = d3.scaleLinear().domain([0, d3.max(values)]).range([1000 - margin, margin]);

    // x and y Axis function
    let x_axis = d3.axisBottom(xScale);
    let y_axis = d3.axisLeft(yScale).ticks(4);
    //X Axis
    let xAxis = axis.append("g").attr("class", "axis")
        .attr("transform", `translate(${0},${1000 - margin})`)
        .call(x_axis)
    // Y Axis
    axis.append("g").attr("class", "axis")
        .attr("transform", `translate(${margin},${0})`)
        .call(y_axis)
    // Labels
    axis.append("g").attr("class", "label")
        .attr("transform", `translate(${500},${1000 - 10})`)
        .append("text")
        .attr("class", "label")
        .text(xLabel)

    axis.append("g")
        .attr("transform", `translate(${35},${500}) rotate(270)`)
        .append("text")
        .attr("class", "label")
        .text(yLabel)
    // Title
    axis.append('text')
        .attr('x', 500)
        .attr('y', 80)
        .attr("text-anchor", "middle")
        .text(title)
        .attr("class", "title")


    axis.append("defs").append("svg:clipPath")
        .attr("id", "clip")
        .append("svg:rect")
        .attr("width", 1000 - margin )
        .attr("height", 1000 - margin )
        .attr("x", margin)
        .attr("y", margin);

    axis.append('g')
        .attr("clip-path", "url(#clip)")
        .selectAll(".bar")
        .data(values)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function (d, i) {
            return xScale(beans[i]);
        })
        .attr("y", function (d) {
            return yScale(d);
        })
        .attr("width", xScale.bandwidth())
        .attr("height", function (d) {
            return 1000 - margin - yScale(d);
        });


    let brush = d3
        .brushX()
        .on("end", brushedEnd)
        .extent([
            [margin, margin],
            [1000 - margin, 1000 - margin]
        ]);


    axis
        .append("g")
        .attr("class", "brush")
        .call(brush);

    function brushedEnd() {
        // use d3.brushSelection to get bounds of the brush
        let selected_items = d3.brushSelection(this); // these are values on the screen
        let lower_bean_level = beans.indexOf(scaleBandInvert(xScale)(selected_items[0]));
        let upper_bean_level = beans.indexOf(scaleBandInvert(xScale)(selected_items[1]));
        let filtered_beans = []

        for(let i = 0 ; i < beans.length; i++) {
            if(lower_bean_level <= i && i <= upper_bean_level){
                filtered_beans.push(beans[i]);
            }
        }
        xScale.domain(filtered_beans)
        // This remove the grey brush area as soon as the selection has been done


        // Update axis and circle position
        // axis.select(".brush").call(brush.move, null)
        x_axis = d3.axisBottom(xScale)

        xAxis.transition().duration(1000)
            .attr("transform", `translate(${0},${1000 - margin})`)
            .call(x_axis)

        axis
            .selectAll(".bar")
            .transition().duration(1000)
            .attr("x", function (d, i) {
                return xScale(beans[i]);
            })

    }

    // https://stackoverflow.com/questions/38633082/d3-getting-invert-value-of-band-scales
    function scaleBandInvert(scale) {
        let domain = scale.domain();
        let paddingOuter = scale(domain[0]);
        let eachBand = scale.step();
        return function (value) {
            let index = Math.round(((value - paddingOuter) / eachBand));
            return domain[Math.floor(Math.min(index, domain.length-1))];
        }
    }
}