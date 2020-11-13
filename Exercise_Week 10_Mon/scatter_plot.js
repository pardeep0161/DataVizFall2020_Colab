function scatter_plot(X,Y,island, markersize,
                      axis_key,
                      title="",
                      xLabel="",
                      yLabel="",
                      margin = 50)
{
    let xScale= d3.scaleLinear().domain(d3.extent(X)).range([0+margin,(1000/3)-margin])
    let yScale= d3.scaleLinear().domain(d3.extent(Y)).range([(1000/3)-margin,0 + margin])
    let colorScale= d3.scaleOrdinal().domain(["Dream","Biscoe","Torgersen"]).range(['steelblue', 'brown', 'red'])
    let axis = d3.select(`#${axis_key}`)
    axis.selectAll('.markers')
        .data(X)
        .enter()
        .append('g')
        .attr('transform', function(d,i) {
            return `translate(${xScale(X[i])}, ${yScale(Y[i])})`})
        .append('circle').attr("r",markersize)
        .style("fill", function (d, i) {
            return colorScale(island[i])
        })
    // x and y Axis function
    let x_axis = d3.axisBottom(xScale).ticks(4)
    let y_axis = d3.axisLeft(yScale).ticks(4)
    //X Axis
    axis.append("g").attr("class","axis")
        .attr("transform", `translate(${0},${(1000/3)-margin})`)
        .call(x_axis)
    // Y Axis
    axis.append("g").attr("class","axis")
        .attr("transform", `translate(${margin},${0})`)
        .call(y_axis)
    // Labels
    axis.append("g").attr("class","label")
        .attr("transform", `translate(${500/3},${(1000/3)})`)
        .append("text")
        .attr("class","label")
        .text(xLabel)

    axis.append("g")
        .attr("transform", `translate(${35/3},${500/3}) rotate(270)`)
        .append("text")
        .attr("class","label")
        .text(yLabel)



    // Title
    axis.append('text')
        .attr('x',500/3)
        .attr('y',(80)/3)
        .attr("text-anchor","middle")
        .text(title)
        .attr("class","title")

}