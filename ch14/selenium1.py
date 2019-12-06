from selenium import webdriver

url = "http://www.naver.com"
brower = webdriver.PhantomJS()

brower.implicitly_wait(3)  # 3초대기

brower.get(url)
# 해당 페이지의 화면을 스크린샷으로 저장한다. 
brower.save_screenshot("website1.png")
brower.quit()