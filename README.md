# timee_pdf2excel
タイミーの源泉徴収票pdfをエクセルの一覧に変換するツール
タイミーの源泉徴収票pdfは複数の会社の源泉徴収票が1つpdfファイルに纏まっています。
確定申告には合計が必要なので一蘭を作成して合計を出力します。

- 確認環境
  Windows11

- python 
    Python 3.12.10

- requirements.txt
requirements.txtを用意しているので必要に応じてインストールしてください。
    pip install -r requirements.txt

- 基本的に必要なライブラリ
1. pandas
2. openpyxl
3. PySide6
4. pdfplumber
  pyinstallerもインストールしていますが、exe化のためなので通常不要です。

- フォルダ構成
    ├─exec;実行モジュール化した「タイミーエクセル変換.zip」ファイルを格納しています。
    ├─GUI :pyside6の.uiファイルを格納しています。
    └─src :複数のソースコードを格納しています。
    
- コード一覧
    .\GUI\mainGUI.ui            : pyside6に付属している「pyside6-designer.exe」で作成したファイル
    .\src\do_uic.py             : 上記、.uiファイルをpythonコードに変換するためのコード（手動でも可能ですが、備忘録としてコード化）
    .\src\edit_data.py          : PDFファイルをエクセルファイルに変換するコード
    .\src\mainGUI.py            : do_uic.pyで自動生成されるコード（編集不可）
    .\src\save_data.py          : GUIで入力されたデータを保存するためのコード
    .\src\timee_pdf2excel.py    : mainGUI.pyを使用して、各コードを実行するためのコード
    .\src\pdf_get_text.py       : PDFファイルからテキストデータを抽出するコード（デバッグのため、単体実行時はテキストファイルを作成します。）

- 使用方法
   1. pythonを実行可能(仮想環境をactivateしてください。)
   2. .\srcに移動する。
   3. 「python timee_pdf2excel.py」を実行
   
   
- その他
   1. 出力サンプル.xlsx :