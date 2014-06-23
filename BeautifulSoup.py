import urllib
from bs4 import BeautifulSoup
import urllib2


def asin2min(asin):
    try:
        x = urllib2.urlopen(
            "http://www.amazon.co.uk/gp/offer-listing/" + asin + "/ref="
                                                                 "dp_olp_new_mbc?ie=UTF8&condition=new").read()

        soup = BeautifulSoup(x, "html.parser")
        pricet = soup.find(class_="olpOfferPrice")
        if pricet != None:
            price = float(pricet.text.strip()[1:])
            shippingp = 0
            for sibling in soup.find(class_="olpOfferPrice").next_siblings:
                sibling = str(sibling)
                if 'class="olpShippingPrice"' in sibling:
                    ship = BeautifulSoup(sibling)
                    shipping = ship.find(class_="olpShippingPrice")
                    shippingp = float(shipping.text.strip()[1:])

            return str(shippingp + price)
        else:
            return ""
    except:
        return ""


def asin2bn(asin):
    prefix = "http://www.amazon.co.uk/dp/"
    url = prefix + asin.strip()
    try:
        conn = urllib.urlopen(url)
        rank, buy_now = "", ""
        for line in conn:
            line = line.strip()
            if '<span id="pricePlusShippingQty"><b class="price">' in line:
                index1 = repr(line).find("\\xa3")
                index2 = line.find("</b>")
                price = float(line[index1:index2])
                shipping = 0
                if "FREE" not in line:
                    index1 = line.find("&nbsp;+&nbsp;")
                    index2 = line[index1 + 15:].find("&") + index1 + 15
                    shipping = float(line[index1 + 14:index2])
                buy_now = str(price + shipping)
                break
        return buy_now
    except:
        return ""
