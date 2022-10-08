from threading import Thread 
import time
from threading import Timer
import requests
from time import time, sleep

def getAllRollDice(id):
	try:
		url = "https://roll-dice1.p.rapidapi.com/rollDice"

		headers = {
			"X-RapidAPI-Key": "44fa34e5a3msh8660905563bb78fp124a41jsncd9b1a24f9d8",
			"X-RapidAPI-Host": "roll-dice1.p.rapidapi.com"
		}


		response = requests.request("GET", url, headers=headers)

		print(response.text)
		sleep(1 - time() % 1)
			
	except ValueError:
		print("Oops! Try again...")

# threads = []

inicio = time()

# for i in range(1, 10000):
# 	t = Thread(target=getAllRollDice, args=(i, ))
# 	threads.append(t)
# 	t.start()
	
# for t in threads:
# 	t.join()
	

for i in range(1, 5000):
	getAllRollDice(i)
	
fim = time()

print("Finished execution with time", fim - inicio)