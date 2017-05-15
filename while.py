while len(listaPrograma) != 0:
	elemento=listaPrograma[0]
	print (listaPrograma)
	print('')
	for nodo in sistema:
		print('Nodo: {} '.format(nodo.name))
		if nodo.activacionFlag== True and nodo.inicioFlag==True and nodo.estado == 0:
			print('Nodo Inicial Recibiendo elemento: {} '.format(elemento))
			nodo.input=elemento
			nodo.operar()


		elif nodo.input!=None and nodo.activacionFlag==True:
			print('Se han generado resultados...')
			nodo.operar()


		for nodoDesc in nodo.Desc:
			print('nodoDesc name: {}'.format(nodoDesc.name))
			print('nodoDesc estado: {}'.format(nodoDesc.estado))
			print('nodoDesc.Asc[nodoDesc.estado]:  {}'.format( nodoDesc.Asc[nodoDesc.estado].name ))
			if nodoDesc.Asc[nodoDesc.estado]=='Inicio':
				print('-------')
			elif nodoDesc.Asc[nodoDesc.estado].name==nodo.name:
				nodoDesc.nodoAux.input=nodo.output
				nodoDesc.nodoAux.activacionFlag=True
				nodoDesc.nodoAux.estado=(nodoDesc.estado+1)%(len(nodoDesc.Asc)+1)
				print('nodoDesc.nodoAux.estado: {}'.format(nodoDesc.nodoAux.estado))

	for nodo in sistema:
		nodo=nodo.nodoAux


	del listaPrograma[0]

