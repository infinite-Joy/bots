import facebook
import yaml


def get_keys():
    with open("fb_keys.yaml", "r") as data:
        try:
            return yaml.load(data)
        except yaml.YAMLError as exc:
            print(exc)


def main():
    # Fill in the values noted in previous steps here
    cfg = get_keys()

    api = get_api(cfg)
    msg = "Hello, world!"
    status = api.put_wall_post(msg)
    return status


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    # Get page token to post as the page. You can skip
    # the following if you want to post as yourself.
    resp = graph.get_object('me/albums')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph
    # You can also skip the above if you get a page token:
    # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
    # and make that long-lived token as in Step 3


if __name__ == "__main__":
    status = main()
    print("posted on page", status)
