import unittest
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
from CertificateDataLoder import CertificateDataLoder
from ConfigurationLoader import ConfigurationLoader
from Model.Event import AnEvent
from AuthorCertificate import AuthorCertificate
from Model.Ad import Advertisement

class test_ConfigurationLoader(unittest.TestCase):

    def setUp(self):
        self.allCertificates = AllCertificates()
        self.certificateDataLoder = CertificateDataLoder()
        self.event = AnEvent()
        self.allCertificates = AllCertificates()
        self.issue = AuthorCertificate()
        self.ad = Advertisement()
        self.configurationLoader = ConfigurationLoader(self.event,self.allCertificates,self.issue,self.ad)

        
        self.f = open('config.yaml', "w")
        self.f.write("Program : XP2020" +"\n")  
        self.f.write("IssuedBy : Anju M Dominic" +"\n") 
        self.f.write("Institution : Quadralogics" +"\n") 
        self.f.write("Date : 29 dec 1982" +"\n") 
        self.f.write("Text : A write-up about the event" +"\n") 
        self.f.write("Template : ./AnuMDominicnew.png" +"\n") 
        self.f.write("Logo : ./logo.png" +"\n")
        self.f.write("Message : As your organizations progresses through its DevXOps journey, what are the best practices that successful teams use that you should follow? Discover what separates successful DevXOps teams from those that fail, and learn the next steps to take on your DevXOps journey" +"\n")
        self.f.write("Banner : ./banner.png" +"\n")
        self.f.write("CTAMessage : Download our E-Book to learn more" +"\n")
        self.f.write("CTALink : www.q.com" +"\n")
        self.f.write("Phone : 898654423" +"\n")
        self.f.write("Email : a@p.com" +"\n")
        self.f.write("WebLink : www.qt.com" +"\n")
        self.f.write("Font : ./res/AngelicaCaroline.ttf" +"\n")
        self.f.write("FontSize : 100"+"\n")
        self.f.write("NameX : 150"+"\n")
        self.f.write("NameY : 160"+"\n")
        self.f.write("QRCodeX : 1500"+"\n")
        self.f.write("QRCodeY : 1600"+"\n")
        self.f.write("QRCodeFrontColor : white"+"\n")
        self.f.write("QRCodeBackColor : black"+"\n")
        self.f.write("QRCodeSize : 10"+"\n")
        self.f.close()  
        self.configurationLoader.loadConfig("config.yaml")      


        

    def test_loadConfig_EventName(self):        
       
        self.assertEqual('XP2020',self.event.getProgram())

    def test_loadConfig_issuedBy(self):        
        
        self.assertEqual('Anju M Dominic',self.event.getIssuer())

    def test_loadConfig_institution(self):        
        
        self.assertEqual('Quadralogics',self.event.getInstitution())
    
    def test_loadConfig_date(self):        
        
        self.assertEqual('29 dec 1982',self.event.getDate())
    
    def test_loadConfig_text(self):        
        
        self.assertEqual('A write-up about the event',self.event.getText())

    def test_loadConfig_template(self):        
        
        self.assertEqual('./AnuMDominicnew.png',self.allCertificates.getTemplate())

    def test_loadConfig_logo(self):        
        
        self.assertEqual('./logo.png',self.ad.getLogo())


    def test_loadConfig_Message(self):        
        
        self.assertEqual('As your organizations progresses through its DevXOps journey, what are the best practices that successful teams use that you should follow? Discover what separates successful DevXOps teams from those that fail, and learn the next steps to take on your DevXOps journey',self.ad.getMessage())


    def test_loadConfig_Banner(self):        
        
        self.assertEqual('./banner.png',self.ad.getBanner())


    def test_loadConfig_CTAMessage(self):        
        
        self.assertEqual('Download our E-Book to learn more',self.ad.getCTAMessage())



    def test_loadConfig_CTALink(self):        
        
        self.assertEqual('www.q.com',self.ad.getCTALink())

    def test_loadConfig_phone(self):        
        
        self.assertEqual(898654423,self.ad.getPhone())


    def test_loadConfig_email(self):        
        
        self.assertEqual('a@p.com',self.ad.getEmail())
    
    def test_loadConfig_Weblink(self):        
        
        self.assertEqual('www.qt.com',self.ad.getWebLink())
    
    def test_loadConfig_font(self):  

        font, size =self.issue.getNameFont()      
        
        self.assertEqual('./res/AngelicaCaroline.ttf',font)
        self.assertEqual(100,size)

    def test_loadConfig_NamePos(self):        
        x,y=self.issue.getNameLocation()
        self.assertEqual(150,x)
        self.assertEqual(160,y)
       
    def test_loadConfig_QRCodePos(self):        
        x,y=self.issue.getQRCodeLocation()
        self.assertEqual(1500,x)
        self.assertEqual(1600,y)

    def test_loadConfig_QRCodeColor(self):        
        fg,bg=self.issue.getQRCodeColor()
        self.assertEqual('white',fg)
        self.assertEqual('black',bg)

    def test_loadConfig_QRCodeSize(self):        
        
        self.assertEqual(10,self.issue.getQRCodeSize())
       

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_ConfigurationLoader)
    unittest.TextTestRunner(verbosity=2).run(suite)