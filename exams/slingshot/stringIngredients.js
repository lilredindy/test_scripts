function is_word(input){

	return true
}


function count_words(words){
	var D = {};

	for (var i = 0; i < words.length; ++i){

		if (words[i].length == 0) 
			throw ("empty word found!");
			

		if (D[words[i]] != undefined)
			D[words[i]] += 1
		else
			D[words[i]] = 1
	}

	return D;

}

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter input: ', (the_input) => {

	//var possible_words = the_input.trim().split(' ');

	if (the_input.length == 0){
		console.log("no input given...");
		rl.close();
		return;
	}

	the_input = the_input.replace(/(^,)|(,$)/g, "") //edge case
	possible_words = the_input.trim().split(/[ ,./;:"]+/); //trim whitespace + split

  	console.log(possible_words);

  	D = count_words(possible_words);

  	for (var key in D)
  		console.log(key, D[key])
  	//console.log(`${is_palindrome(word)}`);

  	rl.close();
});