import asyncio
import requests
import websockets
import json
import base64
import os

API_KEY = os.getenv("API_KEY")  # api key for the wallet you created
if API_KEY is None:
    print("Environment variable is not properly set")
    exit()
TRACK_ADDRESS = ["", ]  # list of accounts to watch

url = base64.b64decode("aHR0cHM6Ly9wdW1wcG9ydGFsLmZ1bi9hcGkvdHJhZGU/YXBpLWtleT0=").decode("utf-8") + API_KEY
uri = base64.b64decode("d3NzOi8vcHVtcHBvcnRhbC5mdW4vYXBpL2RhdGE=").decode("utf-8")


async def subscribe():
    async with websockets.connect(uri) as websocket:
        payload = {
            "method": "subscribeAccountTrade",
            "keys": TRACK_ADDRESS
        }
        await websocket.send(json.dumps(payload))

        async for message in websocket:
            data = json.loads(message)
            if data.get("txType") == "create":
                response = requests.post(url=url, data={
                    "action": "buy",  # "buy" or "sell"
                    "mint": data["mint"],  # contract address of the token you want to trade
                    "amount": 100000,  # amount of SOL or tokens to trade
                    "denominatedInSol": "false",  # "true" if amount is amount of SOL, "false" if amount is number of tokens
                    "slippage": 10,  # percent slippage allowed
                    "priorityFee": 0.005,  # amount used to enhance transaction speed
                    "pool": "pump"  # exchange to trade on. "pump" or "raydium"
                })
                response_data = response.json()  # Tx signature or error(s)
                print(f'Transaction: https://solscan.io/tx/{response_data["signature"]}')


asyncio.run(subscribe())
