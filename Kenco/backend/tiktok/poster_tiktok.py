from selenium.webdriver.common.by import By
from time import sleep
from tiktok.base import Tiktok
from tiktok.auth_tiktok import login_

from pywinauto import application



class Post_tiktok(Tiktok):
    def post_video(self):
        URL_home = "https://www.tiktok.com/"
        cookie_input = "_ttp=2XCXA9cW7OLeIzIlD03vZaU4UB3;_ga=GA1.1.2119301743.1698133886;_tt_enable_cookie=1;d_ticket_ads=dac70d0000c6b00849bc8c6416174a25f4d90;sid_guard_tiktokseller=16de499ffdb019367fb47e6ef3d6a978%7C1698134400%7C863999%7CFri%2C+03-Nov-2023+07%3A59%3A59+GMT;tiktok_webapp_theme=dark;_ga_BZBQ2QHQSP=GS1.1.1698319231.2.1.1698319280.0.0.0;passport_csrf_token=15e3b0d6b6a75292dda6fb6aeed0bf60;passport_csrf_token_default=15e3b0d6b6a75292dda6fb6aeed0bf60;tt_chain_token=eCKrnmWqMMlHW/8E0XDKkA==;d_ticket=280a1783e78fdddb09b21861a8ef20774255a;multi_sids=7241102100620936198%3Af42bfc8f3dbba5a27f047807f24b5d45;cmpl_token=AgQQAPOFF-RO0rRDYVlR6l0__EZFOQORP5MOYNe3pA;sid_guard=f42bfc8f3dbba5a27f047807f24b5d45%7C1715148519%7C15552000%7CMon%2C+04-Nov-2024+06%3A08%3A39+GMT;uid_tt=fc46171efd3c9e0cd0a349b618c20989869f2618b8443a50dee6e4b81d9583a9;uid_tt_ss=fc46171efd3c9e0cd0a349b618c20989869f2618b8443a50dee6e4b81d9583a9;sid_tt=f42bfc8f3dbba5a27f047807f24b5d45;sessionid=f42bfc8f3dbba5a27f047807f24b5d45;sessionid_ss=f42bfc8f3dbba5a27f047807f24b5d45;sid_ucp_v1=1.0.0-KDdkMGFiNTUyNjJlZjU1OGM3ZGFmZjI2ZGM1ZTVhN2JmYjJhMDBhMGQKIAiGiOLO7f_jvmQQ563ssQYYswsgDDCgoPajBjgBQOoHEAMaBm1hbGl2YSIgZjQyYmZjOGYzZGJiYTVhMjdmMDQ3ODA3ZjI0YjVkNDU;ssid_ucp_v1=1.0.0-KDdkMGFiNTUyNjJlZjU1OGM3ZGFmZjI2ZGM1ZTVhN2JmYjJhMDBhMGQKIAiGiOLO7f_jvmQQ563ssQYYswsgDDCgoPajBjgBQOoHEAMaBm1hbGl2YSIgZjQyYmZjOGYzZGJiYTVhMjdmMDQ3ODA3ZjI0YjVkNDU;store-idc=alisg;store-country-code=vn;store-country-code-src=uid;tt-target-idc=alisg;tt-target-idc-sign=nlxd-Nsci9YXa_Zcu9eo-NZU-pPi6ONoQ8-vqBZs_TFNHesH_ouGnfrEasxHWT0O-e7bx0Fga6sKr_sH1zSUehE0sv8-MugQV6QH8LNonPFZEKMwGHSfdbhTfzR8lFomwQFhjV2oaKz4fH96FqC6I1u9zPxGT7jciFwOhb57zgxeJYeGCv5PH5p3MHTTSxY6fKBSafx72ClaxOuOsTGSxkkCD8rU4ezcz_rLD9ht7lipxfU8gYvsgKvlH1bIpZI5t95oYqTU7c3ZCmf2zZZjFlIuCNVuKNvLqOyAPAoYAv0cA5xxvdy45RsNCXMO1pes43jMsWRVfywI4miY9U9fgjS5bNGfAU4h6VsTV7nMOpYDoZFwWrLKkpfQnAIpUYx66bR8Grdpz5b7Uc5ShZ8ymNqu7pqO9835UK80bl0r3n9NicWjCT2l9DYitcfrhnMa-W6muH4EXavczG1kIAaDpmpKeh_Jww_49TOCpzX9RJWsz9HKKpCuP11EYS6lwQzB;last_login_method=email;csrfToken=yvW0UNz9-ZFf7njzavvIv50Rs_GkWN_VCt2s;s_v_web_id=verify_lwlzypxh_cE5hqoOS_2CNL_4Evw_8VkH_v4h3O8pL6tf3;tt_csrf_token=Ln8ila6H-R7lcYIU8f4Z9oEu_Nq2qMgARZes;ak_bmsc=78E26EC5275B24C93D00DC7E29FDCB7E~000000000000000000000000000000~YAAQNfrSF6o4JaOPAQAAGX5urxf5RYEg4/On1GVteKDnzUqltKmSDO20E3hwUjGqU/Pv1F7b8gR44HZYt2Icy7y5uY0UQiMbCmeVIfa6paEGri1FWoWpzzZ9S4Ufdi/FxZCZulonspTnaq0dCMRHC9TZu7Ace9bpXBrEw96D6It1KTy/0jhUT7X9PbiyvpMP8STcPRtXngYJSBUGnyOUI9X1o4Ru/XD22fpddtUSX+Nmq7ge/5yHrUdJEYsLFigZZlmPKMpQeVmJzTzUYSpU2wl4Yvvk5rt4Lp7On+jXIySJee57U9sxT9IXtQOyquLbPQBVOqUPXyyxYNwbgaRjs1jt8Qu2f3L5YT0kkkBWT7TL/81qzXveLv15ezQ9YndERsYU03og0ASVktk=;passport_fe_beating_status=true;ttwid=1%7CNZINXhHbmfHqI2lileAqs0omOT6sjv-l8lWYZVU1nHw%7C1716635206%7C3e7e55a532418605ed709535890190332035d5b91ab6ca762df260e5b1bdf003;odin_tt=898dcc05ac01d127d28982ece2bc260989071f0d727c626439de2c0818c44c62fb1a80a327665b68528b018b3cfc5db7dd45aec6d0bca251edbab1af65bafdb5249aab2096a92ae6834381fa9040c722;perf_feed_cache={%22expireTimestamp%22:1716807600000%2C%22itemIds%22:[%227343157881966988564%22%2C%227369903535418264840%22%2C%227364133768925318406%22]};msToken=uExWgvFYWpwewaSYqV_fph752h5vGZEkq_UC8uoRPweUtF56SOHZZA2ZdQvr-pHW-0O6Rb6wl8SXNdW58CKDo68Ulvifut1XXMjhbCsfkeSsNmsis-TBhPWmcRzwZzD2vPAbht9yAGu8og==;msToken=uExWgvFYWpwewaSYqV_fph752h5vGZEkq_UC8uoRPweUtF56SOHZZA2ZdQvr-pHW-0O6Rb6wl8SXNdW58CKDo68Ulvifut1XXMjhbCsfkeSsNmsis-TBhPWmcRzwZzD2vPAbht9yAGu8og==;|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        login_(self.driver, URL_home, cookie_input)  

        self.driver.get("https://www.tiktok.com/creator#/upload?scene=creator_center")
    
        sleep(5)
        # select_button = self._wait_for_element_located(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div[3]/button[2]/div/div')
        # select_button.click()
        # sleep(5)

        # # Sử dụng pyautogui để điều khiển cửa sổ chọn file
        # pyautogui.write("C:\\Users\\ADMIN\\Desktop\\chang2tech\\tiktok-download\\results\\chang\\Snaptik.app_7253412846963346693.mp4")
        # pyautogui.press("enter")
        # sleep(10)

        # # Locate the hidden file input element and upload the file
        # file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        # sleep(2)
        # self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
        # sleep(3)
        # input_video = self.driver.find_element(By.CSS_SELECTOR, 'input[style="display: block;"]')
        # input_video.send_keys("C:\\Users\\ADMIN\\Desktop\\chang2tech\\tiktok-download\\results\\chang\\Snaptik.app_7253412846963346693.mp4")
        # print("uploaded!")
        # sleep(10)

        # try:
        #     # Locate the hidden file input element and upload the file
        #     file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        #     sleep(2)
        #     self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
        #     sleep(3)
        #     input_video = self.driver.find_element(By.CSS_SELECTOR, 'input[style="display: block;"]')
        #     input_video.send_keys("C:\\Users\\ADMIN\\Desktop\\chang2tech\\tiktok-download\\results\\chang\\Snaptik.app_7253412846963346693.mp4")
        #     print("Video file path sent to input element.")
        #     sleep(15)

        #     # Check if the video has been uploaded
        #     page_source = self.driver.page_source
        #     if "video thumbnail" in page_source:  # Replace this with a more accurate check based on the actual page content
        #         print("Video uploaded successfully!")
        #     else:
        #         print("Video not uploaded. Check the page source for debugging:")
        #         print(page_source)

        #     # Enter your caption
        #     caption_input = self._wait_for_element_located(By.XPATH, "//span[@data-text='true']")
        #     caption_input.clear()
        #     user_input = input("Nhập caption của bạn: ")
        #     caption_input.send_keys(user_input)
        #     sleep(2)
                    
        #     # Cuộn trang đến nút post_video
        #     post_video_button = self._wait_for_element_located(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[11]/button[2]/div/div')
        #     self.driver.execute_script("arguments[0].scrollIntoView();", post_video_button)
        #     sleep(2)  # Đợi một chút để cuộn trang hoàn tất

        #     # Click vào nút post_video sau khi đã cuộn đến đúng vị trí
        #     post_video_button.click()

        # except TimeoutException as e:
        #     print(f"TimeoutException: {str(e)}")
        #     print("Có thể trang web chưa tải xong hoặc XPath không chính xác.")
        #     print(self.driver.page_source)  # In ra HTML để kiểm tra
        
        # except NoSuchElementException as e:
        #     print(f"NoSuchElementException: {str(e)}")
        #     print("Phần tử không được tìm thấy, kiểm tra lại XPath.")
        #     print(self.driver.page_source)  # In ra HTML để kiểm tra

        # finally:
        #     self.driver.quit()


