
import requests



def get_nbu_rate(from_currency):
    response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange")
    response_text = response.text
    usd_rate = find_usd_rate(response_text)
    return usd_rate


def find_usd_rate(response_text):
   values =  valu tes.findall("currency")
    for valute in valutes:
        if valute.find('cc').text == "USD":
            return float(valute.find("rate").text)



find_usd_rate(get_nbu_rate())