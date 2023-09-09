import requests
from datetime import datetime
import time
ticker=input("Enter the ticker symbol:")
from_date = datetime.strptime(input("Enter start date in yyyy/mm/dd format:"),'%Y/%m/%d')
to_date =datetime.strptime(input("Enter end date in yyyy/mm/dd format:"),'%Y/%m/%d')
from_epoch=int(time.mktime(from_date.timetuple()))
to_epoch=int(time.mktime(to_date.timetuple()))
print(from_epoch,to_epoch)

url=f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
content = requests.get(url,headers=headers).content
print(content)

with open('data.csv','wb') as file:
    file.write(content)
