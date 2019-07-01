from time import sleep

class Clock ():
    
    def __init__(self, seconds, minutes, hours):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    
    def run(self):

        self.seconds += 1
        if self.seconds > 59:
            self.minutes += 1
            self.seconds = 0
            if self.minutes > 59:
                self.hours += 1
                self.minutes = 0
                if self.hours >24:
                    self.hours = 0


    def show (self):
        print("%ds:%ds:%ds" %(self.hours, self.minutes, self.seconds))
        sleep(1)

