class ic152():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        self.check()
        
    def check(self):
        if self.roll_no[:3]== 'B23' and len(self.roll_no)==6:
            pass
        else:
            print('Invalid input')
            exit()
        
        if self.marks in range(1,101):
            if self.marks<33:
                print('Fail')
            else:
                print('Pass')
        else:
            print('Invalid input')
            exit()
        

var=ic152('Bharat','B21341',100)
