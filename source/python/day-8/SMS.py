from Mail import Mail

class SMS(Mail):
    def __init__(self, message):
        self.message = message 
        
    def send(self):
        print(f"Message sent via SMS\nMessage: {self.message}")