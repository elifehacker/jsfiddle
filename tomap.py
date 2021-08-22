import pandas as pd

xls = pd.ExcelFile(r"input_all.xls") #use r before absolute file path 

sheetX = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis
cols = ['street address', 'internal reference number', 'postcode','contact', 'phone']
print(sheetX.columns)
with pd.option_context('display.max_seq_items', None):
    print(sheetX['street address'].values[0])

filtered = sheetX[cols]

cols = ['full contact', 'street address']
#filtered['street address'] = filtered['internal reference number']+' '+ filtered['street address']  
filtered['full contact'] = filtered['contact'] +' '+ \
    filtered['phone'].astype(str)+' '+ \
    filtered['internal reference number'] 
print(filtered[cols].values.tolist())

