class AllCertificates:
    """All Certificates """
   

    # default constructor 
    def __init__(self):         
        self.allCertificates =[]
       


    
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