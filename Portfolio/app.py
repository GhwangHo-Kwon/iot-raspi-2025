from flask import Flask, jsonify, render_template
import Adafruit_DHT
from gpiozero import MCP3008

app = Flask(__name__)

# DHT11 설정
sensor = Adafruit_DHT.DHT11
pin = 4  # DHT11 센서 핀 번호

# MQ-2 설정 (MCP3008 ADC 사용)
adc = MCP3008(channel=0)  # 가스 센서가 연결된 ADC 채널 (0번)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor_data')
def sensor_data():
    # 온습도 데이터 읽기
    temperature, humidity = Adafruit_DHT.read_retry(sensor, pin)
    
    # 가스 센서 데이터 읽기
    gas_level = adc.value  # 0과 1 사이의 값 (0: 0V, 1: 3.3V)

    # 온습도 데이터 반환 (온도, 습도)
    if temperature is not None and humidity is not None:
        temp_humidity_data = {
            'temperature': round(temperature, 2),  # 온도
            'humidity': round(humidity, 2)         # 습도
        }
    else:
        temp_humidity_data = {
            'temperature': 'Error',
            'humidity': 'Error'
        }

    # 가스 농도 데이터
    gas_data = {
        'gas_level': round(gas_level, 2)  # 가스 농도 (0.0 ~ 1.0)
    }

    # 온습도 + 가스 농도 데이터를 합쳐서 JSON 형식으로 반환
    return jsonify({**temp_humidity_data, **gas_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
