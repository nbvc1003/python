# 파이썬 매뉴얼을 재귀적으로 다운받는 프로그램
# 모듈 읽어 들이기
from bs4 import BeautifulSoup
from urllib.request import * # 인터넷 데이터 내려 받기
from urllib.parse import * # URL분석
from os import makedirs # directory생성
import os.path, time, re # 정규 표현식을 위한 re 모듈
# 이미 처리한 파일인지 확인하기 위한 변수
# a.html에서 b.html로 이동하는 태그 b.html에서 a.html로 이동하는 태그가 있으면
# 무한 루프가 생길 수 있으므로 두 번 이상 반복하지 않도록 처리 위한 변수
proc_files = {} # 전역 변수 초기화
# HTML 내부에 있는 링크를 추출하는 함수
def enum_links(html, base): # html을 분석하고 링크 추출
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']") # CSS 내용을 찾는다.
    links += soup.select("a[href]") # 링크 _ 링크내용을 찾아서 추가..
    result = []
    # href 속성을 추출하고, 링크를 절대 경로로 변환
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)  # 절대 경로로 변환
        result.append(url)
    return result
# 파일을 다운받고 저장하는 함수
def download_file(url): # 인터넷에 있는 파일 다운로드위한 폴더 생성
    o = urlparse(url)
    # o.netloc = docs.python.org , o.path = /3.5/library/
    savepath = "./" + o.netloc + o.path # ./docs.python.org/3.5/library/

    # 주어진 path가 폴더라면 index.html 을 만들어준다.
    if re.search(r"/$", savepath): # 폴더라면 index.html
        savepath += "index.html"
    savedir = os.path.dirname(savepath) # 해당폴더가 있는지 채크
    # 모두 다운됐는지 확인
    if os.path.exists(savepath):
        return savepath
    # 다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir) # 폴더생성
    # 파일 다운받기
    try:
        print("download=", url)
        urlretrieve(url, savepath) # 다운로드..
        time.sleep(1)  # 1초 휴식
        return savepath
    except:
        print("다운 실패: ", url)
        return None
# HTML을 분석하고 다운받는 함수
def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None:
        return
    if savepath in proc_files:
        return  # 이미 처리됐다면 실행하지 않음
    proc_files[savepath] = True
    print("analyze_html=", url)
    # 링크 추출
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)
    for link_url in links:
        # 링크가 루트 이외의 경로를 나타낸다면 무시 -> 링크 내용이 하위가아닌 외부라면 무시
        if link_url.find(root_url) != 0: # 내부 링크 인지 확인하는 절차 .
            if not re.search(r".css$", link_url):  # re.search(pattern, string)
                # string에서 pattern과 매치하는 텍스트를 탐색
                continue
        # HTML이라면
        if re.search(r".(html|htm)$", link_url):
            # 재귀적으로 HTML 파일 분석하기
            analyze_html(link_url, root_url)
            continue
        download_file(link_url)  # 기타 파일
if __name__ == "__main__":
    # URL에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)