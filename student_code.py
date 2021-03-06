import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB
        
        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if fact.name == "fact" and (not self.facts or self.kb_ask(fact)):
            self.facts.append(fact)
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        binding = []
        for i in self.facts:
            match_res = match(fact.statement, i.statement, None)
            if match_res != 0:
                binding.append(match_res)

        return False if not binding else binding