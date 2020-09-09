from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('E:/Python_2/chromedriver')
driver.implicitly_wait(60)

driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('ulil___lilu')
driver.find_element_by_name('pw').send_keys('gh6811ghgh')
#로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
#네이버페이 구매내역 리스트 불러오기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')
for n in notices:
    print(n.text.strip())
# Chrome을 헤드리스 모드로 설정
options = webdriver.ChromeOptions()
options.add_argument('-headless')
# 화면을 캡처해서 저장
driver.save_screenshot("Website.png")
# 브라우저 종료
