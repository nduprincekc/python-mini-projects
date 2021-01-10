from requests import get  # to make GET request
from os import system, getcwd, path


url = "https://source.unsplash.com/random"
filename = "random.jpg"


def download(url, file_name):
    '''
    downloading the filebb and saving it
    '''
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


def setup(pathtofile):
    '''
    setting the up filebb
    '''
    system("nitrogen --set-auto {}".format(path.join(getcwd(), pathtofile)))


if __name__ == "__main__":
    download(url, filename)
    setup(filename)
