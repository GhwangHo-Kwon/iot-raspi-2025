import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
import pymysql

conn = pymysql.connect(
	host='127.0.0.1',
	port=3306,
	user='root',
	password='',
	database='testdb',
	charset='utf8'
)

dhtPin = 23

GPIO.setmode(GPIO.BCM)
# GPIO.setip(dhtPin, GPIO.IN)

dht = adafruit_dht.DHT11(board.D23)
cursor = conn.cursor()

while True:
	try:
		temperature = dht.temperature
		humidity = dht.humidity
		print(f"Temp: {temperature} ℃")
		print(f"Humid: {humidity} %")
		query = "INSERT INTO temp_humid (temp, humid) VALUES (%s, %s)"
		cursor.execute(query, (temperature, humidity))

		conn.commit()

		time.sleep(1)

	except RuntimeError as error:
		print(error.args[0])
	except KeyboardInterrupt:
		GPIO.cleanup()
		break

dht.exit()
conn.close()
