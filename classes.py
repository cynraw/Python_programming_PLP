class Speaker:
    brand = "beatpill"

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def powerOn(self):
        print(f"powering on {self.color}{self.model} speaker")
    
    def powerOff(self):
        print(f"powering off {self.color}{self.model} speaker")
  

speaker_1 = Speaker("Yellow", "XP-100")
speaker_2 = Speaker("Red", "XP-200")
print(f"Speaker 1 is a {speaker_1.color} {speaker_1.model} speaker from {speaker_1.brand}")
speaker_1.powerOn()
