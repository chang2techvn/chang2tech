#tiktok
from tiktok.downloader import Downloader
from tiktok.parser import Parser
from tiktok.heart_tiktok import Heart
from tiktok.poster_tiktok import Post_tiktok
from tiktok.comment_tiktok import Comment_tiktok 
from tiktok.follow_tiktok import Follow
from tiktok.login_tiktok import Login
#facebook
from facebook.login_face import Login
from facebook.comment_face import Comment
from facebook.craw_data import Crawler
from facebook.post_face import Post


#funtion tiktok
proxy = ''
your_email = 'nerengtseel@hotmail.com'
your_password = 'Toan@1234'

def loging_tiktok():
    login1 = Login(proxy=None, headless=False)
    login1.login_cookie()

def parsing_tiktok(keywords):
    parser = Parser(your_email, your_password, proxy=None, headless=False)
    choice = input("Enter '1' for key, '2' for uid: ")
    for key in keywords:
        if choice == '1':
            parser.parse_by_keyword(key)
        else:
            parser.parse_by_user_id(key)

def downloading_titkok(keywords):
    for key in keywords:
        downloader = Downloader(key, proxy=None, headless=False)
        links = downloader.read_links_file()
        for index, link in enumerate(links, 1):
            print(f"Processing Link {index}/{len(links)}")
            downloader.download(link)

def like_video_tikok():
    heart = Heart()
    heart.heart_video()

def commenting_tiktok():
    comment = Comment_tiktok(proxy=None, headless=True)
    comment.comment_video()

def following_tiktok():
    follow = Follow(proxy=None, headless=False)
    follow.follow_video()

def posting_tiktok():
    post = Post_tiktok(proxy=None, headless=False)
    post.post_video()


#function facbook 
def loging_facebook():
    login_ = Login(proxy=None, headless=False)
    login_.login_cookie()

def commenting_facebook():
    comment_ = Comment(proxy=None, headless=False)
    comment_.comment_by_profile()

def crawing_facebook():
    craw_data = Crawler(proxy=None, headless=False)
    craw_choise = input("'1' for craw group id, '2' for craw uid in group: ")
    if craw_choise == '1':
        craw_data.crawl_group_id()
    elif craw_choise == '2':
        craw_data.crawl_uid_group()

def posting_facebook():
    post_ = Post(proxy=None, headless=False)
    post_.post_profile()


while True:
    choice_service = input("Enter '1' for tiktok, '2' for facebook: ")
    if choice_service == '1':

        choice_tiktok = input("Enter '1' to run the parser,\n'2' to run the downloader,\n'3' to like a video:,\n'4', to post video,\n'5', to comment video\n'6' to login\nOr enter '7' to quit: ")        
        if choice_tiktok == '1' or choice_tiktok == '2':
            keys = []
            num_keys = int(input("Enter the number of keys you want to add: "))
            for i in range(num_keys):
                key = input("Enter key {}: ".format(i+1))
                keys.append(key)
        
        if choice_tiktok == '1':
            parsing_tiktok(keys)
        elif choice_tiktok == '2':
            downloading_titkok(keys)
        elif choice_tiktok == '3':
            like_video_tikok()
        elif choice_tiktok == '4':
            posting_tiktok()
        elif choice_tiktok == '5':
            commenting_tiktok()
        elif choice_tiktok == '6':
            loging_tiktok()
        else:     
            print("Invalid choice. Please enter a valid option or 'q' to quit.")
    
    elif choice_service == '2':
        choice_facebook = input("Enter '1' to login, '2' craw data, '3' to comment '4' to post: ")
        if choice_facebook == '1':
            loging_facebook()
        elif choice_facebook == '2':
            crawing_facebook()
        elif choice_facebook == '3':
            commenting_facebook()
        elif choice_facebook == '4':
            posting_facebook()


