
tokens = ['CTE_N','CTE_T', 'ID', 'CORIZQ', 'CORDER',
          'PARENIZQ', 'PARENDER', 'POR', 'MAS',
          'PUNTOYCOMA', 'DIG', 'IGUALIGUAL', 'NOIGUAL',
          'MENOS', 'ENTRE', 'IGUAL', 'MAYORQUE',
          'MENORQUE', 'COMA']

reservados = {
    'and'       : 'AND',
    'black'     : 'BLACK',
    'call'      : 'CALL',
    'circle'    : 'CIRCLE',
    'color'     : 'COLOR',
    'darkblue'  : 'DARKBLUE',
    'draw'      : 'DRAW', 
    'ellipse'   : 'ELLIPSE',
    'else'      : 'ELSE',
    'end'       : 'END',
    'fucsia'    : 'FUCSIA',
    'get'       : 'GET',
    'green'     : 'GREEN',
    'if'        : 'IF',
    'lightblue' : 'LIGHTBLUE',
    'line'      : 'LINE',
    'list'      : 'LIST',
    'number'    : 'NUMBER',
    'or'        : 'OR',
    'orange'    : 'ORANGE',
    'point'     : 'POINT',
    'procedure' : 'PROCEDURE',
    'program'   : 'PROGRAM',
    'purple'    : 'PURPLE',
    'red'       : 'RED',
    'repeat'    : 'REPEAT',
    'set'       : 'SET',
    'start'     : 'START',
    'text'      : 'TEXT',
    'width'     : 'WIDTH',
    'write'     : 'WRITE',
    'yellow'    : 'YELLOW',
}
tokens += reservados.values()

t_CTE_N       = r'\d+\.\d+'
t_DIG         = r'\d+'
t_CTE_T       = r'"[a-zA-Z_][a-zA-Z0-9_]*"'
t_CORIZQ      = r'\['
t_CORDER      = r'\]'
t_PARENIZQ    = r'\('
t_PARENDER    = r'\)'
t_COMA        = r','
t_PUNTOYCOMA  = r';'
t_MAS         = r'\+'
t_MENOS       = r'-'
t_POR         = r'\*'
t_ENTRE       = r'/'
t_IGUALIGUAL  = r'=='
t_NOIGUAL     = r'!='
t_IGUAL       = r'='
t_MENORQUE    = r'<'
t_MAYORQUE    = r'>'

t_ignore = " \t"

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservados:
        t.type = reservados[ t.value ]
    return t
    
