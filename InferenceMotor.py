#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from BaseRules import BaseRules
from BaseFacts import BaseFacts
from PatternMatching import PatternMatching
""""""
class InferenceMotor(object):
	
	def __init__(self):
		## Test de prueba: problema de las jarras de agua -> Jarra X, capacidad 4L, JarraY, capacidad 3L ##
		self.initial_facts = ["(contents (0,0))"]
		## Respetar espacios entre operaciones, cuidado con la sintaxis ##
		self.rules = ["(contents (?x,?y)) ^ (?x < 4) -> (contents (4,?y))",
					  "(contents (?x,?y)) ^ (?y < 3) -> (contents (?x,3))",
					  "(contents (?x,?y)) ^ (?x > 0) -> (contents (0,?y))",
					  "(contents (?x,?y)) ^ (?y > 0) -> (contents (?x,0))",
					  "(contents (?x,?y)) ^ (?x < 4) ^ (?y > 0) ^ (?x + ?y >= 4) -> (contents (4,?y-4-?x))",
					  "(contents (?x,?y)) ^ (?y < 3) ^ (?x > 0) ^ (?x + ?y >= 3) -> (contents (?y-3-?x,3))",
					  "(contents (?x,?y)) ^ (?x + ?y <= 4) ^ (?y > 0) -> (contents (?x+?y,0))"]
					  #"(contents (?x ?y)) ^ (?x + ?y <= 3) ^ (?x > 0) -> (contents (0,?x+?y))"] 
		self.objective_facts = ["(contents (2,2))"]
		self.facts_database = BaseFacts(self.initial_facts)
		self.rules_database = BaseRules(self.rules)
		## For debug purposes ##
		self.rules_database._set_son(BaseRules)
		self.facts_database._set_son(BaseFacts)
		########################
		self.__init_inference_process()
	
	def __init_inference_process(self):
		while(self.__is_objective_fact_in_visited()==False and self.facts_database._all_visited()==False):
			for not_visited in self.facts_database._get_not_visited():
				print self.facts_database._get_not_visited()
				print "-----------------------------------------"
				for x in xrange(0,len(self.rules_database._get_database())):
					# Pattern matching entre los estados no visitados y las precondiciones de las reglas de la BR #
					applicate_action = True
					pattern_matching = PatternMatching._pattern_matching(not_visited,x,self.rules_database)
					for precondition in pattern_matching[0]:
						if eval(precondition)==False: applicate_action = False
					if applicate_action:
						for x in pattern_matching[1]: 
							print eval(PatternMatching._extract_values_of_data(x))
							if self.facts_database._exists_data(x)==False: 
								self.facts_database._add_data(x)
						# Ejecutar todas las reglas de la BR (de momento estas reglas solo anyaden estados) #
					self.facts_database._add_visited(not_visited)
					
		if(self.__is_objective_fact_in_visited()): print "Proceso correcto, se alcanza el estado"
			
		#End while
	
	def __is_objective_fact_in_visited(self):
		for x in self.objective_facts: 
			if self.facts_database._is_fact_visited(x): return True
		return False
		

InferenceMotor()
