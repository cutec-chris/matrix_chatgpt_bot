#!/usr/bin/env python3
import json
import asyncio
from bot import Bot


async def main():
    fp = open('config.json', 'r')
    config = json.load(fp)
    matrix_bot = Bot(homeserver=config['homeserver'],
                     user_id=config['user_id'],
                     password=config['password'],
                     device_id=config['device_id'],
                     room_id=config.get('room_id', ''),  # provide a default value when the key does not exist
                     api_key=config['api_key'])
    await matrix_bot.login()
    await matrix_bot.sync_forever()


if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(main())
