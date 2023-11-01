import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import googletrans

from PyQt5 import uic

from_class = uic.loadUiType("ui/hjUi.ui")[0]

trans = googletrans.Translator()  # 구글 번역 객체

class GoogleTrans(QMainWindow, from_class, trans):

    def __init__(self):
        super().__init__()
        self.setupUi(self) # 제작해 놓은 ui를 불러오기

        self.setWindowTitle("연습 프로그램") # 윈도우 타이틀
        self.setWindowIcon(QIcon("img/google.png")) #윈도우 아이콘
        self.statusBar().showMessage("Test Program v0.5 2023-11-01")

        self.btn1.clicked.connect(self.btn1_clicked) # 버튼1이 클릭되면 메서드 btn1_clicked 호출
        self.init_btn.clicked.connect(self.init)  # RESET이 클릭되면 메서드 init 호출

        self.lineEdit.textChanged.connect(self.changePrint)
        # lineEdit에 텍스트가 변경될 때마다 changePrint 함수가 실행

        self.lineEdit.returnPressed.connect(self.changePrint)
        # lineEdit에 텍스트가 입력 중(lineEdit가 선택 중)에 엔터키가 클릭되면 changePrint 함수가 실행됨

    def btn1_clicked(self): # 버튼1이 클릭되었을떄 실행될 메서드

        result1 = trans.translate(self, dest="en")  # 한글 -> 영어
        result2 = trans.translate(self, dest="ja")  # 한글 -> 일본어
        result3 = trans.translate(self, dest="zh-cn")  # 한글 -> 중국어
        self.lineEdit.setText(f"입력하신 '{self}'은 영어로 '{result1.text}' 입니다")
        self.lineEdit.setText(f"입력하신 '{self}'은 일본어로 '{result2.text}' 입니다")
        self.lineEdit.setText(f"입력하신 '{self}'은 중국어로 '{result3.text}' 입니다")
        # lineEdit에 setText() 가로 안의 문자열이 출력됨

    def changePrint(self):
        user_text = self.lineEdit.text()
        print(user_text)

    def init(self):
        self.textEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoogleTrans()
    ex.show()
    sys.exit(app.exec_())
