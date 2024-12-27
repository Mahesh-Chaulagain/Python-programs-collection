class Math:
    @staticmethod  #means not changing , do not have access to the instance, does not change anything
    def add5(x):
        return x + 5
    
    @staticmethod
    def pr():
        print("run")
    
Math.pr()
    
