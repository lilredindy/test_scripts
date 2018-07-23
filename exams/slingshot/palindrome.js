'use strict';
function is_palindrome(input){

	for (var i = 0; i < input.length/2; ++i){
		if (input.charAt(i) != input.charAt(input.length-1-i)){
			//console.log("%s is not a palindrome", input);
			return false;
		}
	}
	//console.log("%s is a palindrome", input);
	return true;
}


//is_palindrome("noon");

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter a word: ', (word) => {
	if (is_palindrome(word))
		console.log('%s is a palindrome',word)
	else
		console.log('%s is not a palindrome',word)

  	//console.log(`${is_palindrome(word)}`);

  	rl.close();
});


