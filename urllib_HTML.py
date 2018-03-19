#!python

import sys
import urllib.request

# urlretrieve is a legacy function that worksin 2.7


def main():
    print(
        "Hello there. this is a demo of how to use urllib.request.urlopen" +
        " to get website data.")
    print("urllib.urlretrieve no longer works with Python 3.")

    WORD_list_URL = r"http://learncodethehardway.org/words.txt"
    urllib_code_howto = r"https://docs.python.org/3/howto/urllib2.html"
    flask_REST_code_URL = r"https://blog.miguelgrinberg.com/post/" +
    "designing-a-restful-api-with-python-and-flask"
    py_north_logo1_URL = r"https://secure.meetupstatic.com/photos/event/" +
    "9/2/7/8/global_434497496.jpeg"
    py_north_logo2_URL = r"https://secure.meetupstatic.com/photos/" +
    "theme_head/1/3/3/d/full_6724925.jpeg"

    dumpURL(WORD_list_URL, "words.txt")
    dumpURL(urllib_code_howto, "urllib.html")
    dumpURL(flask_REST_code_URL, "API-python-and-flask.html")
    dumpURL(py_north_logo1_URL, "Logo1.jpg")
    dumpURL(py_north_logo2_URL, "Logo2.jpg")


def dumpURL(URLink, file_name):

    f = urllib.request.urlopen(URLink)      # open the link
    x = f.read()    # read the page
    with open(file_name, 'wb') as out:
        out.write(x)
        out.close()


if __name__ == '__main__':
    main()
