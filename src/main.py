from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

import start_db, random

personas = start_db.startDB()

@app.route('/')
def root():
  p=random.choice(personas)
  print(p['name'])
  return render_template('home.html',p=p), 200

@app.route('/list/')
def list():
  return render_template('list.html',personas=personas),200

@app.route('/search/')
def search():
  search_term = request.args.get('q','')
  if search_term == '':
    return render_template('noSearch.html')
  else:
    results =[]
    for p in personas:
      if search_term in p['name']:
        results.append(dict(p))
    if results == []:
      return render_template('noSearch.html',search_term=search_term)
    else:
      return render_template('search.html',results=results)

@app.route('/persona/')
def noPersona():
  return redirect(url_for('List')),200

@app.route('/persona/<name>')
def persona(name):
  for p in personas:
    if p['name'] == name:
      print p['name']
      return render_template('persona.html',p=p),200
  return render_template('404.html'),404



@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

