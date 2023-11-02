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
        self.statusBar().showMessage("google Trans App v1.0 Copyright")

if __name__ == '__main__':
    app = QApplication(sys.argv) # 앱 닫기 위해서 안함 안닫김
    myApp = MyGoogleTrans()
    myApp.show()
    sys.exit(app.exec_()) # 앱 닫기 위해서 안함 안닫김

