import os
import sys
import glob


def main():
    exec_path = r".venv\Scripts\pyside6-uic.exe" # pyside6-uic.exeのパスを設定してください。

    # このフォルダの.uiファイルの一覧を作成
    ui_files = glob.glob(os.path.join(os.path.dirname(__file__),"../GUI","*.ui"))
    
    if not ui_files:
        print("No .ui files found in the current directory.")
        return

    for ui_file in ui_files:
        # .uiファイルのパスを取得
        ui_path = os.path.abspath(ui_file)
       
        # 出力する.pyファイルのパスを作成
        base_name = os.path.basename(ui_path)
        base_name = base_name.replace(".ui", ".py")
        py_path = os.path.join(os.path.dirname(__file__),base_name)

        # コマンドを実行
        command = f"{exec_path} {ui_path} -o {py_path}"
        print(f"Executing: {command}")
        os.system(command)
        print(f"Generated: {py_path}")


if __name__ == "__main__":
    # スクリプトを実行
    main()
