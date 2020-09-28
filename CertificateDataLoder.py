import os
import csv
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates

class CertificateDataLoder:
    """All Certificates """
   
    # default constructor 
    def __init__(self):  
         self.x=0
    


    def load(self,certificates, inputFileName , email):
        



        with open(inputFileName, 'r') as file:
            reader = csv.reader(file, delimiter = ',')
            for row in reader:
                if email == True :          
                    certificates.append(Certificate( row[1].strip() + " " + row[2].strip(),row[3].strip()))
                else :
                    certificates.append(Certificate( row[1].strip() + " " + row[2].strip(),'NoEmail'))
    
                
        certificates.pop(0)
     
        


