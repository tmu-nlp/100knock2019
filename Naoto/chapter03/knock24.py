import re
num = 0
with open("jawiki-イギリス.json") as fp:
    json_data = fp.readline()
    while json_data:
        media_http_https = re.search("http(s:|:)[a-zA-Z0-9_\./-]+", json_data)
        media_jpg_jpeg = re.search("[^\s:]+\.(jpe?g|JPE?G)", json_data)
        # if media_http_https is not None:
        #     print(media_http_https.group())
        if media_jpg_jpeg is not None:
            print(media_jpg_jpeg.group())
            num += 1
        json_data = fp.readline()

print(num)