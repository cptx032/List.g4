import antlr4
import sys

from ListLexer import ListLexer
from ListParser import ListParser
from TranspilerVisitor import TranspilerVisitor


if __name__ == "__main__":
    with open(sys.argv[1]) as _f:
        input_stream = antlr4.InputStream(_f.read())
    lexer = ListLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ListParser(tokens)
    parser.buildParseTrees = True
    tree = parser.programa()
    transpiler = TranspilerVisitor()
    print("{}".format(transpiler.visit(tree)))
