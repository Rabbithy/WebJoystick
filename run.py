#!/usr/bin/python3.9
import sys
import os
import threading


def run_async(cmd):
	t = threading.Thread(
		target=os.system, 
		args=[cmd]
	)
	t.start()


def main():
	if sys.platform.startswith('linux'):
		run_async('cd backend && sudo venv/bin/python3 main.py')
		run_async('cd frontend && sudo node src/index.js')


if __name__ == '__main__':
	main()
