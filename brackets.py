'''
Balancing Brackets:
Given an input of brackets (string type). Print &#39;YES&#39; if all the brackets are balanced with
opening and closing.
Brackets can be of type {,},[,],(,) Refer to sample input and output for reference
Input:
{[()]}
Output:
YES
Input:
{[(])}
Output:
NO

'''

def brackets(in_array):
    if len(in_array) % 2 == 1:
        return False
    else:
        s=list()
        for element in in_array:
            if (element in ['(','[','{']):
                s.append(element)
            else:
                if not s:
                    return False
                current_element =  s.pop()

                if (current_element == '{'):
                    if element != '}':
                        return False
                elif(current_element == '['):
                    if element != ']':
                        return False
                elif(current_element == '('):
                    if element != ')':
                        return False
    if s:
        return False
    return True

in_str = "{[()]}"
print("Is brackets are balanced :-",brackets(in_str))
