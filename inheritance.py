class Speaker:
    brand = "beatpill"

    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def powerOn(self):
        print(f"powering on {self.color}, {self.model} speaker")
    def powerOff(self):
        print(f"powering off {self.color}, {self.model} speaker")
    
class SmartSpeaker(Speaker):
    def __init__(self, color, model, wifi):
        super().__init__(color, model)
        self.wifi = wifi
    def connect(self):
        print(f"connecting to {self.wifi}")

smart_speaker1 = SmartSpeaker("Yellow", "XP-100", "5G")
print(f"Smart Speaker 1 is a {smart_speaker1.color} {smart_speaker1.model} speaker from {smart_speaker1.brand}")
smart_speaker1.powerOn()  
smart_speaker1.connect() 
