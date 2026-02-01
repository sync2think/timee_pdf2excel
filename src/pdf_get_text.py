import pdfplumber

# PDFファイルを開く


def pdf_get_text(pdf_path, dst_path: str = None):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"

    if dst_path is None:
        return all_text

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(all_text)

    return all_text


if __name__ == "__main__":
    src_path = r"c:\timee.pdf"      # フルパスで入力するpdfファイルを記述してください
    dst_path = r"c:\timee.txt"      # フルパスで出力する確認用テキストファイルを記述してください。
    pdf_get_text(pdf_path, dst_path)
    print(f"PDFファイルのテキストを{dst_path}に保存しました")
