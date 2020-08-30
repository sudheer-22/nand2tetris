import os
import sys
def converttobinary(n):
    temp = ""
    number = ""
    for i in range(15):
        temp = temp+str(n%2)
        n=int(n/2)
    for j in range(15):
        number = number+temp[14-j]
    return number

symbol_dict = {'SP': '000000000000000',
            'LCL': '000000000000001',
            'ARG': '000000000000010',
           'THIS': '000000000000011',
           'THAT': '000000000000100',
             'R0': '000000000000000',
             'R1': '000000000000001',
             'R2': '000000000000010',
             'R3': '000000000000011',
             'R4': '000000000000100',
             'R5': '000000000000101',
             'R6': '000000000000110',
             'R7': '000000000000111',
             'R8': '000000000001000',
             'R9': '000000000001001',
            'R10': '000000000001010',
            'R11': '000000000001011',
            'R12': '000000000001100',
            'R13': '000000000001101',
            'R14': '000000000001110',
            'R15': '000000000001111',
         'SCREEN': '100000000000000',
            'KBD': '110000000000000',}  
def convertTobinary(n):
    temp = ""
    number = ""
    for i in range(15):
        temp = temp+str(n%2)
        n=int(n/2)
    for j in range(15):
        number = number+temp[14-j]
    return number
 
def update_dictionary(intermediate_fileaddress, dict_pass):
#Update labels_symbols-------------------------------------------------------------------
    file = open(intermediate_fileaddress, "r")
    lines = file.readlines()
    c=0
    g=0
    for line in lines:
        if line[0]=="(":
            label = line[1:len(line)-2]
            dict_pass[label] = convertTobinary(g-c)
            c=c+1
        g=g+1
#updates varaible_symbols--------------------------------------------------------------------------
    c=16
    g=0
    for line in lines:
        if line[0] == "@":
            symbol = line[1:len(line)-1]
            status = dict_pass.get(symbol, "Not Found")
            if status == "Not Found":
                dict_pass[symbol] = convertTobinary(c)
                c=c+1
        g=g+1
        
def remove_spacesandcomments(file_address):
    intermediate_filepath = ""
    file = open(file_address, 'r')
    lines = file.readlines()
    intermediate_filepath = file_address.replace('.asm', '.txt')
    output_filepath = file_address.replace('.asm', '.hack')
    file2 = open(intermediate_filepath, "x")
    file3 = open(output_filepath, "x")
    for line in lines:
        c=-1
        new_string = ""
        for i in range(len(line)):
            if line[i] != " ":
                new_string = new_string+line[i]
        for j in range(len(new_string)):
            if(new_string[j] == "/" and new_string[j+1] == "/"):
                c=j
                #print("c", c)
                break
        #print("new_string", new_string)
        if(c>=0 and new_string != " "):
            new_string = new_string[:c]+"\n"
            #print(new_string)
        if len(new_string) != 1:
            #print(new_string)
            file2 = open(intermediate_filepath, "a")
            file2.write(new_string)
            file.close()
    file2.close()
    file3.close()
    return intermediate_filepath, output_filepath
#input_address = sys.argv[1]
input_address = sys.argv[1]
intermediate_fileaddress,output_fileaddress = remove_spacesandcomments(input_address)
update_dictionary(intermediate_fileaddress, symbol_dict)
print(symbol_dict)
def codewriter(output_fileaddress, symbol_dict,command_type, symbol, dest, comp, jump,line):
    file = open(output_fileaddress, "a") 
    comp_dict = {
              '0': '0101010',
              '1': '0111111',
             '-1': '0111010',
              'D': '0001100',
              'A': '0110000',
             '!D': '0001101',
             '!A': '0110001',
             '-D': '0001111',
             '-A': '0110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'D+A': '0000010',
            'A+D': '0000010',
            'D-A': '0010011',
            'A-D': '0000111',
            'D&A': '0000000',
            'D|A': '0010101',
            'M'  : '1110000',
            '!M' : '1110001',
            '-M' : '1110011',
            'M+1': '1110111',
            'M-1': '1110010',
            'D+M': '1000010',
            'M+D': '1000010',
            'D-M': '1010011',
            'M-D': '1000111',
            'D&M': '1000000',
            'D|M': '1010101',}
        
    new_line=""
    jump_dict = {
            'null': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
        }
    
    dest_dict = {'null':'000',
             'M'   :'001',
             'D'   :'010',
             'MD'  :'011',
             'A'   :'100',
             'AM'  :'101',
             'AD'  :'110',
             'AMD' :'111'}
    if command_type == "A_COMMAND":
        file.write("0"+symbol_dict[symbol]+"\n")
    if command_type == "C_COMMAND":
        new_line = "11"+comp_dict[comp]+dest_dict[dest]+jump_dict[jump]
        file.write(new_line+"\n")
def parser(line):
    c = -1
    d = -1
    command_type = ""
    symbol = ""
    dest = "" 
    comp = ""
    jump = ""
    n = len(line)-1
    if line[0] == "@":
        command_type = "A_COMMAND"
    elif line[0] == "(":
        command_type = "L_COMMAND"
    else:
        command_type = "C_COMMAND"
    if command_type == "A_COMMAND":
        symbol = line[1:n]
        dest = "null" 
        comp = "nul"
        jump = "null"
    if command_type == "C_COMMAND":
        for i in range(len(line)):
            if line[i] == "=":
                c = i
            if line[i] == ";":
                d = i
        if c != -1:
            symbol = "null"
            dest = line[:c]
            comp = line[c+1:n]
            jump = "null"
        if d != -1:
            symbol = "null"
            comp = line[0:d]
            jump = line[d+1:d+4]
            dest = "null"
    if command_type == "L_COMMAND":
        symbol = "null"
        dest = "null" 
        comp = "null"
        jump = "null"
    return command_type, symbol, dest, comp, jump
            
file = open(intermediate_fileaddress, "r")
lines = file.readlines()
command_type = ""
symbol = ""
dest = ""
comp = ""
jump = ""
for line in lines:
    command_type, symbol, dest, comp, jump = parser(line)
    codewriter(output_fileaddress,symbol_dict,command_type, symbol, dest, comp, jump, line)
file.close()
file4 = open(output_fileaddress, "r")
file4.close()
os.remove(intermediate_fileaddress)

