import pdb
from PyPDF2 import PdfReader
import pandas as pd
import os

currentFolder = r"C:\Users\mwx1229339\PycharmProjects\pythonProject"
file_path = r"E:\python_codes\pdf_data_excel\RELEASE_101_79297_487_0_US.pdf"

try:
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    txt = text.split("Order")
    order = txt[1].split("\n")[0].strip()

    release_date = txt[2].split("\n")[0].replace("Date", "").strip()

    '''
    In this data extraction by using the the indexes ranges 
    supplier - shipto 
    shipto - billto
    billto - customer account no 
    
    '''
    supplier_data = text[text.index("Supplier") + 8:text.index("Ship To")].replace("\n", "").strip(':').strip()
    ship_To_data = text[text.index("Ship To:") + 7:text.index("Bill To")].replace("\n", "").strip(':').strip()
    bill_To_data = text[text.index("Bill To") + 7:text.index("Customer Account No")].replace("\n", "").strip(
        ':').strip()

    df_data = []

    data = [order, release_date, supplier_data, ship_To_data, bill_To_data]
    # list within a list to use in the pandas
    df_data.append(data)
    pdb.set_trace()

    txt = text.split("Supplier")

    # execution reaches this point in the program, the program stops and you're dropped into the pdb debugger
    # pdb.set_trace()

    df = pd.DataFrame(df_data, columns=['order', 'release_date', 'supplier_data', 'ship_To_data', 'bill_To_data'])

    # excel
    writer = pd.ExcelWriter('output.xlsx')

    # write dataframe to excel
    df.to_excel(writer)

    # save the excel
    print('DataFrame is written successfully to Excel File.')




except Exception as e:
    print(e)




