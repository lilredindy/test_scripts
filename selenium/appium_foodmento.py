import unittest
import logging
import sys
import inspect

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from appium import webdriver
import time

from subprocess import call


global logger
logger = logging.getLogger(__name__) #__name__ == __main__
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)



class FoodmentoSplashScreen():
  CREATE_AN_ACCOUNT_BTN = "CREATE AN ACCOUNT"
  LOG_IN_BTN = "LOG IN"
  LANDING_LOGO = "foodmento-landing-logo.png"
 
  @staticmethod
  def click_login_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoSplashScreen.LOG_IN_BTN).click()
  @staticmethod
  def click_create_acct_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoSplashScreen.CREATE_AN_ACCOUNT_BTN).click()




class FoodmentoLoginPage():
  EMAIL = "Email"
  PASSWORD = "Password"
  LOGIN_BTN = "Login"
  FACEBOOK_LOGIN_BTN = "Facebook Login"


  @staticmethod
  def click_fb_login_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoLoginPage.FACEBOOK_LOGIN_BTN).click()
 
  @staticmethod
  def click_login_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoLoginPage.LOGIN_BTN).click()
  @staticmethod
  def type_email(driver, text):
    driver.find_element_by_accessibility_id(FoodmentoLoginPage.EMAIL).send_keys(text)
  @staticmethod
  def type_password(driver, text):
    driver.find_element_by_accessibility_id(FoodmentoLoginPage.PASSWORD).send_keys(text)



class FoodmentoRegistrationPage():
  FIRST_NAME = "First name"
  LAST_NAME = "Last name"
  EMAIL = "Email"
  PASSWORD = "Password (minimum 6 characters)"
  REGISTER_BTN = "Register"
  DONE_BTN = "Done"
  ARROW_LEFT_BTN = "ArrowLeft"

  @staticmethod
  def type_first_name(driver, text):
    driver.find_element_by_accessibility_id(FoodmentoRegistrationPage.FIRST_NAME).send_keys(text)
  @staticmethod
  def type_last_name(driver, text):
    driver.find_element_by_accessibility_id(FoodmentoRegistrationPage.LAST_NAME).send_keys(text)
  @staticmethod
  def type_email(driver, text):
    driver.find_element_by_accessibility_id(FoodmentoRegistrationPage.EMAIL).send_keys(text)
  @staticmethod
  def type_password(driver, text):
    driver.find_element_by_accessibility_id(FoodmentoRegistrationPage.PASSWORD).send_keys(text)
  @staticmethod
  def click_register_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoRegistrationPage.REGISTER_BTN).click()
  @staticmethod
  def click_done_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoRegistrationPage.DONE_BTN).click()




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


class FoodmentoDiscoverPage:
  DISCOVER_ALL = "Discover all"
  JUST_FOR_YOU = "Just for you"
 
  @staticmethod
  def click_just_for_you_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoDiscoverPage.JUST_FOR_YOU).click()
  def click_discover_all_btn(driver):
    driver.find_element_by_accessibility_id(FoodmentoDiscoverPage.JUST_FOR_YOU).click()


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








    ##################################
    # ACTIONS
    ##################################

class FoodmentoActions():
  @staticmethod
  def is_logged_in(driver):
    #logger.debug(inspect.stack()[0][3])
    try:
      driver.find_element_by_accessibility_id(FoodmentoSplashScreen.LANDING_LOGO)
      return False
    except:
      return True

  @staticmethod
  def fb_login(driver, fb_username, fb_password):
    if (FoodmentoActions.is_logged_in(driver)):
      FoodmentoActions.logout(driver)
    FoodmentoSplashScreen.click_login_btn(driver)
    FoodmentoLoginPage.click_fb_login_btn(driver)
    

  @staticmethod
  def login(driver,username, password):
    #logger.debug(inspect.stack()[0][3])
    if not (FoodmentoActions.is_logged_in(driver)):
      FoodmentoSplashScreen.click_login_btn(driver)
      FoodmentoLoginPage.type_email(driver,username)
      FoodmentoLoginPage.type_password(driver,password)
      FoodmentoLoginPage.click_login_btn(driver)

  @staticmethod
  def force_login(driver,username, password):
    #logger.debug(inspect.stack()[0][3])
    if (FoodmentoActions.is_logged_in(driver)):
      FoodmentoActions.logout(driver)
    FoodmentoSplashScreen.click_login_btn(driver)
    FoodmentoLoginPage.type_email(driver,username)
    FoodmentoLoginPage.type_password(driver,password)
    FoodmentoLoginPage.click_login_btn(driver)
  
 
  @staticmethod
  def logout(driver): 
    #logger.debug(inspect.stack()[0][3])
    if (FoodmentoActions.is_logged_in(driver)):
      FoodmentoMenuBar.click_profile_btn(driver)
      FoodmentoProfilePage.click_settings_btn(driver)
      FoodmentoSettings.click_logout_static_txt(driver)
    
  @staticmethod
  def manual_register(driver, first, last, email, password, referral):
    #logger.debug(inspect.stack()[0][3])

    if (FoodmentoActions.is_logged_in(driver)):
      FoodmentoActions.logout(driver)
    FoodmentoSplashScreen.click_create_acct_btn(driver)
    FoodmentoRegistrationPage.type_first_name(driver, first)
    FoodmentoRegistrationPage.type_last_name(driver, last)
    FoodmentoRegistrationPage.type_email(driver, email)
    FoodmentoRegistrationPage.type_password(driver, password)
    FoodmentoRegistrationPage.click_done_btn(driver)

  @staticmethod
  def fb_register(driver):
    pass



    ##################################
    # SETUP AND TEARDOWN 
    ##################################

