def check_length(s):
    if len(s) < 8:
        return 1
    elif len(s) <12:
        return 2
    else:
        return 3

def check_case(s):
    if s.isupper() or s.islower():
        return 1
    else:
        return 2
    
def check_content(s):
    if s.isalpha():
        return 1
    if s.isalnum():
        return 2
    for x in s:
        if x.isalnum() == False:
            return 3
    
    
def passChecker():
    print("Welcome to the Password Evaluator!\n")
    password = input("Enter a password or \"q\" to quit: ")
    if password == "q":
        return False
    score = 0
    score += check_length(password)
    score += check_case(password)
    score += check_content(password)
    print("Score: ", score)
    tpi = "This password is"
    if score >= 8:
        print(tpi, "strong!")
    elif score >= 6:
        print(tpi, "acceptable.")
    else:
        print(tpi, "weak!")

if __name__ == '__main__':
    passChecker()
