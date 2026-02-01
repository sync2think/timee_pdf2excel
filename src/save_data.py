import configparser
import os
import sys

# config.iniを書込む関数
def save_data(data: dict):
    config = configparser.ConfigParser()
    config.read("config.ini")
    # config["DEFAULT"] = data
    if "pdf_path" in data:
        config["DEFAULT"]["pdf_path"] = data["pdf_path"].replace(" ", "")
    if "excel_path" in data:
        config["DEFAULT"]["excel_path"] = data["excel_path"].replace(" ", "")
    if "first_name" in data:
        config["DEFAULT"]["first_name"] = data["first_name"].replace(" ", "")
    if "last_name" in data:
        config["DEFAULT"]["last_name"] = data["last_name"].replace("", "")
    with open("config.ini", "w") as configfile:
        config.write(configfile)

# config.iniを読み込み辞書を返す関数
def load_data():
    if os.path.exists("config.ini") is False:
        data:dict = {"pdf_path": "", "excel_path": "", "first_name": "", "last_name": ""}
        return data
    config = configparser.ConfigParser()
    config.read("config.ini")
    config_items = config.items("DEFAULT")
    data = dict(config_items)
    return data

if __name__ == "__main__":
    if os.path.exists("config.ini"):
        os.remove("config.ini")

    data = {
        "pdf_path": r"c:\\time.pdf",     # フルパスで入力するpdfファイルを記述してください。
        "excel_path": r"c:\\time.xlsx",  # フルパスで出力するexcelファイルを記述してください。
        "last_name": "ヤマダ",
        "first_name": "タロウ",
    }
    save_data(data)
    data = load_data()

    print(data)