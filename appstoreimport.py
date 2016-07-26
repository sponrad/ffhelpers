import csv
import json
import re, string

def generateName(row):
    temp = [
        " ".join( re.compile('\w+').findall(row['category']) ),
        row['sport_special'],
        " ".join( re.compile('\w+').findall(row['name']) ),
        " ".join( re.compile('\w+').findall(row['alternate']) ),
        ]
    return " ".join(temp)

crdict = csv.DictReader(open("ffinput.csv","rb"))
print("Opening file...")
f = open('appstoreimport.txt', 'w')

original = csv.DictReader(open("ffinput first approved.csv","rb"))
originalproductids = []

for row in enumerate(original, start=1):
    originalproductids.append(row[1]["productid"].strip())

print originalproductids

f.write("""SKU	Product ID	Reference Name	Type	Cleared For Sale	Wholesale Price Tier	Displayed Name	Description	Screenshot Path	Effective Date	End Date	Review Notes	Hosted Content Path
""")

print("Processing data...")

data = ""
for row in enumerate(crdict, start=1):
    if row[1]["productid"].strip() in originalproductids:
        print(row[1]["productid"].strip())
        continue
    sku = "smarterappsflashforce"
    productid = row[1]["productid"].strip()  #no trailing or leading spaces
    referencename = generateName(row[1])
    itemtype = "Non-Consumable"
    description = "Flash Force pattern"
    screenshotpath = "/Users/conradframe/Desktop/ffimages/purchaseExample.png"
    effectivedate = "Now"
    enddate = "None"
    notes = "Light pattern and timing combination for use in the Flash Force app"
    hostedpath = ""

    itemorder = [sku, productid, referencename, itemtype, "yes", 1, referencename, description, screenshotpath, effectivedate, enddate, notes, hostedpath]
    
    data += "\t".join([str(i) for i in itemorder]) + "\n"

f.write(data)
print("done")
