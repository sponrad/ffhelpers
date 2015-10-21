import csv
import json

cr = csv.DictReader(open("ffinput.csv","rb"))
print("Opening file...")
f = open('FFAppMassImport.txt', 'w')

f.write("""SKU	Product ID	Reference Name	Type	Cleared For Sale	Wholesale Price Tier	Displayed Name	Description	Screenshot Path	Effective Date	End Date	Review Notes	Hosted Content Path
""")

print("Processing data...")

data = ""
for row in cr:
    sku = "4"
    productid = row["productid"]
    referencename = generateName(row)
    itemtype = "Non-Consumable"
    description = "Flash Force pattern"
    screenshotpath = "/some/path"
    effectivedate = "2015-11-01"
    enddate = "None"
    notes = ""
    hostedpath = ""

    itemorder = [sku, productid, referencename, itemtype, "yes", "1", referencename, description, screenshotpath, effectivedate, enddate, notes, hostedpath]
    
    data += "\t".join([str(i) for i in itemorder]) + "\n"

f.write(data)
print("done")

def generateName(row):
    #placeholder for now
    return "generated name"
    
