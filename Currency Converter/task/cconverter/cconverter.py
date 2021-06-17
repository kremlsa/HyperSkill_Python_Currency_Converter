import requests
import json

cache = {"usd": json.loads(requests.get("http://www.floatrates.com/daily/usd.json").content),
         "eur": json.loads(requests.get("http://www.floatrates.com/daily/eur.json").content)}

currency_code = input().lower()
while True:
    new_code = input().lower()
    if new_code == "":
        break
    else:
        amount = float(input())
        print("Checking the cache...")
    j_new_code = json.loads(requests.get("http://www.floatrates.com/daily/{}.json".format(new_code)).content)
    if new_code in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache.update({new_code: j_new_code})
    if currency_code == new_code:
        cash = amount
    else:
        cash = j_new_code[currency_code]["inverseRate"] * amount
    print("You received {} {}.".format(round(cash, 2), new_code))

