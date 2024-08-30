from selenium.webdriver.common.by import By
from tiktok.base import Tiktok
from tiktok.auth_tiktok import login_
from time import sleep
from selenium.common import NoSuchElementException

class Follow(Tiktok):
    
    def follow_video(self):
        URL_home = "https://www.tiktok.com/"
        cookie_input = input("Enter new cookie: ")
        login_(self.driver, URL_home, cookie_input)  


        link_heart = "https://www.tiktok.com/@fanhuq/video/7329478558789700871" #input("Input your Video link: ")
        
        self.driver.get(link_heart)
        
        sleep(10)  # Thời gian chờ
        
        try:
            button_heart = self.driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="browse-follow"]')
            button_heart.click()
            print("Followed!")
        except NoSuchElementException:
            print("Could not find followed button.")
        
        self.driver.quit()
