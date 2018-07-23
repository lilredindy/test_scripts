
module.exports.command = function(selector,time,callback) {

  var self = this;

      /*
    //SAYS ELEMENT IS ALWAYS DISPLAYED, EVEN THOUGH IT IS NOT 
    this.element('css selector',selector, function(r){    
      this.elementIdDisplayed(r.value['ELEMENT'], function(r){ console.log(r)});
    });
    */
    //this.waitForElementVisible(selector,1000); //not checking for screen visibility
    //this.waitForElementPresent(selector, 1000); //not checking for screen visibility


  var bClicked = false;


/*
  function httpGetAsync(theUrl, callback)
  {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("POST", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
  }*/




     this.session(function(result) {
     console.log(result.value);
   });



  while (time > 0){
    console.log(time);

    /*
    //THE CLICK CANNOT BE EMBEDDED IN A WHILE B/C THERE IS NO WAY TO BREAK THE LOOP 
    //UPON A SUCCESSFUL CLICK - THIS IS THE NATURE OF THE CALLBACK MECHANISM.
    //THUS CLICKING WILL CONTINUE UNTIL THE TIME EXPIRES
    this.click(selector, function(result){ 
      console.log("the click is done");
      if (result.status == 0) { //0 is click success

      }   
    });*/

    console.log("bClick is " + bClicked);


    if (time < 500)
      this.pause(time);
    else
      this.pause(500);

    time = time -500;
  }



  this.execute(
    function(x) { 
      return x;
    },

    [bClicked], // arguments array to be passed

    function(result) {
      if (typeof callback === "function") {
        callback.call(self, result);
      }
    }
  );

  return this;
};