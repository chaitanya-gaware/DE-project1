class computer: # 1.0 class is created 
    
    def __init__(self, cpu, ram): # 2.0 auto call is created here self id replace by the object name
        self.cpu1 = cpu
        self.ram2 = ram
        
    def config(self): # self is for calling that object 
        print(self.cpu1, self.ram2)
        
        
        
comp1 = computer('i5', 16) # passing 2 but actually its 3, reference to design/defination 2.0
comp2 = computer('Ryzen', 8)# self is object name then cpu and then ram total 3

comp1.config()