#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BaseReality import BaseReality
class BaseRules(BaseReality):
	
	def _get_rule_precond(self,i):
		import re
		try:
			return re.match("^(.*)\s?->.*$",self._get_data(i)).groups()[0]
		except TypeError as te:
			print "Error con el parametro a la expresion regular de extraccion de precondicion de una regla"
		except:
			print "Error con la expresion regular"
			
	def _get_rule_effect(self,i):
		import re
		try:
			return re.match(".*->\s?(.*)$",self._get_data(i)).groups()[0]
		except TypeError as te:
			print "Error con el parametro a la expresion regular de la accion de precondicion de una regla"
		except:
			print "Error con la expresion regular"
	
	def _extract_set_of_preconditions(self,i):
		return self._get_rule_precond(i).split("^")
	
	
# in a rule			
#br = BaseRules(["(contents ?x ?y) ^ (?x < 4) -> (contents 4 ?y)","contents(?x ?y) ^ (?y < 3) -> contents(?x 3)"])
## For debug purposes ##
#br._set_son(BaseRules)
###########################
#print br._get_rule_precond(0)
#print br._extract_set_of_preconditions(0)

