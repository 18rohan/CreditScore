import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

#importing data from bank.xlsx
bank = pd.read_excel("bank.xlsx")
bank.keys()

#DROPPING THE USELESS COLUMNS
bank = bank.drop(['Account No','DATE','TRANSACTION DETAILS','CHQ.NO.','VALUE DATE','.'],axis = 1)

#GETTING THE NON-NULL VALUES FROM 'WITHDRAWAL AMT'
withdraw_df = pd.DataFrame(bank['WITHDRAWAL AMT'])
series = pd.notnull(withdraw_df['WITHDRAWAL AMT'])
withdrawal_data = withdraw_df[series]
withdrawal_data.reset_index(drop = True,inplace = True)

# GETTING THE NON-NULL VALUES FROM 'DEPOSIT AMT'
deposit_df = pd.DataFrame(bank['DEPOSIT AMT'])
series2 = pd.notnull(deposit_df['DEPOSIT AMT'])
deposit_data = deposit_df[series2]
deposit_data.reset_index(drop = True,inplace = True)
deposit_new = deposit_data.iloc[0:53549,:]

#SELECTING LIMITED NUMBER OF DATAPOINTS SO AS TO MATCH THE NON-NULL VALUES
bank_new = bank.iloc[0:53549,:]


#ADDING THE NEW 'WITHDRAWAL AMT' & 'DEPOSIT AMT' COLUMN
bank_new.drop(['DEPOSIT AMT','WITHDRAWAL AMT'],axis = 1,inplace = True)
bank_new2 = bank_new.copy()
bank_new2['DEPOSIT AMT'] = deposit_new
bank_new2['WITHDRAWAL AMT'] = withdrawal_data

print(deposit_new.shape)
print(withdrawal_data.shape)
#print(bank_new2.head())
print("Final Data Shape: ",bank_new2.shape)

bank_new2.to_csv("bank_new_data.csv",index = False)