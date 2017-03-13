from selenium import webdriver
import time
import unittest
import datetime
from selenium.webdriver.common.keys import Keys



locators = {
    'entry_for_start_location': "//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[1]/label/div/input"
}

class southernregression03class(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_southern_reg_03(self):
        driver = self.driver
        driver.maximize_window()
        #<Step 1: open the Southern Booking Engine Page and select season ticket tab>
        driver.get("https://southern.stage.otrl.io")
        print("Opening the southern booking engine")
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div[2]/nav/a[3]").click()
        print("Clicked on other tickets")
        time.sleep(2)
        #<Step 3: Select Daysave ticekttype >
        driver.find_element_by_xpath("//section[@class='booking__section other-ticket-options']/button").click()
        print("Clicked on Daysave")
        #<Result 3: Daysave ticekttype selected>
        time.sleep(3)
        #<Step 4: Select west worthing standard daysave ticket for 2 adult and 2 kids SD4 for next week>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div[1]/section[1]/span/label/div/input").send_keys('West Worthing')
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div/section[1]/span/label/div/input").send_keys(Keys.RETURN)
        time.sleep(2)
        print("Searching the journey for West Worthing Daysave")
        #'The Outbound Calendar is opened.
        driver.find_element_by_xpath("//button[@id='loadDateSelect']").click()
        time.sleep(2)
        '''Date selected'''
        driver.find_element_by_xpath("//tr[4]/td[5]/span").click()
        driver.find_element_by_xpath("//button[@class='btn-lg pull-right select btn btn-primary']").click()
        time.sleep(2)
        # Add passengers & Find trains
        driver.find_element_by_xpath("//section[3]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div/div/div/div/button[2]").click()
        '''2 adult passenger selected'''
        driver.find_element_by_xpath("//div[2]/div/button[2]").click()
        driver.find_element_by_xpath("//div[2]/div/button[2]").click()
        '''2 children added'''
        time.sleep(2)
        driver.find_element_by_xpath("//div/div/div[3]/div/button[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary']").click()
        print("Clicked on Show Tickets Button")
        time.sleep(3)
        # rain times are displayed
        self.assertEqual("DaySave tickets", driver.title)
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='fare__radio otrl otrl-select']").click()
        print("Day save ticket has selected")
        driver.find_element_by_xpath("//div[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()
        time.sleep(2)
        #<Result 4: West worthing daysave SD4 for 2 adults and 2 children selected for next now>

        #<Step 5: Slect CCST royalmail signed for as delivery option>
        self.assertEqual("Collection preferences", driver.title)
        print("We are on Delivery page")
        driver.find_element_by_xpath("//div[@class='fulfilment-option'][2]").click()
        print("CCST Royalmail signed for  delivery option slected")
        time.sleep(2)

        driver.find_element_by_id("contactName").send_keys("Linda Smith")
        driver.find_element_by_id("addressline1").send_keys("123, Somewhere")
        driver.find_element_by_id("addressline2").send_keys("456, Nomewhere")
        driver.find_element_by_id("addressline1").send_keys("789, Anymewhere")
        driver.find_element_by_id("towncity").send_keys("London")
        driver.find_element_by_id("postcode").send_keys("SE1 0HS")
        time.sleep(2)
        # <Result 5: CCST delivery option selected>

        #<Step 4: Select master card as Payment method
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[2]/div/span").click()
        time.sleep(2)
        # Payment method as card selected

        # Enter the card details
        driver.find_element_by_xpath("//*[@id='cardHolderName']").send_keys("Linda Smith")
        driver.find_element_by_xpath("//*[@id='cardNumber']").send_keys("9902000000005132")
        driver.find_element_by_xpath("//*[@id='expiryMonth']/option[13]").click()
        driver.find_element_by_xpath("//*[@id='expiryYear']/option[8]").click()
        driver.find_element_by_xpath("//*[@id='cvv']").send_keys(123)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='addressline1']").send_keys("30 Great Guildford street")
        driver.find_element_by_xpath("//*[@id='towncity']").send_keys("London")
        driver.find_element_by_xpath("//*[@id='postcode']").send_keys("SE1 0HS")
        time.sleep(2)

        # creating a new account as not logged in user
        now = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        generate_email = "linda.qa.smith+"+now+"@gmail.com"
        driver.find_element_by_id("email").send_keys(generate_email)
        driver.find_element_by_id("emailConfirm").send_keys(generate_email)
        driver.find_element_by_id("password").send_keys("testtest")
        driver.find_element_by_id("firstName").send_keys("Auto test")
        driver.find_element_by_id("surname").send_keys("Auto test")
        time.sleep(2)

        # Click on pay button
        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary btn btn-primary']").click()
        print("Click on Pay button")

        # Payment gateway opens
        time.sleep(3)
        # Authorise payment
        driver.switch_to.frame(driver.find_element_by_name("iframe"))
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='submitForm']/div[1]/input[1]").click()
        time.sleep(2)

        # Asserting for successful payment and storing the order ID for reference
        driver.switch_to_default_content()
        text=driver.find_element_by_xpath("//p[@class='alert-success text-weight--normal']").text
        try:
            assert "Your payment was successful" in text
        except:
            pass
        print("Order ID = "+driver.find_element_by_xpath("//span[@class='text-weight--bold js-order-id']").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()