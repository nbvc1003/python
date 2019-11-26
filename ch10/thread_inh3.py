import threading, time, requests

class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    #run 메소드는 매게 변수를 갖지 않는다.
    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, resp.text)

th = HtmlGetter('https://www.nate.com')
th.start()


