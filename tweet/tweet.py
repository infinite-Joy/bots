import twitter
import yaml

with open("keys.yaml", "r") as data:
    try:
        keys = yaml.load(data)
    except yaml.YAMLError as exc:
        print(exc)
