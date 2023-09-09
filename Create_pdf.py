from fpdf import FPDF

pdf = FPDF(orientation='P',unit='pt',format='A4')

pdf.add_page()

#pdf.image('Sample.png',w=65,h=60)

pdf.set_font(family="Times",style='B',size=24)

pdf.cell(w=0, h=50, txt="Address",align='C',ln=1)

#pdf.set_font(family="Times",size=12)
pdf.multi_cell(w=0, h=15, txt="No change")

pdf.output('Address.pdf')
