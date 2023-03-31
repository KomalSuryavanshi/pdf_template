from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics2.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="BI", size=15)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

pdf.output("output.pdf")
