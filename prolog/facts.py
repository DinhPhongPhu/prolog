"""
Fact:   operators: Function or Relation
        arguments: Contrains or Varibles
        negated: A --> -A
"""

class Facts:
    def __init__(self, ops="", args=[], negated=False):
        self.ops = ops
        self.args = args
        self.negated = negated
    
    def __copy__(self):
        return Facts(self.ops, self.args, self.negated)

    def __eq__(self, rhs):      #Compare 2 facts
        if self.ops != rhs.ops: return False
        if self.args != rhs.args: return False
        return self.negated == rhs.negated

    def negate(self):       #Negate a fact
        self.negated = 1 - self.negated
    
    def get_ops(self):
        return self.ops
    
    def get_args(self):
        return self.args

    @staticmethod
    def parse_fact(str_fact):
        str_fact=str_fact.replace(" ","")   #Delete space
        str_fact=str_fact.strip(".")        #Delete dots at the end

        t=str_fact.split("(")
        ops=t[0]
        t2=t[1][:-1]
        args=t2.split(",")

        return Facts(ops,args)

