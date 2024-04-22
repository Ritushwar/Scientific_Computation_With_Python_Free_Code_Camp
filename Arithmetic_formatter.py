def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    arranged_problems = []
    for value in problems:
        operation = value.split(" ")
        if operation[1] not in '+-':
            return "Error: Operator must be '+' or '-'."
        try:
            value_1 = int(operation[0])
            value_2 = int(operation[2])
        except ValueError:
            return 'Error: Numbers must only contain digits.'

        if len(operation[0])>4 or len(operation[2])>4:
            return 'Error: Numbers cannot be more than four digits.' 
        
    #["32","+","698"]
        longest_var = max(len(operation[0]),len(operation[2]))
        width = longest_var + 2
        l1 = f"{operation[0]:>{width}}"
        l2 = operation[1] + f"{operation[2]:>{width-1}}"
        l3 = '_'*width
        
        try:
            arranged_problems[0] += "    " + l1
        except IndexError:
            arranged_problems.append(l1)
        try:
            arranged_problems[1] += "    " + l2
        except IndexError:
            arranged_problems.append(l2)
        try:
            arranged_problems[2] += "    " + l3
        except IndexError:
            arranged_problems.append(l3)
    
        if show_answers:
            if operation[1] == "+":
                ans = int(operation[0]) + int(operation[2])
            else:
                ans = int(operation[0]) - int(operation[2])
        
            a = f"{str(ans):>{width}}"
            try:
                arranged_problems[3] += "    " + a
            except IndexError:
                arranged_problems.append(a)

    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    if show_answers:
        output = output + f"\n{arranged_problems[3]}"
    return output

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2","42 + 25","123 + 49"])}')