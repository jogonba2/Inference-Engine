#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BaseReality import BaseReality
class BaseFacts(BaseReality):
	
	visited_facts = []
		
	def _all_visited(self):
		return len(self.visited_facts)==len(self.database)
	
	def _is_fact_visited(self,fact):
		if fact in self.visited_facts:
			return True
		return False
	
	def _get_not_visited(self):
		return [x for x in self.database if x not in self.visited_facts]
		
	def _add_visited(self,fact):
		self.visited_facts.append(fact)
