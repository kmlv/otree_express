var vm = new Vue({
    components: {
        rangeSlider: RangeSlider
    },
    el: '#app',
    data: function() {
        return Object.assign({
            // DO NOT CHANGE THE FOLLOWING
            prob: {
                a: 0,
                b: 100
            },
            radius: {
                a: 0,
                b: 100
            },
            graph: {
                currentLength: 0,
                svg: null,
                x: null,
                xAxis: null,
                y: null,
                yAxis: null,
                line: null,
                minX: 0,
                maxX: 0,
                minY: 0,
                maxY: 0
            },
            tip: [],
            minMax: [],
            graphData: [],
            selected: [],
            equations: []
        }, appSpecific);
    },
    computed: {
        dimension: function() {
            return {
                width: this.width - this.margin.left - this.margin.right,
                height: this.height - this.margin.top - this.margin.bottom
            }
        }
    },
    watch: {
        'prob.a': function(val, old) {
            this.prob.b = this.constants.maxArea - val;

            var areaA = this.constants.k * val
            var areaB = this.constants.k * this.prob.b

            this.radius.a = Math.pow(areaA / Math.PI, 1);
            this.radius.b = Math.pow(areaB / Math.PI, 1)

            d3.select('[line-index="a"]')
            .attr('r', this.radius.a)
            d3.select('[line-index="b"]')
            .attr('r', this.radius.b)

            this.tip.a.text('(' + this.equation.a.x + ', ' + this.equation.a.y + ') ' + this.prob.a.toFixed(0) + '% ')
            this.tip.b.text('(' + this.equation.b.x + ', ' + this.equation.b.y + ') ' + this.prob.b.toFixed(0) + '% ')
        }
    },
    methods: {
        fn: function(index, x) {
            // m = px * x + py * y
            // so, solve for y , y = m/py - px/py * x
            if (this.mode === 'probability') {
                return this.equation.a.x === x ? this.equation.a.y : this.equation.b.y;
            }else{
                return this.equations[index].m / this.equations[index].py - this.equations[index].px / this.equations[index].py * x;
            }
        },
        fnInverse: function(index, y) {
            if (this.mode === 'probability') {
                return this.equation.a.y === y ? this.equation.a.x : this.equation.b.x;
            }else{
                return this.equations[index].m / this.equations[index].px - this.equations[index].py / this.equations[index].px * y;
            }
        },
        // plots the utility function with step size
        plots: function() {
            if (this.mode === 'probability') {
                var points = [];
                points.push(this.equation.a)
                points.push(this.equation.b)
                this.graphData.push(points)
                return;
            }
            for (var index = 0; index < this.equations.length; index++) {
                this.graphData[index] = [];
                this.graphData[index].push({
                    x: 0,
                    y: this.fn(index, 0)
                })
                this.graphData[index].push({
                    x: this.fnInverse(index, 0),
                    y: 0
                })
            }
        },

        // d3.js
        reset: function() {
            this.equations = []
            this.tip = []
            this.minMax = []
            this.graphData = []
            this.selected = []
            this.equations = []
        },
        sanity: function() {
            this.equations.push(this.equation)
            if (this.mode === 'single') return;
            switch (this.mode) {
                case 'probability':
                this.equations = [];
                this.equations.push({
                    m: 0,
                    py: 0,
                    px: 0
                });
                break;
                case 'independent':
                case 'positive':
                this.equations.push({
                    m: this.equations[0].m,
                    py: this.equations[0].py,
                    px: this.equations[0].px
                })
                break;
                case 'negative':
                this.equations.push({
                    m: this.equations[0].m,
                    py: this.equations[0].px,
                    px: this.equations[0].py
                })
                break;
                default:
                break;
            }
        },
        init: function() {
            var self = this;

            this.graph.svg = d3.select('.graph')
            .append('svg')
            .attr('width', this.dimension.width + this.margin.left + this.margin.right)
            .attr('height', this.dimension.height + this.margin.top + this.margin.bottom)
            .append('g')
            .attr('transform', 'translate(' + this.margin.left + ',' + this.margin.top + ')')

            var length = 0;

            if (this.mode === 'probability') {
                length = 1;
            }else{
                length = this.equations.length
            }

            this.graph.x = d3.scaleLinear()
            .range([0, this.dimension.width])

            this.graph.y = d3.scaleLinear()
            .range([this.dimension.height, 0])

            this.graph.line = d3.line().x(function(d) {
                return self.graph.x(d.x)
            }).y(function(d) {
                return self.graph.y(d.y)
            })

            this.graph.minX = Math.min.apply(null, this.graphData.map(function(d) {
                return Math.min.apply(null, d.map(function(c) {
                    return c.x
                }))
            }))
            this.graph.maxX = Math.max.apply(null, this.graphData.map(function(d) {
                return Math.max.apply(null, d.map(function(c) {
                    return c.x
                }))
            }))
            this.graph.minY = Math.min.apply(null, this.graphData.map(function(d) {
                return Math.min.apply(null, d.map(function(c) {
                    return c.y
                }))
            }))
            this.graph.maxY = Math.max.apply(null, this.graphData.map(function(d) {
                return Math.max.apply(null, d.map(function(c) {
                    return c.y
                }))
            }))

            for (var i = 0; i < this.equations.length; i++) {
                this.minMax[i] = {};
                this.minMax[i].minX = Math.min.apply(null, this.graphData[i].map(function(d) {
                    return d.x
                }))
                this.minMax[i].maxX = Math.max.apply(null, this.graphData[i].map(function(d) {
                    return d.x
                }))
                this.minMax[i].minY = Math.min.apply(null, this.graphData[i].map(function(d) {
                    return d.y
                }))
                this.minMax[i].maxY = Math.max.apply(null, this.graphData[i].map(function(d) {
                    return d.y
                }))
            }

        },
        drawAxis: function() {
            var tickStep = 10;
            var xTicks = [], x = 0, yTicks = [], y = 0;
            do {
                xTicks.push(x)
                x += tickStep;
            } while(x <= (this.scale.type === 'fixed' ? this.scale.max : this.graph.maxX))

            do {
                yTicks.push(y)
                y += tickStep;
            } while(y <= (this.scale.type === 'fixed' ? this.scale.max : this.graph.maxY))

            this.graph.xAxis = d3.axisBottom(this.graph.x).tickValues(xTicks);
            this.graph.yAxis = d3.axisLeft(this.graph.y).tickValues(yTicks);

            this.graph.svg.append('g')
            .attr('transform', 'translate(0, ' + this.dimension.height + ')')
            .call(this.graph.xAxis)

            this.graph.svg.append('text')
            .attr('transform', 'translate(' + (this.dimension.width / 2) + ', ' + (this.dimension.height + this.margin.top + 15) + ')')
            .style('text-anchor', 'middle')
            .text(this.label.x)

            this.graph.svg.append('g')
            .call(this.graph.yAxis)

            this.graph.svg.append('text')
            .attr('transform', 'rotate(-90)')
            .attr('y', 0 - this.margin.left)
            .attr('x', 0 - (this.dimension.height / 2))
            .attr('dy', '1em')
            .style('text-anchor', 'middle')
            .text(this.label.y)
        },
        // draw the equation with d3.js
        draw: function() {
            var self = this;

            if (this.scale.type === 'dynamic') {
                this.graph.x.domain([0, this.graph.maxX])
                this.graph.y.domain([0, this.graph.maxY])
            }else{
                this.graph.x.domain([0, this.scale.max])
                this.graph.y.domain([0, this.scale.max])
            }

            for (var index = 0; index < this.equations.length; index++) {
                this.graph.svg.append('path')
                .attr('class', 'line')
                .attr('d', this.graph.line(this.graphData[index]))
            }
        },
        showSelect: function() {
            var self = this;

            var randomX;

            var length = 0;

            if (this.mode === 'probability') {
                length = 1;
            }else{
                length = this.equations.length
            }

            for (var index = 0; index < length; index++) {

                if (this.mode === 'probability') {
                    randomX = this.equation.a.x;
                }else{
                    if (index === 0) {
                        randomX = (Math.random() * (this.graph.maxX - this.graph.minX) + this.graph.minX);
                    }else{
                        var currentXValue = self.fnInverse(index, randomX);
                        if (currentXValue > self.minMax[index].maxX) currentXValue = self.minMax[index].maxX;
                        if (currentXValue < self.minMax[index].minX) currentXValue = self.minMax[index].minX;
                        randomX = currentXValue
                    }

                    this.$set(this.selected, index, {
                        x: null,
                        y: null
                    })

                    this.selected[index].x = randomX.toFixed(this.precision);
                    this.selected[index].y = self.fn(index, randomX).toFixed(this.precision);

                    self.tip[index] = this.graph.svg
                    .append('text')
                    .attr('x', self.graph.x(randomX))
                    .attr('y', self.graph.y(self.fn(index, randomX)) - 15)
                    .text('(' + self.selected[index].x + ', ' + self.selected[index].y + ')')

                }

                var drag = d3.drag().on('drag', function(d) {
                    var index = d3.select(this).attr('line-index');

                    var xValue = self.graph.x.invert(d3.event.x);
                    if (xValue > self.minMax[index].maxX) xValue = self.minMax[index].maxX;
                    if (xValue < self.minMax[index].minX) xValue = self.minMax[index].minX;
                    var x = self.graph.x(xValue);

                    var yValue = self.fn(index, xValue);
                    var y = self.graph.y(yValue)
                    if (y < 0) y = 0;

                    this.x ? this.x.baseVal.value = x : this.cx.baseVal.value = x;
                    this.y ? this.y.baseVal.value = y : this.cy.baseVal.value = y;
                    self.selected[index].x = xValue.toFixed(self.precision)
                    self.selected[index].y = yValue.toFixed(self.precision)

                    if (self.tip && self.tip[index]) {
                        self.tip[index]
                        .attr('x', x)
                        .attr('y', y - 15)
                        .text('(' + xValue.toFixed(self.precision) + ', ' + yValue.toFixed(self.precision) + ')')
                    }

                    if (self.mode !== 'probability') {
                        var otherIndex = 1 - index;
                        switch (self.mode) {
                            case 'negative':
                            var other = d3.select('[line-index="' + otherIndex + '"]');
                            var otherXValue = self.fnInverse(otherIndex, xValue);
                            if (otherXValue > self.minMax[otherIndex].maxX) otherXValue = self.minMax[otherIndex].maxX;
                            if (otherXValue < self.minMax[otherIndex].minX) otherXValue = self.minMax[otherIndex].minX;
                            var otherX = self.graph.x(otherXValue);

                            var otherYValue = xValue
                            var otherY = self.graph.y(otherYValue)
                            if (otherY < 0) otherY = 0;

                            if (other.attr('cx')) {
                                other.attr('cx', otherX)
                                other.attr('cy', otherY)
                            }else{
                                other.attr('x', otherX)
                                other.attr('y', otherY)
                            }

                            self.selected[otherIndex].x = otherXValue.toFixed(self.precision)
                            self.selected[otherIndex].y = otherYValue.toFixed(self.precision)

                            if (self.tip && self.tip[otherIndex]) {
                                self.tip[otherIndex]
                                .attr('x', otherX)
                                .attr('y', otherY - 15)
                                .text('(' + otherXValue.toFixed(self.precision) + ', ' + otherYValue.toFixed(self.precision) + ')');
                            }

                            break;
                            case 'positive':
                            var other = d3.select('[line-index="' + otherIndex + '"]');

                            if (other.attr('cx')) {
                                other.attr('cx', x)
                                other.attr('cy', y)
                            }else{
                                other.attr('x', x)
                                other.attr('y', y)
                            }

                            self.selected[otherIndex].x = xValue.toFixed(self.precision)
                            self.selected[otherIndex].y = yValue.toFixed(self.precision)

                            if (self.tip && self.tip[otherIndex]) {
                                self.tip[otherIndex]
                                .attr('x', x)
                                .attr('y', y - 15)
                                .text('(' + xValue.toFixed(self.precision) + ', ' + yValue.toFixed(self.precision) + ')')
                            }

                            break;
                        }
                    }
                })

                var generate = function() {
                    if (self.mode === 'probability') {
                        self.prob.a = (Math.random() * (100 - 0) + 0);
                        ['a', 'b'].forEach(function(s) {
                            self.graph.svg.append('circle')
                            .attr('r', self.radius[s])
                            .attr('line-index', s)
                            .attr('cx', function(d) {
                                return self.graph.x(self.equation[s].x)
                            })
                            .attr('cy', function(d) {
                                return self.graph.y(self.fn(index, self.equation[s].x))
                            })
                            self.tip[s] = self.graph.svg
                            .append('text')
                            .attr('x', self.graph.x(self.equation[s].x))
                            .attr('y', self.graph.y(self.fn(index, self.equation[s].x)) - 15)
                            .text('(' + self.equation[s].x + ', ' + self.equation[s].y + ') ' + self.prob[s].toFixed(0) + '% ')
                        })
                        return;
                    }
                    if (index === 0) {
                        return self.graph.svg.append('circle')
                        .attr('r', 5)
                        .attr('line-index', index)
                        .attr('cx', function(d) {
                            return self.graph.x(randomX)
                        })
                        .attr('cy', function(d) {
                            return self.graph.y(self.fn(index, randomX))
                        }).call(drag)
                    }else{
                        return self.graph.svg.append('rect')
                        .attr('width', 10)
                        .attr('height', 10)
                        .attr('line-index', index)
                        .attr('x', function(d) {
                            return self.graph.x(randomX)
                        })
                        .attr('y', function(d) {
                            return self.graph.y(self.fn(index, randomX))
                        }).call(drag)
                    }
                }
                generate();
            }
        },
        start: function() {
            this.reset();
            this.sanity()
            this.plots()
            this.init()
            this.draw()
            this.drawAxis()
            this.showSelect()
        },
        update: function() {
            d3.select('svg').remove();
            this.start();
        }
    },
    mounted: function() {
        this.start();
    }
})
