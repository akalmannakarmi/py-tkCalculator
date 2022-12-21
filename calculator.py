import math

class Calculator():
    def __init__(self):
        pass
    
    def calculate(self,problem):
        result = self.separate(problem)
        print(f"Problem: {result}")
        result = self.calc(result)
        return result

    def separate(self,text):
        result = []
        num = 0
        word = ""
        num_decimal = 0
        i = -1
        for letter in text:
            i += 1
            if letter.isnumeric():
                if word != "":
                    result.append(word)
                    word = ""
                if letter == "0" and num == 0:
                    if text[i + 1] != "." and not text[i + 1].isnumeric():
                        result.append(int(letter))
                if num_decimal > 0:
                    num = num + (int(letter) / pow(10, num_decimal))
                    num_decimal += 1
                else:
                    num = num * 10 + int(letter)
            elif letter == ".":
                num_decimal = 1
            elif letter == " ":
                pass
            else:
                if num != 0:
                    result.append(num)
                if (letter == "+" or letter == "-" or letter == "/"
                        or letter == "^" or letter == "(" or letter == ")"
                        or letter == "*"or letter=="!" or letter == "%"):
                    if word != "":
                        result.append(word)
                        word = ""
                    result.append(letter)
                else:
                    word = word + letter
                num = 0
                num_decimal = 0
        if num != 0:
            result.append(num)
        return result

    def breakCalc(self,value=[]):
        startI = 0
        endI = -1
        foundO = 0
        foundC = 0
        i=0
        for letter in value:
            if letter == '(':
                if foundO==0:
                    startI = i
                foundO +=1
            elif letter == ')':
                foundC +=1
                if foundO==foundC:
                    endI = i
                    print(endI)
                    break
            i+=1
        if foundO>0:
            value[startI] = self.calc(value[startI+1:endI])
            for j in range(0,endI-startI):
                value.pop(startI+1)
        
        return value
                
                
        
        
    def calc(self,result):
        if len(result)<=0:
            return
        i=0
        length = len(result)
        while i<length:
            if result[i] == '(':
                result = self.breakCalc(result)
                i=0
                length = len(result)
            i+=1
        
        print(f"Calc:{result}")
        
        # !,\,^
        i = 0
        length = len(result)
        while i < length:
            if result[i]=='!':
                result[i-1]= math.factorial(result[i-1])
                result.pop(i)
            elif result[i] == '\\':
                result[i-1]= result[i-1] % result[i+1]
                result.pop(i)
                result.pop(i)
            elif result[i]=='^':
                result[i-1]= pow(result[i-1],result[i+1])
                result.pop(i)
                result.pop(i)
            else:
                i+=1
            length = len(result)
        
        # %,*,/
        i = 0
        length = len(result)
        while i < length:
            if result[i]=='%':
                result[i-1]/=100
                result.pop(i)
            elif result[i] == '*':
                result[i-1]= result[i-1] * result[i+1]
                result.pop(i)
                result.pop(i)
            elif i+1<length and type(result[i])!=str and type(result[i+1])!=str:
                result[i]= result[i] * result[i+1]
                result.pop(i+1)
            elif result[i] == '/':
                result[i-1]= result[i-1] / result[i+1]
                result.pop(i)
                result.pop(i)
            else:
                i+=1
            length = len(result)
        
        # +,-
        i = 0
        length = len(result)
        while i < length:
            if result[i]=='+':
                if i-1<0 or type(result[i-1])==str:
                    result[i]=+result[i+1]
                    result.pop(i+1)
                else:
                    result[i-1]= result[i-1] + result[i+1]
                    result.pop(i)
                    result.pop(i)
            elif result[i] == '-':
                if i-1<0 or type(result[i-1])==str:
                    result[i]=-result[i+1]
                    result.pop(i+1)
                else:
                    result[i-1]= result[i-1] - result[i+1]
                    result.pop(i)
                    result.pop(i)
            else:
                i+=1
            length = len(result)
            
        while i < len(result):
            if (result[i] == "tan"):
                result[i + 2] = (result[i + 2] * math.pi) / 180
                result[i] = math.tan(result[i + 2])
                result.pop(i + 3)
                result.pop(i + 2)
                result.pop(i + 1)
                i = 0
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "log"):
                result[i] = math.log(result[i + 2], result[i + 4])
                result.pop(i + 5)
                result.pop(i + 4)
                result.pop(i + 3)
                result.pop(i + 2)
                result.pop(i + 1)
                i = 0
            i += 1
        print(f"result:{result}")
        return result[0]