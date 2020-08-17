import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Demo-Excel.xlsx')
worksheet = workbook.add_worksheet("Demo Excel Tabela")
worksheet.set_column("A:E", 15)
#naslov vo tabelata
style_naslov=workbook.add_format({'bold': True, "align" : "center", 'border': 1})
worksheet.write("A1", "Филијала", style_naslov)
worksheet.write("B1", "Број на полиси", style_naslov)
worksheet.write("C1", "Број на агенти", style_naslov)
worksheet.write("D1", "Вкупна премија", style_naslov)

style_podatoci=workbook.add_format({"align" : "center", 'border': 1})
#podatoci red 1
worksheet.write("A2", "Скопје", style_podatoci)
worksheet.write("A3", "Тетово", style_podatoci)
worksheet.write("A4", "Охрид", style_podatoci)
worksheet.write("A5", "Велес", style_podatoci)
worksheet.write("A5", "Кочани", style_podatoci)
worksheet.write("A6", "Струмица", style_podatoci)

#podatoci red 2
worksheet.write("B2", "10.000", style_podatoci)
worksheet.write("B3", "8.000", style_podatoci)
worksheet.write("B4", "5.000", style_podatoci)
worksheet.write("B5", "6.000", style_podatoci)
worksheet.write("B5", "3.000", style_podatoci)
worksheet.write("B6", "9.000", style_podatoci)

#podatoci red 2
worksheet.write("C2", "10.000", style_podatoci)
worksheet.write("C3", "8.000", style_podatoci)
worksheet.write("C4", "5.000", style_podatoci)
worksheet.write("C5", "6.000", style_podatoci)
worksheet.write("C5", "3.000", style_podatoci)
worksheet.write("C6", "9.000", style_podatoci)

#podatoci red 4
worksheet.write("D2", "1.275.143,00", style_podatoci)
worksheet.write("D3", "958.123,00", style_podatoci)
worksheet.write("D4", "689.723,00", style_podatoci)
worksheet.write("D5", "765.489,00", style_podatoci)
worksheet.write("D5", "412.322,00", style_podatoci)
worksheet.write("D6", "1.159.255,00", style_podatoci)


workbook.close()
