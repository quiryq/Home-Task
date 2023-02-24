import json

json_file = open("/home/nurdauletms/Документы/pp2/w4/Lab/JSON/sample_data.JSON")

data = json.load(json_file)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for item in data['imdata']:
    
    print(item['l1PhysIf']['attributes']['dn'], end="" * 10)
    print(item['l1PhysIf']['attributes']['descr'], end=" " * 30)
    print(item['l1PhysIf']['attributes']['speed'], end=" " * 3)
    print(item['l1PhysIf']['attributes']['mtu'])