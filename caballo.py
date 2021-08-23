import webbrowser
import threading

def open():
	while True:
		webbrowser.open('https://www.youtube.com/watch?v=Jv4O_XeHPyA')

threads = []

for i in range(16):
	t = threading.Thread(target=open)
	t.daemon = True
	threads.append(t)

for i in range(16):
	threads[i].start()

for i in range(16):
	threads[i].join()
