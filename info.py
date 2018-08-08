class Info:
	def __init__(self, id, nameDist, dataRef, potenciaInstalada, dateTime):
		self.id = id
		self.nomeDist = nameDist
		self.dataRef = dataRef
		self.potenciaInstalada = potenciaInstalada
		self.dateTime = dateTime

	def __str__(self):
		return 'id: ' + str(self.id) + '\nGeracao Distribuida:' + self.nomeDist + '\nData referencia:' + self.dataRef + '\nPontencia instalada:' + self.potenciaInstalada + '\nData de processamento:' + self.dateTime