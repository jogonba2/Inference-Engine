#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BaseRules import BaseRules
import re
class PatternMatching:
	
	@staticmethod
	def _pattern_matching(fact,i,rules_database):
		## Extracts values of fact (0 -> name of fact, 1..n -> value ##
		name_fact      = PatternMatching._extract_name_of_data(fact).strip()
		values_fact    = PatternMatching._extract_values_of_data(fact).split(",")
		## Extracts declaration of fact in rule ##
		preconditions  = rules_database._extract_set_of_preconditions(i)
		postconditions = rules_database._extract_set_of_postconditions(i)
		name_rule      = PatternMatching._extract_name_of_data(preconditions[0]).strip()
		variables_rule = PatternMatching._extract_values_of_data(preconditions[0]).split(",")
		## Make associations ##
		association_dict = {}
		if(name_fact==name_rule and len(values_fact)==len(variables_rule)):
			for x in xrange(0,len(variables_rule)):
				association_dict[variables_rule[x]] = values_fact[x]
		## Replace associations in the rest of preconditions ##
		for x in xrange(1,len(preconditions)):
			for key in association_dict.keys(): preconditions[x] = preconditions[x].replace(key,association_dict[key])
		for x in xrange(0,len(postconditions)):
			for key in association_dict.keys(): postconditions[x] = postconditions[x].replace(key,association_dict[key])
		return [preconditions[1:],postconditions]
		
		
	@staticmethod
	def _extract_name_of_data(data):
		return re.match("\((.*)\s?\((.*)\)\)",data.strip()).groups()[0]
	
	@staticmethod
	def _extract_values_of_data(data):
		return re.match("\((.*)\s?\((.*)\)\)",data.strip()).groups()[1]
		
		
		

#br = BaseRules(["(contents (?x,?y)) ^ (?x   < 4) -> (contents (4,?y))"])
#PatternMatching._pattern_matching("(contents(5,0))",0,br)
		
		



