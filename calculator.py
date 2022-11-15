import math

class Calculator():
    def __init__(self):
        pass
    
    def calculate(self,problem):
        result = self.separate(problem)
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
            elif letter == "%":
                num = num / 100
            elif letter == " ":
                pass
            else:
                if num != 0:
                    result.append(num)
                if (letter == "+" or letter == "-" or letter == "/"
                        or letter == "^" or letter == "(" or letter == ")"
                        or letter == "*"):
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


    def calc(self,result):
        print(result)
        i = 0
        while i < len(result):
            if (result[i] == "/"):
                result[i - 1] = result[i - 1] / result[i + 1]
                result.pop(i + 1)
                result.pop(i)
                print(result)
                i = 0
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "*"):
                result[i - 1] = result[i - 1] * result[i + 1]
                result.pop(i + 1)
                result.pop(i)
                print(result)
                i = 0
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "+"):
                result[i - 1] = result[i - 1] + result[i + 1]
                result.pop(i + 1)
                result.pop(i)
                print(result)
                i = 0
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "-"):
                result[i - 1] = result[i - 1] - result[i + 1]
                result.pop(i + 1)
                result.pop(i)
                print(result)
                i = -1
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "MOD"):
                result[i - 1] = result[i - 1] - int(
                    result[i - 1] / result[i + 1]) * result[i + 1]
                result.pop(i + 1)
                result.pop(i)
                print(result)
                i = 0
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "sin"):
                result[i + 2] = (result[i + 2] * math.pi) / 180
                result[i] = math.sin(result[i + 2])
                result.pop(i + 3)
                result.pop(i + 2)
                result.pop(i + 1)
                print(result)
                i = 0
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "cos"):
                result[i + 2] = (result[i + 2] * math.pi) / 180
                result[i] = math.cos(result[i + 2])
                result.pop(i + 3)
                result.pop(i + 2)
                result.pop(i + 1)
                print(result)
                i = 0
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "tan"):
                result[i + 2] = (result[i + 2] * math.pi) / 180
                result[i] = math.tan(result[i + 2])
                result.pop(i + 3)
                result.pop(i + 2)
                result.pop(i + 1)
                print(result)
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
                print(result)
                i = 0
            i += 1
        i = 0
        while i < len(result):
            if (result[i] == "!"):
                result[i] = math.factorial(result[i - 1])
                result.pop(i - 1)
                print(result)
                i = 0
            i += 1

        return result[0]