

import json
b={"name":"sonam","age":20,"vellage":"maujpur","post":"barezi","distric":"Ghazipur"}
with open("question6.json","r")as file:
     json.dump(b,file,indent=5)