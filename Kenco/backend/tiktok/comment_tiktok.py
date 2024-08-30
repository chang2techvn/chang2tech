from selenium.webdriver.common.by import By
from tiktok.base import Tiktok
from tiktok.auth_tiktok import login_
from time import sleep
from selenium.common import NoSuchElementException

class Comment_tiktok(Tiktok):
    
    def comment_video(self):
        URL_home = "https://www.tiktok.com/"
        cookie_input = input("Enter new cookie: ")
        login_(self.driver, URL_home, cookie_input)


        link_comment = "https://www.tiktok.com/@fanhuq/video/7329478558789700871" #input("Input your Video link: ")
        self.driver.get(link_comment)
          # Thời gian chờ
        
        try:
            comment_input = self._wait_for_element_located(By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div')
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", comment_input)
            comment_input.send_keys("kkk")
            sleep(5)
            post_comment = self._wait_for_element_located(By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]')
            post_comment.click()
            print("Commented")
        except NoSuchElementException:
            print("Could not find comment button.")
        
        self.driver.quit()


