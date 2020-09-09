from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_argument('-headless')
browser = Chrome('E:/Python_2/chromedriver')
# 적당한 웹 페이지 열기
browser.get("https://google.com")
# 자바스크립트 실행
r = browser.execute_script("return 100 + 50")
print(r)
