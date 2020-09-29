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
    def __init__(self , name ,email): 

        self.name=name
        self.email=email
       

    def Email(self):
        return self.email  



    def Name(self):
        return self.name