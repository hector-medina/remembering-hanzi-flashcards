from fpdf import FPDF
from Char import Char
from data import data
import math

pdf = FPDF()

LIMIT_PER_PAGE = 20;

page_pairs = int(math.ceil(len(data)/LIMIT_PER_PAGE ))
pdf.add_font('fireflysung', '','fireflysung.ttf', uni=True)


for pp in range(page_pairs):
    pdf.add_page()
    pdf.set_font('fireflysung', '', 48)
    pdf.set_fill_color(255)

    x = 0
    y = 0
    for f in range(5):
        pdf.set_font('fireflysung', '', 48)
        for i in range(4):
            pdf.cell(48, 40, data[(i+f*4)+(pp*LIMIT_PER_PAGE)].char, "L:1 T:1 R:1", 0, 'C')
        pdf.cell(48,40, "",  ln=True)
        pdf.set_font('fireflysung', '', 15)
        for i in range(4):
            pdf.cell(48, 12, data[(i+f*4)+(pp*LIMIT_PER_PAGE)].index, "L:1 B:1 R:1", 0, 'R')
        pdf.cell(48,12, "",  ln=True)

    pdf.add_page()

    pdf.set_font('times', '', 10)
    for f in range(5):
        for i in range(4):
            pdf.set_y(11+52*f)
            pdf.set_x(8+48*i)
            pdf.multi_cell(48, 12, data[(3-i+f*4)+(pp*LIMIT_PER_PAGE)].meaning, "L:1 T:1 R:1 B:1", 0, "L")
        for i in range(4):
            pdf.set_y(23+52*f)
            pdf.set_x(8+48*i)
            pdf.multi_cell(48, 38, "", "L:1 T:1 R:1 B:1", 0, "L")
        for i in range(4):
            pdf.set_y(23+52*f)
            pdf.set_x(8+48*i)
            pdf.multi_cell(48, 5, data[(3-i+f*4)+(pp*LIMIT_PER_PAGE)].explain, "L:1 T:1 R:1", 0, "L")
        for i in range(4):
            pdf.set_y(51+52*f)
            pdf.set_x(8+48*i)
            pdf.multi_cell(48, 12, data[(3-i+f*4)+(pp*LIMIT_PER_PAGE)].sound, "L:1 T:1 R:1 B:1", 0, "L")

pdf.output("Hanzi para recordar - flashcards.pdf")
