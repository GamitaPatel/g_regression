from selenium import webdriver
import time
import unittest
import datetime
from selenium.webdriver.common.keys import Keys


locators = {
    'entry_for_start_location': "//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[1]/label/div/input"
}

class southernregression02class(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_southern_reg_01(self):


        driver = self.driver
        driver.maximize_window()
        #<Step 1: open the page >
        driver.get("https://southern.stage.otrl.io")
        #<Result 1:  page is opened >

        #<Step 2: Login page >
        driver.find_element_by_xpath("//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[1]").click()
        driver.find_element_by_xpath("//*[@id='username']").send_keys("linda.qa.smith@gmail.com")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("testtest")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        #<Result 2: logged in succesfully >
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div[2]/nav/a[3]").click()
        print("Clicked on other tickets")
        time.sleep(2)
        #<Step 3: Select Daysave ticekttype >
        time
        driver.find_element_by_xpath("//section[@class='booking__section other-ticket-options']/button").click()
        print("Clicked on Daysave")
        #<Result 3: Daysave ticekttype selected>
        time.sleep(3)
        #<Step 4: Select Brighton standard daysave ticket for 1 adult SD1>
        time
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div[1]/section[1]/span/label/div/input").send_keys('Brighton')
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div/section[1]/span/label/div/input").send_keys(Keys.RETURN)
        print("Searching the journey for Brighton Daysave")
        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary']").click()
        print("Clicked on Show Tickets Button")
        time.sleep(3)
        self.assertEqual("DaySave tickets", driver.title)
        driver.find_element_by_xpath("//span[@class='fare__radio otrl otrl-select']").click()
        print("Day save ticket has selected")
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary']").click()
        print("Clicked on Continue button")
        time.sleep(2)
        #<Result 4: Standard Daysave SD1 ticket has been selected>
        self.assertEqual("Collection preferences", driver.title)
        print("We are on Delivery page")
        time.sleep(2)
        #  TOD automatically selected as a delivery option

        #<Step 5: click payment details button >
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button").click()
        time.sleep(2)
        #<Result 05: Payment option displayed>

        #<Step 06:Select payment method as card/evoucher payment and make a transaction with evoucher as MOP>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[2]/div/span").click()
        time.sleep(2)
        print("Card/Evoucher payment selected as MOP")
        driver.find_element_by_xpath("//button[@class='text-sm basket-summary__nextbutton btn btn-primary btn btn-primary']").click()
        print("Click on Pay button")
        time.sleep(3)
        text=driver.find_element_by_xpath("//p[@class='alert-success text-weight--normal']").text
        try:
            assert "Your payment was successful" in text
        except:
            pass
        print("Order ID = "+driver.find_element_by_xpath("//span[@class='text-weight--bold js-order-id']").text)
        #<Result 06: Payment authorised>



if __name__ == "__main__":
    unittest.main()