# Week 5 - Wednesday 
## Example 4.3
## d3.area generator

<ol>
<li>
Stack Generator needed to stack data:

```
    let stack = d3.stack()
        .keys(['y01', 'y02', 'y03','y04']);
    let stackedSeries = stack(data);
```
</li>
<li>
Area generator to make d attribute for path

```
    let area = d3.area()
            .x(function(d, i) {
                return i * 100;
            })
            .y0(function(d) {
                return yScale(d[0]);
            })
            .y1(function(d) {
                return yScale(d[1]);
            });

```
</li>
<li> append path to svg

```
   svg.selectAll('path')
        .data(stackedSeries)
        .enter()
        .append('path')
        .style('fill', function(d, i) {
            return stackcolors[i];
        })
        .attr('d', area)
```

</li>
</ol>
