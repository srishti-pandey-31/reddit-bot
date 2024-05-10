
#create a reddit account and fill the details below

import praw

client_id = 'your client id'
client_secret = 'your client secret'
username = 'username your account holds'
password = 'account password'
user_agent = 'basic_bot v1.0' 



reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent,
)



print(f"Logged in as: {reddit.user.me()}")


subreddit_name = input("Enter subreddit name: ") #for getting the top 10 post of any subredit, enter the title
subreddit = reddit.subreddit(subreddit_name)
hot_posts = subreddit.hot(limit=10)

for post in hot_posts:
    print(f"Title: {post.title}")
    print(f"Author: {post.author}")
    print(f"URL: {post.url}")
    print("-------------")