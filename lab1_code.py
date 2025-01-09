class calculator:
    def __init__(self,x,Y):
        self.num1=x
        self.Num2=Y
        self.History=[]

    def ADD(self):
        result=self.num1+self.Num2
        print(f"{self.num1} + {self.Num2} = {result}")
        # return result

    def subtract(self):
        r=self.num1-self.Num2
        print(f"{self.num1} - {self.Num2} = {r}")
        # return r

    def multiply(self):
        result=self.num1*self.Num2
        print(f"{self.num1} * {self.Num2} = {result}")
        # return self.num1*self.Num2

    def divide(self):
        if self.Num2!=0:
            result=self.num1/self.Num2
            print(f"{self.num1} / {self.Num2} = {result}")
            # return self.num1/self.Num2
        else:
            print("Cannot divide by zero")
            # return None
            #dummy comment for dummy push