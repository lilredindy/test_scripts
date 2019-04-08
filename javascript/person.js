function Person(first, last, age, gender, interests) {
  
  // property and method definitions
  this.first = first;
  this.last = last;
//...
}

var person1 = new Person('Bob', 'Smith', 32, 'male', ['music', 'skiing']);

console.log(person1.valueOf());

