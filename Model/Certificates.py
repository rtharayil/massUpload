class AllCertificates:
    """All Certificates """
   

    # default constructor 
    def __init__(self):         
        self.allCertificates =[]
        self.QRPosX =0
        self.QRPosY =0

        self.NamePosX =0
        self.NamePosY =0

    
       
    def setQRCodeLocation(self,x,y):
        self.QRPosX =x
        self.QRPosY =y

    def setNameLocation(self,x,y):
        self.NamePosX =x
        self.NamePosY =y

    def getNameLocation(self):
        return self.NamePosX , self.NamePosY 

    def getQRCodeLocation(self):
        return self.QRPosX , self.QRPosY 
    
    def getAllCertificates(self):
        return self.allCertificates

class Certificate:

     # default constructor 
    def __init__(self , name ,email): 

        self.name=name
        self.email=email
       

    def Email(self):
        return self.email  



    def Name(self):
        return self.name