from reddit import get_top_posts
from reddit import all_subreddits


def test_get_top_posts():
    res = get_top_posts("Python")
    assert res["title"]


def test_all_subreddits():
    res = all_subreddits(["Python", "haskell"])
    assert res["Python"]["score"] and res["haskell"]["score"]
