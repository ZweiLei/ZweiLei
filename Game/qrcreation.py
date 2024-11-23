import pyqrcode
import os

class QRCreate:
    def __init__(self) -> None:
        self.path = self.get_path()
        self.text = self.get_text()
        self.filename = self.get_filename()

    def get_path(self):
        path = input("输入二维码存放的文件夹：")
        return path
    
    def get_text(self):
        text = input("输入要创建二维码的文字: ")
        return text
    
    def get_filename(self):
        return input("输入新二位码的文件名：")
    
    def create_qr(self):
        current_dir = os.getcwd()
        if current_dir != self.path:
            os.chdir(self.path)
        qr_code = pyqrcode.create(self.text)
        qr_code.svg(f"{self.filename}.svg", scale = 8)

qrcode = QRCreate()
qrcode.create_qr()

        














