from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

def personasAppend(bigList,key,list):
  bigList.append(dict(zip(key,list)))
  return None

keys = ['name', 'arcana','starting level','inherits','img']

izanagi = ['Izanagi','Fool','1','Elec','img/Izanagi.jpg']
pixie = ['Pixie','Magician','2','Ice','img/Pixie.jpg']
saki_mitama =['Saki Mitama','Priestess','11','Recovery','img/Saki_Mitama.jpg']
senri = ['Senri','Empress','9','Recovery','img/Senri.jpg']
oberon = ['Oberon','Emperor','12','Elec','img/Oberon.jpg']
omoikane = ['Omoikane','Hierophant','7','Elec','img/Omoikane.jpg']
queen_mab = ['Queen Mab','Lovers','25','Elec','img/Queen_mab.jpg']
slime = ['Slime','Chariot','2','Phys','img/Slime.jpg']
angel = ['Angel','Justice','4','Wind','img/Angel.jpg']


personas = []
personasAppend(personas,keys,izanagi)
personasAppend(personas,keys,pixie)
personasAppend(personas,keys,saki_mitama)
personasAppend(personas,keys,senri)
personasAppend(personas,keys,oberon)
personasAppend(personas,keys,omoikane)
personasAppend(personas,keys,queen_mab)
personasAppend(personas,keys,slime)
personasAppend(personas,keys,angel)


@app.route('/')
def root():
  return render_template('home.html'), 200

@app.route('/list/')
def list():
  return render_template('list.html',personas=personas),200

@app.route('/search/')
def search():
  search_term = request.args.get('q','')
  if search_term == '':
    return render_template('noSearch.html')
  else:
    for p in personas:
      if p['name'] == search_term:
        print p['name']
        return p['name']
  return "not found"

@app.route('/persona/<chara>/')
def persona(chara):
  for p in personas:
    if p['name'] == chara
      print p['name']
  return render_template('persona.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

