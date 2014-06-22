import amazonproduct
from BeautifulSoup import asin2min, asin2bn
import unicodedata

def if_error(func, input, default_value):
    try:
        r = func(input)
    except:
        r = default_value
    return r

api = amazonproduct.API(locale='uk')

barcodes = open('barcodes.txt')
output = open('b2a.csv', 'w')
output.write('sep = |\nbarcode|ASIN|Amazon Title|Rank|MinPrice|BuyNow\n')
x = 0
y = 1
for line in barcodes:
    x += 1
    bc = line.strip()
    try:
        result = api.item_lookup(bc, SearchIndex='All', IdType='EAN',
                                 ResponseGroup="Small,SalesRank")
        for item in result.Items.Item:
            #try:
            #    output.write(
            #        '%s|%s|%s|%d|%s|%s\n' % (
            #            bc, item.ASIN, item.ItemAttributes.Title,
            #            item.SalesRank,
            #            asin2min(item.ASIN), asin2bn(item.ASIN)))
            #except:
            #    output.write("%s|exception||||\n" % (bc))

            #try:
            #    asin = str(item.ASIN)
            #except:
            #    asin = ""
            #try:
            #    title = str(item.ItemAttributes.Title)
            #except:
            #    title = ""
            #try:
            #    rank = str(item.SalesRank)
            #except:
            #    rank = ""
            #try:
            #    min = asin2min(item.ASIN)
            #except:
            #    min = ""
            #try:
            #    bn = asin2bn(item.ASIN)
            #except:
            #    bn = ""

            if bc == "5060149520178":
                pass
            asin = str(item.ASIN) if hasattr(item, "ASIN") else ""
            title = str(item.ItemAttributes.Title.text.encode('ascii','ignore')) if hasattr(item, "ItemAttributes") and hasattr(item.ItemAttributes, "Title") else ""
            rank = str(item.SalesRank) if hasattr(item, "SalesRank") else ""
            min = asin2min(item.ASIN) if hasattr(item, "ASIN") else ""
            bn = asin2bn(item.ASIN) if hasattr(item, "ASIN") else ""
            output.write('%s|%s|%s|%s|%s|%s\n' % (bc, asin, title, rank, min, bn))

    except:
        output.write("%s|exception||||\n" % (bc))
output.close()
