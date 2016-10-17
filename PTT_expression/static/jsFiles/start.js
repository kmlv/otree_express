//var Game = angular.module('Game', []);

//Game.controller("gameController",

angular.module('Game', []).controller("gameController",
    ["$rootScope", "$scope", "$sce", "$timeout", function($rootScope, $scope, $sce, $timeout)
{
    // config files
    $scope.parsedIncome = 0;
    $scope.incomegoal = 10;
    $scope.treatment = 1;

    $scope.showpage = {
        beforeGame: true,
        game: true,
        setup: true
    };

    $scope.income = 0;
    $scope.totalincome = 0;
    $scope.taskGoal = 5;
    $scope.task = 1;

    // time variables
    $scope.timelimit = 35;
    $scope.time = 35;
    $scope.practiceRound = 1;
    $scope.validClick = false;


    // finishes questions onto money part
    // barrier : have all people ready for part 2
    $scope.practiceTimeout = function() {
      $scope.time--;
      if ($scope.time < 1) {
      } else
        $scope.mytimeout = $timeout($scope.practiceTimeout,1000);
    };
    $scope.onTimeout = function() {
      $scope.time--;
      if ($scope.time < 1) {
        console.log("Times up");
        $scope.nexttask();
      }
      else $scope.mytimeout = $timeout($scope.onTimeout,1000);
    };

    $scope.showgame = function() {
        var targetIncome = $('#target').val();
        $scope.incomegoal = targetIncome;
        console.log('scope goal', $scope.incomegoal);
        console.log('from jquery ',  targetIncome);
        console.log("task ", $scope.task);

        var gameType = $('#type').val();
        console.log('type', gameType);
        if (gameType === 'practice'){
            $scope.taskGoal = 2;
        }

        $scope.showpage.beforeGame = true;
        $scope.showpage.game = true;
        $scope.showpage.setup = true;

      //start tooltip
        /*
      $('[data-toggle="instructions"]').popover({
        html: true,
        trigger: 'focus hover'
      });
*/
      $scope.points = [];
      $scope.plot = $.plot("#placeholder",[{
          data: $scope.points,
          points: {
            show : true,
            fill: true,
            fillColor: '#DAA831'
          },
          color: '#FFCD72'
        }], {
          xaxis: {
              ticks:10,
              min:0,
              max:100
          },
          yaxis: {
              ticks:10,
              min:0,
              max:100,
              position: 'left'
          },
          grid: {
            clickable: true
          }
      });

      $scope.locatorState = new LocatorState(document.getElementById("locator"),
                                            "#points", false, "#nearness", "#location");

      $scope.locatorState.setGoal();
      $scope.locatorState.reset();

        $("#placeholder").bind("plotclick", function(event, pos, item) {
            if(pos.x < 0) pos.x = 0.5;
            if (pos.y < 0) pos.y = 0.5;
            if(pos.y > 100) pos.y = 100;
            if (pos.x > 100) pos.x = 100;
          console.log('x ' + pos.x + ' y : ' + pos.y);
          $scope.points.pop();
        $scope.points.push([pos.x, pos.y]);
            if(pos.x != 0 || pos.y != 0){
                $scope.validClick = true;
            }

        console.log($scope.maxpoints);

        $scope.plot.setData([{
          data: $scope.points,
          clickable: false,
          points: {
            show: true,
            fill: true,
            fillColor: '#DAA831',
            radius: 10
          },
          color: '#FFCD72'
        }]);
        $scope.plot.draw();
        $scope.locatorState.update(pos);
        $scope.locatorState.draw();
      });

      $timeout.cancel($scope.mytimeout);
      $scope.time = $scope.timelimit;
      $scope.mytimeout = $timeout($scope.onTimeout,1000);
    };

    $scope.nexttask = function() {
        if ($scope.income > $scope.incomegoal * 100  || $scope.task >= $scope.taskGoal) {
          $timeout.cancel($scope.mytimeout);
          console.log("done with game.");
          $scope.showpage.game = false;
            $("#hideNext").show();
          console.log("income : " + $scope.income);
            return;
        }

        if(!$scope.validClick) return;

        $scope.task++;
        console.log("task ", $scope.task);
        $scope.income += $scope.locatorState.getPointvalue();
        $scope.maxpoints = (Math.floor(Math.random() * 80) + 40);// * $scope.scale;
        $("#income").text("So far, your income is $" +
          $scope.floatToMoney($scope.income).toFixed(2) + ".");
        // save income as integer
        $scope.parsedIncome = $scope.floatToMoney($scope.income).toFixed(2);
        $('#task_reward').val($scope.parsedIncome);
        console.log('totalIncome ', $scope.income);
        console.log('parsedIncome', $scope.parsedIncome);
        console.log('saved income to div ', $('#task_reward').val());

        // reaches income goal or passes max number of tasks, done with game
         //else {
          //$scope.task++;
          $scope.points.pop();
          $scope.plot.setData([$scope.points]);
          $scope.plot.draw();
          $scope.locatorState.setGoal();
          $scope.locatorState.point.update(0);
          $scope.locatorState.reset();

          $timeout.cancel($scope.mytimeout);
          $scope.time = $scope.timelimit;
          $scope.mytimeout = $timeout($scope.onTimeout,1000);
        //}
  };

    $scope.floatToMoney = function(number) {
      return parseFloat(parseInt(number)) / 100;
    };

    function Point(x, y, radius) {
      this.x = x || 0;
      this.y = y || 0;
      this.value = 0;
      this.radius = radius || 10;
      this.fill = "#EEEEEE";
    }

    Point.prototype.update = function(value) {
      this.value = value;
    };

    Point.prototype.draw = function(ctx) {
      // draws triangle
      /*
      var path = new Path2D();
      var l = this.radius * Math.sqrt(3) / 4;
      path.moveTo(this.x, this.y - this.value - l);
      path.lineTo(this.x - this.radius, this.y - this.value + l);
      path.lineTo(this.x + this.radius, this.y  - this.value + l);
      ctx.fill(path);
      */
      ctx.beginPath();
      ctx.arc(this.x, this.y - this.value, this.radius, 0, 2*Math.PI);
      ctx.fillStyle = '#CC1600';
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = '#660B00';
      ctx.stroke();
    };

    Point.prototype.reset = function(ctx) {
        $scope.validClick = false;
      this.value = 0;
      this.draw(ctx);
    };

    function LocatorState(canvas, pointsLocation, practice, nearid, locationid, maxpoints) {
      this.canvas = canvas;
      this.pointsLocation = pointsLocation;
      this.nearid = nearid;
      this.locationid = locationid;
      this.practice = practice;
      this.width = canvas.width;
      this.height = canvas.height;
      this.ctx = canvas.getContext('2d');
      this.side = "right";
      this.direction = "up";
      this.location = "Click";
      this.distance = null;
      this.goal = {
        x: null,
        y: null
      };
      this.pointvalue = 0;
      this.linelength = 3 * this.height / 4;
      this.maxlength = Math.sqrt(square(100 - 0) + square(100 - 0));

      this.point = new Point(this.width / 2, this.height * 7 / 8, 15);
      $scope.maxpoints = (Math.floor(Math.random() * 80) + 20);// * $scope.scale;

      if (this.practice) $scope.maxpoints = maxpoints;// * $scope.scale;

      $(this.pointsLocation).text("0.0");
    }

    LocatorState.prototype.getPointvalue = function() {
      return this.pointvalue;
    };

    LocatorState.prototype.setGoal = function() {
      this.goal = {
        x: Math.floor(Math.random() * 100),
        y: Math.floor(Math.random() * 100)
      };
    };

    $scope.maxpoints = 0;
    LocatorState.prototype.update = function(guess) {
      if ($scope.debug) console.log("goal ", this.goal);
      this.distance = Math.sqrt(square(this.goal.x - guess.x) + square(this.goal.y - guess.y));
      this.distance < 20 ? this.location = "Close!" : this.location = "Far!";
      // update locator position
      this.pointvalue = $scope.maxpoints - this.distance * $scope.maxpoints / this.maxlength;
      var linescale = this.pointvalue * this.linelength / $scope.maxpoints;
      this.point.update(linescale);
      if (!this.practice)
        $("#earned").text("Money earned for this task (cents) : " + parseFloat(this.pointvalue).toFixed(1));
      $(this.pointsLocation).text(parseFloat(this.pointvalue).toFixed(1));

      guess.x > this.goal.x ? this.side = "left" : this.side = "right";
      guess.y > this.goal.y ? this.direction = "down" : this.direction = "up";
    };

    function square(x) {
      return x * x;
    }

    // clears canvas
    LocatorState.prototype.clear = function() {
      this.ctx.clearRect(0,0,this.width,this.height);
    };

    // draws inital locator
    LocatorState.prototype.draw = function() {
      this.clear();

      // draws text
      $(this.nearid).text(this.location);
      $(this.locationid).text("Go " + this.side + "-" + this.direction);
      // draws line
      this.ctx.beginPath();
      this.ctx.moveTo(this.width / 2, this.height / 8);
      this.ctx.lineTo(this.width / 2, this.height / 8 + this.linelength);
      this.ctx.lineWidth = 6;
      this.ctx.strokeStyle = '#660B00';
      this.ctx.stroke();

      // draws numbers

      // draw locator
      this.point.draw(this.ctx);
    };

    LocatorState.prototype.reset = function() {
      $(this.nearid).text("Click inside the square");
      $(this.locationid).text("");
      $(this.pointsLocation).text("0.0");

      this.clear();
      // draw line
      this.ctx.beginPath();
      this.ctx.moveTo(this.width / 2, this.height / 8);
      this.ctx.lineTo(this.width / 2, this.height / 8 + this.linelength);
      this.ctx.lineWidth = 6;
      this.ctx.stroke();
      // draw point
      this.point.reset(this.ctx);
    };

  }]);
