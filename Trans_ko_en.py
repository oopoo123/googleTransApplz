import sys

import googletrans

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# -------------------------- 모듈

form_class = uic.loadUiType("ui/KoEn.ui")[0]

class GoogleKE(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("한/영 번역기")
        self.setWindowIcon(QIcon("icon/google.png"))
        self.statusBar().showMessage("google Trans App v1.0 Copyright ⓒ HJP")

        self.en_btn.clicked.connect(self.trans_en)
        self.ko_btn.clicked.connect(self.trans_ko)
        self.reset_btn.clicked.connect(self.reset)

    def trans_en(self):
        trans_kor = self.ko_text.text()
        trans = googletrans.Translator()

        trans_k = trans.translate(trans_kor, dest='en')
        self.en_text.append(trans_k.text)


    def trans_ko(self):
        trans_eng = self.en_line.text()
        trans = googletrans.Translator()

        trans_e = trans.translate(trans_eng, dest='ko')
        self.ko_line.append(trans_e.text)

    def reset(self):
        self.ko_text.clear()
        self.en_line.clear()
        self.en_text.clear()
        self.ko_line.clear()



if __name__=="__main__":
    app = QApplication(sys.argv)
    myT = GoogleKE()
    myT.show()
    sys.exit(app.exec_())


