import urllib.request

response = urllib.request.urlopen(
    "http://en.wikipedia.org/wiki/List_of_HTTP_status_codes")
print(response)
print(dir(response))
print(response.status)
responsetext = response.read()
print(len(responsetext))
print(type(responsetext))
with open('status.html', 'wb') as filepointer:
    filepointer.write(responsetext)
