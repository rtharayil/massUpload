class Advertisement:
    """A simple advertisement class"""
   

    # default constructor 
    def __init__(self): 
        
        self.message =''
        self.logo =''
        self.banner = ''
        self.CTALink=''
        self.CTALMessage=''
        self.phone= ''
        self.email =''
        self.webLink =''
        self.bLabel =''

  

    def setMessage(self ,message):
        self.message = message 


    def setLogo(self,logo):
        self.logo = logo

    def setBanner(self,banner):
        self.banner = banner

    def setCTALink(self,link):
        self.CTALink = link

    def setCTAMessage(self,message):
        self.CTALMessage= message
    
    def setPhone(self,number):
        self.phone= number

    def setEmail(self ,email):
        self.email = email

    def setWebLink(self,link):
        self.webLink = link

    def setButtonLabel(self,link):
        self.bLabel = link


        
    def getMessage(self):
        return self.message  
    
    def getLogo(self):
        return self.logo

    def getBanner(self):
        return self.banner
    
    def getCTALink(self):
        return self.CTALink

    def getCTAMessage(self):
        return self.CTALMessage

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    def getWebLink(self):
        return self.webLink

    def getButtonLabel(self):
        return self.bLabel