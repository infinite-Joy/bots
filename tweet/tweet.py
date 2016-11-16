import twitter
import yaml
import sys

with open("keys.yaml", "r") as data:
    try:
        keys = yaml.load(data)
    except yaml.YAMLError as exc:
        print(exc)

api = twitter.Api(consumer_key=keys["data"]["consumer_key"],
                  consumer_secret=keys["data"]["consumer_secret"],
                  access_token_key=keys["data"]["access_token_key"],
                  access_token_secret=keys["data"]["access_token_secret"])

# users = api.GetFriends()

# print([u.screen_name for u in users])

message = "best code is no code at all"

try:
    status = api.PostUpdate(message)
except UnicodeDecodeError:
    print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
    print("Try explicitly specifying the encoding with the --encoding flag")
    sys.exit(2)
print("%s just posted: %s" % (status.user.name, status.text))