# -----------------------------

        # #Enter your caption
        # caption_input = self._wait_for_element_located(By.XPATH, "//span[@data-text='true']")
        # caption_input.clear()
        # user_input = input("Nhập caption của bạn: ")
        # caption_input.send_keys(user_input)
        # sleep(2)
                
        #         # Cuộn trang đến nút post_video
        # post_video_button = self._wait_for_element_located(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[11]/button[2]/div/div')
        # self.driver.execute_script("arguments[0].scrollIntoView();", post_video_button)
        # sleep(2)  # Đợi một chút để cuộn trang hoàn tất

        # # Click vào nút post_video sau khi đã cuộn đến đúng vị trí
        # post_video_button.click()

        # self.driver.quit()

        # # #Them lien ket 
        # # product_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/span')
        # # product_button.click()
        # # sleep(2)
        # # #next
        # # next_button_1 = self.driver.find_element(By.XPATH, '//*[@id=":rk:"]/div[2]/div/div/div[2]/button[2]/div/div')
        # # next_button_1.click()
        # # sleep(1000000)
        # # Add_id_product = self.driver.find_element(By.CSS_SELECTOR, 'input[class="TUXTextInputCore-input"]')
        # # id_product = input("nhap id sp: ")
        # # Add_id_product.send_keys(id_product)
        # # sleep(2)
        # # next_button_2 = self.driver.find_element(By.XPATH, '//*[@id=":r36:"]/div[3]/button[2]/div/div')
        # # next_button_2.click()
        # # sleep(2)
        # # add_button = self.driver.find_element(By.XPATH, '//*[@id=":r39:"]/div[3]/button[2]/div/div')
        # # add_button.click()
        # # sleep(1000005)
