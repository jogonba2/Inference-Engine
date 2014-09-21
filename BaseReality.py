#!/usr/bin/env python
class BaseReality:
	
	def __init__(self,data_base):
		self.database = data_base
		self.type_son = None
	
	
	def _get_database(self): return self.database
	def _set_son(self,obj): self.type_son = obj

	def _get_data(self,i):
		try:
			return self.database[i]
		except IndexError as ie:
			if "BaseRules" in str(self.type_son): print "Index of the rule is not valid !"
			else: print "Index of the fact is not valid !"
			
	def _del_data_by_index(self,i):
		try:
			self.database.pop(i)
		except IndexError as ie:
			if "BaseRules" in str(self.type_son): print "Index of the rule is not valid !"
			else: print "Index of the fact is not valid !"
	
	def _del_data_by_data(self,fact):
		try:
			self.database.pop(self._get_index_of_fact(fact))
		except ValueError as ve:
			if "BaseRules" in str(self.type_son): print "Rule is not in the rules list !"
			else: print "Fact is not in the facts list !"
			
		
	def _add_data(self,fact):
		self.database.append(fact)
	
	def _get_index_of_data(self,fact):
		try:
			return self.database.index(fact)
		except ValueError as ve:
			if "BaseRules" in str(self.type_son): print "Rule is not in the rules list !"
			else: print "Fact is not in the facts list !"
			
	def __str__(self):
		return "\n".join([str(x) + " -> " + self.database[x] for x in xrange(0,len(self.database))])
