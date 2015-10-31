from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

def personasAppend(bigList,key,list):
  bigList.append(dict(zip(key,list)))
  return None

keys = ['name','arcana','startinglevel','inherits','reflects','absorbs','blocks','resists','weak','img']

izanagi = ['Izanagi','Fool','1','Electric','-','-','Dark','Electric','Wind','img/Izanagi.jpg']
pixie = ['Pixie','Magician','2','Ice','-','-','-','Wind','Fire','img/Pixie.jpg']
saki_mitama =['Saki Mitama','Priestess','11','Recovery','-','-','-','Ice','Wind','img/SakiMitama.png']
senri = ['Senri','Empress','9','Recovery','-','-','Fire','-','Electric','img/Senri.jpg']
oberon = ['Oberon','Emperor','12','Electric','-','-','Electric','Fire','Wind','img/Oberon.jpg']
omoikane = ['Omoikane','Hierophant','7','Electric','-','-','-','Electric','Ice','img/Omoikane.jpg']
queen_mab = ['Queen Mab','Lovers','25','Electric','-','-','Electric','-','Wind','img/Queen_mab.jpg']
slime = ['Slime','Chariot','2','Physical','-','-','-','Physical','Fire','img/Slime.jpg']
angel = ['Angel','Justice','4','Wind','-','-','-','Wind,Light','Dark','img/Angel.jpg']
forneus = ['Fourneus','Hermit','6','Ice','-','-','Dark','Ice','Electric','img/Forneus.jpg']
fortuna = ['Fortuna','Fortune','35','Wind','-','-','Fire,Wind','-','-','img/Fortuna.jpg']
sandman =['Sandman','Strength','5','Wind','-','-','-','Wind','Electric','img/Sandman.jpg']
berith = ['Berith','Hanged Man','15','Physical','-','-','Fire','-','Wind','img/Berith.jpg']
ghoul = ['Ghoul','Death','9','Ailment','-','-','Ice','-','Fire,Light','img/Ghoul.jpg']
apsaras =['Apsaras','Temperance','4','Recovery','-','-','-','-','Fire','img/Apsaras.jpg']


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
personasAppend(personas,keys,forneus)
personasAppend(personas,keys,fortuna)
personasAppend(personas,keys,sandman)
personasAppend(personas,keys,berith)
personasAppend(personas,keys,ghoul)
personasAppend(personas,keys,apsaras)

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
    results =[]
    for p in personas:
      if search_term in p['name']:
        results.append(dict(p))
    if results == []:
      return render_template('noSearch.html',search_term=search_term)
    else:
      return render_template('search.html',results=results)

@app.route('/persona/<chara>/')
def persona(chara):
  for p in personas:
    if p['name'] == chara:
      print p['name']
      return render_template('persona.html',p=p)
  return "nope.jpg"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

