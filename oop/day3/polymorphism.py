class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly.")


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


bird_list = [Bird(), Sparrow(), Ostrich()]
for bird in bird_list:
    bird.intro()
    bird.flight()