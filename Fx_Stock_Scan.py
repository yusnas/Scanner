import matplotlib.pyplot as plt
import numpy as np
#from sklearn import datasets, linear_model
import pandas as pd
#from pandas_datareader import data as web
import datetime as dt
import csv
 
# Load CSV and columns
#df = pd.read_csv("C:/files/EURCADla.csv")
#df = pd.read_csv("C:/files/USDCAD1D.csv")
#df = pd.read_csv("C:/files/GBPCHFD1.csv")

#pdfile = pd.read_csv('C:/files/sp5002012.txt')              
#print pdfile.loc[1]




def Scanner(symbol,startdate,enddate):
 #dfweb = pd.read_csv("C:/files/yahoo/"+symbol+".csv")
 
 #STOCK DATA
 #dfweb = web.get_data_yahoo(symbol+'=X',start='2017.3.01',end='2017.6.16')
 dfweb = web.get_data_yahoo(symbol+'=X',startdate,enddate)
 
 #CURRENCY DATA
 #dfweb = web.DataReader('EURUSD=X','yahoo')['Close']
 #dfdata = web.get_data_fred('DEXJPUS')
 
 #dfdata= dfweb[['Close']]
 
 #dfdata = dfweb[['Open','High','Low','Close']]
 dfdata= dfweb[['Close']]
 slippage = 0



 X = dfdata['Close']
 Ylength = len(X)
 Y = X[len(X)-2:]
 Y24 = X[len(X)-4:]
 Y28 = X[len(X)-8:]
 Y4 = X[len(X)-16:]
 Y8 = X[len(X)-32:]
 #Y16 =X[117:]
 Y16 = X[len(X)-64:]
 #Y = X[212:]
 Y32 = X[len(X)-128:]
 Y128 = X[len(X)-256:]

 Block = (Y.max() - Y.min()) / 12
 Block24 = (Y24.max() - Y24.min()) / 12
 Block28 = (Y28.max() - Y28.min()) / 12
 Block4 = (Y4.max() - Y4.min()) / 12
 Block8 = (Y8.max() - Y8.min()) / 12
 Block16 = (Y16.max() - Y16.min()) / 12
 Block32 = (Y32.max() - Y32.min()) / 12
 #Block64 = (Y64.max() - Y64.min()) / 8
 Block128 = (Y128.max() - Y128.min()) / 12

 B = Block * 10000
 B24 = Block24 *10000
 B28 = Block28 * 10000
 B4 = Block4 * 10000
 B8 = Block8 * 10000
 B16 = Block16 * 10000
 B32 = Block32 * 10000
 B128 = Block128 * 10000




 Yi = Y.min() + (0.00 + Block) * 6 
 Y24i = Y24.min() + (0.00 + Block24) *6 
 Y28i =  Y28.min() + (0.00 + Block28) *6
 Y4i =  Y4.min() + (0.00 + Block4) *6 
 Y8i = Y8.min() + (0.00 + Block8) *6 
 Y16i = Y16.min() + (0.00 + Block16) *6
 Y128i =  Y128.min() + (0.00 + Block128) *6 

 Yh = Y.min() + (0.00 + Block) *10 
 Y24h = Y24.min() + (0.00 + Block24) *10 
 Y28h =  Y28.min() + (0.00 + Block28) *10 
 Y4h =  Y4.min() + (0.00 + Block4) * 10 
 Y8h = Y8.min() + (0.00 + Block8) *10 
 Y16h = Y16.min() + (0.00 + Block16) *10 
 Y128h =  Y128.min() + (0.00 + Block128) *10 

 Yl = Y.min() + (0.00 + Block) *2 
 Y24l = Y24.min() + (0.00 + Block24) *2 
 Y28l =  Y28.min() + (0.00 + Block28) *2 
 Y4l =  Y4.min() + (0.00 + Block4) * 2 
 Y8l = Y8.min() + (0.00 + Block8) *2 
 Y16l = Y16.min() + (0.00 + Block16) *2 
 Y128l =  Y128.min() + (0.00 + Block128) *2 


 if(( B  <= 7 ) and (B  > 0)): B = 7
 if(( B  <= 15 ) and (B  >7)): B = 15
 if(( B  <= 30 ) and (B  >15)): B = 30
 if(( B <= 60) and (B >30)): B = 60
 if(( B <= 120) and (B >60)): B = 120

 if(( B24  <= 7 ) and (B24  > 0)): B24 = 7
 if(( B24  <= 15 ) and (B24  >7)): B24 = 15
 if(( B24  <= 30 ) and (B24  >15)): B24 = 30
 if(( B24 <= 60) and (B24 >30)): B24 = 60
 if(( B24 <= 120) and (B24 >60)): B24 = 120

 if(( B28  <= 7 ) and (B28  > 0)): B28 = 7
 if(( B28  <= 15 ) and (B28  >7)): B28 = 15
 if(( B28  <= 31 ) and (B28  >15)): B28 = 30
 if(( B28 <= 60) and (B28 >31)): B28 = 60
 if(( B28 <= 120) and (B28 >60)): B28 = 120

 if(( B4  <= 7 ) and (B4  > 0)): B4 = 7
 if(( B4  <= 15 ) and (B4  >7)): B4 = 15
 if(( B4  <= 31 ) and (B4  >15)): B4 = 30
 if(( B4 <= 60) and (B4 >31)): B4 = 60
 if(( B4 <= 120) and (B4>60)): B4 = 120

 if(( B8  <= 7 ) and (B8  > 0)): B8 = 7
 if(( B8  <= 15 ) and (B8  >7)): B8 = 15
 if(( B8  <= 31 ) and (B8  >15)): B8 = 30
 if(( B8 <= 60) and (B8 >31)): B8 = 60
 if(( B8 <= 120) and (B8 >60)): B8 = 120

 if(( B16  <= 7 ) and (B16  > 0)): B16 = 7
 if(( B16 <= 15 ) and (B16  >7)): B16 = 15
 if(( B16  <= 31 ) and (B16  >15)): B16 = 30
 if(( B16 <= 60) and (B16 >31)): B16 = 60
 if(( B16 <= 120) and (B16 >60)): B16 = 120





 Top = (Y.max()+ Y24.max() + Y28.max())/3
 Bottom = (Y.min()+ Y24.min() + Y28.min())/3
 #print"----------------------------------------------"

 Top2 = (Yh +Y24h + Y28h) / 3
 Bottom2 = (Yl + Y24l + Y28l) /3
 
 #Tp = (Top + Top2)/2
 #Bm = (Bottom +Bottom2)/2
 
 Tp = Top2
 Bm = Bottom2
 
 #Tp = (Y4l +Y8h)/2
 #Bm = (Y4l +Y8l)/2
 
 
 #Tp = (Y8h +Y16h)/2
 #Bm = (Y8l +Y16l)/2
 
 #Tp = (Top2 + Y4l +Y8h + +Y16h)/4
 #Bm = (Bottom2 + Y4l +Y8l + Y16l)/4
 
 price_checkup = Y[len(Y)-1:].max()
 price_checkdown = Y[len(Y)-1:].min()
 
 if (price_checkup + (slippage/100) > Tp):
  # print"What should I do : Sell",symbol," @", round(Tp,5)
  ActionSignal = "Sell"
  #if (Y[len(Y)-1:].max() < Tp and Y[len(Y)-1:].min() > Bm):
 if (price_checkup < Tp and price_checkdown > Bm):
   #print"What should I do : Do Nothing...WAIT!",symbol
   ActionSignal = "Wait"
  #if (Y[len(Y)-1:].min() + (slippage/100) < Bm):
 if (price_checkdown + (slippage/100) < Bm):
    #print"What should I do : Buy",symbol," @", round(Bm,5), 
    ActionSignal = "Buy"
 return price_checkup,price_checkdown,Tp,Bm,symbol,ActionSignal

