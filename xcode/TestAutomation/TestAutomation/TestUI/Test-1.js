var testName = "Test 1";

var target = UIATarget.localTarget();

UIALogger.logMessage(target.model());
UIALogger.logMessage(target.systemName());
UIALogger.logMessage(target.systemVersion());


var app = target.frontMostApp();

var window = app.mainWindow();


//--
UIALogger.logStart( testName );


app.logElementTree();

window.tabBar().buttons()["Second"].tap();

app.logElementTree();

//var len = window.elements.length;

//UIALogger.logMessage("crap "+ len);

/*
var foo = window.elements();

for (i=0;i<foo.length;++i)
{
    foo[i].logElement();
}

for (i=0;i<foo.length;++i)
{
    UIALogger.logMessage(foo[i].name())
}


//test for existence of toolbar
window.toolbar().logElement();
if (window.toolbar())
    UIALogger.logFail( testName + ": window toolbar is true" );
if (!window.toolbar().isValid())
    UIALogger.logPass( testName + ": window toolbar is not valid" );


//test for static text
UIALogger.logFail( testName + ": window has " + window.staticTexts().length + " static text fields");
if (window.staticTexts()["First View"].isValid())
{
    UIALogger.logPass( testName + ": static text with name 'First View' is valid");
    window.staticTexts()["First View"].tap();
    window.staticTexts()["First View"].doubleTap();
    target.captureScreenWithName("screenshot1");
}
else
UIALogger.logFail( testName + ": static text with name 'First View' is not valid" );


if (!window.staticTexts()["RecipeName"].checkIsValid())
UIALogger.logFail( testName + ": static text with name 'RecipeName' is not valid");


if (window.staticTexts()["First View"].isEnabled())
UIALogger.logPass( testName + "'first view' element is enabled");

if (window.textFields()["User Text"].isEnabled())
UIALogger.logPass( testName + "'USER TEXT' element is enabled");

if (window.staticTexts()["The text is"].isEnabled())
UIALogger.logPass( testName + "'The text is' element is enabled");

if (window.staticTexts()["RecipeName"].isEnabled())
UIALogger.logPass( testName + "'Recipe Name' element is enabled");

/*
//-- select the elements
UIALogger.logMessage( "Select the first tab" );

var tabBar = app.tabBar();
var selectedTabName = tabBar.selectedButton().name();
if (selectedTabName != "First") {
	tabBar.buttons()["First"].tap();
}



//-- tap on the text fiels
UIALogger.logMessage( "Tap on the text field now" );

var recipeName = "Unusually Long Name for a Recipe";
window.textFields()[0].setValue(recipeName);

target.delay( 10 );

//-- tap on the text fiels
UIALogger.logMessage( "Dismiss the keyboard" );


var x = app.keyboard().keys();
//app.logElementTree();

var x = app.keyboard().keys();
//UIATarget.localTarget().frontMostApp().keyboard().keys()["a"].tap();
//UIATarget.localTarget().frontMostApp().keyboard().keys()["return"].tap();

target.delay( 10 );

UIATarget.localTarget().frontMostApp().keyboard().typeString("Hello world\n");
target.delay( 10 );

for (i=0;i<x.length;++i)
{
    x[i].logElement();
}

/*
var textValue = window.staticTexts()["RecipeName"].value();

UIALogger.logMessage( "text value=" + textValue  );


if (textValue === recipeName){
	UIALogger.logPass( testName ); 
}
else{
	UIALogger.logFail( testName ); 
}
*/