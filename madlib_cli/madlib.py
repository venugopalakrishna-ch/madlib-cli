import re
welcome_text ="""
Welcome to Madlib game, it reads in a template file and writes a file back out with user input injected.
Mad Libs is a phrasal template word game where user will be prompted for a list of words to substitute for blanks in a sentence or story before reading aloud.
The game is frequently played as a party game or as a pastime.
"""
input_text = """Here are the sentances you will need to fill in values for the words enclosed in {}:
"""
output_text = "Here is the output after substituting your values:\n"

def openFile(filepath):
    try:
        return open(filepath)        
    except IOError:
        print("The file does not exist")
     

def readFile(input_file):
    return input_file.read()       

def parse(template):
    return re.findall(r"\{(.*?)\}",template)  

def userInput(userchoices): 
    userInputs = list ()   
    for prompt_user in userchoices:
        input_string = input("Enter value for input {" + prompt_user +"}:")
        userInputs.append(input_string)
    return userInputs

def injectUserInputs(template,choices,useinputs):       
    for i in range(len(choices)):        
        template = template.replace("{"+choices[i]+"}",useinputs[i],1)    
    return template

def writeToFile(output_template,output_path):
    output_file = open(output_path,"w")
    output_file.write(output_template)

if __name__ == "__main__": 
    print(welcome_text)
    input_file = openFile("assets/sample.txt")
    template = readFile(input_file)
    print(input_text,template),
    choices=parse(template)
    userinputs = userInput(choices)
    output_template = injectUserInputs(template,choices,userinputs)
    print(output_text,output_template)
    writeToFile(output_template,"assets/sample_outpu.txt")

