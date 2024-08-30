# from selenium.webdriver.common.by import By
# from time import sleep
# from tiktok.base import Tiktok
# from tiktok.auth import login_
# from pywinauto import Desktop, Application 




# class Post(Tiktok):
#     def post_video(self):
#         URL_home = "https://www.tiktok.com/"
#         cookie_input = input("Enter new cookie: ")
#         login_(self.driver, URL_home, cookie_input)  

#         self.driver.get("https://www.tiktok.com/creator#/upload?scene=creator_center")
    
#         sleep(5)
#         select_button = self._wait_for_element_located(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div[3]/button[2]/div/div')
#         select_button.click()
#         sleep(5)

#         # Mở cửa sổ chọn tệp
#         app = Desktop(backend="uia").window(title="Open")  # Phải điền đúng title của cửa sổ Open trên máy tính của bạn
#         app.wait('visible')

#         # Tìm và nhập đường dẫn vào ô tìm kiếm
#         edit = app["Address"]
#         edit.set_text("C:\\Users\\ADMIN\\Desktop\\chang2tech\\tiktok-download\\results\\chang\\Snaptik.app_7253412846963346693.mp4")

#         # Bấm Enter để mở tệp
#         app["Open"].type_keys("{ENTER}")
#         #   # Sử dụng pywinauto để tìm cửa sổ mở file
#         # app = application.Application(backend="uia").connect(title_re="Open")
#         # open_dlg = app.Open
#         # open_dlg.set_focus()
        
#         # # Nhập đường dẫn file vào ô đường dẫn
#         # open_dlg.Edit.set_text("C:\\Users\\ADMIN\\Desktop\\chang2tech\\tiktok-download\\results\\chang\\Snaptik.app_7253412846963346693.mp4")


#         #Enter your caption
#         caption_input = self._wait_for_element_located(By.XPATH, "//span[@data-text='true']")
#         caption_input.clear()
#         user_input = input("Nhập caption của bạn: ")
#         caption_input.send_keys(user_input)
#         sleep(2)
                
#                 # Cuộn trang đến nút post_video
#         post_video_button = self._wait_for_element_located(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[11]/button[2]/div/div')
#         self.driver.execute_script("arguments[0].scrollIntoView();", post_video_button)
#         sleep(2)  # Đợi một chút để cuộn trang hoàn tất

#         # Click vào nút post_video sau khi đã cuộn đến đúng vị trí
#         post_video_button.click()

# #         self.driver.quit()

# #         # #Them lien ket 
# #         # product_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/span')
# #         # product_button.click()
# #         # sleep(2)
# #         # #next
# #         # next_button_1 = self.driver.find_element(By.XPATH, '//*[@id=":rk:"]/div[2]/div/div/div[2]/button[2]/div/div')
# #         # next_button_1.click()
# #         # sleep(1000000)
# #         # Add_id_product = self.driver.find_element(By.CSS_SELECTOR, 'input[class="TUXTextInputCore-input"]')
# #         # id_product = input("nhap id sp: ")
# #         # Add_id_product.send_keys(id_product)
# #         # sleep(2)
# #         # next_button_2 = self.driver.find_element(By.XPATH, '//*[@id=":r36:"]/div[3]/button[2]/div/div')
# #         # next_button_2.click()
# #         # sleep(2)
# #         # add_button = self.driver.find_element(By.XPATH, '//*[@id=":r39:"]/div[3]/button[2]/div/div')
# #         # add_button.click()
# #         # sleep(1000005)




from selenium.webdriver.common.by import By
from time import sleep
from tiktok.base import Tiktok
from tiktok.auth import login_
import pyautogui
from pywinauto import application

