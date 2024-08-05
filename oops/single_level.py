class Car:
    def start(self):
        print("Car started")
class New(Car):
    def close(self):
        print("Closed")

obj=New()
obj.start()