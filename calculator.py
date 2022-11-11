class stack:
    def __init__(self, size = None):
        self.s = []
        self.top = None
        self.size = size
    def push(self, value : any):
        if self.top == None:
            self.top = 0
            self.s.append(value)
        else:
            if self.size != None and self.size != None and self.top < self.size:
                self.top += 1
                self.s.append(value)
            elif self.size == None:
                self.top += 1
                self.s.append(value)
    def pull(self):
        if self.top != None:
            if self.top == 0:
                self.top = None
                return self.s.pop()
            else:
                self.top -= 1
                return self.s.pop()
    def peak(self):
        if self.top != None:
            return self.s[self.top]

evaluatingStack = stack()
tempStack = stack()
evalString = '( 1 * (2 + 3)/4) - (5 * (6 + 7 / 8))'
operators ='^/*+-'
print(evalString)
for i in evalString:
    if i == ' ':
        continue
    elif i not in operators and i not in "()":
        evaluatingStack.push(i)
    else:
        if i == "(":
            tempStack.push(i)
            
            
        elif i == ")":
            if tempStack.top != None:
                while tempStack.peak() != "(":
                    evaluatingStack.push(tempStack.pull())
                tempStack.pull()
        else:
            if tempStack.top != None:
                if tempStack.peak() in operators and  operators.index(tempStack.peak()) >= operators.index(i):
                    tempStack.push(i)
                elif tempStack.peak() in operators:
                    evaluatingStack.push(tempStack.pull())
                    tempStack.push(i)
                else:
                    tempStack.push(i)

print(evaluatingStack.s)
st = ''
for i in evaluatingStack.s:
    st += i
print(st)
outputStack = stack()
for i in st:
    if i not in operators:
        outputStack.push(i)
        print(*outputStack.s)
    else:
        value2 = outputStack.pull()
        value1 = outputStack.pull()
        outputStack.push(str(eval(value1+ i+ value2)))
        print(*outputStack.s)
#run = True
#while run:
#    value = evaluatingStack.pull()
#    if value not in operators:
#        evaluatingStack.push(value)
#        print("hello")
#    else:
#        value2 = evaluatingStack.pull()
#        value1 = evaluatingStack.pull()
#        evaluatingStack.push(str(value1+value+value2))
#    if value == None:
#        run = False
#print(evaluatingStack.s)