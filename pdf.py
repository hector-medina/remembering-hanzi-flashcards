from fpdf import FPDF
from Char import Char

pdf = FPDF()
pdf.add_page()
pdf.add_font('fireflysung', '','fireflysung.ttf', uni=True)
pdf.set_font('fireflysung', '', 48)

pdf.set_fill_color(255)


data = [
    Char('一', 'yi4', 'UNO', '1- 1234567890-1234567890'),
    Char('二', 'er4', 'DOS', '2- 1234567890-1234567890\n1234567890-1234567890'),
    Char('三', 'san1', 'TRES', '3- Una raya horizontal'),
    Char('四', 'si4', 'CUATRO', '4- Una raya horizontal'),
    Char('五', 'wu3', 'CINCO', '5- Una raya horizontal'),
    Char('六', 'liu4', 'SEIS', '6-Una raya horizontal'),
    Char('七', 'qi1', 'SIETE', '7- Una raya horizontal'),
    Char('八', 'ba1', 'OCHO', '8- Una raya horizontal ahsadh dhhdye djdkh '),
    Char('九', 'jiu2', 'NUEVE', '9- Una raya horizontal'),
    Char('十', 'shi2', 'DIEZ', '10- Una raya horizontal'),
    Char('口', 'kou3', 'BOCA', '11- Una raya horizontal'),
    Char('日', 'ri4', 'DÍA', '12- Una raya horizontal'),
    Char('月', 'yue4', 'MES', '13- Una raya horizontal'),
    Char('田', 'tian2', 'CAMPO DE ARROZ', '14- Una raya horizontal'),
    Char('目', 'mu4', 'OJO', '15- Una raya horizontal'),
    Char('古', 'gu3', 'ANTIGUO', '16- Una raya horizontal'),
]
#
# pdf.cell(48, 50, data2[0].char, "L:1 T:1 R:1", 0, 'C')
# pdf.cell(48,50, "",  ln=True)
# pdf.cell(48, 12, str(0+1), "L:1 B:1 R:1", 0, 'R')
# # pdf.cell(48,12, "",  ln=True)
# pdf.ln(12)
#
# pdf.add_page()
#
# pdf.cell(48, 50, data2[0].meaning, "L:1 T:1 R:1", 0, 'C')
# pdf.cell(48,50, "",  ln=True)
# pdf.cell(48, 12, data2[0].sound, "L:1 B:1 R:1", 0, 'R')
# pdf.cell(48,12, "",  ln=True)
# pdf.cell(48, 12, data2[0].explain, "L:1 B:1 R:1", 0, 'R')
# pdf.cell(48,12, "",  ln=True)

#
# data = [ "一", "二", "三", "四",
#          "五", "六", "七", "八",
#          "九", "十", "口", "日",
#          "月", "田", "目", "古"]

x = 0
y = 0

#
# for i in range(4):
#     pdf.cell(48, 50, data[i], "L:1 T:1 R:1", 0, 'C')
#
# # pdf.cell(48,50, "",  ln=True)
#
# pdf.set_font('fireflysung', '', 15)
# for i in range(4):
#     pdf.cell(48, 12, str(i+1), "L:1 B:1 R:1", 0, 'R')

for f in range(4):
    pdf.set_font('fireflysung', '', 48)
    for i in range(4):
        pdf.cell(48, 50, data[i+f*4].char, "L:1 T:1 R:1", 0, 'C')
    pdf.cell(48,50, "",  ln=True)
    pdf.set_font('fireflysung', '', 15)
    for i in range(4):
        pdf.cell(48, 12, str(f*4+i+1), "L:1 B:1 R:1", 0, 'R')
    pdf.cell(48,12, "",  ln=True)

pdf.add_page()

pdf.set_font('times', '', 10)
for f in range(4):
    for i in range(4):
        pdf.set_y(11+62*f)
        pdf.set_x(8+48*i)
        pdf.multi_cell(48, 12, data[3-i+f*4].meaning, "L:1 T:1 R:1 B:1", 0, "L")
    for i in range(4):
        pdf.set_y(23+62*f)
        pdf.set_x(8+48*i)
        pdf.multi_cell(48, 38, "", "L:1 T:1 R:1 B:1", 0, "L")
    for i in range(4):
        pdf.set_y(23+62*f)
        pdf.set_x(8+48*i)
        pdf.multi_cell(48, 5, data[3-i+f*4].explain, "L:1 T:1 R:1", 0, "L")
    for i in range(4):
        pdf.set_y(61+62*f)
        pdf.set_x(8+48*i)
        pdf.multi_cell(48, 12, data[3-i+f*4].sound, "L:1 T:1 R:1 B:1", 0, "L")

#
# for f in range(4):
#     pdf.set_font('times', '', 12)
#     for i in range(4):
#         if f == 0:
#             pdf.set_y(12)
#         else :
#             pdf.set_y(12+50*f)
#         pdf.multi_cell(48, 12, data[3-i+f*4].meaning, "L:1 T:1 R:1 B:1", 0, 'L')
#     pdf.cell(48,12, "",  ln=True)
#     for i in range(4):
#         pdf.multi_cell(48, 38,'', "L:1 T:1 R:1 B:1", 0, 'R')
#     pdf.cell(48,38, "",  ln=True)
#     for i in range(4):
#         pdf.cell(48, 12, data[3-i+f*4].sound, "L:1 B:1 R:1 T:1", 0, 'L')
#     pdf.cell(48,12, "",  ln=True)
#     # for i in range(4):
#     #     # pdf.cell(48, 38, data[3-i+f*4].getExplainLimitLine(), "L:1 T:1 R:1 B:1", 0, 'R')
#     #     if f == 0:
#     #         pdf.set_xy(10+48*1, 22)
#     #     else :
#     #         pdf.set_xy(11+60*i , f*65+24)
#     #     pdf.multi_cell(48, 5, data[3-i+f*4].explain, "", 0, 'R')
#     # pdf.cell(48,0, "",  ln=True)




pdf.output("Hanzi para recordar - flashcards.pdf")
