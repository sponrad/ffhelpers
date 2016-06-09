import csv
import json

def generateName(row):
    temp = [
        row['category'],
        row['alternate'],
        row['name'],
        ]
    return " ".join(temp)[0:54]

def getPrice(row):
    return int( float(row["price"])*1000000 )


crdict = csv.DictReader(open("ffinput.csv","rb"))
print("Opening file...")
f = open('playstoreimport.csv', 'w')

a = csv.writer(f)

#"product_id","publish_state","purchase_type","autotranslate ","locale; title; description","autofill","country; price"

print("Processing data...")

data = []
for row in enumerate(crdict, start=1):
    product_id = row[1]["productid"].strip()  #no trailing or leading spaces
    publish_state = "published"
    purchase_type = "managed_by_android"
    autotranslate = "false"
    localetitledescription = "en_US; "+generateName(row[1]) + "; Flash Force Pattern"
    autofill = "true"
    countryprice = str(getPrice(row[1]))

    #itemorder = [sku, productid, referencename, itemtype, "yes", 1, referencename, description, screenshotpath, effectivedate, enddate, notes, hostedpath]
    itemorder = [product_id, publish_state, purchase_type, autotranslate, localetitledescription, autofill, countryprice]

    if getPrice(row[1]) > 1:
        data.append(itemorder)
    else:
        print countryprice

a.writerows(data)
f.close()
print("done")
