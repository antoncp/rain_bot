import requests


def get_clouds_image():
    """Get gif-image from Buienradar with current position of clouds
    over the Netherlands.
    """
    try:
        gif_url = 'https://api.buienradar.nl/image/1.0/RadarMapNL?w=500&h=512'
        with open('media/clouds/now.gif', 'wb') as f:
            f.write(requests.get(gif_url).content)
        return True
    except Exception as e:
        print(e.message, e.args)
        return False
