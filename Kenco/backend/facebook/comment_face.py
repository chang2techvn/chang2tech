from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pywinauto import Desktop, Application
from time import sleep

from tiktok.base import Tiktok 
from facebook.auth_face import login_face
from time import sleep
import json 


class Comment(Tiktok):
    def __init__(self, proxy=None, headless=True):
        super().__init__(proxy, headless)

    def login_comment(self):
        URL_face_home = "https://www.facebook.com/"
        default_file = 'C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\cookies\\default_cookie_fb.json'
        with open(default_file, 'r') as file:
            cookie_input = json.load(file)
        login_face(self.driver, URL_face_home, cookie_input)  



    def comment_by_profile(self):
        #call function login first
        self.login_comment()
        sleep(2)
        #Get link profile
        # choice_comment = input("Comment by '1' link(page/profile) or '2' uid?")
        # if choice_comment == 1:
        #     link_comment = input("Input your link: ")
        # else:
        #     link_comment = 'https://www.facebook.com/profile.php?id=' + input("Input your Uid: ")
          # Get the file path containing the links
        # file_path = "C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\craw\\uid_group.txt"
        # # Read links from file
        # with open(file_path, 'r') as file:
        #     links = file.readlines()
        links = "https://www.facebook.com/100030133000687"
        self.driver.get(links)
        sleep(2)

        comment_text = "ê. pà mua thử đồ shop này chưa? https://s.shopee.vn/605agTMkKZ" #input("Enter your comment: ")

        # Tìm ô comment và nhập nội dung comment
        # num_iterations = 10 #int(input("Enter number of loop: "))
        # for _ in range(num_iterations):
        self.driver.execute_script("window.scrollBy(0, 1500);")
        sleep(4)
        image_box = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Attach a photo or video"]')
        image_box.click()
        sleep(7)

            # Tìm phần tử input của file và gửi đường dẫn của tệp tin
        file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys("C:\\Users\\ADMIN\\Desktop\\chang2tech\\Kenco\\backend\\facebook\\data\\image\\imagetest.jpg")
        sleep(9)
    
        comment_box = self.driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
        sleep(5)
        comment_box.send_keys(comment_text)
        comment_box.send_keys(Keys.ENTER)
        print("Commented!")
