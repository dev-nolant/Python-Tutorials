numA = [4,1,6,10,2,3,7,9,11,12,5,8]
numB = [2,12,10,11,1,3,7,9,4,8,5,6]
choice = input("Add or multiply?")
len = len(numA)
try:
    def main():   
        if 'add' or 'multiply' in choice:
            if choice == 'add':
                for FOOA in range(len):
                    print("Add together: "+str(numA[FOOA])+" and "+str(numB[FOOA])+" then input the answer below!")
                    user_answer = input("Answer: ")
                    if int(user_answer) == (numA[FOOA]+numB[FOOA]):
                        input("Great job! - press enter to continue")
                    else:
                        input("Awww, wrong answer - the correct answer was "+str(FOOA+numB[0]))
                        main()
            if choice == 'multiply':
                    for FOOA in range(len):
                        print("Multiply together: "+str(numA[FOOA])+" and "+str(numB[FOOA])+" then input the answer below!")
                        user_answer = input("Answer: ")
                        if int(user_answer) == (numA[FOOA]*numB[FOOA]):
                            input("Great job! - press enter to continue")
                        else:
                            input("Awww, wrong answer - the correct answer was "+str(FOOA*numB[0]))
                            main()
        else:
            input("please try it in lowercase! - press enter")
            main()
except:
    input("Something went wrong")
main()
