import unittest
import html_test_report
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test(unittest.TestCase):

    BaseURL = 'https://www.google.com/'
    BaseText = 'google'
    SearchText = 'selenium'
    SearchURL = 'https://www.selenium.dev'
    HeaderXPath = "//h1[@class='display-1 mt-0 mt-md-5 pb-1']"
    VerifyHeaderText = "Selenium automates browsers. That's it!"
    TitleErrorMsg = "WebPage Title Not Matching"
    HeaderMissingErrorMsg = "Could Not Find Header Text"
    ChromeDriverPath = "./drivers/chromedriver.exe"

    # FireFoxDriverPath = "./drivers/geckodriver.exe" #Uncomment to launch with Firefox browser
    # EdgeDriverPath = "./drivers/msedgedriver.exe"

    @classmethod  # Method to Initialize  Drivers
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(cls.ChromeDriverPath)
        # cls.driver = webdriver.Firefox(cls.FireFoxDriverPath)
        # cls.driver = webdriver.Edge(cls.EdgeDriverPath)

    def test_SearchSeleniumInGoogle(self):
        self.driver.get(self.BaseURL)  # Launch Google In Browser
        self.driver.maximize_window()  # Maximize Browser Window
        elem = self.driver.find_element(By.TAG_NAME, 'input')  # Locate The Search Field
        elem.send_keys(self.SearchText + Keys.RETURN)  # Enter "Selenium" And Press Enter
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.SearchURL).click()  # Search For Selenium.Dev URL in Page
        element = self.driver.find_element(By.XPATH, self.HeaderXPath).text  # Store The Header Text To element
        self.assertEqual(self.VerifyHeaderText, element, self.HeaderMissingErrorMsg)  # Validate the HeaderText

    @classmethod  # Method to Close The Browser Window
    def tearDownClass(cls):
        cls.driver.quit()
        print("Tests Completed")


if __name__ == "__main__":
    unittest.main(testRunner=html_test_report.HtmlTestRunner())  # Code To Generate Test Report
