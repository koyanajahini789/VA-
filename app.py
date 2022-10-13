from flask import Flask, jsonify, request,render_template
from VirtualAssistant import virtual_assistant
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')
   #return "Hello Welcome to my world"
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      transcript = request.form['transcript']
      print(transcript)
      result = virtual_assistant(transcript)
      return jsonify({'result':result})
app.run()

