import io
import json
import pathlib
import sys

import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
    raise SystemExit("Usage: python generate_url_qr.py https://your-approved-site.example/")

base = sys.argv[1].split("#", 1)[0].rstrip("/")
if base.endswith("/index.html"):
    base = base[:-11]
meds = json.loads(pathlib.Path(__file__).with_name("medication_index.json").read_text())
out = pathlib.Path(__file__).with_name("MedSafe360_URL_QR_Labels.pdf")
canvas_pdf = canvas.Canvas(str(out), pagesize=A4)
page_width, page_height = A4

for i, med in enumerate(meds):
    if i and i % 12 == 0:
        canvas_pdf.showPage()
    slot = i % 12
    col, row = slot % 3, slot // 3
    x = 12 * mm + col * 66 * mm
    y = page_height - (13 + row * 70) * mm
    canvas_pdf.roundRect(x, y - 64 * mm, 61 * mm, 61 * mm, 4 * mm)
    url = f"{base}/#{med['id']}"
    image = qrcode.make(url).convert("RGB")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    canvas_pdf.drawImage(ImageReader(buffer), x + 10 * mm, y - 44 * mm, 40 * mm, 40 * mm)
    canvas_pdf.setFont("Helvetica-Bold", 8)
    name = med["name"][:27] + "..." if len(med["name"]) > 30 else med["name"]
    canvas_pdf.drawCentredString(x + 30.5 * mm, y - 50 * mm, name)
    canvas_pdf.setFont("Helvetica", 8)
    canvas_pdf.drawCentredString(x + 30.5 * mm, y - 56 * mm, med["id"])

canvas_pdf.save()
print("Created:", out)
