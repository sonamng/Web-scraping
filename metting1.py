

import json
a={"name":"rajeev","class":12,"age":18,"city":"ghazipur"}
with open("DATA.JSON","w")as file:
     json.dump(a,file,indent=3)
