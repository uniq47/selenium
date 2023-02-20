import urllib.request
import os


def download(url, FILE):
    # if file is exists open the fiml file return contents
    # else crawl adnd return the content
    if os.path.exists(FILE):
        with open(FILE, 'rb') as fp:
            return fp.read()

    response = urllib.request.urlopen(url)
    print(response.status)
    responsetext = response.read()

    with open(FILE, 'wb') as filepointer:
        filepointer.write(responsetext)

    return responsetext


# response = urllib.request.urlopen(
#     "http://en.wikipedia.org/wiki/List_of_HTTP_status_codes")
# print(response)
# print(dir(response))
# print(response.status)
#  with open('status.html', 'wb') as filepointer:
#     filepointer.write(responsetext)
# print(len(responsetext))
# print(type(responsetext))


page = download(
    url="http://en.wikipedia.org/wiki/List_of_HTTP_status_codes",
    FILE="status.html",)
