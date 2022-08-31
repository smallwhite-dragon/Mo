from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QSplashScreen


class SplashPanel(QSplashScreen):
    def __init__(self):
        super(SplashPanel, self).__init__()
        message_font = QFont()
        message_font.setBold(True)
        message_font.setPointSize(14)
        self.setFont(message_font)
        pixmap = QPixmap("img/industry.jpg") #/Markware/backend/
        self.setPixmap(pixmap)
        self.timer = QTimer()
        self.timer.timeout.connect(self.num_timeout)
        self.timer.start(1000)
        self.num = 1
        self.showMessage('正在加载...', alignment=Qt.AlignBottom, color=Qt.white)
        self.show()

    def num_timeout(self):
        self.num += 1
        load_msg = '正在加载......'
        if self.num % 2:
            load_msg = '正在加载...'
        self.showMessage(load_msg+str(self.num) + '%', alignment=Qt.AlignBottom, color=Qt.white)
        if self.num == 100:
            self.timer.stop(1000)

    def mousePressEvent(self, evt):
        pass
        # 重写鼠标点击事件，阻止点击后消失
    def mouseDoubleClickEvent(self, *args, **kwargs):
        pass
        # 重写鼠标移动事件，阻止出现卡顿现象
    def enterEvent(self, *args, **kwargs):
        pass
        # 重写鼠标移动事件，阻止出现卡顿现象
    def mouseMoveEvent(self, *args, **kwargs):
        pass
        # 重写鼠标移动事件，阻止出现卡顿现象