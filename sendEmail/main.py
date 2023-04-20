import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from mail import Ui_MainWindow
from email_send import send_email


class EmailSender(QMainWindow):
        def __init__(self):
                super(EmailSender, self).__init__()  # clas'ı self'e atadık

                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)  # MainWin. içindeki setupUİ sınıfı self'e atadık

                self.ui.pushButton.clicked.connect(self.send_email)
        def send_email(self):
                if self.ui.txtBaslik.text():
                        send_email(kime=self.ui.txtBaslik.text(),email=self.ui.txtMesaj.toPlainText())
                else:
                        mesaj=QMessageBox() 
                        mesaj.setIcon(QMessageBox.Critical)
                        mesaj.setText("Lütfen boşlukları doldurunuz..")
                        mesaj.setWindowTitle("HATA")
                        mesaj.exec_()       

app = QApplication(sys.argv)
win = EmailSender()
win.show()
sys.exit(app.exec_()) # app.execc programa etkilşimli ilerleme saglar yani kullanıcı
                        # hareketlerine göre ilerletir
