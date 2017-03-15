from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support.ui import Select
import datetime

class SouthernRegTest_1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_purchase_daysave_southern(self):

        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://southern.stage.otrl.io/search")
        print("Opening Southern Booking Engine")

        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div[2]/nav/a[3]").click()
        print("Clicked on other tickets")
        time.sleep(2)
        driver.find_element_by_xpath("//section[@class='booking__section other-ticket-options']/button").click()
        print("Clicked on Daysave")
        time.sleep(3)
        enter_origin_station = "Brighton"
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div[1]/section[1]/span/label/div/input").send_keys(enter_origin_station)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div/section[1]/span/label/div/input").send_keys(Keys.RETURN)
        print("Searching the journey for " + enter_origin_station +" Daysave")
        time.sleep(3)
        '''
        driver.find_element_by_xpath("//*[@id='loadDateSelect']/i").click()
        print("Calender Loaded")
        driver.find_element_by_xpath("//td[@id='rw_7_calendar__month_2-18']").click()
        driver.find_element_by_xpath("//div[@class='modal-footer']/div/button[2]").click()
        print("date selected")


        # <Step 3: In Tickets tab, click on the Outbound Calendar.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[1]/div/div[2]/button").click()
        time.sleep(3)
        # <Result 3: 'The Outbound Calendar is opened.>

        #driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[1]/div/div[2]/div/div/div[1]/button[3]").click()

        # <Step 4: Click on date March 15 2017 in the Calendar.>
        driver.find_element_by_xpath("//*[@id='rw_1_calendar__month_2-15']").click()
        time.sleep(3)
        # <Result 4: 'March 15 2017 is selected as the Outbound travel date.>

        # <Step 5: Click on the 'Passengers and Railcards button'.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/button").click()
        time.sleep(3)
        # <Result 5: The 'Passengers and Railcards' dialog is opened.>

        # <Step 6: In 'Passengers and Railcards' dialog, click 'Select' button.>
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(3)
        # <Result 6: The default of '1 Adult - No railcards added' is saved and the dialog is closed.>

        '''

        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary']").click()
        print("Clicked on Show Tickets Button")
        #time.sleep(3)
        self.assertEqual("Find DaySave tickets", driver.title)
        driver.find_element_by_xpath("//span[@class='fare__radio otrl otrl-select']").click()
        print("Day save ticket has selected")

        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary']").click()
        print("Clicked on Continue button")
        time.sleep(2)

        self.assertEqual("Collection preferences", driver.title)
        print("We are on Delivery page")
        #time.sleep(2)

        #choose TOD as a delivery option

        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div[2]/div[1]/label/span/span/span[1]").click()
        print("TOD delivery option slected")

        '''
        #choose CCST as a delivery option

        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div[3]/div/label/span/span/span[1]").click()
        print("CCST delivery option selected")
        driver.find_element_by_id("contactName").send_keys("Linda Smith")
        self.enter_customer_address()
        time.sleep(2)
        '''

        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button").click()
        print("Clicked on payment details")
        time.sleep(2)
        self.assertEqual("Payment details", driver.title)

        #Select Method of Payment
        # PAYPAL as MOP
       # driver.find_element_by_xpath("//*[@id='paypal-container']").click()

        # Card-evoucher MOP


        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div[2]/div[2]").click()
        time.sleep(2)
        driver.find_element_by_id("cardHolderName").send_keys("Linda Smith")
        driver.find_element_by_id("cardNumber").send_keys("9900000000000010")

        select = Select (driver.find_element_by_id("expiryMonth"))
        select.select_by_value('05')

        select = Select (driver.find_element_by_id("expiryYear"))
        select.select_by_value('2020')

        driver.find_element_by_id("cvv").send_keys("536")
       # self.enter_customer_address()


        # as not logged in user-creating a new account
        now = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        generate_email = "linda.qa.smith+"+now+"@gmail.com"
        driver.find_element_by_id("email").send_keys(generate_email)

def enter_customer_address(self):
        driver = self.driver
        driver.find_element_by_id("addressline1").send_keys("123, Somewhere")
        driver.find_element_by_id("addressline2").send_keys("456, Nomewhere")
        driver.find_element_by_id("addressline1").send_keys("789, Anymewhere")
        driver.find_element_by_id("towncity").send_keys("London")
        driver.find_element_by_id("postcode").send_keys("SE1 0HS")

















def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
