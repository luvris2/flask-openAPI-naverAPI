# OpenAPI 이용하려면 requests 라이브러리 이용
import requests

from flask import request
from flask_restful import Resource
from ref.config import Config

class PapagoResource(Resource):
    def get(self) :
        # 헤더 설정, 부여받은 파파고 API키 입력
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Naver-Client-Id" : Config.naver_papago_client_id,
            "X-Naver-Client-Secret" : Config.naver_papago_client_secret,
        }

        # 파라미터로 번역 할 텍스트 받기
        text = request.args['text']

        # source=원본언어, target=목적언어, text=번역할텍스트(최대 5000자)
        data = {
            "source" : "ko",
            "target" : "en",
            "text" : text
        }

        # 데이터를 보낼 URL, 데이터, API키가 담긴 헤더 정보
        res = requests.post(Config.naver_papago_url, data=data, headers=headers)
        res = res.json()
        res['message']['result']['srcLangType']

        return {
            "원본언어" : res['message']['result']['srcLangType'],
            "원문" : text,
            "번역언어" : res['message']['result']['tarLangType'],
            "번역" : res['message']['result']['translatedText']
        }, 200