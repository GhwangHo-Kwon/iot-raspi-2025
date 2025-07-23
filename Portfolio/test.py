from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

def read_temperature_humidity():
    # 가상의 온도와 습도 데이터를 생성
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(40.0, 60.0)
    return temperature, humidity

def read_gas_level():
    # 가상의 가스 농도 생성
    gas_level = random.uniform(0.0, 1.0)
    return gas_level

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor_data')
def sensor_data():
    # 가상의 센서 값 생성
    temperature, humidity = read_temperature_humidity()
    gas_level = read_gas_level()

    # JSON 형식으로 반환
    return jsonify({
        'temperature': round(temperature, 2),
        'humidity': round(humidity, 2),
        'gas_level': round(gas_level, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
