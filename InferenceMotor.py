#!/usr/bin/env python
# -*- coding: utf-8 -*-  

class InferenceMotor(object):
	
	def __init__(self):
		## Test de prueba: problema de las jarras de agua -> Jarra X, capacidad 4L, JarraY, capacidad 3L ##
		self.initial_facts = ["(contents 0 0)"]
		self.rules = ["(contents ?x ?y) ^ (?x < 4) -> (contents 4 ?y)",
					  "(contents ?x ?y) ^ (?y < 3) -> (contents ?x 3)",
					  "(contents ?x ?y) ^ (?x > 0) -> (contents 0 ?y)",
					  "(contents ?x ?y) ^ (?y > 0) -> (contents ?x 0)",
					  "(contents ?x ?y) ^ (?x < 4) ^ (?y > 0) ^ ((?x + ?y) >= 4) -> (contents 4 (?y - (4 - ?x))"]
		self.objective_facts = ["(contents 4 0)"]
		self.facts_database = BaseFacts(self.initial_facts)
		self.rules_database = BaseRules(self.rules)
		self.__init_inference_process()
	
	def __init_inference_process(self):
		while(self.__is_objective_fact_in_visited() or self.facts_database._all_visited()):
			pass
			# Pattern matching entre los estados no visitados y las precondiciones de las reglas de la BR #
			# Ejecutar todas las reglas de la BR (de momento estas reglas solo anyaden estados #
		#End while
	
	def __is_objective_fact_in_visited(self):
		for x in self.objective_facts: 
			if x in self.facts_database._is_fact_visited(x): return True
		return False
		

