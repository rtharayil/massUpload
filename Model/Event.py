class AnEvent:
    """A simple example class"""
   

    # default constructor 
    def __init__(self): 
        self.programName =''
        self.issuedBy = ''
        self.institution=''
        self.date =''
        self.text =''
        self.code =''


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

    def setEventCode(self ,code):
        self.code = code 

       
    def getProgram(self):
        return self.programName

    def getEventCode(self):
        return self.code
    
    def getIssuer(self):
        return self.issuedBy

    def getInstitution(self):
        return self.institution

    def getDate(self):
        return self.date

    def getText(self):
        return self.text 


    