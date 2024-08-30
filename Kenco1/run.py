# from tiktok.downloader import Downloader
# from tiktok.parser import Parser
# from tiktok.heart import Heart
from tiktok.poster import Post
# from tiktok.comment import Comment 
# from tiktok.follow import Follow
# from tiktok.login import Login

proxy = ''
your_email = 'nerengtseel@hotmail.com'
your_password = 'Toan@1234'



# def loging():
#     login1 = Login(proxy=None, headless=False)
#     login1.login_cookie()


# def parsing(keywords):
#     parser = Parser(your_email, your_password, proxy=None, headless=False)
#     choice = input("Enter '1' for key, '2' for uid: ")
#     for key in keywords:
#         if choice == '1':
#             parser.parse_by_keyword(key)
#         else:
#             parser.parse_by_user_id(key)

# def downloading(keywords):
#     for key in keywords:
#         downloader = Downloader(key, proxy=None, headless=False)
#         links = downloader.read_links_file()
#         for index, link in enumerate(links, 1):
#             print(f"Processing Link {index}/{len(links)}")
#             downloader.download(link)

# def like_video():
#     # Khởi tạo một đối tượng Heart và truyền cùng một cửa sổ trình duyệt
#     heart = Heart()
#     heart.heart_video()

# def commenting():
#     comment = Comment(proxy=None, headless=False)
#     comment.comment_video()

# def following():
#     follow = Follow(proxy=None, headless=False)
#     follow.follow_video()

def posting():
    post = Post(proxy=None, headless=False)
    post.post_video()

while True:
    choice = input("Enter '1' to run the parser,\n'2' to run the downloader,\n'3' to like a video:,\n'4', to post video,\n'5' to post video,\n'6', to comment video\nOr enter 'q' to quit:\n'7' to login: ")

    if choice == '1' or choice == '2':
        keys = []
        num_keys = int(input("Enter the number of keys you want to add: "))
        for i in range(num_keys):
            key = input("Enter key {}: ".format(i+1))
            keys.append(key)

    # if choice == '1':
    #     parsing(keys)
    # elif choice == '2':
    #     downloading(keys)
    # elif choice == '3':
    #     like_video()
    if choice == '4':
        posting()
    # elif choice == '5':
    #     commenting()
    # elif choice == '6':
    #     following()
    # elif choice == '7':
    #     loging()
    # elif choice.lower() == 'q':
        # break
    else:
        print("Invalid choice. Please enter a valid option or 'q' to quit.")