import json
import requests
import time


def req_type():
    while True:
        my_request_type=input("What is you request?(buy/sell)").strip().lower()
        if my_request_type in ["buy","sell"]:
            return my_request_type
        else:
            pass
def req_symbol():
    while True:
        my_request_symbol=input("What symbol?(BTC,ETH)").strip().lower()
        if my_request_symbol in ["btc","eth"]:
            return my_request_symbol
        else:
            pass



class History:
    def __init__(self) -> None:
        self.window=[]
    def add_number(self,n):
        self.window.append(n)
        if len(self.window)>5:
            self.window=self.window[-5:]
    def get_statistics(self):
        mean=sum(self.window)/len(self.window)
        minimum=min(self.window)
        maximum=max(self.window)
        return mean,minimum,maximum
    def ready(self):
        return len(self.window)==5

def main():
    interval = 2
    my_request_type= req_type()
    my_request_symbol=req_symbol()
    history=History()
    while True:
        history.add_number(get_symbol_rate(my_request_type,my_request_symbol))
        if history.ready():
            mean,minimum,maximum=history.get_statistics()
            print(f"Minimum {my_request_symbol.upper()} price in past 10 seconds:",minimum)
            print(f"Maximum {my_request_symbol.upper()} price in past 10 seconds:",maximum)
            print(f"Mean {my_request_symbol.upper()} price in past 10 seconds:",mean)
        time.sleep(interval)



def extract_symbol_rate(symbol_jason,my_request_type):
    if my_request_type=="sell":
        usd_rate = float(symbol_jason['bids'][0][0])
    elif my_request_type=="buy":
        usd_rate = float(symbol_jason['asks'][0][0])
    return usd_rate

def get_symbol_rate(my_request_type,my_request_symbol):
    symbol_jason= (requests.get(f"https://api.binance.com/api/v3/depth?symbol={my_request_symbol.upper()}USDT")).json()
    return extract_symbol_rate(symbol_jason,my_request_type)

if __name__=="__main__":
    main()