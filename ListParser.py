# Generated from List.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2")
        buf.write("\16\2\r\3\3\3\3\3\3\3\3\3\3\5\3\25\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\35\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4%\n\4\f")
        buf.write("\4\16\4(\13\4\3\5\3\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13")
        buf.write("\5\3\5\3\5\3\5\2\3\6\6\2\4\6\b\2\2\29\2\13\3\2\2\2\4\24")
        buf.write("\3\2\2\2\6\34\3\2\2\2\b)\3\2\2\2\n\f\5\4\3\2\13\n\3\2")
        buf.write("\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2")
        buf.write("\2\17\20\7\f\2\2\20\21\7\3\2\2\21\25\5\6\4\2\22\23\7\4")
        buf.write("\2\2\23\25\5\6\4\2\24\17\3\2\2\2\24\22\3\2\2\2\25\5\3")
        buf.write("\2\2\2\26\27\b\4\1\2\27\35\7\f\2\2\30\35\5\b\5\2\31\35")
        buf.write("\7\r\2\2\32\35\7\7\2\2\33\35\7\b\2\2\34\26\3\2\2\2\34")
        buf.write("\30\3\2\2\2\34\31\3\2\2\2\34\32\3\2\2\2\34\33\3\2\2\2")
        buf.write("\35&\3\2\2\2\36\37\f\t\2\2\37 \7\5\2\2 %\5\6\4\n!\"\f")
        buf.write("\b\2\2\"#\7\6\2\2#%\5\6\4\t$\36\3\2\2\2$!\3\2\2\2%(\3")
        buf.write("\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\7\3\2\2\2(&\3\2\2\2)*\7")
        buf.write("\t\2\2*/\5\6\4\2+,\7\n\2\2,.\5\6\4\2-+\3\2\2\2.\61\3\2")
        buf.write("\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61/\3\2\2\2\62")
        buf.write("\63\7\13\2\2\63\t\3\2\2\2\b\r\24\34$&/")
        return buf.getvalue()


class ListParser ( Parser ):

    grammarFileName = "List.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'print'", "'.'", "'+'", "'false'", 
                     "'true'", "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NOME", "INT" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_exp = 2
    RULE_lista = 3

    ruleNames =  [ "programa", "comando", "exp", "lista" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NOME=10
    INT=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListParser.ComandoContext)
            else:
                return self.getTypedRuleContext(ListParser.ComandoContext,i)


        def getRuleIndex(self):
            return ListParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ListParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.comando()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ListParser.T__1 or _la==ListParser.NOME):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOME(self):
            return self.getToken(ListParser.NOME, 0)

        def exp(self):
            return self.getTypedRuleContext(ListParser.ExpContext,0)


        def getRuleIndex(self):
            return ListParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = ListParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ListParser.NOME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(ListParser.NOME)
                self.state = 14
                self.match(ListParser.T__0)
                self.state = 15
                self.exp(0)
                pass
            elif token in [ListParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(ListParser.T__1)
                self.state = 17
                self.exp(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOME(self):
            return self.getToken(ListParser.NOME, 0)

        def lista(self):
            return self.getTypedRuleContext(ListParser.ListaContext,0)


        def INT(self):
            return self.getToken(ListParser.INT, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListParser.ExpContext)
            else:
                return self.getTypedRuleContext(ListParser.ExpContext,i)


        def getRuleIndex(self):
            return ListParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ListParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ListParser.NOME]:
                self.state = 21
                self.match(ListParser.NOME)
                pass
            elif token in [ListParser.T__6]:
                self.state = 22
                self.lista()
                pass
            elif token in [ListParser.INT]:
                self.state = 23
                self.match(ListParser.INT)
                pass
            elif token in [ListParser.T__4]:
                self.state = 24
                self.match(ListParser.T__4)
                pass
            elif token in [ListParser.T__5]:
                self.state = 25
                self.match(ListParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ListParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 28
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 29
                        self.match(ListParser.T__2)
                        self.state = 30
                        self.exp(8)
                        pass

                    elif la_ == 2:
                        localctx = ListParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        self.match(ListParser.T__3)
                        self.state = 33
                        self.exp(7)
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListParser.ExpContext)
            else:
                return self.getTypedRuleContext(ListParser.ExpContext,i)


        def getRuleIndex(self):
            return ListParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)




    def lista(self):

        localctx = ListParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ListParser.T__6)
            self.state = 40
            self.exp(0)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ListParser.T__7:
                self.state = 41
                self.match(ListParser.T__7)
                self.state = 42
                self.exp(0)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(ListParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         




