# employee.py
from flask import Flask, render_template, request

app = Flask(__name__)

contacts = []
@app.route('/')
def index():
	return render_template('add.html')

@app.route('/submit', methods=['POST'])
def submit():
	name = request.form.get('name')
	phone = request.form.get('phone')
	email = request.form.get('email')
	contacts.append({'name':name, 'phone':phone, 'email':email})
	return f"<h3>입력 완료: {name}-{phone}-{email}</h3><br><a href='/'>돌아가기</a>"

@app.route('/list', methods=['GET'])
def get_list():
	info = "<h3>직원 정보</h3><ul>"

	for contact in contacts:
		info += f"<tr><td>Name: </td><td>{contact['name']}</td></tr><br>"
		info += f"<tr><td>Phone: </td><td>{contact['phone']}</td></tr><br>"
		info += f"<tr><td>Email: </td><td>{contact['email']}</td></tr><br>"

	info += "</ul><br><a href='/'>돌아가기</a>"

	return info

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
