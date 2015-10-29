from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

izanagi = ['Izanagi','Fool','1','Elec']
pixie = ['pixie','Magician','2','Ice']
saki_mitama = ['Saki Mitama','Priestess','11','Recovery']
senri = ['Senri','Empress','9','Recovery']

personas = {'Izanagi': izanagi,'Pixie':pixie,'Saki Mitama':saki_mitama,'Senri':senri}


@app.route('/')
def root():
  return render_template('home.html'), 200

@app.route('/list/')
def list():
  return render_template('list.html'),200

@app.route('/search/')
def search():
  if request.method == 'POST'
    print request.form
    q = request.form['q']
    for  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

