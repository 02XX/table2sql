from PySide6.QtWidgets import QWidget,QApplication,QFileDialog
from PySide6.QtCore import QThread,Signal,QObject
#from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest,QNetworkReply
from window import Ui_table2sql
import requests,base64,io,os
import pandas as pd
from dotenv import load_dotenv
load_dotenv("./.env")

class tableThread(QThread):
    finishedReply = Signal(dict)
    def __init__(self,img_path) -> None:
        super().__init__()
        # 请登录后前往 “工作台-账号设置-开发者信息” 查看 x-ti-app-id
        # 示例代码中 x-ti-app-id 非真实数据
        self._app_id = os.getenv("app_id")
        # 请登录后前往 “工作台-账号设置-开发者信息” 查看 x-ti-secret-code
        # 示例代码中 x-ti-secret-code 非真实数据
        self._secret_code = os.getenv("secret_code")
        self._img_path = img_path
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    def recognize(self):
        # 通用表格识别
        url = 'https://api.textin.com/ai/service/v2/recognize/table?excel=1'
        head = {}
        try:
            image = self.get_file_content(self._img_path)
            head['x-ti-app-id'] = self._app_id
            head['x-ti-secret-code'] = self._secret_code
            result = requests.post(url, data=image, headers=head)
            return result.text
        except Exception as e:
            return e
    def setPath(self,path):
        self._img_path = path
    def run(self):
        text = self.recognize()
        text = eval(text)
        self.finishedReply.emit(text)

class handleExcel(QObject):
    finishedSql = Signal(str,str)
    def __init__(self,text) -> None:
        super().__init__()
        self.text = text
    def handle(self):
        decoded_data = base64.b64decode(self.text["result"]["excel"])
        memory_file = io.BytesIO(decoded_data)
        df = pd.read_excel(memory_file)
        df.to_excel("output.xlsx", index=False)
        self.column_names = df.columns.tolist()
        data_range = range(0, df.shape[0])
        self.data_list = []
        for i in data_range:
            row_data = df.iloc[i].tolist()
            row_data = [str(item) for item in row_data]
            self.data_list.append(row_data)
    def generateSQL(self):
        #创建表
        schema = "CREATE TABLE {0} "
        schema = schema + "(" + ', '.join(self.column_names) + ");"
        #插入数据
        sql = "INSERT INTO {0} VALUES "
        for i in self.data_list:
            temp = "("+', '.join(i) + ") "
            sql += temp   
        sql = sql[:-1]
        sql += ";"
        self.finishedSql.emit(sql,schema)
    def setText(self,text):
        self.text = text

class mainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_table2sql()
        self.ui.setupUi(self)
        self.text = {}
        self.path = ""
        self.work = tableThread(self.path)
        self.handle_excel = handleExcel(self.text)
        # connect
        self.work.finishedReply.connect(self.saveText)
        self.handle_excel.finishedSql.connect(self.showSQL)
        self.ui.postPushButton.clicked.connect(self.postData)
        self.ui.sqlPostPushButton.clicked.connect(self.generSQL)
        self.ui.openPushButton.clicked.connect(self.openFile)
    def openFile(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            self.path=selected_file
            self.ui.plainTextEdit.setPlainText("打开成功")
    def postData(self):
        self.work.setPath(self.path)
        self.work.start()
    def saveText(self,text):
        self.text = text
        self.ui.plainTextEdit.setPlainText("post finished")
    def generSQL(self):
        self.handle_excel.setText(self.text)
        self.handle_excel.handle()
        self.handle_excel.generateSQL()
    def showSQL(self,sql,schema):
        table_name = "relation"
        if self.ui.lineEdit.text() != "":
            table_name = self.ui.lineEdit.text()
        self.ui.plainTextEdit.setPlainText(sql.format(table_name))
        self.ui.plainTextEdit_2.setPlainText(schema.format(table_name))
app = QApplication()
window = mainWindow()
window.show()
app.exec()