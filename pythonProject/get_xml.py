import urllib.request
import re


def take_price(name):
    url = 'https://iss.moex.com/iss/engines/stock/markets/shares/securities/{n}.xml'.format(n=name)

    page = urllib.request.urlopen(url)

    html_code = page.read().decode('utf-8')
    link = r'(<row SECID="'+name+r'".{0,10000})'
    feed_dict = re.findall(link, html_code)
    k = ''
    for d in feed_dict:
        a = re.findall(r'(BOARDID="TQBR".{0,50}BID.{0,5000})', d)
        if len(a)>0:
            k = a[0]
            bid = k[k.find('BID')+5:k.find('"', k.find('BID')+5)]
            offer = k[k.find('OFFER')+7:k.find('"', k.find('OFFER')+7)]
            updatetime = k[k.find('UPDATETIME')+12:k.find('"', k.find('UPDATETIME')+12)]
            systime = k[k.find('SYSTIME')+9:k.find('"', k.find('SYSTIME')+9)]
    return name, float(bid), float(offer), updatetime, systime

#take_price("AFLT")
