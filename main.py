import json
from datetime import datetime
from http.client import responses



print("Lesson 9")

import urllib.request
import json
from dataclasses import dataclass
from typing import List

@dataclass
class Rate:
    baseCurrency:str
    currency:str
    saleRateNB:float
    purchaseRateNB:float
    saleRate:float
    purchaseRate:float

@dataclass
class ArchiveRecord:
    date:str
    bank:str
    baseCurrency:int
    baseCurrencyLit:str
    exchangeRate:List[Rate]

    def Show(self):
        print("Date:",self.date)
        for item in self.exchangeRate:
            print("\t\tCurrency:",item.baseCurrency,"to Currency:",item.currency,"=> Sale rate:",item.saleRateNB,"Purchase rate:",item.purchaseRateNB)


cringe = urllib.request.build_opener()
responses= cringe.open("https://api.privatbank.ua/p24api/exchange_rates?date=01.12.2014")

json_data = responses.read().decode("utf-8")
data_dict = json.loads(json_data)

record = ArchiveRecord(
    date=data_dict["date"],
    bank=data_dict["bank"],
    baseCurrency=data_dict["baseCurrency"],
    baseCurrencyLit=data_dict["baseCurrencyLit"],
    exchangeRate=[
        Rate(
            baseCurrency=rate.get("baseCurrency", ""),
            currency=rate["currency"],
            saleRateNB=rate.get("saleRateNB", 0.0),
            purchaseRateNB=rate.get("purchaseRateNB", 0.0),
            saleRate=rate.get("saleRate", 0.0),
            purchaseRate=rate.get("purchaseRate", 0.0)
        )
        for rate in data_dict["exchangeRate"]
    ]
)

print(json_data)
print()

print(record)
print()

record.Show()