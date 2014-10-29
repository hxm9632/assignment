# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

LETTER = 0;
DIGIT  =1;
UNKNOWN = 99;
EOF 	 = -1;
INT_LIT 	 = 10;
IDENT		 = 11;
ASSIGN_OP	 = 20;
ADD_OP 	 = 21;
SUB_OP 	 = 22;
MULT_OP 	 = 23;
DIV_OP 	 = 24;
LEFT_PAREN  = 25;
RIGHT_PAREN = 26;
lexeme=[]
for i in range(100):
    lexeme.append(i);
lexLen =0;
LastToken="";
currentChar="";
currentClass="";
nextToken =EOF;
fo="";

def lookup(ch):
    nextToken = EOF;
    print(ch);
    if(ch=='('):     
        nextToken = LEFT_PAREN;
    elif(ch==')'):     
        nextToken = RIGHT_PAREN;
    elif(ch=='+'):     
        nextToken = ADD_OP;  
    elif(ch=='-'):     
        nextToken = SUB_OP;
    elif(ch=='*'):     
        nextToken = MULT_OP; 
    elif(ch=='/'):     
        nextToken = DIV_OP;
    else:
     nextToken = EOF;   
     addChar(ch);
     return nextToken;     
     
def lex(charClass):
    nextToken = EOF;
    print(charClass);
    if(charClass==LETTER):
        addChar(currentChar);
        charClass = getChar();
        while (charClass == LETTER | charClass == DIGIT):
            addChar(currentChar);
            charClass = getChar();
            nextToken = IDENT;			
    elif(charClass==DIGIT):
        addChar(currentChar);
        charClass = getChar();
        while (charClass == DIGIT): 
          addChar(currentChar);
          charClass = getChar();	
          nextToken = INT_LIT;
    elif(charClass==UNKNOWN):        
       nextToken=lookup(currentChar);
    elif(charClass==EOF):             
        nextToken = EOF;
        lexeme[0] = 'E';
        lexeme[1] = 'O';
        lexeme[2] = 'F';
        lexeme[3] = 0;	
        
    print("next token is ");
    print(nextToken);
    print("next lexeme is ");
    print(lexeme);

    return nextToken;

def addChar(token):
    if (lexLen <= 98):
        lexeme[lexLen+1] = token;
        lexeme[lexLen] = 0;
    else:    
        print("Error - lexeme is too long \n");	
def sebestaScanner(filename):
    global fo; 
    try:
        fo = open(filename, "r+");
    except :
         print("Unexpected error in reaing file");
         raise
   
def scan():
    charClass = UNKNOWN;
    nextToken = EOF;
    try:
        nextToken = lex(charClass);
        print(nextToken);
        while(nextToken !=EOF ):
            if(nextToken != IDENT & nextToken !=INT_LIT):
                charClass = getChar();
            else:
                charClass = currentClass;
                nextToken = lex(charClass);
    except:	
        print("Unexpected error");
        raise

def getChar():
    print('xcxc');
    charClass = UNKNOWN;
    token= fo.read(1)
    print(token);    
    
    if not token:
     charClass = EOF;
    else:
        while(token.isspace()):
            token= fo.read(1);
        if(token.isalpha()): 
            charClass= LETTER;
        elif(token.isdigit()):     
            charClass = DIGIT;
    currentChar = token;
    currentClass = charClass;
    print(currentClass);
    print(currentChar);
    return charClass;            

#inputfile=raw_input("Enter the input file");
inputfile="test.txt";
sebestaScanner(inputfile);
scan();

    
   


		       
    
   
