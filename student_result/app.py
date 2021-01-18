from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<name>/result')
def result(name):
   dict = {'phy':50,'che':60,'maths':70}
   sum=0
   for i in dict.values():
      sum = sum+i
   avg=(sum/300) * 100
   return render_template('student.html', result = dict, name=name, total=avg)

if __name__ == '__main__':
   app.run(debug = True)
