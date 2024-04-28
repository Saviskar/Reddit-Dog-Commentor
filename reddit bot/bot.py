import praw
import config

def bot_login():
    r = praw.Reddit(user_name = config.user_name,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "savishkar's dog commenter bot v0.1")
    print("Logged in!")

    return r

def run_bot(r):
    print("Obtaining 25 comments...")
    for comment in r.subreddit('test').comments(limit=25):
        if "dog" in comment.body:
            print("String with \"dog\" found in comments " + comment.id)
            comment.reply("I also love dogs! [Here](https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cute_dog.jpg/2560px-Cute_dog.jpg) is an image of one!")
            print("Replied to comment" + comment.id)

while True:
    r = bot_login()
    run_bot(r)