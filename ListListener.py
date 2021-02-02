# Generated from List.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ListParser import ListParser
else:
    from ListParser import ListParser

# This class defines a complete listener for a parse tree produced by ListParser.
class ListListener(ParseTreeListener):

    # Enter a parse tree produced by ListParser#programa.
    def enterPrograma(self, ctx:ListParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ListParser#programa.
    def exitPrograma(self, ctx:ListParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ListParser#comando.
    def enterComando(self, ctx:ListParser.ComandoContext):
        pass

    # Exit a parse tree produced by ListParser#comando.
    def exitComando(self, ctx:ListParser.ComandoContext):
        pass


    # Enter a parse tree produced by ListParser#exp.
    def enterExp(self, ctx:ListParser.ExpContext):
        pass

    # Exit a parse tree produced by ListParser#exp.
    def exitExp(self, ctx:ListParser.ExpContext):
        pass


    # Enter a parse tree produced by ListParser#lista.
    def enterLista(self, ctx:ListParser.ListaContext):
        pass

    # Exit a parse tree produced by ListParser#lista.
    def exitLista(self, ctx:ListParser.ListaContext):
        pass



del ListParser