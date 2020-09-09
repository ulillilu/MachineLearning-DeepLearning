#로그인하고 마이페이지에 접근하기
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = "vpdlzm2"
PASS = "gh6811ghgh"

session = requests.session()

login_info = {
    "m_id": USER,  # 아이디 지정
    "m_passwd": PASS  # 비밀번호 지정
}
url_login = "https://www.yes24.com/Templates/FTLogin.aspx"
res = session.post(url_login, data=login_info)
res.raise_for_status()

url_mypage = "http://www.yes24.com/Member/FTMypageMain.aspx" 
res = session.get(url_mypage)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")