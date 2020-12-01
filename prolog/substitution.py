class Subtitution:
    def __init__(self):
        self.mappings = dict()
    
    def __eq__(self, rhs):
        return self.mappings == rhs.mappings

    def empty(self):
        return len(self.mappings == 0)
    
    def contain(self, varialble):
        return varialble in self.mappings
    
    #def __hash__(self):

    def subtitute_of(self, var):
        return self.mappings[var]
    
    
    
