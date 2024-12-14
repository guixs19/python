import requests
import time
while True:
    response=requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")   
    cotação=response.json()
    dolar_cotação=cotação["USDBRL"]["bid"]
    print(f"cotação do dolar:{dolar_cotação}")
    euro_cotação=cotação["EURBRL"]["bid"]
    print(f"cotação do euro:{euro_cotação}")
    bitcoin_cotação=cotação['BTCBRL']["bid"]
    print(f"cotação do bitcoin:{bitcoin_cotação}")
    print("/////////////////////////////////////////")
    time.sleep(3)
    


