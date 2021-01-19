from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student_data.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      sum = 0
      print(result)
      data = list(result.values())[1:]
      for i in data :
          sum = sum + int(i)
      avg = (sum / 300) * 100
      name = list(result.values())[0]
      return render_template("result.html",result = result, avg=avg, name = name)

if __name__ == '__main__':
   app.run(debug = True)