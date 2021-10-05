
import json
a={"name":"ravi","age":21,"city":"chandauli"}
with open("question5.json","w")as file:
     json.dump(a,file,indent=4)