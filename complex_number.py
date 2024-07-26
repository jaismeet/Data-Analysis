# print(1+2)  
# print(type(1))
# print(type("apna"))
# print("apna" +"college")
# print([1,2,3] +[4,5,6])
# print((1,2,3) +(4,5,6))
# print(type((1,2,3)))
# print(type([1,2,3]))


class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
        
    def showNumber(self):
        print(self.real,"i +" ,self.img,"j")
        
        
    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal,newimg)
    
    def __sub__(self,num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return complex(newreal,newimg)
    
            
                
num1=complex(5,6)
num1.showNumber()        

num2=complex(4,7)
num2.showNumber()        

# num3=num1.add(num2)
# num3.showNumber()


num3=num1+num2
num3.showNumber()



num3=num1-num2
num3.showNumber()