/*
function Counter() {
	 this.num = 0;
}

var a = new Counter();
console.log(a.num);
*/



/*
function Counter() {
  this.num = 0;

  this.timer = setInterval(function add() {
    this.num++;
    console.log(this.num); //this bound to global window object
  }, 1000);
}

var b = new Counter();

*/


function Counter() {
  this.num = 0;
var that = this;
  this.timer = setInterval(() => {
    this.num++;
	console.log(this == that);
    console.log(this.num); //this bound to Counter object 
  }, 1000);
}

var b = new Counter();

