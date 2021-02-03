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


    # Enter a parse tree produced by ListParser#atribuicao.
    def enterAtribuicao(self, ctx:ListParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by ListParser#atribuicao.
    def exitAtribuicao(self, ctx:ListParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by ListParser#impressao.
    def enterImpressao(self, ctx:ListParser.ImpressaoContext):
        pass

    # Exit a parse tree produced by ListParser#impressao.
    def exitImpressao(self, ctx:ListParser.ImpressaoContext):
        pass


    # Enter a parse tree produced by ListParser#concatenacao.
    def enterConcatenacao(self, ctx:ListParser.ConcatenacaoContext):
        pass

    # Exit a parse tree produced by ListParser#concatenacao.
    def exitConcatenacao(self, ctx:ListParser.ConcatenacaoContext):
        pass


    # Enter a parse tree produced by ListParser#definicaoLista.
    def enterDefinicaoLista(self, ctx:ListParser.DefinicaoListaContext):
        pass

    # Exit a parse tree produced by ListParser#definicaoLista.
    def exitDefinicaoLista(self, ctx:ListParser.DefinicaoListaContext):
        pass


    # Enter a parse tree produced by ListParser#soma.
    def enterSoma(self, ctx:ListParser.SomaContext):
        pass

    # Exit a parse tree produced by ListParser#soma.
    def exitSoma(self, ctx:ListParser.SomaContext):
        pass


    # Enter a parse tree produced by ListParser#booleanTrue.
    def enterBooleanTrue(self, ctx:ListParser.BooleanTrueContext):
        pass

    # Exit a parse tree produced by ListParser#booleanTrue.
    def exitBooleanTrue(self, ctx:ListParser.BooleanTrueContext):
        pass


    # Enter a parse tree produced by ListParser#booleanFalse.
    def enterBooleanFalse(self, ctx:ListParser.BooleanFalseContext):
        pass

    # Exit a parse tree produced by ListParser#booleanFalse.
    def exitBooleanFalse(self, ctx:ListParser.BooleanFalseContext):
        pass


    # Enter a parse tree produced by ListParser#variavel.
    def enterVariavel(self, ctx:ListParser.VariavelContext):
        pass

    # Exit a parse tree produced by ListParser#variavel.
    def exitVariavel(self, ctx:ListParser.VariavelContext):
        pass


    # Enter a parse tree produced by ListParser#integer.
    def enterInteger(self, ctx:ListParser.IntegerContext):
        pass

    # Exit a parse tree produced by ListParser#integer.
    def exitInteger(self, ctx:ListParser.IntegerContext):
        pass


    # Enter a parse tree produced by ListParser#lista.
    def enterLista(self, ctx:ListParser.ListaContext):
        pass

    # Exit a parse tree produced by ListParser#lista.
    def exitLista(self, ctx:ListParser.ListaContext):
        pass



del ListParser