class Post(Tiktok):
    def post_video(self):
        URL_home = "https://www.tiktok.com/"
        cookie_input = "_ttp=2XCXA9cW7OLeIzIlD03vZaU4UB3;_ga=GA1.1.2119301743.1698133886;_tt_enable_cookie=1;d_ticket_ads=dac70d0000c6b00849bc8c6416174a25f4d90;sid_guard_tiktokseller=16de499ffdb019367fb47e6ef3d6a978%7C1698134400%7C863999%7CFri%2C+03-Nov-2023+07%3A59%3A59+GMT;tiktok_webapp_theme=dark;_ga_BZBQ2QHQSP=GS1.1.1698319231.2.1.1698319280.0.0.0;passport_csrf_token=15e3b0d6b6a75292dda6fb6aeed0bf60;passport_csrf_token_default=15e3b0d6b6a75292dda6fb6aeed0bf60;tt_chain_token=eCKrnmWqMMlHW/8E0XDKkA==;d_ticket=280a1783e78fdddb09b21861a8ef20774255a;multi_sids=7241102100620936198%3Af42bfc8f3dbba5a27f047807f24b5d45;cmpl_token=AgQQAPOFF-RO0rRDYVlR6l0__EZFOQORP5MOYNe3pA;sid_guard=f42bfc8f3dbba5a27f047807f24b5d45%7C1715148519%7C15552000%7CMon%2C+04-Nov-2024+06%3A08%3A39+GMT;uid_tt=fc46171efd3c9e0cd0a349b618c20989869f2618b8443a50dee6e4b81d9583a9;uid_tt_ss=fc46171efd3c9e0cd0a349b618c20989869f2618b8443a50dee6e4b81d9583a9;sid_tt=f42bfc8f3dbba5a27f047807f24b5d45;sessionid=f42bfc8f3dbba5a27f047807f24b5d45;sessionid_ss=f42bfc8f3dbba5a27f047807f24b5d45;sid_ucp_v1=1.0.0-KDdkMGFiNTUyNjJlZjU1OGM3ZGFmZjI2ZGM1ZTVhN2JmYjJhMDBhMGQKIAiGiOLO7f_jvmQQ563ssQYYswsgDDCgoPajBjgBQOoHEAMaBm1hbGl2YSIgZjQyYmZjOGYzZGJiYTVhMjdmMDQ3ODA3ZjI0YjVkNDU;ssid_ucp_v1=1.0.0-KDdkMGFiNTUyNjJlZjU1OGM3ZGFmZjI2ZGM1ZTVhN2JmYjJhMDBhMGQKIAiGiOLO7f_jvmQQ563ssQYYswsgDDCgoPajBjgBQOoHEAMaBm1hbGl2YSIgZjQyYmZjOGYzZGJiYTVhMjdmMDQ3ODA3ZjI0YjVkNDU;store-idc=alisg;store-country-code=vn;store-country-code-src=uid;tt-target-idc=alisg;tt-target-idc-sign=nlxd-Nsci9YXa_Zcu9eo-NZU-pPi6ONoQ8-vqBZs_TFNHesH_ouGnfrEasxHWT0O-e7bx0Fga6sKr_sH1zSUehE0sv8-MugQV6QH8LNonPFZEKMwGHSfdbhTfzR8lFomwQFhjV2oaKz4fH96FqC6I1u9zPxGT7jciFwOhb57zgxeJYeGCv5PH5p3MHTTSxY6fKBSafx72ClaxOuOsTGSxkkCD8rU4ezcz_rLD9ht7lipxfU8gYvsgKvlH1bIpZI5t95oYqTU7c3ZCmf2zZZjFlIuCNVuKNvLqOyAPAoYAv0cA5xxvdy45RsNCXMO1pes43jMsWRVfywI4miY9U9fgjS5bNGfAU4h6VsTV7nMOpYDoZFwWrLKkpfQnAIpUYx66bR8Grdpz5b7Uc5ShZ8ymNqu7pqO9835UK80bl0r3n9NicWjCT2l9DYitcfrhnMa-W6muH4EXavczG1kIAaDpmpKeh_Jww_49TOCpzX9RJWsz9HKKpCuP11EYS6lwQzB;last_login_method=email;perf_feed_cache={%22expireTimestamp%22:1715565600000%2C%22itemIds%22:[%227347658633737473281%22%2C%227367235009322700048%22%2C%227351714546047831316%22]};tt_csrf_token=GNVHuWcQ-jAroZU9ff-rXvvJczswztXl6wSo;ak_bmsc=BCEB8147F461E3E84D7074820851B7A6~000000000000000000000000000000~YAAQNPrSF9xdB1CPAQAA5L2DbBeQUqIc88k9cA5PgY4pS9KGl80TFSEoM2Bxa6p8NMtUgueoThk9mnGcSAX4TWKJIzq46dv46/y+vBi0YU4wHn3B0FrvZkSc8pScEPzuQbTBJ9JW8hEg9vjv5ak5CAlOJG5JLhDG0zKmOpXfGaOZzuU5j4cYYhrH1vGeBjVZn1/B/S3bVnjnP4+DyhAyuv8i/DAYblwaCRk3cI5tzP5CUJbA1Zje2SQrKDkGI+hriK6Uf5hioyIwanKCNvUB1rPIyO0ZzOwG4qojMYzgQ2rd5mc1yf4g13YM1wTJhsJq5CSJm9EIAcW7gnymG5tQ4YWvhZBH0nQN1btzHTlPhCFBlkxEvqBBMY1xxokqkgvFdKLC9Am60PYFXWGJ;passport_fe_beating_status=true;ttwid=1%7CNZINXhHbmfHqI2lileAqs0omOT6sjv-l8lWYZVU1nHw%7C1715512527%7C7ee2fc7de71f16ee30021860f9bca510ab98397aa9746188f0c829a2fb611cba;odin_tt=0274cba0377788c50503bdac826b5a5fd7d1a8cc070f09ab4560e35b0070f9ca377b82deaf23e5c696698a46adcd3fa1f5572bd500b5c03fb51fe104b0b0de47;msToken=zpj_3rZPawTHABBQM0TETqGQz1hzlIawZsB7om1vvgMtcv5s2OhCLz6usrleYqXdM42YnJffA48trnHDorVvBfJ-C4uLMg1580OvfYYSeJgZ812U9KbNMcS1cpBXjrpb46AXENI=;msToken=zpj_3rZPawTHABBQM0TETqGQz1hzlIawZsB7om1vvgMtcv5s2OhCLz6usrleYqXdM42YnJffA48trnHDorVvBfJ-C4uLMg1580OvfYYSeJgZ812U9KbNMcS1cpBXjrpb46AXENI=;|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        login_(self.driver, URL_home, cookie_input)  

        self.driver.get("https://www.tiktok.com/creator#/upload?scene=creator_center")
    
        sleep(5)
        select_button = self._wait_for_element_located(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div[3]/button[2]/div/div')
        select_button.click()
        sleep(5)

        # Sử dụng pyautogui để điều khiển cửa sổ chọn file
        pyautogui.write("C:\\Users\\ADMIN\\Desktop\\chang2tech\\tiktok-download\\results\\chang\\Snaptik.app_7253412846963346693.mp4")
        pyautogui.press("enter")
        sleep(10)

        # Sử dụng pywinauto để tìm cửa sổ mở file
        app = application.Application(backend="uia").connect(title_re="Open")
        open_dlg = app.Open
        open_dlg.set_focus()
        
        # Nhập đường dẫn file vào ô đường dẫn
        open_dlg.Edit.set_text("C:\\Users\\ADMIN\\Desktop\\chang2tech\\tiktok-download\\results\\chang\\Snaptik.app_7253412846963346693.mp4")

        # Nhập caption
        caption_input = self._wait_for_element_located(By.XPATH, "//span[@data-text='true']")
        caption_input.clear()
        user_input = input("Nhập caption của bạn: ")
        caption_input.send_keys(user_input)
        sleep(2)
                
        # Cuộn trang đến nút post_video
        post_video_button = self._wait_for_element_located(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[11]/button[2]/div/div')
        self.driver.execute_script("arguments[0].scrollIntoView();", post_video_button)
        sleep(2)  # Đợi một chút để cuộn trang hoàn tất

        # Click vào nút post_video sau khi đã cuộn đến đúng vị trí
        post_video_button.click()

        self.driver.quit()
