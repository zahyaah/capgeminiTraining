from Mail import Mail

class Whatsapp(Mail):
    def __init__(self, message):
        self.message = message
        
    def send(self):
        print(f"Message sent via Whatsapp\nMessage: {self.message}")