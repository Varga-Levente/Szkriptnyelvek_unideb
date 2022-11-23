import requests as rq
import json

def main():
    response = rq.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
    image_data = json.loads(response.text)
    print("https://bing.com"+image_data['images'][0]['url'])

if __name__ == '__main__':
    main()