import requests
from config import Config

# URL, client_id, client_secret은 config 파일에 있음
# 헤더 설정, 부여받은 네이버검색 API키 입력
headers = {
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Naver-Client-Id" : Config.naver_search_client_id,
    "X-Naver-Client-Secret" : Config.naver_search_client_secret,
}

# 필수  query = 검색어 UTF-8 인코딩
# 추가 옵션 display = 검색 결과 출력 건수 지정 (최소10(기본값)~최대100)
# 추가 옵션 start = 검색 시작 위치 (최소1(기본값)~최대1000)
# 추가 옵션 sort = 정렬(sim:유사도(기본값), date:날짜)

# GET호출, requests.get()함수 이용, 데이터 셋팅
data = {
    "query" : "마녀"
}

res = requests.get(Config.naver_search_news_url, params=data, headers=headers)

res = res.json()

print(res)