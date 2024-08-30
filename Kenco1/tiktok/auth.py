import re

def extract_cookies(cookie):
    cookies = {}
    if not cookie:
        return cookies

    # Sử dụng regular expression để tìm các cặp key-value trong chuỗi cookie
    cookie_pairs = re.findall(r'([^;=\s]+)=([^;]+)', cookie)
    
    for key, value in cookie_pairs:
        cookies[key] = value
    return cookies

def login_(driver, URL_home, cookie_input):
    driver.get(URL_home)
    cookies = extract_cookies(cookie_input)

    for key, value in cookies.items():
        driver.add_cookie({'name': key, 'value': value})
        
    driver.get(URL_home)