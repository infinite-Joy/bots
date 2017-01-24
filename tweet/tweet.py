import twitter
import yaml
import sys


def read_keys():
    with open("keys.yaml", "r") as data:
        try:
            return yaml.load(data)
        except yaml.YAMLError as exc:
            print(exc)


def tweet(api, message):
    # message = "best code is no code at all"

    try:
        status = api.PostUpdate(message)
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        print("Try explicitly specifying the encoding with the --encoding flag")
        sys.exit(2)
    print("%s just posted: %s" % (status.user.name, status.text))

if __name__ == "__main__":
    msg = sys.argv[1]
    keys = read_keys()
    api = twitter.Api(consumer_key=keys["data"]["consumer_key"],
                      consumer_secret=keys["data"]["consumer_secret"],
                      access_token_key=keys["data"]["access_token_key"],
                      access_token_secret=keys["data"]["access_token_secret"])
    tweet(api, msg)

