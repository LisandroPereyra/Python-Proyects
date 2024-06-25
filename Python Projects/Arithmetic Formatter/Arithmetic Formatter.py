import re

def arithmetic_arranger(problems, show_answers=False):
    if len(problems)<6:
        
        first = ""
        second = ""
        lines  = ""
        reslt = ""
        arrenged_format = ""
        
        for problem in problems:
            if(re.search("[^\s0-9.+-]", problem)):
                if(re.search("[/]", problem) or re.search("[*]", problem)):
                    return "Error: Operator must be '+' or '-'."
                return 'Error: Numbers must only contain digits.'

            first_number = problem.split(" ")[0]
            operator = problem.split(" ")[1]
            second_number = problem.split(" ")[2]

            if(len(first_number)>4 or len(second_number)>4):
                return 'Error: Numbers cannot be more than four digits.'
            
            result=""
            if operator == "+":
                result = str(int(first_number)+int(second_number))
            elif operator == "-":
                result = str(int(first_number)-int(second_number))

            bar_length= max(len(first_number), len(second_number)) + 2
            top= str(first_number).rjust(bar_length)
            bottom = operator + str(second_number).rjust(bar_length - 1)
            line=""
            res= str(result).rjust(bar_length)
            for s in range (bar_length):
                line +="-"    

            if problem != problems[-1]:
                first += top + "    "
                second += bottom + "    "
                lines  += line + "    "
                reslt += res + "    "
            
            else:
                first += top 
                second += bottom 
                lines  += line 
                reslt += res

        if show_answers:
            arrenged_format = first + "\n" + second + "\n" + lines + "\n" + reslt
        else:
            arrenged_format = first + "\n" + second + "\n" + lines
        return arrenged_format

    else:
        return('Error: Too many problems.')
    

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')