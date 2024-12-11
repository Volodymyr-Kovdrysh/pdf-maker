from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
pdf.add_font('Times New Roman', '', 'Times New Roman Regular.ttf', uni=True)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    # header
    pdf.set_font(family="Times", size=24, style='B')
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L",ln=1)
    pdf.line(10,21, 200, 21)

    # footer

    pdf.ln(265)
    pdf.set_font(family="Times", size=8, style='I')
    pdf.set_text_color(200, 200, 200)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")


    for i in range(row['Pages'] - 1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family="Times", size=8, style='I')
        pdf.set_text_color(200, 200, 200)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")





pdf.add_page()
pdf.set_font(family="Times New Roman", size=14)
pdf.set_text_color(0, 0, 255)
pdf.cell(w=0,h=14, txt="Привіт!", align="L", ln=1)


pdf.output('output.pdf')
