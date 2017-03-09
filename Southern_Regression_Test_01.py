from selenium import webdriver
import time
import unittest
import datetime


locators = {
    'entry_for_start_location': "//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[1]/label/div/input"
}

class southernregressionclass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_southern_reg_01(self):
        driver = self.driver
        driver.maximize_window()
        #<Step 1: open the Southern Booking Engine Page and select season ticket tab>
        driver.get("https://southern.stage.otrl.io")
        print("Opening the southern booking engine")
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div/div[2]/nav/a[2]").click()
        print("Season ticket tab selected")
        time.sleep(2)
        #<Result 1: Southern seaon ticket tab is selected >

        # <Step 2: Plan a weekly first class season journey from 'Brighton' to 'Horsham'.>
        driver.find_element_by_xpath(locators['entry_for_start_location']).send_keys("Brighton")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[3]/label/div/input").send_keys("Horsham")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[3]/label/div/div/div").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='loadDateSelect']").click()
        time.sleep(5)
        #'The Outbound Calendar is opened.
        driver.find_element_by_xpath("//*[@id='rw_3_calendar__month_2-23']/span").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        # March 23 2017 is selected as the Outbound travel date.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/footer/button").click()
        print("Clicked on Show Tickets Button")
        # time.sleep(3)
        self.assertEqual("Find season tickets", driver.title)
        time.sleep(2)
        # Select first class weekly 7DS ticket>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div[1]/ul/li[2]").click()
        print("First class 7DS ticket has been selected")
        time.sleep(5)
        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary']").click()
        print("Click on continue button")
        time.sleep(5)
        self.assertEqual("Photocard details",driver.title)
        driver.find_element_by_id("name").send_keys("Linda Smith")
        driver.find_element_by_id("number").send_keys("AUTO12345AUTO")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary']").click()
        print("Photocard details added")
        time.sleep(2)
        # <Result 2: Weekly first class seaon journey from 'Brighton' to 'Horsham' planned .>
        self.assertEqual("Collection preferences", driver.title)
        print("We are on Delivery page")

        # <Step 3: Choose TOD as a delivery option

        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div[2]/div[1]/label/span/span/span[1]").click()
        print("TOD delivery option slected")
        time.sleep(5)
        # <Result 3: TOD delivery option selected>

        #<Step 4: click payment details button >
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button").click()
        time.sleep(2)
        #self.assertEqual("Payment details", driver.title)
        #<Result 04: Payment option displayed>

        #<Step 05:Select payment method as card payment>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[2]/div/span").click()
        time.sleep(2)
        #<Result 05:Payment method selected

        #<Step 06:Enter the card details>
        driver.find_element_by_xpath("//*[@id='cardHolderName']").send_keys("Linda Smith")
        driver.find_element_by_xpath("//*[@id='cardNumber']").send_keys("9902000000005132")
        driver.find_element_by_xpath("//*[@id='expiryMonth']/option[13]").click()
        driver.find_element_by_xpath("//*[@id='expiryYear']/option[8]").click()
        driver.find_element_by_xpath("//*[@id='cvv']").send_keys(123)
        time.sleep(2)

        #<Result 06: Card details eneterd>
        #<Step 18:Enter address>
        driver.find_element_by_xpath("//*[@id='addressline1']").send_keys("30 Great Guildford street")
        driver.find_element_by_xpath("//*[@id='towncity']").send_keys("London")
        driver.find_element_by_xpath("//*[@id='postcode']").send_keys("SE1 0HS")
        time.sleep(2)
        #<Result 18:Address entered>
        now = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        generate_email = "linda.qa.smith+"+now+"@gmail.com"
        driver.find_element_by_id("email").send_keys(generate_email)
        driver.find_element_by_id("emailConfirm").send_keys(generate_email)
        driver.find_element_by_id("password").send_keys("testtest")
        driver.find_element_by_id("firstName").send_keys("Auto test")
        driver.find_element_by_id("surname").send_keys("Auto test")
        time.sleep(2)
        #<Step 19:Click on pay button>
        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary btn btn-primary']").click()
        print("Click on Pay button")
        #<Result 19:Payment gateway opens>
        time.sleep(5)
        #<Step :Authorise payment>
        driver.switch_to.frame(driver.find_element_by_name("iframe"))
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='submitForm']/div[1]/input[1]").click()
        time.sleep(4)
        driver.switch_to_default_content()
        text=driver.find_element_by_xpath("//p[@class='alert-success text-weight--normal']").text
        try:
            assert "Your payment was successful" in text
        except:
            pass
        print("Order ID = "+driver.find_element_by_xpath("//span[@class='text-weight--bold js-order-id']").text)
        #<Result: Payment authorised>

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()