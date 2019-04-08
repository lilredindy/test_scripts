var myMap = new Map();
myMap.set(NaN, 'not a number');

console.log(myMap.get(NaN)); // "not a number"

var otherNaN = Number('foo');
console.log(myMap.get(otherNaN)); // "not a number"


