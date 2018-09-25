import json, os
import pandas as pd
import numpy as np
from collections import Counter
TextFiles = []
FName = []
csv_rows = []
commenterid = []

for root, dirs, files in os.walk("/Users/aaaa/Desktop/"):
    for file in files:
        if file.endswith("chatinfo.txt"):
            path = "/Users/aaaa/Desktop/"
            filepath = os.path.join(path,file)
            head, filename = os.path.split(filepath)
            TextFiles.append(filepath)
            FName.append(filename)
            
            n_commenters = 0
            with open(filepath) as open_file:
                for line in open_file:
                    jsondata = json.loads(line)
                    if "commenter" in jsondata:
                        commenterid.append(jsondata["commenter"]["_id"])
                        
                        list_set = set(commenterid)
                        unique_list = (list(list_set))

                    for x in list_set:
                        n_commenters += 1
                        
                        commenterid.clear()
                csv_rows.append([filename, n_commenters])
df = pd.DataFrame(csv_rows, columns=['FileName', 'Unique_Commenters'])
df.to_csv('CommeterID.csv', index=False)



        
                    
                    
        
    
