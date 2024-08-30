from selenium.webdriver.common.by import By
from tiktok.base import Tiktok
from facebook.auth_face import login_face
from time import sleep
import pyautogui
import json

class Post(Tiktok):
    def __init__(self, proxy=None, headless=False):
        super().__init__(proxy, headless)

    def post_profile(self):
        URL_face_home = "https://www.facebook.com/"
        default_file = 'C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\cookies\\default_cookie_fb.json'
        with open(default_file, 'r') as file:
            cookie_input = json.load(file)
        login_face(self.driver, URL_face_home, cookie_input)  
        
     
        sleep(5)

        find_post = self.driver.find_element(By.CSS_SELECTOR, 'div[class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
        find_post.click()
        sleep(5)

        image_button = self.driver.find_element(By.CSS_SELECTOR, 'img[class="x1b0d499 xl1xv1r"]')
        image_button.click()

        sleep(2)
        image_button_2 = self.driver.find_element(By.CSS_SELECTOR, 'div[class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x1iyjqo2 x2lwn1j xl56j7k"]')
        image_button_2.click()

        sleep(2)

        
        pyautogui.write("C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\image\\imagetest.jpg")
        pyautogui.press("enter")
        sleep(10000)
        self.driver.get(URL_face_home)

        sleep(5)

        find_post = self.driver.find_element(By.CSS_SELECTOR, 'div[class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
        find_post.click()
        sleep(5)

        image_button = self.driver.find_element(By.CSS_SELECTOR, 'img[class="x1b0d499 xl1xv1r"]')
        image_button.click()

        sleep(2)
        image_button_2 = self.driver.find_element(By.CSS_SELECTOR, 'div[class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x1iyjqo2 x2lwn1j xl56j7k"]')
        image_button_2.click()

        sleep(2)
        
        pyautogui.write("C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\image\\imagetest.jpg")
        pyautogui.press("enter")


        sleep(8)
        caption = "have a nice day"
        caption_input = self.driver.find_element(By.CSS_SELECTOR, 'p[class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
        caption_input.send_keys(caption)
        sleep(5)
        post_button = self.driver.find_element(By.CSS_SELECTOR, 'span[class="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft"]')
        post_button.click()

        sleep(19999)


