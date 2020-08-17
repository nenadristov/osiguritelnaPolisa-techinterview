import xlsxwriter
import os

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Demo-Excel.xlsx')
worksheet = workbook.add_worksheet("Demo Excel Tabela")
worksheet.set_column("A:E", 15)
#naslov vo tabelata
style_naslov=workbook.add_format({'bold': True, "align" : "center",'border': 1})
worksheet.write("A1", "Филијала", style_naslov)
worksheet.write("B1", "Број на полиси", style_naslov)
worksheet.write("C1", "Број на агенти", style_naslov)
worksheet.write("D1", "Вкупна премија", style_naslov)

style_podatoci=workbook.add_format({"align" : "center", 'border': 1})
#podatoci red 1
red=2
while True:
    
    #vnesuvanje podatoci
    mesto_filijala=input("Внесете место на филијалата\n")
    br_polisi=int(input("Внесете број на полиси\n"))
    br_agenti=int(input("Внесете број на агенти\n"))
    vk_premija=float(input("Внесете вкупна премија\n"))

    #vneseuvanje na podatocite vo excel
    worksheet.write("A{}".format(red), mesto_filijala, style_podatoci)
    worksheet.write("B{}".format(red), br_polisi, style_podatoci)
    worksheet.write("C{}".format(red), br_agenti, style_podatoci)
    worksheet.write("D{}".format(red), vk_premija, style_podatoci)
    
    #if-else dali da prodolzi programata
    nov_red=input("Дали ќе внесувате нов ред податоци Да/Не\n")
    if nov_red.lower()=="не":
        break 
    else : pass




workbook.close()
os.startfile("Demo-Excel.xlsx")
