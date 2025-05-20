import asyncio
import requests
import websockets
import json
import base64

API_KEY = ""  # api key for the wallet you created

TRACK_ADDRESS = ["", ]  # list of accounts to watch
TRACK_ADDRESS = [address.strip() for address in TRACK_ADDRESS]

url = base64.b64decode("aHR0cHM6Ly9wdW1wcG9ydGFsLmZ1bi9hcGkvdHJhZGU/YXBpLWtleT0=").decode("utf-8") + API_KEY
uri = base64.b64decode("d3NzOi8vcHVtcHBvcnRhbC5mdW4vYXBpL2RhdGE=").decode("utf-8")


async def subscribe():
    async with websockets.connect(uri, ping_interval=20,) as websocket:
        payload = {
            "method": "subscribeAccountTrade",
            "keys": TRACK_ADDRESS
        }
        await websocket.send(json.dumps(payload))

        async for message in websocket:
            data = json.loads(message)
            if data.get("txType") == "create" and data.get("pool") == "pump":
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
                signature = response_data.get("signature")
                if signature is not None:
                    print(f'Transaction: https://solscan.io/tx/{response_data["signature"]}')
                else:
                    print(f"Transaction not successful: {response_data}")


asyncio.run(subscribe())