def t_error(t):
    print("Character ilegal'%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

def p_Programa(t):
    '''Programa   : PROGRAM ID Vars Programa1 Start END'''

def p_Programa1(t):
    '''Programa1  : 
                  | Procedure Programa1'''

def p_Var(t):
    '''Var        : Type ID Var1 Var2'''

def p_Var1(t): 
    '''Var1      : 
                  | COMA ID Var1'''

def p_Var2(t):
    '''Var2       : IGUAL Ctvar'''

def p_List(t):
    '''List       : LIST Type ID IGUAL CORIZQ DIG CORDER'''

def p_Type(t):
    '''Type       : TEXT
                  | NUMBER'''

def p_Procedure(t):
    '''Procedure  : PROCEDURE ID PARENIZQ Procedure1 PARENDER Vars Statement END'''

def p_Procedure1(t):
    '''Procedure1 : 
                  | Type ID Procedure2'''

def p_Procedure2(t):
    '''Procedure2 : 
                  | COMA Type ID Procedure2'''

def p_Start(t):
    '''Start      : START Vars Statement END'''

def p_Vars(t):
    '''Vars       : 
                  | Var Vars
                  | List Vars'''

def p_Statement(t):
    '''Statement  : 
                  | Repeat
                  | Condition
                  | Assignment
                  | Get
                  | Write
                  | Call
                  | Set
                  | Draw'''

def p_Set(t):
    '''Set        : SET Color
                  | SET Width'''

def p_Width(t):
    '''Width      : WIDTH PARENIZQ DIG PARENDER PUNTOYCOMA'''

def p_Color(t):
    '''Color      : COLOR PARENIZQ Varcolor PARENDER PUNTOYCOMA'''

def p_Varcolor(t):
    '''Varcolor   : DARKBLUE
                  | LIGHTBLUE
                  | PURPLE
                  | ORANGE
                  | RED
                  | GREEN
                  | BLACK
                  | YELLOW
                  | FUCSIA'''

def p_Draw(t):
    '''Draw       : DRAW Draw1'''

def p_Draw1(t):
    '''Draw1      : Point
                  | Line
                  | Ellipse
                  | Circle'''

def p_Point(t):
    '''Point      : POINT PARENIZQ Ctvar COMA Ctvar PARENDER PUNTOYCOMA'''

def p_Line(t):
    '''Line       : LINE PARENIZQ Ctvar COMA Ctvar COMA Ctvar COMA Ctvar PARENDER PUNTOYCOMA'''

def p_Circle(t):
    '''Circle     : CIRCLE PARENIZQ Ctvar COMA Ctvar COMA Ctvar PARENDER PUNTOYCOMA'''

def p_Ellipse(t):
    '''Ellipse    : ELLIPSE PARENIZQ Ctvar COMA Ctvar COMA Ctvar COMA Ctvar PARENDER PUNTOYCOMA'''

def p_Write(t):
    '''Write      : WRITE PARENIZQ Ctvar PARENDER PUNTOYCOMA'''

def p_Get(t): 
    '''Get        : GET PARENIZQ Ctvar PARENDER PUNTOYCOMA'''

def p_Assignment(t): 
    '''Assignment : ID Assignment1 IGUAL Exp4 PUNTOYCOMA'''

def p_Assignment1(t):
    '''Assignment1 : 
                   | CORIZQ DIG CORDER'''

def p_Condition(t):
    '''Condition   : IF PARENIZQ Exp PARENDER Statement Condition1 END'''

def p_Condition1(t):
    '''Condition1  : ELSE Statement'''

def p_Repeat(t):
    '''Repeat      : REPEAT PARENIZQ Exp PARENDER Statement END'''

def p_Call(t):
    '''Call        : CALL ID PARENIZQ Ctvar Call1 PARENDER PUNTOYCOMA'''

def p_Call1(t):
    '''Call1       : 
                   | COMA Ctvar Call1'''

def p_Ctvar(t):
    '''Ctvar       : Ctvar1 CTE_N
                   | CTE_T
                   | ID Ctvar2'''

def p_Ctvar1(t):
    '''Ctvar1      : 
                   | MENOS'''

def p_Ctvar2(t):
    '''Ctvar2      :
                   | CORIZQ DIG CORDER'''

def p_Exp(t):
    '''Exp         : Exp2 Exp1'''

def p_Exp1(t):
    '''Exp1        : 
                   | OR Exp2 Exp1''' 

def p_Exp2(t):
    '''Exp2        : Exp3 Exp21'''

def p_Exp21(t):
    '''Exp21       : 
                   | AND Exp3 Exp21'''

def p_Exp3(t):
    '''Exp3        : Exp4 Exp31'''

def p_Exp31(t):
    '''Exp31       : 
                   | IGUALIGUAL Exp4
                   | NOIGUAL Exp4
                   | MAYORQUE Exp4
                   | MENORQUE Exp4'''

def p_Exp4(t):
    '''Exp4        : Term Exp41'''

def p_Exp41(t):
    '''Exp41       : 
                   | MAS Exp41
                   | MENOS Exp41'''

def p_Term(t):
    '''Term        : Factor Term1'''

def p_Term1(t):
    '''Term1       : 
                   | POR Term1
                   | ENTRE Term1'''                                                                             

def p_Factor(t):
    '''Factor      : PARENIZQ Exp PARENDER
                   | Ctvar'''  


def p_error(t):
    global success
    success = 0
    print("Error de sintaxis '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

success = 1

while 1:
    try:
        s = input('input > ')   # Use raw_input on Python 2
    except EOFError:
        break
    yacc.parse(s)
    if (success):
        print "Todo bien :D"