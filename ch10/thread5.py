import time, threading, requests

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, resp.text)

th = threading.Thread(target=getHtml, args=("https://www.google.com",))
th.start()

print("작업 종료")

