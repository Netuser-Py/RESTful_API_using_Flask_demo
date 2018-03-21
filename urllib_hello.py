#!python

import sys
import urllib.request

# urlretrieve is a legacy function that worksin 2.7


def main():
    print(
        "Hello there. this is a demo of how to use urllib.request.urlopen" +
        " to get website data.")
    print("urllib.urlretrieve no longer works with Python 3.")

    hello_URL = r"http://127.0.0.1:5000/"
    dumpURL(hello_URL, "hello.txt")


def dumpURL(URLink, file_name):

    f = urllib.request.urlopen(URLink)      # open the link
    x = f.read()    # read the page
    with open(file_name, 'wb') as out:
        out.write(x)
        out.close()


if __name__ == '__main__':
    main()
