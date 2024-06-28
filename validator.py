class PDA:
    def __init__(self):
        self.stack = []
        self.state = "q0"
        self.operatorler = {'+', '-', '*', '/'}
    
    def transition(self, char):
        if self.state == "q0":
            if char.isdigit():
                self.state = "q1"
            elif char == '(':
                self.stack.append(char)
                self.state = "q0"
            else:
                self.state = "error"

        elif self.state == "q1":
            if char in self.operatorler:
                self.state = "q2"
            elif char == ')':
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                    self.state = "q1"
                else:
                    self.state = "error"
            elif char.isdigit():
                self.state = "q1"
            else:
                self.state = "error"

        elif self.state == "q2":
            if char.isdigit():
                self.state = "q1"
            elif char == '(':
                self.stack.append(char)
                self.state = "q0"
            else:
                self.state = "error"
    
    def process_string(self, input_string):
        prev_char = ""
        for i, char in enumerate(input_string):
            self.transition(char)
            if self.state == "error":
                return False
            # Sağ parantezden sonra rakam gelmemesi kontrolü
            if prev_char == ')' and char.isdigit():
                return False
            # Bölme operatöründen sonra sıfır olup olmadığını kontrol et
            if prev_char == '/' and char == '0':
                return False
            prev_char = char

        if self.stack:
            return False

        return self.state == "q1"

def validate_expression(expression):
    pda = PDA()
    return pda.process_string(expression)

# Testler
ifadeler = [
    "(1+2)*(3/4)",
    "((2+3)*(4-1))",
    "(1+2*(3/4)",
    "(1+2)*(3/4))",
    "1+2)*3",
    "(1+2)*(3/4",
    "1+2",
    "((1+2)*3)/0",
    "1/0+2",
    "(1+2)/0",
    "(1+0)/0",
    "(2)2+2",
    "((4)/ 2)",
    "(4/2)-8",
    "(3)"
]

for ifade in ifadeler:
    print(f"{ifade}: {'Tanir' if validate_expression(ifade) else 'Tanimaz'}")
