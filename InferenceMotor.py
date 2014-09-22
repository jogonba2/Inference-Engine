#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from BaseRules import BaseRules
from BaseFacts import BaseFacts
from PatternMatching import PatternMatching
""""""
class InferenceMotor(object):
	
	def __init__(self):
		## Test: water jug problem -> Jug X, init contents 0, Jug Y, init contents 0 ##
		self.initial_facts  = ["(contents (0,0))"]
		## View syntax in the rules set ##
		self.rules = ["(contents (?x,?y)) ^ (?x < 4) -> (contents (4,?y))",
					  "(contents (?x,?y)) ^ (?y < 3) -> (contents (?x,3))",
					  "(contents (?x,?y)) ^ (?x > 0) -> (contents (0,?y))",
					  "(contents (?x,?y)) ^ (?y > 0) -> (contents (?x,0))",
					  "(contents (?x,?y)) ^ (?x < 4) ^ (?y > 0) ^ (?x + ?y >= 4) -> (contents (4,?y-4-?x))",
					  "(contents (?x,?y)) ^ (?y < 3) ^ (?x > 0) ^ (?x + ?y >= 3) -> (contents (?x-?y-3,3))",
					  "(contents (?x,?y)) ^ (?x + ?y <= 4) ^ (?y > 0) -> (contents (?x+?y,0))",
					  "(contents (?x,?y)) ^ (?x + ?y <= 3) ^ (?x > 0) -> (contents (0,?x+?y))"] 
		self.objective_facts = ["(contents (4,3))"] 
		self.problem_name    = "WaterJugProblem"
		self.facts_database  = BaseFacts(self.initial_facts)
		self.rules_database  = BaseRules(self.rules)
		## For debug purposes ##
		self.rules_database._set_son(BaseRules)
		self.facts_database._set_son(BaseFacts)
		########################
		print "[+] Initialising process with facts and rules stablished...\n"
		self.__init_inference_process()
		print "[+] End process, please review the report :)\n"
	
	def __init_inference_process(self):
		with open(self.problem_name,"w") as fd:
			founded = False
			while(self.facts_database._get_not_visited()!=[]):
				for not_visited in self.facts_database._get_not_visited():
					if(self.__is_objective_fact_in_visited()==True): founded = True; break;
					for x in xrange(0,len(self.rules_database._get_database())):
						fd.write("Applying to: " + not_visited + " rule: " + self.rules_database._get_data(x) + "\n")
						try: pattern_matching = PatternMatching._pattern_matching(not_visited,x,self.rules_database);
						except AttributeError as ae: fd.write("\nMatching not done for this fact-rule please revise syntax\n"+
															  "\n\n---------------------------------------------------\n\n"); continue;
						fd.write("Matching done: " + str(pattern_matching[0]) + "\nTesting if is acumplished: ")
						apply_effect = True
						for precondition in pattern_matching[0]:
							try: 
								if eval(precondition) == False: apply_effect = False; break;
							except SyntaxError as se: apply_effect = False
						if apply_effect:
							for postcondition in pattern_matching[1]:
								effect = PatternMatching._evaluate_postcondition(postcondition).strip()
								fd.write(effect+"\n")
								if self.facts_database._exists_data(effect) == False: self.facts_database._add_data(effect);
						else: fd.write("No rule cumplishment\n")
						fd.write("\n\n---------------------------------------------------\n\n"	)
					self.facts_database._add_visited(not_visited)
				if(founded): break;
			if(founded): fd.write("Process correctly executed, status have been reached :)"); 
			else:        fd.write("Process not correctly executed, status have not been reached :(");
		fd.close()		
		#End while
	
	def __is_objective_fact_in_visited(self):
		for x in self.objective_facts: 
			if self.facts_database._is_fact_visited(x): return True
		return False
		

InferenceMotor()
