from urllib.parse import unquote
import requests, re

# user input fb reel url
url_reel = input("Enter url reel: ").replace("www","mbasic")
response = requests.get(url_reel)

# parse url
if 'video_redirect' in response.text:
    reel = re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"', response.text)
    download_url = unquote(reel.group(1)).replace(";","&")
    
    # download video
    response = requests.get(download_url)
    size = round(int(response.headers.get("Content-Length")) / 1024)
    
    # display size in video
    print(f"Video size is {size} KB")

    # save the video
    with open("video.mp4", "wb") as s:
        for data in response.iter_content(chunk_size=1024):
            s.write(data)

        # display success download
        print("Download Success!")
else:
    exit("video not found")