class FoodmentoTests(unittest.TestCase):


    def setUp(self):
      logger.debug(inspect.stack()[0][3])

      desired_caps = {
        'platformName': 'iOS',
        #'deviceName': 'Shri\'s iPhone (12.1.2)',
        #'deviceName': 'iPhone (13.6.1)',
        'deviceName': 'iPhone sucks',
        'platformVersion':'10.3',
        #'udid': 'de5c416ac7fc0204ed28879163b4965ab992380c',
        #'udid': '0cb04126a11b0c5454b522f0f78720f0dc80d718',
        'udid': '4443449a13de797bc614c5d0fe785168371a7492',
        'automationName': 'XCUITest',
        'bundleId': 'com.foodmento.foodmento',
        #'bundleId': 'com.apple.calculator',
        #'usePrebuiltWDA': True
      }
      self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

      #self.driver.implicitly_wait(5000) #THIS ACTUALLY WORKS WHEN SWTICHING APPS!!
      #self.driver.reset() #this seems to kill the app nothing more

      #IMPLICIT LOGIN TO AVOID EXPLICIT LOGIN WITHIN TEST...IS THIS BEST???
      #FoodmentoActions.login(self.driver,"lilredindy@gmail.com", "maverick")


    def tearDown(self):
        #FoodmentoActions.logout(self.driver) #
        logger.debug(inspect.stack()[0][3])
        self.driver.quit()






    ##################################
    # A BATTERY OF TESTS 
    ##################################
   
    @unittest.skip("")
    def test_profile_name(self):
      logger.debug(inspect.stack()[0][3])
      FoodmentoActions.login(self.driver,"lilredindy@gmail.com", "maverick")
      FoodmentoMenuBar.click_profile_btn(self.driver)
      name = FoodmentoProfilePage.get_name(self.driver)
      assert(name == "Foo N.")
      #is this test completed???

    
    @unittest.skip("")
    def test_login_with_invalid_email(self):
      logger.debug(inspect.stack()[0][3])
      FoodmentoActions.force_login(self.driver,"lilredindy", "maverick")
      self.driver.find_element_by_accessibility_id("Invalid email") #NoSuchElementException if no alert shown
      self.driver.find_element_by_accessibility_id("OK").click() #NoSuchElementException if no alert shown


    @unittest.skip("")
    def test_login_with_valid_creds(self):
      logger.debug(inspect.stack()[0][3])
      FoodmentoActions.force_login(self.driver,"lilredindy@gmail.com", "maverick")
      #this test is not complete until we assert something....


    
    #@unittest.skip("")
    def test_fb_login(self):
      logger.debug(inspect.stack()[0][3])
      FoodmentoActions.fb_login(self.driver,"lilredindy@gmail.com", "flower45")

      #SWITCH THE CONTEXT OF THE DRIVER (THIS MAY BE ONLY ONE OF MULT WAYS)
      #webview = self.driver.contexts.last
      #self.driver.switch_to.context(webview)
      self.driver.execute_script('mobile: activateApp', {'bundleId': 'com.apple.mobilesafari'})
      #self.driver.delete_all_cookies() ios_webkit proxy it seems...and only cookies assoc w/current webpage
      
      #EXPLICITLY WAIT FOR THE FB LOGIN PAGE TO APPEAR 
      element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Mobile Number or Email")))
      element.send_keys("lilredindy@gmail.com")
      #self.driver.hide_keyboard() #FIXES A BUG 2 SEND CALLS
      element.send_keys(Keys.ENTER) #OR THIS FIXES AS WELL
      
      self.driver.find_element_by_accessibility_id("Password").send_keys("flower45")
      self.driver.find_element_by_accessibility_id("Log In").click()

      #NO GOOD WAY TO CLEAR BROWSER CACHE...
      #this test is not complete until we assert something....
  


    @unittest.skip("")
    def test_registration(self):
      logger.debug(inspect.stack()[0][3])
      FoodmentoActions.manual_register(self.driver, "foo", "bar", "shriamin@yandex.com", "maverick", "")
            #this test is not complete until we assert something....

    
    @unittest.skip("")
    def test_existing_registration_with_diff_pwd(self):
      logger.debug(inspect.stack()[0][3])
      FoodmentoActions.manual_register(self.driver, "foo", "bar", "shriamin@yandex.com", "maverick123", "")
      self.driver.find_element_by_accessibility_id("Dismiss").click() #NoSuchElementException if no alert shown

    @unittest.skip("")
    def test_registration_with_missing_last_name(self):
      logger.debug(inspect.stack()[0][3])
      FoodmentoActions.manual_register(self.driver, "foo", "", "shriamin@yandex.com", "maverick123", "")
      self.driver.find_element_by_accessibility_id("Please enter a last name.") #NoSuchElementException if no alert shown
      self.driver.find_element_by_accessibility_id("OK").click() #NoSuchElementException if no alert shown

 


if __name__ == '__main__':
    unittest.main()
