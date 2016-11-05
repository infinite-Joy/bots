import praw

user_agent = "Comment Reader 1.0 by /u/infinite-Joy"

r = praw.Reddit(user_agent=user_agent)

submissions = r.get_subreddit('Python').get_top(limit=5)
for x in submissions:
        print(str(x))
