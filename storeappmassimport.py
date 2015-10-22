import csv
import json

def generateName(row):
    temp = [
        row['category'],
        row['name'],
        row['alternate']
        ]
    return " ".join(temp)

crdict = csv.DictReader(open("ffinput.csv","rb"))
print("Opening file...")
f = open('FFAppMassImport.txt', 'w')

f.write("""SKU	Product ID	Reference Name	Type	Cleared For Sale	Wholesale Price Tier	Displayed Name	Description	Screenshot Path	Effective Date	End Date	Review Notes	Hosted Content Path
""")

print("Processing data...")

data = ""
for row in enumerate(crdict, start=1):
    sku = "smarterappsflashforce"
    productid = row[1]["productid"].strip()  #no trailing or leading spaces
    referencename = generateName(row[1])
    itemtype = "Non-Consumable"
    description = "Flash Force pattern"
    screenshotpath = "/Users/conradframe/Desktop/ffimages/purchaseExample.png"
    effectivedate = "2015-10-01"
    enddate = "2025-11-01"
    notes = ""
    hostedpath = ""

    itemorder = [sku, productid, referencename, itemtype, "yes", 1, referencename, description, screenshotpath, effectivedate, enddate, notes, hostedpath]
    
    data += "\t".join([str(i) for i in itemorder]) + "\n"

f.write(data)
print("done")
