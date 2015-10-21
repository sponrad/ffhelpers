import csv
import json

cr = csv.reader(open("ffinput.csv","rb"))
print("Opening file...")
f = open('ffoutput.txt', 'w')

f.write("""//
//  store-data.swift
//  whoscheering
//
//  Created by Conrad on 5/25/15.
//  Copyright (c) 2015 Conrad. All rights reserved.
//

import Foundation

struct StoreData{
    
    static let initialData: [[String]] = [
""")

print("Processing data...")
data = ''
for row in cr:
    data += str(row).replace('"', '\"').replace("'",'"') + ",\n"

#print data
print("done")
f.write(data)

f.write("""]
}""")
