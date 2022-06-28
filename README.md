네이버 API를 사용하는 테스트 리파지토리입니다.
# API Keys
- 보안을 위해 config파일에 API 키를 따로 지정하여 변수를 호출하여 사용하였습니다.
- 테스트 진행시 각자의 API키를 생성하여 이용해주시길바랍니다.

# RESTful API Server
- 메인 실행 파일은 app.py 파일입니다.
- 추가 리소스 파일은 resources 폴더 내에 위치해있습니다.
- 클래스 사용의 혼선을 최소화하기 위해 API마다 파일로 생성해두었습니다.

# 파파고 API
### papago.py
- 파파고를 이용하여 API서버에서 사용자의 문장을 입력받아 번역한 결과를 보여줍니다.
- 테스트 코드로는 ref폴더에 papago_test.py 파일이 포함되어있습니다.
- [참고 자료](https://developers.naver.com/docs/papago/papago-nmt-api-reference.md)

# 네이버 검색 API
### naver_search.py
- 네이버 검색 API를 이용하여 API서버에서 사용자의 문장을 입력받아 인터넷에서 검색된 결과를 보여줍니다.
- 테스트 코드로는 ref폴더에 naver_search_test.py 파일이 포함되어있습니다.
- [참고 자료](https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4)
  - 검색 API가 여러개이므로 상황에 맞게 설정해주세요.