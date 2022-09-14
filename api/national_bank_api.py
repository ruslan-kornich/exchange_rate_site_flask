import xml.etree.ElementTree as ET
import requests
from models import Xrate
from api import  _Api
import datetime
from config import logging, LOGGER_CONFIG

class Api(_Api):
    def __init__(self):
        super().__init__("NationalApi")
    def _update_rate(self, xrate):
        rate = self._get_national_rate(xrate.from_currency)
        return rate


log = logging.getLogger("NationalApi")
fh = logging.FileHandler(LOGGER_CONFIG["file"])
fh.setLevel(LOGGER_CONFIG["level"])
fh.setFormatter(LOGGER_CONFIG["formatter"])
log.addHandler(fh)
log.setLevel(LOGGER_CONFIG["level"])


def update_xrates(from_currency, to_currency):
    log.info(f"Started update for {from_currency}=> {to_currency}")
    xrate = XRate.select().where(XRate.from_currency == from_currency, XRate.to_currency == to_currency).first()
    log.debug(f'Rate before {xrate}')
    xrate.updated = datetime.datetime.now()
    xrate.save()

    log.debug(f"Rate after: {xrate}")
    log.info(f"Finished update for: {from_currency}=> {to_currency}")

def get_nbu_rate(from_currency):
    response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange")
    log.debug(f"response.encoding: {response.encoding}")
    response_text = response.text
    log.debug(f"response.text {response_text}")
    usd_rate = find_usd_rate(response_text)
    return usd_rate

def find_usd_rate(response_text):
    root = ET.fromstring(response_text)
    valutes = root.findall("Valute")
    for valute in valutes:
        if valute.find('Charcode').text == "USD"
            return float(valute.find("Value").text

        raise  ValueError("Invalid NBU response: USD not found "))
