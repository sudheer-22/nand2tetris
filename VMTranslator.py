# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:56:13 2020

@author: sudhe
"""

import os
import sys
#------------------------------------------------------------------------------
#Seperates the lexical elements present in each commandline
def parser(new_line):
    operation = ""
    segment = ""
    index = ""
    command_type = ""
    if new_line[0:3] == "pop":
        operation = operation+"pop"
        new_line = new_line[3:]
        command_type = "C_POP"
    if new_line[0:4] == "push":
        operation = operation+"push"
        new_line = new_line[4:]
        command_type = "C_PUSH"
    #print("new_line", new_line, len(new_line))
    if(new_line[0:2] == "gt" or new_line[0:3] == "add" or new_line[0:2] == "lt" or new_line[0:2] == "eq"
       or new_line[0:3] == "sub" or new_line[0:3] == "neg" or new_line[0:2] == "or" or new_line[0:3] == "not" or new_line[0:3] == "and"):
        operation = operation+new_line
        command_type = "C_ARITHEMATIC"
    for j in range(len(new_line)):
        if(ord(new_line[j]) <= ord("9") and ord(new_line[j]) >= ord("0")):
            index = index+new_line[j]
        elif new_line[j] != " ":
            segment = segment+new_line[j]
    return command_type, operation, segment, index
##-------------------------------------------------------------------------------------------------------
#Codewriter function
def codewriter(command_type, operation, segment, index, g, filepath):
    file3 = open(output_filepath, "a")
#PUSH instructions---------------------------------------------------------------------------------------
    if command_type == "C_PUSH":
        #print("1st if)
        file3.write("\n"+"//"+operation+" "+segment+"\n")
        if segment[0:len("constant")] == "constant":
            #print("2nd if")
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@SP\n"+
                        "A=M\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "M=M+1\n")
        if segment[0:len("local")] == "local":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@LCL\n"+ 
                        "A=M+D\n"+
                        "D=M\n"+
                        "@SP\n"+
                        "A=M\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "M=M+1\n")
        if segment[0:len("argument")] == "argument":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@ARG\n"+ 
                        "A=M+D\n"+
                        "D=M\n"+
                        "@SP\n"+
                        "A=M\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "M=M+1\n")
        if segment[0:len("this")] == "this":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@THIS\n"+ 
                        "A=M+D\n"+
                        "D=M\n"+
                        "@SP\n"+
                        "A=M\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "M=M+1\n")
        if segment[0:len("that")] == "that":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@THAT\n"+ 
                        "A=M+D\n"+
                        "D=M\n"+
                        "@SP\n"+
                        "A=M\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "M=M+1\n")
        if segment[0:len("static")] == "static":
            file3.write("@Foo."+index+"\n"+
                        "D=M\n"+
                        "@SP\n"+
                        "A=M\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "M=M+1\n")
        if segment[0:len("pointer")] == "pointer":
            if index[0:1] == "0":
                file3.write("@THIS\n"+
                            "D=M\n"+
                            "@SP\n"+
                            "A=M\n"+
                            "M=D\n"+
                            "@SP\n"+
                            "M=M+1\n")
            if index[0:1] == "1":
                file3.write("@THAT\n"+
                            "D=M\n"+
                            "@SP\n"+
                            "A=M\n"+
                            "M=D\n"+
                            "@SP\n"+
                            "M=M+1\n")
        if segment[0:len("temp")] == "temp":
            file3.write("@5\n"+
                        "D=A\n"+
                        "@"+index+"\n"+
                        "A=A+D\n"+
                        "D=M\n"+
                        "@SP\n"+
                        "A=M\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "M=M+1\n")
#------------------------------------------------------------------------------------------------------           
#pop instructions-----------------------------------------------------------------------------------------
    if command_type == "C_POP":
        file3.write("\n"+"//"+operation+" "+segment+"\n")
        if segment[0:len("local")]== "local":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@LCL\n"+
                        "D=M+D\n"+
                        "@R13\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "AM=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "@R13\n"+
                        "A=M\n"+
                        "M=D\n")
                        #"@R13\n"+
                        #"M=0\n"
        if segment[0:len("argument")]=="argument":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@ARG\n"+
                        "D=M+D\n"+
                        "@R13\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "AM=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "@R13\n"+
                        "A=M\n"+
                        "M=D\n")
                        #"@R13\n"+
                        #"M=0\n")
        if segment[0:len("this")]=="this":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@THIS\n"+
                        "D=M+D\n"+
                        "@R13\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "AM=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "@R13\n"+
                        "A=M\n"+
                        "M=D\n")
                        #"@R13\n"+
                        #"M=0\n")
        if segment[0:len("that")]=="that":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@THAT\n"+
                        "D=M+D\n"+
                        "@R13\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "AM=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "@R13\n"+
                        "A=M\n"+
                        "M=D\n")#+
                        #"@R13\n"+
                        #"M=0\n")
        if segment[0:len("static")]=="static":
            file3.write("@SP\n"+
                        "AM=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "@Foo."+index+"\n"+
                        "M=D\n")
        if segment[0:len("temp")]=="temp":
            file3.write("@"+index+"\n"+
                        "D=A\n"+
                        "@5\n"+
                        "D=A+D\n"+
                        "@R13\n"+
                        "M=D\n"+
                        "@SP\n"+
                        "AM=M-1\n"+
                        "D=M\n"+
                       # "M=0\n"+
                        "@R13\n"+
                        "A=M\n"+
                        "M=D\n")
                        #"@R13\n"+
                        #"M=0\n")
        if segment[0:len("pointer")]== "pointer":
            #print("1st if\n")
            if index[0:1] == "0":
                #print("2nd if")
                file3.write("@SP\n"+
                            "AM=M-1\n"+
                            "D=M\n"+
                            #"M=0\n"+
                            "@THIS\n"+
                            "M=D\n")
            if index[0:1] == "1":
                file3.write("@SP\n"+
                            "AM=M-1\n"+
                            "D=M\n"+
                            #"M=0\n"+
                            "@THAT\n"+
                            "M=D\n")
#--------------------------------------------------------------------------------------------------------        
#Arithematic instructions------------------------------------------------------------------------
    if command_type == "C_ARITHEMATIC":
        file3.write("\n"+"//"+operation+"\n")
        if operation[0:3] == "add":
            file3.write("@SP\n"+
                        "A=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "A=A-1\n"+
                        "M=M+D\n"+
                        "@SP\n"+
                        "M=M-1\n")
        if operation[0:3] == "sub":
            file3.write("@SP\n"+
                        "A=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "A=A-1\n"+
                        "M=M-D\n"+
                        "@SP\n"+
                        "M=M-1\n")
        if operation[0:3] == "neg":
            file3.write("@SP\n"+
                        "D=0\n"
                        "A=M-1\n"+
                        "M=D-M\n")
        if operation[0:3] == "not":
            file3.write("@SP\n"+
                        "A=M-1\n"+
                        "M=!M\n")
        if operation[0:2] == "eq":
            file3.write("@SP\n"+
                         "AM=M-1\n"+
                         "D=M\n"+
                         "A=A-1\n"+
                         "D=M-D\n"+
                         "@TRUE"+str(g)+"\n"+
                         "D;JEQ\n"+
                         "@SP\n"+
                         "A=M-1\n"+
                         "M=0\n"+
                         "@END"+str(g)+"\n"+
                         "0;JMP\n"+
                         "(TRUE"+str(g)+")\n"+
                         "@SP\n"+
                         "A=M-1\n"+
                         "M=-1\n"+
                         "(END"+str(g)+")\n")
        
        if operation[0:2] == "gt":
            file3.write("@SP\n"+
                         "AM=M-1\n"+
                         "D=M\n"+
                         "A=A-1\n"+
                         "D=M-D\n"+
                         "@TRUE"+str(g)+"\n"+
                         "D;JGT\n"+
                         "@SP\n"+
                         "A=M-1\n"+
                         "M=0\n"+
                         "@END"+str(g)+"\n"+
                         "0;JMP\n"+
                         "(TRUE"+str(g)+")\n"+
                         "@SP\n"+
                         "A=M-1\n"+
                         "M=-1\n"+
                         "(END"+str(g)+")\n")
        if operation[0:2] == "lt":
            file3.write("@SP\n"+
                         "AM=M-1\n"+
                         "D=M\n"+
                         "A=A-1\n"+
                         "D=M-D\n"+
                         "@TRUE"+str(g)+"\n"+
                         "D;JLT\n"+
                         "@SP\n"+
                         "A=M-1\n"+
                         "M=0\n"+
                         "@END"+str(g)+"\n"+
                         "0;JMP\n"+
                         "(TRUE"+str(g)+")\n"+
                         "@SP\n"+
                         "A=M-1\n"+
                         "M=-1\n"+
                         "(END"+str(g)+")\n")
        if operation[0:3] == "and":
            file3.write("@SP\n"+
                        "A=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "A=A-1\n"+
                        "M=M&D\n"+
                        "@SP\n"+
                        "M=M-1\n")
        if operation[0:2] == "or":
            file3.write("@SP\n"+
                        "A=M-1\n"+
                        "D=M\n"+
                        #"M=0\n"+
                        "A=A-1\n"+
                        "M=M|D\n"+
                        "@SP\n"+
                        "M=M-1\n")
##------------------------------------------------------------------------------------------------------ 
##this section removes spaces and comments
input_filepath = sys.argv[1]
file = open(input_filepath, "r")
lines = file.readlines()
#print(lines)
#new_lines = []
intermediate_filepath = input_filepath.replace('.vm', '.txt')
output_filepath = input_filepath.replace('.vm', '.asm')
file2 = open(intermediate_filepath, "x")
for line in lines:
    c=-1
    new_string = ""
    for i in range(len(line)):
        if line[i] != " ":
            new_string = new_string+line[i]
    for j in range(len(new_string)):
        if(new_string[j] == "/" and new_string[j+1] == "/"):
            c=j
            break
    #print("new_string", len(new_string))
    if(c>0 and new_string != " "):
        new_string = new_string[:c]+"\n"
    #print(new_string)
    if len(new_string) != 1:
        #print(new_string)
        file2 = open(intermediate_filepath, "a")
        file2.write(new_string)
file2 = open(intermediate_filepath, "r")
#print("new lines", file2.readlines())
#file2.close()
#file.close()
#-----------------------------------------------------------------------------
#sends each line to parser and codewriter
intermediate_lines = file2.readlines()
#print("len", len(intermediate_lines))
file3 = open(output_filepath, "x")
for g in range(len(intermediate_lines)):
    command_type, operation, segment, index = parser(intermediate_lines[g])
    #print(command_type)
    codewriter(command_type, operation, segment, index,g, output_filepath)
file2.close()
file.close()
file3.close()
os.remove(intermediate_filepath)