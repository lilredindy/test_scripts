
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

  while (time > 0){
    console.log(time);

    this.click(selector, function(result){ 
      if (result.status == 0) { //0 is click success
        bClicked = true;  //NOT WORKING: cannot set global var in local func
      }   
    });

    if (bClicked)
      break;

    if (time < 500)
      this.pause(time);
    else
      this.pause(500);

    time = time -500;
  }


  console.log("bClick is " + bClicked);

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