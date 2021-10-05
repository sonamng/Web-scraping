import json
a={"a":12,"b":13,"c":14,"d":34}
with open("question8.json","w")as file:
     json.dump(a,file,indent=5)
