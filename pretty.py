import sys

json_file_path = ''
try:
    json_file_path = sys.argv[1]
except:
    pass

file_path = ''
try:
    file_path = sys.argv[2]
except:
    pass

if json_file_path:
    with open(json_file_path,"r") as json_file:
        json_content = json_file.read()
        pretty(json_content, file_path)

def pretty(json, file_path):
    json_str = str(json)
    result = ""
    is_tupple = False
    spacing = "    "
    total_spacing = ""
    close_curly_braces = False
    n = 4
    for letter in json_str:
        if letter == "{":
            result += letter 
            result += '\n'
            total_spacing += spacing
            result += total_spacing
        elif letter == "}":
            result += '\n'
            total_spacing = total_spacing[:-n]
            result += total_spacing
            result += letter 
            close_curly_braces = True
        elif (letter == ","):
            result += letter
            if is_tupple:
                pass
            else:
                result += '\n'
                result += total_spacing
        elif letter == "(":
            is_tupple = True
            result += letter
        elif letter == ")":
            is_tupple = False
            result += letter
        else:
            result += letter
    
    if file_path:
        with open(file_path,"w") as txt:
            txt.write(result)
    else:
        print(result)
