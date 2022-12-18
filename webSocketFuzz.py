import sys
import websocket
import json


ws = websocket.WebSocket()
ws.connect("ws://websocketSV:websocketPORT")


passread = str(sys.argv[1])


def doIt(o):
    
    idx = 0
    payList = []
    with open(passread) as lines:
        passList = lines.read().splitlines()

    for x in passList:
        
        
        ws.send(json.dumps({
        "id": passList[idx]
        }))
        
        result = ws.recv()
        
        
        idx = idx + 1
        if result != "Ticket Doesn't Exist":
            print("SV Response:", result)
            print(passList[idx])
        
    

doIt(passread)