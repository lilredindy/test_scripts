var myMap = new Map();
var keyString = 'foo';
var keyObj = {};
var keyFunc = function() {};

// setting the values
myMap.set(keyString, "value a");
myMap.set(keyObj, 'value b');
myMap.set(keyFunc, 'value d');

console.log(myMap);

myMap.size; // 3

// getting the values
myMap.get(keyString);    // "value a"
myMap.get(keyObj);       // "value b"
myMap.get(keyFunc);      // "value d"

console.log(myMap.get(keyString));   // "value a" because keyString === 'foo'
console.log(myMap.get({}));           // undefined, because keyObj !== {}
console.log(myMap.get(function() {})); // undefined, because keyFunc !== function () {}



