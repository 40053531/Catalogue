def personasAppend(bigList,key,list):
  bigList.append(dict(zip(key,list)))
  return None


keys = ['name','arcana','startinglevel','inherits','reflects','absorbs','blocks','resists','weak','img','info']

izanagi = ['Izanagi','Fool','1','Electirc','-','-','Dark','Electirc','Wind','img/Izanagi.jpg','Izanagi (伊弉諾) is a Japanese creation deity born of the seven divine generations in Japanese mythology. He is also referred to in various chronicles such as the Kojiki and Nihon Shiki as Izanagi-no-mikoto (伊弉諾尊), the "male-who-invites". He and Izanami created many of the islands and deities of Japan. When Izanami died, Izanagi tried to retrieve her from the underworld, but failed. He mistakenly looks at her while shes in a rotting, monstrous state in the underworld, which shames her. She attempts to kill him, and swears to kill a thousand of his men a day. Izanagi claims that he will make sure that a thousand and five hundred will be born each day.']
pixie = ['Pixie','Magician','2','Ice','-','-','-','Wind','Fire','img/Pixie.jpg','According to the local folklore of southwest England, pixies are small mischievous creatures that inhabit the countryside and woodlands that like to play pranks on humans. Depending on the tale told, pixies can vary in size from tiny enough to fit in the palm of a humans hand to the size of a small child, although they are always a good deal below the size of an average human. They can be portrayed with or without wings, and over the years have taken on many traits usually associated with fairies, often leading to the common misconception that they are one and the same.']
saki_mitama = ['Saki Mitama','Priestess','11','Recovery','-','-','-','Ice','Wind','img/SakiMitama.png','One of the four great aspects of Shinto thought, it brings great bounty from the hunt. It is said to aid in love, profit, and growth, and can create new paths.']
senri = ['Senri','Empriss','9','Recovery','-','-','Fire','-','Electic','img/Senri.jpg','"In Japanese folklore, the senri are creatures that come into being when an extremely old mountain cat undergoes a spiritual transformation. It can take the form of a beautiful young lady and seduce unfortunate men that wonder into the mountains. It then steals their life energy in order to sustain itself and gain more power. The senri is the highest rank of bakeneko, and it is said that other animals that have become demonized gather life energy so that they themselves can become Senri. The senri are akin to the Chinese spirit animals known as the yao jing, which achieve human form after many years of training in the art of Taoism.']
oberon = ['Oberon','Emperor','12','Electirc','-','-','Electirc','Fire','Wind','img/Oberon.jpg','The King of the Fairies and the husband of Titania, the Fairy Queen. He rules over moonlight, dreams, and all fairy rites. He first became widely known when he appeared as a character in Shakespeare’s "A Midsummer Night’s Dream," but appeared earlier in the 13th century French epic "Huon of Bordeaux." In some stories, specifically in "Huon of Bordeaux," it is said that he is the son of Morgan le Fey and Julius Caesar, believed to have been born sometimes after Caesar’s defeat of Pompey.']
omoikane = ['Omoikane','Hierophant','7','Electric','-','-','-','Electirc','Ice','img/Omoikane.jpg','Omoikane is a Shinto god of wisdom and intelligence. His name means "serving ones thoughts." A heavenly deity, identified as a child of Takami-Musubi, who is always called upon to "ponder" and give good counsel in the deliberations of the heavenly deities. Appears to have descended from the heavens in the heavenly descent myth. Omoikane was a deity of wisdom or good counsel able to hold many thoughts at once or to combine in one mind the mental powers of many individuals.']
queen_mab = ['Queen Mab','Lovers','25','Electric','-','-','Electirc','-','Wind','img/Queen_mab.jpg','Mab, also known as Medb or Meive, is the queen of Connacht. Famous for her capricious nature and her many lovers, she wages many wars for sake of her continued glory. The Cattle Raid of Cooley makes her cross paths with her archenemy Cu Chulainn, who shamed her numerous times by slaying her pets, warriors and handmaidens.']
slime = ['Slime','Chariot','2','Physical','-','-','-','Physical','Fire','img/Slime.jpg','In the Dungeons & Dragons fantasy role-playing game, an ooze is a type of creature. This category includes such monsters as slimes, jellies, deadly puddings, and similar mindless, amorphous blobs. They can be used by Dungeon Masters as enemies or allies of the player characters. Many oozes dwell underground, and most secrete an acid from their skin that dissolves flesh and other materials rapidly. Oozes are essentially blind, but more than make up for that with an ability called "blindsight", which allows them to discern nearby objects and creatures without needing to see them visually.']
angel = ['Angel','Justice','4','Wind','-','-','-','Wind,Light','Dark','img/Angel.jpg','Angels have been recorded in various religious lore as celestial beings who faithfully serve God.']
forneus = ['Forneus','Hermit','6','Ice','-','-','Dark','Ice','Electirc','img/Forneus.jpg','According to the writings in The Lesser Key of Solomon, Forneus is the thirtieth spirit listed in the Goetia. He is a Great Marquis of Hell with twenty-nine legions under his command, partly comprised of the order of Angels and Thrones, and appears as a sea monster. When summoned, he can make men well-versed in rhetoric, give him a good name, teach him foreign tongues, and make him trusted by friend and foe alike.']
fortuna = ['Fortuna','Fortune','35','Wind','-','-','Fire, Wind','-','-','img/Fortuna.jpg','The goddess of Fortune and luck in Roman mythology, daughter of Jupiter, and hopefully brought good luck. She can be represented veiled or blind. Used to be a goddess of blessing and fertility, mainly being worshiped by mothers.']
sandman = ['Sandman','Strength','5','Wind','-','-','-','Wind','Electric','img/Sandman.jpg','Originating from Northern European lore, he brings good dreams by sprinkling magical sand onto the eyes of children while they sleep at night. The rheum in ones eyes upon waking is believed to be the result of the Sandmans work the previous evening.']
berith = ['Berith','Hanged Man','15','Physical','-','-','Fire','-','Wind','img/Berith.jpg','According to the writings in The Lesser Key of Solomon, Berith is the twenty-eighth spirit listed in the Goetia. He rides a gigantic red horse and burns those without manners. He is a Great Duke of Hell with twenty-six legions of demons under his command. He is depicted as a knight or soldier wearing red armour and a golden crown. In order to speak with him the conjurer must wear a silver ring and hold it before his face. He gives true answers to all things past, present and future as long as he is asked, but when not answering questions is a liar. He can turn any metal into gold, give dignities and confirm them.']
ghoul = ['Ghoul','Death','9','Ailment','-','-','Ice','-','Fire, Light','img/Ghoul.jpg','Demon of ancient Arabian folklore. The word "ghoul" is Arabic for "demon," referring to creatures who were believed to dwell in graveyards and abandoned places.']
apsaras = ['Apsaras','Temperance','4','Recovery','-','-','-','-','Fire','img/Apsaras.jpg','Apsaras (Sanskrit: अप्सरा) also known as Vidhya Dhari, according to Hindu and Buddhist mythology, are spirits that appear in the form of young, beautiful women who have mastered the fine art of celestial dance. They are the wives of Indras servants, Gandharvas, and are known to entertain the gods and fallen heroes, dancing in the divine palaces to music made by their husbands. They are frequently equated with the water-elemental nymphs and naiads of Ancient Greeks, and depictions of them can be seen in Cambodian and Balinese culture.']
ukobach = ['Ukobach','Devil','3','FIre','-','-','-','Fire','Ice','img/Ukobach.png','A lesser demon of Hell. Ukobach has no free will and will only follow the commands of higher demons. He is in charge of maintaining the oil in the infernal boilers, and will often torture the souls trapped in Hell. Ukobachs only ability is to start fires.']
tao_tie = ['Tao Tie','Tower','35','Almighty','Dark','-','-','-','-','img/Tao_tie.jpg','The Taotie, also known by its Japanese name Toutetsu, is said to be a Chinese monster of unknown origin. It is said that it is a greedy monster with an insatiable appetite, and as punishment, only its head remains. Fear of the monster led its image to be cast on Chinese bronzes and ritual vessels. Along with Taown, Hun Dun and Qiong Qi, it is one of the Four Fiends, prominent Chinese demons representing evil virtues. Tao Tie represents gluttony.']
kaiwan = ['Kaiwan','Star','24','Support','-','-','Dark','-','Physical','img/Kaiwan.jpg','An Astro-Mythological deity in Assyrian mythology. He is associated with the planet Saturn. Kaiwan is also one of the names of Hastur the unspeakable in Lovecraftian lore.']
andras = ['Andras','Moon','20','Recovery','-','-','Electic','-','Wind','img/Andras.jpg','According to the writings in The Lesser Key of Solomon, Andras is the sixty-third spirit listed in the Goetia. He is a Great Marquis of Hell with thirty legions of demons under his command. He is depicted as a humanoid with an angels wings and an owls head, riding a black wolf and holding a bright sword. Among the spirits of the Goetia, Andras is one of the most violent and dangerous to summon. The conjurer and any attendants he may have must stay within a magic circle at all times no matter how much Andras tempts them to leave it, or he will surely kill them. He is able to control a persons anger or inflict rage upon any person the conjurer desires and tempt people to kill their servants or masters. If so asked, Andras will gladly kill any person the conjurer desires, and in certain demonology it is suggested that Flauros is his servant.']
cu_sith = ['Cu Sith','Sun','10','Wind','-','-','-','Wind','Fire','img/Cu_sith.jpg','Cu Sith (pronounced Coo Shee) is a giant otherworldly dog which haunts the Scottish highlands and fairy mounds. It is said to be roughly the size of a horse and have shaggy green fur with a long often braided tail. Cu Sith, though capable of hunting silently, would often let out three terrifying barks, which could be heard over long distances. These three barks would herald the coming of Cu Sith and warn farmers and sailors to lock up their women at night, lest the great hound come and snatch them away to supply milk for the fairy children.']
anubis = ['Anubis','Judgement','59','Light','-','-','Light','-','-','img/Anubis.jpg','Anubis is widely known as the Egyptian deity of mummification. In this role, he oversees the mummification process of the dead, and is usually seen in hieroglyphic tomb-carvings as overseeing the burial ritual for the pharaohs and those of royal lineage - this is due to the priest involved wearing the masks of Anubis to symbolize him as the overseer of the ritual.']
izanagi_no_okami = ['Izanagi-no-Okami','World','91','No','-','-','-','Physical, Fire, Ice, Electic, Wind','-','img/Izanagi_no_okami.jpg','The name "Ōkami", which means "Great Deity", symbolizes Izanagis true identity as the deity born of the seven divine generations in Japanese mythology.']

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

