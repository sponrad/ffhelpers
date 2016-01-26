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
f = open('androidimport.csv', 'w')

a = csv.writer(f)

#"product_id","publish_state","purchase_type","autotranslate ","locale; title; description","autofill","country; price"

print("Processing data...")

data = []
for row in enumerate(crdict, start=1):
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
    
    data.append(",".join([str(i) for i in itemorder]))

a.writerows(data)
f.close()
print("done")
