#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BaseReality import BaseReality
import re
class BaseRules(BaseReality):
	
	def _get_rule_precond(self,i):	
		try:
			return re.match("^(.*)\s?->.*$",self._get_data(i)).groups()[0]
		except TypeError as te:
			print "Error con el parametro a la expresion regular de extraccion de precondicion de una regla"
		except:
			print "Error con la expresion regular"
			
	def _get_rule_effect(self,i):
		try:
			return re.match(".*->\s?(.*)$",self._get_data(i)).groups()[0]
		except TypeError as te:
			print "Error con el parametro a la expresion regular de la accion de precondicion de una regla"
		except:
			print "Error con la expresion regular"
	
	def _extract_set_of_preconditions(self,i):
		return self._get_rule_precond(i).split("^")
	
	def _extract_set_of_postconditions(self,i):
		return self._get_rule_effect(i).split("^")
