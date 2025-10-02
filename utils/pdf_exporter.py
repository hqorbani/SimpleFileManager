from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
import arabic_reshaper
from bidi.algorithm import get_display
import re
import os

# ثبت فونت‌ها
pdfmetrics.registerFont(TTFont("BNazanin", "fonts/BNazanin.ttf"))
pdfmetrics.registerFont(TTFont("Courgette-Regular", "fonts/Courgette-Regular.ttf"))  # اگر فایل TTF نداری، از فونت پیش‌فرض استفاده کن

def is_farsi(text):
    return bool(re.search(r'[\u0600-\u06FF]', text))

def prepare_text(text):
    if is_farsi(text):
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    return text

def export_file_list_to_pdf(file_list, output_path="file_report.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # عنوان
    c.setFont("BNazanin", 14)
    title = prepare_text("📄 گزارش فایل‌های بارگذاری‌شده")
    c.drawRightString(width - 50, height - 50, title)

    # تاریخ
    timestamp = prepare_text("تاریخ تولید: ") + datetime.now().strftime("%Y/%m/%d")
    c.setFont("BNazanin", 10)
    c.drawRightString(width - 50, height - 70, timestamp)

    # لیست فایل‌ها
    y = height - 100
    for file in file_list:
        file_id, filename, filepath = file
        line = f"{file_id}. {filename} — {filepath}"

        if is_farsi(line):
            c.setFont("BNazanin", 11)
            c.drawRightString(width - 50, y, prepare_text(line))
        else:
            c.setFont("Courgette-Regular", 11)
            c.drawString(50, y, line)

        y -= 25
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
