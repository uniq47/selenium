import urllib.request


def downlaod(url, FILE):

    response = urllib.request.urlopen(url)
    print(response.status)
    responsetext = response.read()
    with open('status.html', 'wb') as fp:
    fp.write(responsetext)

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
    url="http://en.wikipedia.org/wiki/List_of_HTTP_status_codes"
    FILE="status.html")
