import twitter
import yaml

with open("keys.yaml", "r") as data:
    try:
        print(yaml.load(data))
    except yaml.YAMLError as exc:
        print(exc)
