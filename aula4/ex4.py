class Sensor():
	def __init__(self,temperatura):
		self.__temperatura = temperatura
	def set_temperatura(self):
		if -50 <= temperatura <= 150:
			self.__temperatura = temperatura
		else:
			print("Valor inválido")
	def status(self):
		if -50 <= self.__temperatura <= 80:
			print("Normal")
		elif 81 <= self.__temperatura <= 120:
			print("Alerta")
		else:
			print("Crítico")
temp1 = Sensor(65)
temp2 = Sensor(90)
temp3 = Sensor(-45)
temp4 = Sensor(145)
temp1.status()
temp2.status()
temp3.status()
temp4.status()
