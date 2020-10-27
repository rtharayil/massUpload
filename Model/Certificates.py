class AllCertificates:
    """All Certificates """
   

    # default constructor 
    def __init__(self):         
        self.allCertificates =[]
        self.template=''


    
    def getAllCertificates(self):
        return self.allCertificates


    def getTemplate(self):
        return self.template


    def setTemplate(self ,template):
        self.template =template
        
class Certificate:

     # default constructor 
    def __init__(self , nameFirst, nameSecond ,email): 

        self.firstName=nameFirst
        self.secondName=nameSecond
        self.email=email
        self.url =""
        self.webURI = ""
        self.fileName=self.genCertFileName()
       

    def Email(self):
        return self.email  



    def getName(self):
        return self.firstName , self.secondName

    def Name(self):
        return self.firstName  + " "+ self.secondName

    def uri(self):
        return self.url

    def getWebURL(self):
        return self.webURI
    
    def set_webURL(self,url):
        self.webURI =url
    
    def set_uri(self,url):
        self.url =url

    def set_fileName(self,fileName):
        self.fileName = fileName

    def get_FileName(self):
        return self.fileName
    
    def genCertFileName(self):
        return  self.firstName.replace(" ", "") + self.secondName.replace(" ", "")