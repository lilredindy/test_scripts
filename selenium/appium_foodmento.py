import unittest
import sys

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium import webdriver
import time

from subprocess import call


class FoodmentoProfilePage():
  ICON_SETTING_WHITE_35 = "icon setting white 35"
  ICON_ADDFRIENDS_WHITE_30 ="icon addfriends white 30"
  NAME = "//XCUIElementTypeStaticText[@name=\"Foo N.\"]"
  FOLLOWERS = "//XCUIElementTypeButton[@name=\"0 followers\"]"
  FOLLOWING = "//XCUIElementTypeButton[@name=\"6 following\"]"
  PLACES = "Places"
  DISHES = "Dishes"
  LOVED = "Loved"
  WANTS = "Wants"

  @staticmethod #vs @classmethod??
  def click_places_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoProfilePage.PLACES).click()
  @staticmethod
  def click_dishes_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoProfilePage.DISHES).click()
  @staticmethod
  def click_loved_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoProfilePage.LOVED).click()
  @staticmethod
  def click_wants_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoProfilePage.WANTS).click()
  @staticmethod
  def get_name(driver):
    return driver.find_element_by_xpath(FoodmentoProfilePage.NAME).get_attribute("value")  
  @staticmethod
  def click_settings_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoProfilePage.ICON_SETTING_WHITE_35).click()
  @staticmethod
  def click_addfriends_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoProfilePage.ICON_ADDFRIENDS_WHITE_30).click()


class FoodmentoSettings():
  LOGOUT = "Logout"
 
  @staticmethod
  def click_logout_static_txt(driver):
    driver.find_element_by_accessibility_id(FoodmentoSettings.LOGOUT).click()



class FoodmentoMenuBar():
  PROFILE_WHITE_40 = "profile white 40"
  NOTIFICATION_WHITE_40 = "notification white 40"
  PLUS_WHITE_40= "plus white 40"
  SEARCH_WHITE_40 = "search white 40"
  HOME_WHITE_41 = "home white 41"

  @staticmethod
  def click_profile_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoMenuBar.PROFILE_WHITE_40).click()
  @staticmethod
  def click_notification_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoMenuBar.NOTIFICATION_WHITE_40).click()
  @staticmethod
  def click_plus_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoMenuBar.PLUS_WHITE_40).click()
  @staticmethod
  def click_search_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoMenuBar.SEARCH_WHITE_40).click()
  @staticmethod
  def click_home_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoMenuBar.HOME_WHITE_41).click()



class FoodmentoSplashScreen():
  CREATE_AN_ACCOUNT = "CREATE AN ACCOUNT"
  LOG_IN = "LOG IN"
  LANDING_LOGO = "foodmento-landing-logo.png"
 
  @staticmethod
  def click_login_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoSplashScreen.LOG_IN).click()
  @staticmethod
  def click_create_acct_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoSplashScreen.CREATE_AN_ACCOUNT).click()


class FoodmentoLoginPage():
  EMAIL = "Email"
  PASSWORD = "Password"
  LOGIN = "Login"
 
  @staticmethod
  def click_login_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoLoginPage.LOGIN).click()
  @staticmethod
  def type_email(driver, text):
    driver.find_element_by_accessibility_id(FoodmentoLoginPage.EMAIL).send_keys(text)
  @staticmethod
  def type_password(driver, text):
    driver.find_element_by_accessibility_id(FoodmentoLoginPage.PASSWORD).send_keys(text)


class FoodmentoDiscoverPage:
  DISCOVER_ALL = "Discover all"
  JUST_FOR_YOU = "Just for you"
 
  @staticmethod
  def click_just_for_you_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoDiscoverPage.JUST_FOR_YOU).click()
  def click_discover_all_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoDiscoverPage.JUST_FOR_YOU).click()


class FoodmentoActions():
  @staticmethod
  def is_logged_in(driver):
    try:
      driver.find_element_by_accessibility_id(FoodmentoSplashScreen.LANDING_LOGO)
      return False
    except:
      return True

  @staticmethod
  def login(driver,username, password):
    if not (FoodmentoActions.is_logged_in(driver)):
      FoodmentoSplashScreen.click_login_btn(driver)
      FoodmentoLoginPage.type_email(driver,username)
      FoodmentoLoginPage.type_password(driver,password)
      FoodmentoLoginPage.click_login_btn(driver)
      #self.click_login_btn()
      #self.driver.find_element_by_accessibility_id('Email').send_keys(username); 
      #self.driver.find_element_by_accessibility_id('Password').send_keys(password);
      #self.driver.find_element_by_accessibility_id('Login').click()
    else:
      print("already logged in!")
 
  @staticmethod
  def logout(driver): 
    #should logout check if user is logged in? 
    if (FoodmentoActions.is_logged_in(driver)):
      FoodmentoMenuBar.click_profile_btn(driver)
      FoodmentoProfilePage.click_settings_btn(driver)
      FoodmentoSettings.click_logout_static_txt(driver)
    else:
      print ("already logged out!") #is this type of thing needed???

    


class FoodmentoTests(unittest.TestCase):

    def setUp(self):
      print ("setup")
      desired_caps = {
        'platformName': 'iOS',
        'deviceName': 'iPhone sucks (10.3.3)',
        'platformVersion':'',
        'udid': '4443449a13de797bc614c5d0fe785168371a7492',
        'automationName': 'XCUITest',
        'bundleId': 'com.foodmento.foodmento',
        #'usePrebuiltWDA': True
      }
      self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

      #IMPLICIT LOGIN TO AVOID EXPLICIT LOGIN WITHIN TEST...IS THIS BEST???
      FoodmentoActions.login(self.driver,"lilredindy@gmail.com", "maverick")


    def tearDown(self):
        print ("teardown")
        #FoodmentoActions.logout(self.driver)
        #self.driver.quit()






    ##################################
    # A BATTERY OF TESTS 
    ##################################
   
    @unittest.skip("")
    def test_profile_name(self):
      print ("test_profile_name")
      FoodmentoMenuBar.click_profile_btn(self.driver)
      name = FoodmentoProfilePage.get_name(self.driver)
      print (name)
      assert(name == "Foo N.")
      #is this test completed???

    
    @unittest.skip("")
    def test_login_with_invalid_email(self):
      print ("test_login_with_invalid_email")
      FoodmentoActions.logout(self.driver)  #b/c setup() calls login()....is this good???
      FoodmentoActions.login(self.driver,"lilredindy", "maverick")
      #this test is not complete until we assert something....
      #old code below before re-factor into classes
      #self.driver.find_element_by_accessibility_id('LOG IN').click()
      #self.driver.find_element_by_accessibility_id('Email').send_keys("lilredindy"); #invalid email
      #self.driver.find_element_by_accessibility_id('Password').send_keys("maverick");
      #self.driver.find_element_by_accessibility_id('Login').click()

    #@unittest.skip("")
    def test_login_with_valid_creds(self):
      print ("test_login_with_valid_creds")
      FoodmentoActions.logout(self.driver) #b/c setup() calls login()....is this good???
      FoodmentoActions.login(self.driver,"lilredindy@gmail.com", "maverick")
      #this test is not complete until we assert something....
      #old code below before re-factor into classes
      #self.driver.find_element_by_accessibility_id('LOG IN').click()
      #self.driver.find_element_by_accessibility_id('Email').send_keys("lilredindy@gmail.com"); #invalid email
      #self.driver.find_element_by_accessibility_id('Password').send_keys("maverick");
      #self.driver.find_element_by_accessibility_id('Login').click()


      

if __name__ == '__main__':
    unittest.main()