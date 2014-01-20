import amazonproduct
from BeautifulSoup import asin2min

api = amazonproduct.API(locale='uk')

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
                                 ResponseGroup="Small,SalesRank")
        for item in result.Items.Item:
            output.write(
                '%s|%s|%s|%d|%s\n' % (
                    bc, item.ASIN, item.ItemAttributes.Title,
                    item.SalesRank,
                    asin2min(item.ASIN)))
    except:
        output.write("%s||||\n" % (bc))
output.close()
