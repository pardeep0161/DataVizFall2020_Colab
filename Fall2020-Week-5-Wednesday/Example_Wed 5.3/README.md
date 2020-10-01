# Week 5 - Wednesday 
## Example 4.3
## d3.stack generator

<ol>
<li>
Generator:

```
    let stack = d3.stack()
        .keys(['y01', 'y02', 'y03','y04']);
    let stackedSeries = stack(data);
```
</li>
<li>
Svg element

```
    let svg = d3.select('svg#main')

    let groups = svg.selectAll('g')
        .data(stackedSeries)
        .enter()
        .append('g')
        .style('fill', function(d, i) {
            return stackcolors[i];
        });

```
</li>

<li> append "rect" to each of "groups" elements

```
 groups.selectAll('rect')
        .data(function(d) {
            return d;
        })
        .enter()
        .append('rect')
        .attr('width', function(d) {
            return d[1] - d[0];
        })
        .attr('x', function(d) {
            return d[0];
        })
        .attr('y', function(d, i) {
            return i * 20;
        })
        .attr('height', 20);

```


</li>
</ol>
