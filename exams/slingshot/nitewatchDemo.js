
module.exports = {
  'Demo test Google' : function (browser) {
    browser
      .url('http://www.google.com')
      .waitForElementVisible('body', 1000)
      .setValue('input[type=text]', 'nightwatch')
      //.waitForElementVisible('input[name=btnK]', 1000) //
      //.click('input[name=btnK]')
      .waitAndClick('input[name=btnK]',5000, function(result){
           this.assert.ok(result.value);
      })
      .pause(1000) //if click occurs wait for page to load
      .assert.containsText('#main', 'Night Watch')
      .end();
  }
};

