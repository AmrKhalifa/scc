from ast.visualizer import Visualizer
from parser_ import Parser
from lexer import Lexer
from compiler.compiler import Compiler
code = """
void main(){


    for(1;1;1){
    }


    return;
}
"""

lex = Lexer(text=code)
lex2 = Lexer(text=code)
parser = Parser(lexer=lex)
parser2 = Parser(lexer=lex2)
comp = Compiler(parser=parser)
viz = Visualizer(parser=parser2)


print(comp.compile())
#viz.visualize()


