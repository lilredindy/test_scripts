const prepareBark = dog => {
  const say = `${dog} barked!` 
  console.log("preparing...");
  function cb () {
    console.log(say)
  }
	return cb; //execute cb later
	return cb();//execute cb now
}

//basically a callback is returning a function 
const rogerBark = prepareBark("Roger") 
const sydBark = prepareBark("Syd")

rogerBark()
sydBark()

prepareBark("Roger")
prepareBark("Syd")

