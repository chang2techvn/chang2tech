from selenium.webdriver.common.by import By
from time import sleep
from tiktok.base import Tiktok
from selenium.common.exceptions import NoSuchElementException
from tiktok.auth_tiktok import login_

class Heart(Tiktok):
    def heart_video(self):
        # Đăng nhập trước khi thực hiện hành động trên video
        URL_home = "https://www.tiktok.com/"
        cookie_input = input("Enter new cookie: ")
        login_(self.driver, URL_home, cookie_input)  

        # Thực hiện thao tác trên video # Thời gian chờ
        link_heart = "https://www.tiktok.com/@nbun167/video/7366132423568018704"
        self.driver.get(link_heart)
        sleep(5) 
        try:
            button_heart = self.driver.find_element(By.CSS_SELECTOR, 'span[data-e2e="like-icon"]')
            button_heart.click()
            sleep(15)
            print("Liked!")
        except NoSuchElementException:
            print("Could not find like button.")

        self.driver.quit()
