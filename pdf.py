from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font('fireflysung', '','fireflysung.ttf', uni=True)
pdf.set_font('fireflysung', '', 48)

pdf.set_fill_color(255)


data = [ "一", "二", "三", "四",
         "五", "六", "七", "八",
         "九", "十", "口", "日",
         "月", "田", "目", "古"]

x = 0
y = 0


# for i in range(4):
#     pdf.cell(48, 50, data[i], "L:1 T:1 R:1", 0, 'C')
#
# pdf.cell(48,50, "",  ln=True)
#
# pdf.set_font('fireflysung', '', 15)
# for i in range(4):
#     pdf.cell(48, 12, str(i+1), "L:1 B:1 R:1", 0, 'R')

for f in range(4):
    pdf.set_font('fireflysung', '', 48)
    for i in range(4):
        pdf.cell(48, 50, data[i+f*4], "L:1 T:1 R:1", 0, 'C')
    pdf.cell(48,50, "",  ln=True)
    pdf.set_font('fireflysung', '', 15)
    for i in range(4):
        pdf.cell(48, 12, str(f*4+i+1), "L:1 B:1 R:1", 0, 'R')
    pdf.cell(48,12, "",  ln=True)

pdf.output("Hanzi para recordar - flashcards.pdf")
