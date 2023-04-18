#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime,os,glob,re, pytz,patoolib,sys
import pandas as pd
dt = datetime.datetime.now()
# Get current date and time
startTime = dt.now(pytz.timezone('Asia/Dubai'))
startTime =  str(startTime.strftime("%Y-%m-%d %H:%M:%S"))
# file_timeStamp = str(startTime.strftime("%Y%m%d _%H:%M:%S"))

# email data 
email = ${email}
str = email["body"]
src_email = email["mimeFile"]
subject = email["subject"]

# attachments in the emails 
attach_list = email["files"]
compres_list = []
output_list = []

def uncompress_folder(src, dst):
    try:
        patoolib.extract_archive(src, outdir=dst)
        os.remove(src)

    except Exception as e:
        print("Unable to process " + src + " retrying")
        print(sys.exc_info()[1])
        pass

    for root, dirs, files in os.walk(dst):
        # pdb.set_trace()
        for filename in files:
            if re.search(r'\.zip$', filename) or re.search(r'\.bz2$', filename) or \
                    re.search(r'\.z$', filename) or re.search(r'\.rar$', filename):
                fileSpec = os.path.join(root, filename)
                uncompress_folder(fileSpec, root)
            else:
                fileSpec = os.path.join(root, filename)
                print(" No need to extract again", fileSpec)

# uncompress_folder(rar_path, rar_path)

ext =[".zip", ".rar", ".xlsx", ".pdf"]
compres_list = [string for string in attach_list if string.endswith(tuple(ext))]
po_list = []

if compres_list:
    data_falg=1
    for i in compres_list:
        src_path,folder_name = os.path.split(i)
        uncompress_folder(src_path, src_path)
        
        file_name = folder_name.replace('HWITS', '').replace('HW', '').replace('.rar', '').strip()
        po_num = file_name[:6]
         
        po_list.append(po_num)
        
        
        try:
            src_path = r'{}'.format(src_path)
            print('src path :', src_path)
            input_list =[]
          
            # print('main input list :',input_list)
            
            for root, dirs, files in os.walk(src_path):
                 for name in files:
                    input_list.append(os.path.join(root,name))
                
            input_list = [k for k in input_list if k.endswith('.xlsx') ]
            input_list = [x for x in input_list if ('naar' in x or 'NAAR' in x or 'Naar' in x)  ]
            print('input list = ',input_list)
            # print('src path => ',src_path)
            if input_list:
                for item in input_list:
                    df = pd.read_excel(item, sheet_name=0)
                    cols = df.columns.tolist()
        
        
                    if len(cols) == 29:
                        format = 1
                        print("File format : ", format)
                        df2 = pd.read_excel(item, skiprows=12)
                        df2.columns = df2.iloc[0]
                        df2.drop(index=df2.index[0], axis=0, inplace=True)
                        df2 = df2[['Pat Request Date', 'Po Number', 'Item Code','Item Description', 'Quantity', 'Unit Price','Amount']]
                        rename_cols = {
                            'Po Number': 'PO No', 'Pat Request Date': 'Pat Date', 'Item Code': 'Cpart No',
                            'Item Description': 'Cpart Description',
                            'Quantity': 'Quantity', 'Unit Price': 'Unit Price', 'Amount': 'Total Delivery Amount'
                        }
        
                        # sum the cul code with Qty and remove duplicates one line
                        pdb.set_trace()
                        df2 = df2[df2['Po Number'] == po_num]
                       # df2 = df2.groupby(['Pat Request Date', 'Po Number', 'Item Code','Item Description', 'Quantity', 'Unit Price','Amount'], as_index=False).agg({'Quantity': 'sum'})
                        output_file = folder_name.replace('.rar', '')
                        
                        dt = datetime.datetime.now()
                        # Get current date and time
                        st = dt.now(pytz.timezone('Asia/Dubai'))
                        
                        file_timeStamp = str(st.strftime("%Y%m%d _%H:%M:%S"))
                        
                        output_path = os.path.join(currentFolder +'\\' + output_file + file_timeStamp  + '.xlsx')
                        
                        df2.to_excel(output_path, index=False)
                        output_list.append(output_path)
        
                    elif len(cols) == 19: # multiple tables into one table
                        format = 2
                        print("File format : ", format)
                        df3 = pd.read_excel(item)
                        df3.dropna(inplace=True)
                        df3 = df3.drop_duplicates()
                        df3 = df3[df3['SNo.'] != 'SNo.']
                        old_headers_list = df3.columns.tolist()
                        new_cols = df3.columns.tolist()
                        new_cols = [c.replace("\n", " ") for c in new_cols]
                        new_header = {old_headers_list[i]: new_cols[i] for i in range(len(old_headers_list))}
                        df3.rename(new_header, axis="columns", inplace=True)
        
                        df3 = df3[['PO Number','PAT Date','CUL Code','CUL Description','AsBuilt Qty', 'Unit Price','Net  AsBuilt']]
                        rename_cols={
                        'PO Number': 'PO No' , 'PAT Date': 'Pat Date', 'CUL Code': 'Cpart No', 'CUL Description': 'Cpart Description' ,
                        'AsBuilt Qty': 'Quantity', 'Unit Price': 'Unit Price', 'Net  AsBuilt': 'Total Delivery Amount'
                        }
                        df3.rename(columns=rename_cols)
        
                        df3 = df3.groupby(
                            ['PO Number','PAT Date','CUL Code','CUL Description','AsBuilt Qty', 'Unit Price','Net  AsBuilt'], as_index=False).agg({'AsBuilt Qty': 'sum'})
                       
                       
                        dt = datetime.datetime.now()
                        # Get current date and time
                        st = dt.now(pytz.timezone('Asia/Dubai'))
                        file_timeStamp = str(st.strftime("%Y%m%d _%H:%M:%S"))
                        
                        output_path = os.path.join(currentFolder +'\\' + output_file + file_timeStamp  + '.xlsx')
                        df3.to_excel(output_path, index=False)
                        output_list.append(output_path)
        
        except Exception as e:
            print(e)

         
         
else:
    data_flag= 0

# glob.glob(path + "\*.xlsx")

