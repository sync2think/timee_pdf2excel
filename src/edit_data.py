import pandas as pd
import csv
import openpyxl
from openpyxl.styles.borders import Border, Side
import os
import sys

from pdf_get_text import pdf_get_text


def adjust_column_width(sheet):
    # No.列が"合計"行までチェックする。
    # 各列の最大文字数から列幅を調整する。
    for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
                elif len(str(cell.value)) == 0:
                    break
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        sheet.column_dimensions[column].width = adjusted_width
        if "会社住所" in col[0].value:
            adjusted_width = (max_length) * 1.8
            sheet.column_dimensions[column].width = adjusted_width
        if "会社名" in col[0].value:
            adjusted_width = (max_length + 1) * 2.0
            sheet.column_dimensions[column].width = adjusted_width
        if "退職日" in col[0].value:
            adjusted_width = (max_length + 4) * 1.2
            sheet.column_dimensions[column].width = adjusted_width

    # sheet.column_dimensions["A"].width = 8


def adjust_column_format(sheet):
    # 給与	源泉徴収額列を探す
    for col in sheet.columns:
        if "給与" in col[0].value or "源泉徴収額" in col[0].value:
            for cell in col:
                for cell in col:
                    cell.number_format = '"¥"#,##0'


def add_border_line(sheet):
    # 罫線を引く
    side = Side(style="thin", color="000000")
    border = Border(top=side, bottom=side, left=side, right=side)
    for row in sheet:
        for cell in row:
            sheet[cell.coordinate].border = border


def edit_excel(src_path, dst_path):
    workbook = openpyxl.load_workbook(src_path)
    # sheet = workbook.active
    # シートは１シートしかないので、シートを取得
    sheet = workbook.worksheets[0]
    # シート名をタイミー源泉徴収票にする
    sheet.title = "タイミー源泉徴収票"
    # 列幅の調整
    adjust_column_width(sheet)
    # 給与	源泉徴収額の書式を1000　→ ￥1,000とする。
    adjust_column_format(sheet)
    # 罫線を引く
    add_border_line(sheet)
    # dst_pathに保存
    workbook.save(dst_path)
    workbook.close()


def edit_data(src_path: str, dst_path: str, first_name: str, last_name: str):
    all_text = pdf_get_text(src_path, None)
    if all_text is None:
        print(f"PDFファイルを読み込めませんでした。{src_path}")
        return
    lines = all_text.split("\n")
    salary = 0
    total_salary = 0
    total_source_tax = 0
    salary_list = []
    salary_dict: dict = {}
    flg_nenmatu = False
    flg_dst_place = False
    flg_dst_name = False
    flg_skip_line = True
    for line in lines:
        if (first_name in line) and (last_name in line):
            flg_skip_line = False
            continue
        if flg_skip_line:
            continue
        if "給与" in line:
            items = line.split()
            salary = int(f"{items[1]}{items[2]}")
            total_salary += salary
            salary_dict["給与"] = salary
            salary_dict["源泉徴収額"] = int(f"{items[3]}")
            total_source_tax += salary_dict["源泉徴収額"]
            continue
        if "年調未済" in line:
            flg_nenmatu = True
            continue
        if flg_nenmatu:
            items = line.split()
            date_str = f"令和{items[0]}年{items[1]}月{items[2]}日"
            flg_nenmatu = False
            flg_dst_place = True
            salary_dict["退職日"] = date_str
            continue
        if flg_dst_place:
            salary_dict["会社住所"] = line
            flg_dst_place = False
            flg_dst_name = True
            continue
        if flg_dst_name:
            items = line.split()
            salary_dict["会社名"] = items[0]
            salary_dict["電話番号"] = str(items[1])
            flg_dst_name = False
            salary_list.append(salary_dict.copy())
            salary_dict = {}
            continue

    # リストの辞書をpandasのDataFrameに変換
    df = pd.DataFrame(salary_list)
    # No.を追加
    df["No."] = range(1, len(df) + 1)
    # 列の順番を変更
    df = df.reindex(
        columns=[
            "No.",
            "会社名",
            "給与",
            "源泉徴収額",
            "退職日",
            "会社住所",
            "電話番号",
        ]
    )
    # 合計行の追加 "給与", "源泉徴収額"の合計を追加して他の列は空白にする。　合計行のNo.は合計にする。
    total_row = pd.DataFrame(
        [
            {
                "No.": "合計",
                "会社名": "",
                "給与": total_salary,
                "源泉徴収額": total_source_tax,
                "退職日": "",
                "会社住所": "",
                "電話番号": "",
            }
        ]
    )
    df = pd.concat([df, total_row])
    if ".csv" in dst_path.lower():
        df.to_csv(dst_path, index=False, encoding="utf-8", quoting=csv.QUOTE_ALL)
    else:
        df.to_excel(dst_path, index=False)
        edit_excel(dst_path, dst_path)

    if ".csv" in dst_path:
        dst_path = dst_path.replace(".csv", ".xlsx")
        df.to_excel(dst_path, index=False)
        edit_excel(dst_path, dst_path)


if __name__ == "__main__":
    src_path = r"c:\timee.pdf"      # フルパスで入力するpdfファイルを記述してください
    dst_path = r"c:\timee.xlsx"     # フルパスで出力するexcelファイルを記述してください。
    edit_data(src_path, dst_path, "タロウ", "ヤマダ")
    print(f"データを{dst_path}に保存しました")
