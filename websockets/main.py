import asyncio
import json
import logging
import websockets
#import pickle

logging.basicConfig()

STATE = {"value": "empty"}

USERS = set()

STATES = []

def state_event():
    return json.dumps({"type": "data", **STATE})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
#        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data:
                STATE["value"] = data["data"]
                STATES = []
                for state in STATE["value"]:
                    STATES.append(state["text"])
                print(STATES)
                await notify_state()
            else:
                logging.error("Massage is empty")
    finally:
        await unregister(websocket)
#        if len(USERS) == 0:
#            forDB = pickle.dumps(STATES)



start_server = websockets.serve(counter, "0.0.0.0", 3001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()