class MyState:
    state = "home state"
    def __init__(self, name):
        self.name = name
    def print_state(self):
        print("My state is: {}".format(self.name))
tamilnadu = MyState("Tamil Nadu")
andhra = MyState("Andhra Pradesh")
tamilnadu.print_state()
andhra.print_state()

    
    
    