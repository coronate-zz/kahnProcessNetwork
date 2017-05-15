

class Node:
	function ="Some function"
	Desc=list()
	Asc=list()
	salidaFlag=False
	inicioFlag=False
	activacionFlag=False
	estado = 0
	nodoAux=None
	outputFlag=False


	def crearDesc( self, otherNode ):
		self.Desc.append(otherNode)

	def crearAsc(self, otherNode ):
		self.Asc.append(otherNode)

	def primerNodo(self):
		self.inicioFlag=True
		self.activacionFlag=True
		self.crearAsc('Inicio')

	def salidaNodo(self):
		self.salidaFlag=True
		self.activacionFlag=False

class FuncionClass(Node):

    def __init__(self, name, tipo):
        self.name = name
        self.input=None
        self.output=None
        self.tipo=tipo
        self.Desc=list()
        self.Asc=list()


    def operar(self):
    	if self.tipo=='Append':
    		print('{} Generando Append'. format(self.name))
    		if (self.input==None):
    			print('ERROR no input')
    		else:
    			self.output=self.input
    			self.output.append('--//--')
    			print('\t{}:  Output intermedio {}'.format(self.name, self.output))
    			self.outputFlag=True
    			if self.salidaFlag==True:
    				print('\t\t ------>{}:  Output SALIDA {}'.format(self.name, self.output))
    			print('\n')

    	elif self.tipo == 'First':
    		print('{} Generando First'. format(self.name))
    		if (self.input==None):
    			print('ERROR no input')
    		else:
    			self.output=self.input[0]
    			print('\t{}:  Output intermedio {}'.format(self.name, self.output))
    			self.outputFlag=True
    			if self.salidaFlag==True:
    				print('\n\t\t ------>{}:  Output SALIDA {}\n'.format(self.name, self.output))
    			print('\n')

    	elif self.tipo == 'Remainder':
    		print('{} Generando Remainder'. format(self.name))
    		if (self.input==None):
    			print('ERROR no input')
    		else:
    			self.output=self.input[1:]
    			print('\t{}:  Output intermedio {}'.format(self.name))
    			self.outputFlag=True
    			if self.salidaFlag==True:
    				print('\n\t\t ------>{}:  Output SALIDA {}\n'.format(self.name, self.output))
    			print('\n')

    	else:
    		print('ERROR')

    def insertInput(self, newInput):
    	self.input= newInput



try:
	del nodo1
except Exception:
	pass
try:
	del nodo2
except Exception:
	pass
try:
	del nodo3
except Exception:
	pass




prueba=FuncionClass('prueba','Append')


prueba.name

lista=['uno', 2, 3, 'catorce']

prueba.insertInput(lista)



nodo1=FuncionClass('nodo1', 'First')
nodo1.primerNodo()


nodo2=FuncionClass('nodo2', 'First')
nodo2.salidaNodo()

nodo3=FuncionClass('nodo3', 'First')


nodo1.crearDesc(nodo2)
nodo2.crearDesc(nodo3)
nodo3.crearDesc(nodo1)

nodo1.crearAsc(nodo3)
nodo2.crearAsc(nodo1)
nodo3.crearAsc(nodo2)



sistema=[nodo1, nodo2, nodo3]


listaPrograma=[['uno',2, 3, 'catorce'],['Hello World', 1234, 'ACN'],['Pink Floyd', 'Black Sabbath', 'Led Zeppeli' ]]




#------------------- Program Execution -------------------



for i in range(1,10):
	elemento=listaPrograma[0]
	print (listaPrograma)
	print('')
	for nodo in sistema:
		#Primero creamos un nodo auxuliar para alterar los elementos de nodo
		#y al final regresamos pasamos lo cambios nodoAux->nodo
		nodo.nodoAux=nodo

		print('Nodo: {} '.format(nodo.name))
		if nodo.activacionFlag== True and nodo.inicioFlag==True and nodo.estado == 0:
			print('---------------------------------------------------------')
			print('Nodo Inicial Recibiendo elemento: {} '.format(elemento))
			print('---------------------------------------------------------')
			nodo.input=elemento
			nodo.nodoAux.operar()
			nodo.nodoAux.estado=(nodo.estado+1)%len(nodo.Asc)
			nodo.activacionFlag=False
			nodo.nodoAux.activacionFlag=False
			#print('******************{}'.format(nodo.nodoAux.estado))

		elif nodo.input!=None and nodo.activacionFlag==True:
			print('Se han generado resultados...')
			nodo.operar()


		for nodoDesc in nodo.Desc:
			print('\t\t**nodoDesc name: {}'.format(nodoDesc.name))
			print('\t\t**nodoDesc estado: {}'.format(nodoDesc.estado))
			
			try: 
				print('\t\t\tFirst try: estado=Inicio  {}'.format(nodoDesc.Asc[nodoDesc.estado]=='Inicio'))
				print('\t\t\t-------')	
			except Exception:
				print('\t\t\tNO INICIO')

			try:
			 	if  nodoDesc.Asc[nodoDesc.estado].name==nodo.name and nodo.outputFlag==True:
					nodoDesc.nodoAux.input=nodo.output
					nodoDesc.nodoAux.activacionFlag=True
					nodoDesc.nodoAux.estado=(nodoDesc.estado+1)%len(nodoDesc.Asc)
					print('\t\t\tnodoDesc.nodoAux.estado: {}'.format(nodoDesc.nodoAux.estado))
				else:
					print('\t\t\tEl estado no coincide o no esta listo...')

			except Exception:
				print('\t\t\tNodo no contine informacion en Asc')
			
	
	for nodo in sistema:
		nodo=nodo.nodoAux
		print('\n\t***CHECK Name: {}   Estado: {}   \n\tInput: {}   Output: {}   '.format(nodo.name, nodo.estado, nodo.input, nodo.output))	
	#Borramos de la lista para no repetir elelemntos

	if nodo1.activacionFlag==True:
		del listaPrograma[0]
		try:
			print(listaPrograma[0])
		except Exception:
			break




try:
  doSomething()
except Exception: 
  pass
