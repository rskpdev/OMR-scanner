from flask import Flask, render_template, request
from werkzeug import secure_filename
from scanner import Scanner
from flask import jsonify
import os

app = Flask(__name__)
scanner = Scanner()
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save("temp")
      result = scanner.scan("temp")
      os.remove("temp")
      return jsonify({x:result[x] for x in range(5)})

		
if __name__ == '__main__':
   app.run(debug = True)