class AnEvent:
    """A simple example class"""
   

    # default constructor 
    def __init__(self): 
        self.programName =''
        self.issuedBy = ''
        self.institution=''
        self.date =''
        self.text =''


    def setProgram(self ,programe):
        self.programName = programe
    
    def setIssuer(self,issuedBy):
        self.issuedBy = issuedBy

    def setInstitution(self,institution):
        self.institution =institution

    def setDate(self ,date):
        self.date = date 

    def setText(self ,text):
        self.text = text 

       
    def getProgram(self):
        return self.programName
    
    def getIssuer(self):
        return self.issuedBy

    def getInstitution(self):
        return self.institution

    def getDate(self):
        return self.date

    def getText(self):
        return self.text 


    