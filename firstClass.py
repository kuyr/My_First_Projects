import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class yourLogoSiteTest (unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')
        #self.driver.maximize_window()


    def test_login(self):
        elem1 = self.driver.find_element_by_class_name('login')
        elem1.click()

        elem2 = self.driver.find_element_by_name('email')
        elem2.send_keys('eegweni6@gmail.com')

        elem3 = self.driver.find_element_by_name('passwd')
        elem3.send_keys('test1234')

        elem4 = self.driver.find_element_by_class_name('icon-lock')
        elem4.click()        
        self.assertIn('My account', self.driver.title)

    
    def test_positive_search(self):
        elem5 = self.driver.find_element_by_id('search_query_top')
        elem5.send_keys('dress')

        elem6 = self.driver.find_element_by_class_name('button-search') 
        elem6.click()

        self.assertIn('product-count', self.driver.page_source)  
    
    def test_Negatve_Search(self):

        elem7 = self.driver.find_element_by_id('search_query_top')
        elem7.send_keys('spoon')

        elem8 = self.driver.find_element_by_class_name('button-search')
        elem8.click() 

        self.assertIn('0 results have been found.', self.driver.page_source)

             
        time.sleep(5)
    
        
        


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