def test_run():
 startdate = '2017.2.14'
 enddate = '2017.6.3'
 
 i=0
 pdfile = pd.read_csv('C:/files/sp5002017c2.txt') 
 #symbol = pdfile['A'].loc[i]
 flnam9e = open('ernie.csv', 'wb') 
 trade = csv.writer(flname, delimiter=',',quoting=csv.QUOTE_MINIMAL) 
 trade.writerow(['Symbol','Sell Price','Buy Price','What Should I do'])
  
 
 print("Symbol","     ","Top","           ","Bottom","     ","What Should I do")
 while i < 13:
     #for i < 100:
     symbol = pdfile['A'].loc[i]
     price_checkup,price_checkdown,Tp,Bm,symbol,ActionSignal= Scanner(symbol,startdate,enddate)
     trade.writerow([symbol,round(Tp,4),round(Bm,4),ActionSignal])
     i=i+1
     #print"Symbol","             ","Top","                    ","Bottom"
     print (symbol,"         ",round(Tp,4),"          ",round(Bm,4),"      ",ActionSignal)
     #print Tp, Bm
     
     #Open the file

 trade.writerow(['Start-date',startdate,'End-date',enddate])  
 flname.close 
 print ("from :", startdate, " to this date:", enddate)
       
 #price_checkup,price_checkdown,Tp,Bm,symbol,slippage = Scanner(symbol)
 #print"****************************"
 
 #symbol = "GBPCHF=X"
 #price_checkup,price_checkdown,Tp,Bm,symbol,ActionSignal= Scanner(symbol)
 #print symbol,"         ",round(Tp,4),"          ",round(Bm,4),"      ",ActionSignal 
 
 
 #if (Y[len(Y)-1:].max() + (slippage/100) > Tp):
 """if (price_checkup + (slippage/100) > Tp):
  print"What should I do : Sell",symbol," @", round(Tp,5)

 #if (Y[len(Y)-1:].max() < Tp and Y[len(Y)-1:].min() > Bm):
 if (price_checkup < Tp and price_checkdown > Bm):
  print"What should I do : Do Nothing...WAIT!",symbol

 #if (Y[len(Y)-1:].min() + (slippage/100) < Bm):
 if (price_checkdown + (slippage/100) < Bm):
   print"What should I do : Buy",symbol," @", round(Bm,5),"""
 
if __name__=="__main__":
     test_run()
     #simulate()
 
 
