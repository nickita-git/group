import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт
import argparse
import requests
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--coords', nargs=2)
parser.add_argument('--size', nargs=2)
args = parser.parse_args()
map_params = {
    "ll": ','.join(args.coords),
    "l": 'map',
    "spn": ','.join(args.size)}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(
    response.content)).show()
