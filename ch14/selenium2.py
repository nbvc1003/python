from selenium import webdriver

USER = "nbvcn"
PASS = "nam7663007"

brower = webdriver.PhantomJS()
brower.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login"
brower.get(url_login)
print("로그인 ")

e = brower.find_element_by_id("id")
e.clear()
# 현재 네이버 로그인은 업체측에서 막아 놓음
e.send_keys(USER)
e = brower.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)
form = brower.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit() # 로그인 버튼을 클릭합니다.

brower.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
# 쇼핑 목록 출력하기
products = brower.find_elements_by_css_selector(".p_info span")
print(products)
for product in products:
    print("-", product.text)

