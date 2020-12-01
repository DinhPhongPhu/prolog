from facts import Facts

"""
Rules:  conclusion: is a Fact
        premises: a list of facts
"""
class Rules:
    def __init__(self, conclusion = Facts(), premises = []):
        self.conclusion = conclusion
        self.premises = premises

        self.duplicate = self.detect_duplicate()
        self.ops = self.get_ops()       #Get a set of facts
        

    def copy(self):
        return Rules(self.conclusion.copy(), self.premises.copy())
    
    def count_premises(self):
        return len(self.premises)

    def detect_duplicate(self):     #duplicate fact
        count=self.count_premises()
        for i in range (0,count-1):
            if self.premises[i].ops==self.premises[i+1].ops: return True
        return False

    def get_ops(self):
        ops = set()
        for i in self.premises:
            ops.add(self.premises.ops)
        return ops

    def fact_in_rule(self, fact):
        return fact in self.ops
    
    @staticmethod
    def parse_rule(str_rule):
        str_rule=str_rule.replace(" ","")   #Delete space
        str_rule=str_rule.strip(".")        #Delete dots at the end

        arr1=str_rule.split(":-")

        conclusion = Facts.parse_fact(arr1[0])

        s=arr1[1]
        premises=[]

        while(s.find(")")!=len(s)-1):
            idx=s.find(")")
            temp=s[:idx+1]
            s=s[idx+2:]
            temp_fact=Facts.parse_fact(temp)
            premises.append(temp_fact)
        
        temp_fact=Facts.parse_fact(s)
        premises.append(temp_fact)

        return Rules(conclusion, premises)
