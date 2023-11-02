import sys

from PyQt5 import uic      # Qt Designer에서 제작한 ui를 불러와주는 클래스
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans
# ----------------------- 모듈 준비 완료

form_class = uic.loadUiType("ui/hjUi.ui")[0]
# Qt Designer에서 제작한 ui 불러오기

class MyGoogleTrans(QMainWindow, form_class):
    def __init__(self): # 초기화자(생성자) 실행되면 처음실행되는 것
        super().__init__() # 부모 클래스의 초기화자 호출
        self.setupUi(self) # 제작해 놓은 googleUi.ui를 연결
        self.setWindowTitle("구글 번역기") # 번역기 앱의 타이틀
        self.setWindowIcon(QIcon("icon/google.png")) # 번역기 앱의 아이콘
        self.statusBar().showMessage("google Trans App v1.0 Copyright ⓒ HJP")

        self.bnt_trans.clicked.connect(self.trans_function) # trans_function의 시그널(signar)
        self.input_kor_test.returnPressed.connect(self.changePrint)
        self.reset_btn.clicked.connect(self.reset)

    def trans_function(self): # trans_function의 슬롯(slot)
        trans_kor = self.input_kor_test.text() # input_kor_test에 입력된 한글을 가져옴

        trans = googletrans.Translator() # 구글트랜스 모듈의 객체(번역해 주는 객체

        # print(googletrans.LANGCODES) # 번역 언어 ticker 불러오기

        trans_eng = trans.translate(trans_kor, dest='en') # 영어 번역결과
        trans_jap = trans.translate(trans_kor, dest='ja') # 일본어 번역결과
        trans_chn = trans.translate(trans_kor, dest='zh-cn') # 중국어 번역결과

        self.output_eng_text.append(trans_eng.text)
        self.output_jap_text.append(trans_jap.text)
        self.output_chn_text.append(trans_chn.text)

    def changePrint(self):
        user_text = self.input_kor_test.text()
        print(user_text)

    def reset(self): # 슬롯
        self.input_kor_test.clear()
        self.output_eng_text.clear()
        self.output_jap_text.clear()
        self.output_chn_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv) # 앱 닫기 위해서(안함 안닫김)
    myApp = MyGoogleTrans()
    myApp.show()
    sys.exit(app.exec_()) # 앱 닫기 위해서(안함 안닫김)

