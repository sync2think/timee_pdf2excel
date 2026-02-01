# -*- coding: utf-8 -*-
import sys
import os
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from mainGUI import Ui_dialog
from pdf_get_text import pdf_get_text
from edit_data import edit_data
from save_data import load_data, save_data
from PySide6.QtCore import QThread, Signal

class MainGUI(QDialog, Ui_dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # シグナルの接続
        self.pushButtonPdfFile.clicked.connect(self.select_pdf)
        self.pushButtonExcelFile.clicked.connect(self.select_excel)

        # config.ini からデータを読み込み    
        self.data = load_data()
        self.lineEditPdfFile.setText(self.data["pdf_path"])
        self.lineEditExcelFile.setText(self.data["excel_path"])
        if self.data["first_name"] != "" or self.data["last_name"] != "":
            self.lineEditFirstName.setText(self.data["first_name"])
            self.lineEditLastName.setText(self.data["last_name"])

        # labelNoticeに表示する文言を確認
        display_text = ""
        flg_error = False
        if self.data["pdf_path"] == "":
            display_text += "PDFファイルを選択してください。\n"
            flg_error = True
        if self.data["excel_path"] == "":
            display_text += "出力ファイルを指定してください。\n"
            flg_error = True
        if self.data["last_name"] == "":
            display_text += "苗字をカタカナで入力してください。\n"
            flg_error = True
        if self.data["first_name"] == "":
            display_text += "名前をカタカナで入力してください。\n"
            flg_error = True
        if flg_error is False:
            display_text = "OKボタンで処理を開始します。"
        self.labelNotice.setText(display_text)
        # buttonBox.accepted は setupUi で self.accept に接続されています。
        # 処理を実行するために accept メソッドをオーバーライドします。


    def select_pdf(self):
        """PDFファイル選択ダイアログを表示"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "PDFファイルを選択", "", "PDF Files (*.pdf)"
        )
        if file_path:
            self.lineEditPdfFile.setText(file_path)
            # 出力ファイル名の提案（同名のxlsx）
            base_name = os.path.splitext(file_path)[0]
            self.lineEditExcelFile.setText(base_name + ".xlsx")

    def select_excel(self):
        """保存先ファイル選択ダイアログを表示"""
        current_path = self.lineEditExcelFile.text()
        dir_path = os.path.dirname(current_path) if current_path else ""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "保存先を選択", dir_path, "Excel Files (*.xlsx);;CSV Files (*.csv)"
        )
        if file_path:
            self.lineEditExcelFile.setText(file_path)

    def accept(self):
        """OKボタンが押されたときの処理"""
        pdf_path = self.lineEditPdfFile.text()
        excel_path = self.lineEditExcelFile.text()

        # 入力チェック
        if not pdf_path or not os.path.exists(pdf_path):
            QMessageBox.warning(self, "エラー", "有効なPDFファイルを選択してください。")
            return

        if not excel_path:
            QMessageBox.warning(self, "エラー", "出力ファイルを指定してください。")
            return

        first_name = self.lineEditFirstName.text()
        last_name = self.lineEditLastName.text()
        if first_name == "" or last_name == "":
            QMessageBox.warning(self, "エラー", "苗字と名前をカタカナで入力してください。")
            return
        try:
            # 1. config.ini を保存
            # 日本は、苗字が先になるので、last_nameを先にする。
            data = {
                "pdf_path": pdf_path,
                "excel_path": excel_path,
                "last_name": last_name,
                "first_name": first_name,
            }
            save_data(data)

            # 2. データの編集とExcel/CSV保存
            edit_data(pdf_path, excel_path, first_name, last_name)

            QMessageBox.information(
                self, "完了", f"処理が完了しました。\n保存先: {excel_path}"
            )

            # ダイアログを閉じる
            super().accept()

        except Exception as e:
            QMessageBox.critical(
                self, "エラー", f"処理中にエラーが発生しました:\n{str(e)}"
            )
            # エラー時はダイアログを閉じない


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec())
