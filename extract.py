import pandas as pd
import json
import requests
from bs4 import BeautifulSoup

def choose_ru(ru):
    ru_codes = { "central": 6, "fisica": 8, "quimicas": 9 }
    return ru_codes[ru] 

def rucard_api(code):
    u_base =  f'https://uspdigital.usp.br/rucard/Jsp/cardapioSAS.jsp?codrtn={code}'
    return u_base
    
if __name__ == '__main__':
    
    ru = input('Choose the RU:' )
    code = choose_ru(ru)
    
    print(rucard_api(code))