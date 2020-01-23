import gdown
import sys

url = 'https://drive.google.com/uc?id='
output = 'spam.txt'


def download(id, dest):
    print(url + id)
    gdown.download(url + id, output, quiet=False)


file_id = sys.argv[1]
destination = sys.argv[2]

download(file_id, destination)

