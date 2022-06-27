# OpenAPI 이용하려면 requests 라이브러리 이용
import requests
from config import Config

# 해당 URL로 번역 요청
URL = "https://openapi.naver.com/v1/papago/n2mt"

# 헤더 설정, 부여받은 파파고 API키 입력
headers = {
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Naver-Client-Id" : Config.client_id,
    "X-Naver-Client-Secret" : Config.client_secret,
}

# source=원본언어, target=목적언어, text=번역할텍스트(최대 5000자)
data = {
    "source" : "ko",
    "target" : "en",
    "text" : "만나서 반갑습니다."
}

# 데이터를 보낼 URL, 데이터, API키가 담긴 헤더 정보
res = requests.post(URL, data=data, headers=headers)

print(res.json()['message']['result']['translatedText'])