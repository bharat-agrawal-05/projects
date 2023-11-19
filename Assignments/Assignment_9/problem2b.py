class stack():
    def __init__(self):
        self.contents=[]
        self.element=None

    def __str__(self):
        if self.isEmpty():
            return None
        else:
            return str(self.contents[::-1])

    def isEmpty(self):
        if len(self.contents)==0:
            return True
        else:
            return False

    def push(self,elem):
        self.contents+=[elem]

    def pop(self):
        
        if self.isEmpty():
            return None
        else:
            self.element=self.contents[-1]
            self.contents=[self.contents[i] for i in range(0,len(self.contents)-1)]
            return self.element

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.contents[-1]

stack_list=stack()
choice=''
while choice!=4:
    choice=eval(input("Enter 1 to push to stack \nEnter 2 to pop from stack \nEnter 3 t peek from the stack \nEnter 4 to exit \nINPUT ="))
    if choice == 1:
        element=eval(input('Enter the element to be pushed: '))
        stack_list.push(element)
        print(stack_list)
    elif choice ==2:
        print(f'{stack_list.pop()} has been popped')
        print(stack_list)
    elif choice ==3:
        print(stack_list.peek())
    elif choice ==4:
        break