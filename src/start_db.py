def personasAppend(bigList,key,list):
  bigList.append(dict(zip(key,list)))
  return None


keys = ['name','arcana','startinglevel','inherits','reflects','absorbs','blocks','resists','weak','img']

izanagi = ['Izanagi','Fool','1','Electirc','-','-','Dark','Electirc','Wind','img/Izanagi.jpg']
pixie = ['Pixie','Magician','2','Ice','-','-','-','Wind','Fire','img/Pixie.jpg']
saki_mitama = ['Saki Mitama','Priestess','11','Recovery','-','-','-','Ice','Wind','img/SakiMitama.png']
senri = ['Senri','Empriss','9','Recovery','-','-','Fire','-','Electic','img/Senri.jpg']
oberon = ['Oberon','Emperor','12','Electirc','-','-','Electirc','Fire','Wind','img/Oberon.jpg']
omoikane = ['Omoikane','Hierophant','7','Electric','-','-','-','Electirc','Ice','img/Omoikane.jpg']
queen_mab = ['Queen Mab','Lovers','25','Electric','-','-','Electirc','-','Wind','img/Queen_mab.jpg']
slime = ['Slime','Chariot','2','Physical','-','-','-','Physical','Fire','img/Slime.jpg']
angel = ['Angel','Justice','4','Wind','-','-','-','Wind,Light','Dark','img/Angel.jpg']
forneus = ['Forneus','Hermit','6','Ice','-','-','Dark','Ice','Electirc','img/Forneus.jpg']
fortuna = ['Fortuna','Fortune','35','Wind','-','-','Fire, Wind','-','-','img/Fortuna.jpg']
sandman = ['Sandman','Strength','5','Wind','-','-','-','Wind','Electric','img/Sandman.jpg']
berith = ['Berith','Hanged Man','15','Physical','-','-','Fire','-','Wind','img/Berith.jpg']
ghoul = ['Ghoul','Death','9','Ailment','-','-','Ice','-','Fire, Light','img/Ghoul.jpg']
apsaras = ['Apsaras','Temperance','4','Recovery','-','-','-','-','Fire','img/Apsaras.jpg']
ukobach = ['Ukobach','Devil','3','FIre','-','-','-','Fire','Ice','img/Ukobach.png']
tao_tie = ['Tao Tie','Tower','35','Almighty','Dark','-','-','-','-','img/Tao_tie.jpg']
kaiwan = ['Kaiwan','Star','24','Support','-','-','Dark','-','Physical','img/Kaiwan.jpg']
andras = ['Andras','Moon','20','Recovery','-','-','Electic','-','Wind','img/Andras.jpg']
cu_sith = ['Cu Sith','Sun','10','Wind','-','-','-','Wind','Fire','img/Cu_sith.jpg']
anubis = ['Anubis','Judgement','59','Light','-','-','Light','-','-','img/Anubis.jpg']
izanagi_no_okami = ['Izanagi-no-Okami','World','91','No','-','-','-','Physical, Fire, Ice, Electic, Wind','-','img/Izanagi_no_okami.jpg']

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
personasAppend(personas,keys,ukobach)
personasAppend(personas,keys,tao_tie)
personasAppend(personas,keys,kaiwan)
personasAppend(personas,keys,andras)
personasAppend(personas,keys,cu_sith)
personasAppend(personas,keys,anubis)
personasAppend(personas,keys,izanagi_no_okami)

def startDB():
  return personas

