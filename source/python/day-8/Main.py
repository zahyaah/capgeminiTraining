from SMS import SMS 
from Email import Email
from Whatsapp import Whatsapp

smsObject = SMS("Hi, I hope you're doing well.") 
emailObject = Email("My name is Zayd")
whatsappObject = Whatsapp("Hey!")

smsObject.send()
emailObject.send()
whatsappObject.send()