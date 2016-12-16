import amazonproduct
from BeautifulSoup import asin2min, asin2bn
import unicodedata
import time


api = amazonproduct.API(locale='uk')
# config at C:\Users\user\.amazon-product-api

barcodes = open('barcodes.txt')
output = open('b2a.csv', 'w')
output.write('sep = |\nbarcode|ASIN|Amazon Title|Rank|MinPrice\n')
x = 0
y = 1
for line in barcodes:
    x += 1
    bc = line.strip()
    try:
        result = api.item_lookup(bc, SearchIndex='All', IdType='EAN',
                                 ResponseGroup="Small,SalesRank,Offers")
        for item in result.Items.Item:
            asin = str(item.ASIN) if hasattr(item, "ASIN") else ""
            title = str(
                item.ItemAttributes.Title.text.encode(
                    'ascii', 'ignore')) if \
                hasattr(item, "ItemAttributes") and \
                hasattr(item.ItemAttributes, "Title") else ""
            rank = str(item.SalesRank) if hasattr(item, "SalesRank") else ""
            # minprice = asin2min(item.ASIN) if hasattr(item, "ASIN") else ""
            minprice = item.OfferSummary.LowestNewPrice.Amount if hasattr(item.OfferSummary, "LowestNewPrice") else ""
            # bn = asin2bn(item.ASIN.text) if hasattr(item, "ASIN") else ""
            # bn = 0
            output.write('%s|%s|%s|%s|%s\n' % (bc, asin, title, rank, minprice))
    except Exception as err:
        print err
        output.write("%s|exception|%s||\n" % (bc, err.msg))
    time.sleep(1)

output.close()
