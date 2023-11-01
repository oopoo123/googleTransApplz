import pprint

import googletrans

trans = googletrans.Translator() # 구글 번역 객체

str = input("번역할 문장을 입력하세요:")

# pprint.pprint(googletrans.LANGUAGES) # 번역 언어 ticker 불러오기 (pprint 세로로 데이터 불러오기)

result1 = trans.translate(str, dest="en") # 한글 -> 영어
result2 = trans.translate(str, dest="ja") # 한글 -> 일본어
result3 = trans.translate(str, dest="zh-cn") # 한글 -> 중국어

print(f"입력하신 '{str}'은 영어로 '{result1.text}' 입니다")
print(f"입력하신 '{str}'은 일본어로 '{result2.text}' 입니다")
print(f"입력하신 '{str}'은 중국어로 '{result3.text}' 입니다")