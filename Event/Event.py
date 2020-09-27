class AnEvent:
    """A simple example class"""
    programName =' '
    issuedBy = ''

    # default constructor 
    def __init__(self,programe,issuedBy): 
        self.programName = programe
        self.issuedBy =issuedBy
       
    def getProgram(self):
        return self.programName
    
    def getIssuer(self):
        return self.issuedBy