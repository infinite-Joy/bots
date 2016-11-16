import twitter
import yaml

with open("keys.yaml", "r") as data:
    try:
        keys = yaml.load(data)
        print(keys["data"]["consumer_key"])
    except yaml.YAMLError as exc:
        print(exc)

api = twitter.Api(consumer_key=keys["data"]["consumer_key"],
                  consumer_secret=keys["data"]["consumer_secret"],
                  access_token_key=keys["data"]["access_token_key"],
                  access_token_secret=keys["data"]["access_token_secret"])

users = api.GetFriends()

print([u.screen_name for u in users])
