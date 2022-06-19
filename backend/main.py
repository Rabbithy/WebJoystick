import asyncio
import json

import websockets
import keyboard

CONTROLS = {
	1: {
		'start': '8',
		'select': '7',
		'up': 'up',
		'left': 'left',
		'down': 'down',
		'right': 'right',
		'a': 'z',
		'b': 'x',
		'x': 'c',
		'y': 'v'
	},
	2: {
		'start': '0',
		'select': '9',
		'up': 'w',
		'left': 'a',
		'down': 's',
		'right': 'd',
		'a': '1',
		'b': '2',
		'x': '3',
		'y': '4'
	},
	3: {
		'start': 'enter',
		'select': 'backspace',
		'up': 'u',
		'left': 'h',
		'down': 'j',
		'right': 'k',
		'a': 'f',
		'b': 'g',
		'x': 'b',
		'y': 'n'
	}
}


async def serve_client(ws):
	msg = await ws.recv()

	handshake_event = json.loads(msg)
	control_number = handshake_event.get('control')
	control = CONTROLS.get(control_number)	
	
	async for msg in ws:
		event = json.loads(msg)
		if event['type'] == 'KEY_DOWN':
			key = control.get(event['key'])
			keyboard.press(key)
		elif event['type'] == 'KEY_UP':
			key = control.get(event['key'])
			keyboard.release(key)


async def main():
	async with websockets.serve(serve_client, '', 1024):
		await asyncio.Future()


if __name__ == '__main__':
	asyncio.run(main())
