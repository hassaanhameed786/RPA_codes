import glob
import pdb
import pandas, os
import pandas as pd

curr_path = r"E:\Kuwait STC\Data"
save_path = r'E:\Kuwait STC\Data\output'

filenames = glob.glob(curr_path + "\*.xlsx")
input_list = []

try:
    input_list = [os.path.join(curr_path, f) for f in os.listdir(curr_path) if f.endswith('.xlsx')]

    if input_list:
        for item in input_list:
            df = pd.read_excel(item, sheet_name=0)
            cols = df.columns.tolist()
            # roma attachmentss

            if len(cols) == 29:
                format = 1
                print("File format : ", format)
            #
            # This code use if format == 1
                df2 = pd.read_excel(item, skiprows=12)
                df2.columns = df2.iloc[0]
                print('dataframe col_ name : ', df2.columns)
                # Drop first row using drop()
                df2.drop(index=df2.index[0], axis=0, inplace=True)

                df2.to_excel(save_path + '\PAT DETAILS1.1.3_.xlsx', index=False)


            elif len(cols) == 19:
                format = 2
                print("File format : ", format)

                # This code use if format == 2

                df3 = pd.read_excel(item)
                # remove the empty rows
                df3.dropna(inplace=True)
                # remove the duplicate data
                df3 = df3.drop_duplicates()
                df3 = df3[df3['SNo.'] != 'SNo.']
                # not useful data in the excel same as duplicate
                # df = df.drop(index=df.index[], axis=0, inplace=True)
                # replace the \n with the space
                old_headers_list = df3.columns.tolist()
                new_cols = df3.columns.tolist()
                new_cols = [c.replace("\n", " ") for c in new_cols]
                new_header = {old_headers_list[i]: new_cols[i] for i in range(len(old_headers_list))}
                df3.rename(new_header, axis="columns", inplace=True)
                # writer
                df3.to_excel(save_path + '\P1-6NEW1.2.1.xlsx', index=False)


            elif cols[0] == 'SNo.':
                format = 3
                print("File format : ", format)
            else:
                print('Complete the data extraction')




except Exception as e:
    print(e)
