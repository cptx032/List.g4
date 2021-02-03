# Generated from List.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ListParser import ListParser
else:
    from ListParser import ListParser

# This class defines a complete generic visitor for a parse tree produced by ListParser.

class ListVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ListParser#programa.
    def visitPrograma(self, ctx:ListParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#atribuicao.
    def visitAtribuicao(self, ctx:ListParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#impressao.
    def visitImpressao(self, ctx:ListParser.ImpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#concatenacao.
    def visitConcatenacao(self, ctx:ListParser.ConcatenacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#definicaoLista.
    def visitDefinicaoLista(self, ctx:ListParser.DefinicaoListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#soma.
    def visitSoma(self, ctx:ListParser.SomaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#booleanTrue.
    def visitBooleanTrue(self, ctx:ListParser.BooleanTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#booleanFalse.
    def visitBooleanFalse(self, ctx:ListParser.BooleanFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#variavel.
    def visitVariavel(self, ctx:ListParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#integer.
    def visitInteger(self, ctx:ListParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListParser#lista.
    def visitLista(self, ctx:ListParser.ListaContext):
        return self.visitChildren(ctx)



del ListParser