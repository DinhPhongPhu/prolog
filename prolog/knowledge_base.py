from rules import Rules
from facts import Facts
from sentence import Sentence

class Knowledge_Base:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_potential_facts(self, rule):        #???
        facts = []
        for i in self.facts:
            if rule.fact_in_rule(i.ops):
                facts.append(i)
        return facts
    
    @staticmethod
    def declare(kb, input):
        while input:
            sent_str, input = Sentence.next(input)
            sent_type = Sentence.classify(sent_str)
            if sent_type == 'fact':
                fact = Facts.parse_fact(sent_str)
                kb.add_fact(fact)
            elif sent_type == 'rule':
                rule = Rules.parse_rule(sent_str)
                kb.add_rule(rule)
    