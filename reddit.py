import praw
import json
import yagmail

user_agent = "Comment Reader 1.0 by /u/infinite-Joy"

r = praw.Reddit(user_agent=user_agent)

def get_top_posts(sbreddt):
    """
    usage:
        get_top_posts("Python")
        Version 3.5.0 of praw is outdated. Version 4.3.0 was released 4 days ago.
        {'124 :: VIM and Python - a match made in heaven':
            {'score': '124',
            'short_link': 'http://redd.it/5pnttx',
            'url': 'https://realpython.com/blog/python/
                vim-and-python-a-match-made-in-heaven/',
            'title': 'VIM and Python - a match made in heaven'
            }
        }
    """
    submissions = r.get_subreddit(sbreddt).get_top(limit=5)
    for sub in submissions:
        return { str(sub): {
            "title": str(sub.title),
            "short_link": sub.short_link,
            "url": sub.url,
            "score": str(sub.score)
        }}


def all_subreddits(list_subreddits):
    return {x: get_top_posts(x) for x in list_subreddits}


def construct_email(subreddits):
    return json.dumps(all_subreddits(subreddits))


def send_email(subreddits):
    self_email_id = "joydeepubuntu"
    to_email_id = "joydeep@hackerearth.com"
    subject = "reddit posts"
    email_body = construct_email(subreddits)
    m = yagmail.SMTP(self_email_id)
    m.send(to_email_id, subject, email_body)


if __name__ == "__main__":
    print(get_top_posts("Python"))
