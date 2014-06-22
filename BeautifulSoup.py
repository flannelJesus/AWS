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
    return ""
