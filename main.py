from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)    #Pages shouldnt break the size

df = pd.read_csv("topics2.csv")

for index, row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", style="BI", size=15)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)

        # To Add Footer #
        pdf.ln(260)
        pdf.line(x1=10, y1=282, x2=200, y2=282)
        pdf.set_font(family="Times", style="BI", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)




pdf.output("output.pdf")
