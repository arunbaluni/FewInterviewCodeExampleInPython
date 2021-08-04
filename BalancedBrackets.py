# This code will check if the input expression has Balanced Brackets or NOT
# Brackets used in expression are '{', '[', '(', '}', ']', ')'

'''
def checkBalance(String):
    return bool
'''

def checkBalance(stringExpression):
	stack = []
	
	for item in stringExpression:
		if item in ('{', '(', '[') :
			stack.append(item)

		else:
			if not stack:
				return False
			choice = stack.pop()
				
			if(choice == '('):
				if(item == '}' or item == ']'):
					return False
			if(choice == '['):
				if(item == '}' or item == ')'):
					return False
			if(choice == '{'):
				if(item == ')' or item == ']'):
					return False
	return True
	
if __name__ == "__main__":
	
    # Check with correct and incorrect balanced brackets,  1 item, 2 item, empty testcases
    expr_list = ['{([({})]))', '{([({})])}', '{', '{)', '']
    
    for expr in expr_list:
        print(expr)
        
        if(len(expr) < 2):
            print("Minimum 2 items required in expression to check Bracket balance")
        else:
            if(checkBalance(expr)):
                print("It's Balanced")
            else:
                print("It is not balanced")