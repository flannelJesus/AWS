import amazonproduct
from BeautifulSoup import asin2min, asin2bn

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

            try:
                asin = str(item.ASIN)
            except:
                asin = ""
            try:
                title = str(item.ItemAttributes.Title)
            except:
                title = ""
            try:
                rank = str(item.SalesRank)
            except:
                rank = ""
            try:
                min = asin2min(item.ASIN)
            except:
                min = ""
            try:
                bn = asin2bn(item.ASIN)
            except:
                bn = ""
            output.write('%s|%s|%s|%s|%s|%s\n' % (bc, asin, title, rank, min, bn))

    except:
        output.write("%s|exception||||\n" % (bc))
output.close()
