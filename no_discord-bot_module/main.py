import asyncio
import websockets
import json
import requests

TOKEN = env.TOKEN
class Bot:
    interval = None
    sequence = None
    
async def heartbeat(websocket):
    print("heartbeat")
    while Bot.interval is not None:
        await websocket.send(json.dumps({"op": 1, "d": Bot.sequence}))
        await asyncio.sleep(Bot.interval)

async def receive(websocket):
    print("receive")
    async for message in websocket:
        data = json.loads(message)
        if data["op"] == 0:
            c = data["d"]
            Bot.sequence = int(data["s"])
            event_type = data["t"]
            if event_type == "MESSAGE_CREATE":
                if not "bot" in c["author"]:
                    content = c["content"]
                    if content == "( ・∇・)":
                        res = "( ・∇・)"
                        
                    elif "えい！" in content:
                        res = "えい！"
                        
                    elif content.startswith("オウム返し"):
                        r = content.removeprefix('オウム返し')
                        res = r if r else "えい！"
                        
                    elif data["d"]["channel_id"] == env.CHANNEL_ID:
                        match content:
                            case "すいちゃんは〜？":
                                res = "今日も可愛い〜！"
                            case "ミオしゃ":
                                res = "うちうち！うちだよ！大神ミオだよ〜！"
                        continue
                    else:
                        continue
                    requests.post("https://discord.com/api/v10/channels/" + data["d"]["channel_id"] + "/messages", 
                                headers = {"authorization": TOKEN, "content-type": "application/json"},
                                json = {"content": res}
                            )

async def main():
    print("main")
    async with websockets.connect('wss://gateway.discord.gg/?v=6&encoding=json') as websocket:
        await websocket.send(json.dumps({"op": 2, "d": {"token": TOKEN, "properties": { "$os": "windows", "$device": "disco"}, "presence": {"status": "online", "afk": False}}}))
        data = json.loads(await websocket.recv())
        if data["op"] == 10:
            Bot.interval = (data["d"]["heartbeat_interval"] - 2000) / 1000
            if Bot.interval is None:
                return
        
        await asyncio.gather(heartbeat(websocket), receive(websocket))
    
        
asyncio.run(main())
