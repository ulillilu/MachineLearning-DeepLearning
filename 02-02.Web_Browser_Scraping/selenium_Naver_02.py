#로그인 후 쇼핑 목록 출력법2
from selenium.webdriver import Chrome, ChromeOptions

USER = "ulil___lilu"
PASS = "gh6811ghgh"

options = ChromeOptions()
options.add_argument('-headless')
browser = Chrome('E:/Python_2/chromedriver')

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

products = browser.find_elements_by_css_selector(".p_info span")
print(products)
for product in products:
  print("-", product.text)
