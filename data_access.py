import urllib.request, json
from info import Info
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db =  client.visualizador_app
collection = db.dados_outorga

def getOutorgaJSON():
	with urllib.request.urlopen("http://www.aneel.gov.br/dados/relatorios?p_p_id=dadosabertos_WAR_dadosabertosportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=gerarGeracaoDistribuidaJSON&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=1") as url:
		data = json.loads(url.read().decode('latin-1'))
		#for i in range(len(data)):
		#	info = Info(data[i]['ideGeracaoDistribuida'], data[i]['nomGeracaoDistribuida'], str(data[i]['mesReferencia']) + '-' + str(data[i]['anoReferencia']), data[i]['mdaPotenciaInstaladakW'], data[i]['dthProcessamento'])
		#	Infos.append(info)
		return data#Infos

def upsertOutorgaInfo():
	collection = db.dados_outorga
	documents = getOutorgaJSON()
	for document in documents:
		collection.update_one({"ideGeracaoDistribuida":document["ideGeracaoDistribuida"]}, {'$set':document}, True)

def getOutorgas():
	collection = db.dados_outorga
	documents = collection.find()
	infosOutorgas = []
	for document in documents:
		outorga = Info(document['ideGeracaoDistribuida'], document['nomGeracaoDistribuida'], str(document['mesReferencia']) + '-' + str(document['anoReferencia']), document['mdaPotenciaInstaladakW'], document['dthProcessamento'])
	return infosOutorgas	




