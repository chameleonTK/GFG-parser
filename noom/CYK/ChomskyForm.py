from noom import Production

class ChomskyForm:
	def __init__(self,debug = False):
		self.debug = debug


	def findNullable(self,grammar):
		production = grammar.production
		nullable = set()
		prodLen = len(production)
		checked = [False for i in range(prodLen)]

		isPass = False
		while (not isPass) :
			isPass = True
			
			for i in range(prodLen):
				if checked[i]:
					continue

				if production[i].isEpsilon():
					checked[i]=True
					nullable.add(production[i].left)
					isPass = False
				else:
					if production[i].left in nullable:
						checked[i] = True

					isNullable = True
					for ele in production[i].right:
						if ele not in nullable:
							isNullable = False
							break

					if isNullable:
						nullable.add(production[i].left)
						isPass = False
						checked[i]=True
		return nullable

	def generatePossibleProd(self,grammar,nullable):
		newProd = {}
		for non in grammar.nonterminal:
			newProd[non] = set()
		index = self.indexing(grammar)

		for prod in grammar.production:
			newRight = [ "" ]
			for r in prod.right:
				length = len(newRight)
				if r in nullable:

					if len(index[r]) == 1:
						continue

					for i in range(length):
						newRight.append( newRight[i]+" "+r)
				else:
					
					for i in range(length):
						newRight[i] = newRight[i]+" "+r

			for n in newRight:
				n = n.strip() 
				if n=="":
					continue
				newProd[prod.left].add(n)

		return newProd

	def removeEpsilon(self,grammar):
		nullable = self.findNullable(grammar)
		newProd = self.generatePossibleProd(grammar,nullable)

		production = []
		for k in newProd:
			for r in newProd[k]:
				p = Production.Production(k,r,None)		
				production.append(p)

		grammar.production = production
		return grammar

	def initDerivable(self,grammar):
		derivable = {}

		for non in grammar.nonterminal:
			derivable[non] = set()
		
		
		for prod in grammar.production:
			if len(prod.right) == 1 and grammar.isNonTerminal( prod.right[0]):
				derivable[prod.left].add(prod.right[0])

		isPass = False
		while not isPass:
			isPass = True
			for k in derivable:
				tmp = list(derivable[k])
				for v in tmp:
					for x in derivable[v]:
						if x not in derivable[k]:
							derivable[k].add(x)
							isPass = False

		return derivable

	def removeOriginalUnitProd(self,grammar):
		i = 0
		removeIndex = []
		for prod in grammar.production:
			if len(prod.right) == 1 and grammar.isNonTerminal( prod.right[0]):
				removeIndex.append(i)
			i+=1

		for i in range(len(removeIndex)-1,-1,-1):
			p = grammar.production.pop(removeIndex[i])

	def indexing(self,grammar):
		index = {}
		for non in grammar.nonterminal:
			index[non] = []
		
		for prod in grammar.production:
			index[prod.left].append(prod)
		return index

	def removeUnitProduction(self,grammar):
		derivable = self.initDerivable(grammar)
		self.removeOriginalUnitProd(grammar)

		index = self.indexing(grammar)

		for k in derivable:
			for v in derivable[k]:
				for pro in index[v]:
					r = " ".join(pro.right)
					p = Production.Production(k,r,None)
					grammar.production.append(p)

		return grammar

	def removeUselessSymbol(self,grammar):
		return grammar

	def extractProduction(self,grammar):

		for nt in grammar.nonterminal:
			if nt.startswith("tmp"):
				raise Exception("Terminal must not begin with 'tmp'. Please change it.")

		tmpIndex = 1
		production = []
		nonterminal = list(grammar.nonterminal)

		for prod in grammar.production:
			prev = prod.left
			if self.debug:
				print prod

			for i in range(len(prod.right)-1):
				if i == len(prod.right)-2:
					var1, var2 = prod.right[i], prod.right[i+1]
				else:
					var1, var2 = prod.right[i], "tmp"+str(tmpIndex) 
					nonterminal.append("tmp"+str(tmpIndex) )

				if grammar.isTerminal(var1):
					var1 = "tmp"+var1

				if grammar.isTerminal(var2):
					var2 = "tmp"+var2


				p = Production.Production(prev,var1+" "+var2,None)
				production.append(p)
				if self.debug:
					print prev," -> ",var1,var2

				prev = "tmp"+str(tmpIndex)
				tmpIndex+=1

			if len(prod.right)==1:
				var1 = prod.right[0]
				if grammar.isTerminal(var1):
					p = Production.Production(prod.left,var1,None)
					production.append(p)
					if self.debug:
						print prod.left," -> ",var1
						
			if self.debug:
				print "============"

		for t in grammar.terminal:
			nonterminal.append( "tmp"+t )
			p = Production.Production("tmp"+t ,t,None)
			production.append(p)

		grammar.production = production
		grammar.nonterminal = set(nonterminal)

		return grammar

	def toCNF(self,grammar):
		s1 = self.removeEpsilon(grammar)
		s2 = self.removeUnitProduction(s1)
		#s3 = self.removeUselessSymbol(s2)
		s3 = self.extractProduction(s2)
		return s3

	def toNonEpsilon(self,grammar):
		s1 = self.removeEpsilon(grammar)
		return s1