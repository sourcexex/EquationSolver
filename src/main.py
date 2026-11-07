import sys
import time

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from core import tools
from ui.ui_MainWindow import Ui_MainWindow
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox



logging.basicConfig(level=logging.DEBUG)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        logging.debug("程序已启动")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("就绪")
        button_solve = QAction("求解",self)
        button_clear = QAction("清除",self)
        button_solve.triggered.connect(self.solve_clicked)
        button_clear.triggered.connect(self.clear_clicked)
        button_solve.setStatusTip("求解方程")
        button_clear.setStatusTip("清除全部")
        self.ui.lineEdit_eqn.setStatusTip("输入方程,多个方程用 \",\" 隔开,没有等号默认等于0")
        self.ui.lineEdit_range.setStatusTip("输入约束范围,如 \"0<=x<=99\" ")
        self.ui.lineEdit_unknow.setStatusTip("输入未知数,多个未知数用 \",\" 隔开,不填为自动")
        self.ui.toolBar.addAction(button_solve)
        self.ui.toolBar.addAction(button_clear)
        self.ui.action_clear.triggered.connect(self.clear_clicked)
        self.ui.action_solve.triggered.connect(self.solve_clicked)
        self.ui.action_about.triggered.connect(self.about_clicked)
        self.ui.action_help.triggered.connect(self.help_clicked)

    def clear_clicked(self):
        logging.debug("清除按钮已按下")
        self.ui.lineEdit_eqn.setText("")
        self.ui.lineEdit_unknow.setText("")
        self.ui.textBrowser_output.setText("")
        self.ui.textBrowser_output.setEnabled(False)
        self.ui.lineEdit_range.setText("")

    def solve_clicked(self):
        global time_used, answer
        logging.debug("求解按钮已按下")
        eqn = self.ui.lineEdit_eqn.text()
        unknow = self.ui.lineEdit_unknow.text()
        if self.ui.radioButton_fr_auto.isChecked():
            fr = None
        elif self.ui.radioButton_fr_true.isChecked():
            fr = True
        elif self.ui.radioButton_fr_false.isChecked():
            fr = False
        if self.ui.radioButton_im_auto.isChecked():
            im = None
        elif self.ui.radioButton_im_true.isChecked():
            im = True
        elif self.ui.radioButton_im_false.isChecked():
            im = False
        if self.ui.radioButton_ne_auto.isChecked():
            ne = None
        elif self.ui.radioButton_ne_true.isChecked():
            ne = True
        elif self.ui.radioButton_ne_false.isChecked():
            ne = False
        if unknow == "":
            unknow = None
        if self.ui.lineEdit_range.text() is None:
            constraints = None
        else:
            constraints = self.ui.lineEdit_range.text()
        try:
            time_1 = time.time()
            answer = tools.solve_equation(eqn, unknow, fr, im, ne, constraints)
            time_2 = time.time()
            time_used = time_2-time_1
            logging.debug(f"结果:{answer}\n用时:{time_used}")
        except Exception as e:
            logging.error(f"错误:{e}")
            if self.ui.lineEdit_eqn.text() == "":
                self.ui.textBrowser_output.setText("未填写方程!!!\n请填写方程")
                self.ui.textBrowser_output.setEnabled(True)
            else:
                self.ui.textBrowser_output.setText(f"求解方程出错,请检查方程是否错误!!!\n详细错误信息如下:\n{str(e)}")
                self.ui.textBrowser_output.setEnabled(True)
        if answer is None:
            self.ui.textBrowser_output.setText("此方程无解!!!\n请检查范围，未知数和方程是否正确")
        else:
            if isinstance(answer,dict) == False and len(answer) > 1:
                str_result = "以下是所有解:\n"
                for i in range(len(answer)):
                    ans_tmp = answer[i]
                    str_result = str_result + str(ans_tmp)[1:-1] + "\n"+"-"*10+"\n"
                    str_result = str_result+"\n用时: "+str(time_used)
                self.ui.textBrowser_output.setText(str_result)
            else:
                self.ui.textBrowser_output.setText(str(answer)[1:-1]+"\n\n用时:"+str(time_used))
        self.ui.textBrowser_output.setEnabled(True)

    def about_clicked(self):
        logging.debug("关于按钮已按下")
        about_msg = QMessageBox()
        about_msg.setWindowTitle("关于")
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        about_msg.setWindowIcon(icon)
        about_msg.setText("Equation Solver\n版本: v1.0\n作者: SourceX")
        about_msg.show()
        about_msg.exec()

    # def about_clicked(self):
    #     logging.debug("关于按钮已按下")
    #     self.w = Ui_Dialog()
    #     self.w.show()


    def help_clicked(self):
        logging.debug("帮助按钮已按下")
        help_msg = QMessageBox()
        help_msg.setWindowTitle("帮助")
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        help_msg.setWindowIcon(icon)
        help_msg.setText(tools.show_help())
        help_msg.show()
        help_msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()