from ListVisitor import ListVisitor

class TranspilerVisitor(ListVisitor):

    def visitBooleanTrue(self, context):
        return "True"

    def visitBooleanFalse(self, context):
        return "False"

    def visitInteger(self, context):
        return context.getText()

    def visitPrograma(self, context):
        return "\n".join([self.visit(node) for node in context.children])

    def visitImpressao(self, context):
        return "print({})".format(self.visitChildren(context))

    def visitVariavel(self, context):
        return context.getText()

    def visitAtribuicao(self, context):
        return "{} = {}".format(
            context.NOME().getText(),
            self.visit(context.exp())
        )

    def visitSoma(self, context):
        l_exp = self.visit(context.exp(0))
        r_exp = self.visit(context.exp(1))
        # see: https://stackoverflow.com/a/8294654
        code = """
{l_exp} + {r_exp} if ((type({l_exp}) == type({r_exp})) and (bool not in [type({l_exp}), type({r_exp})])) else (lambda e: (_ for _ in ()).throw(e))(ValueError('It is not possible sum "{l_exp}" with "{r_exp}"'))
"""
        return code.strip().format(l_exp=l_exp, r_exp=r_exp)

    def visitConcatenacao(self, context):
        l_exp = self.visit(context.exp(0))
        r_exp = self.visit(context.exp(1))
        code = """
{l_exp} * {r_exp} if (type({l_exp}) is ListList and type({r_exp}) is ListList) else (lambda e: (_ for _ in ()).throw(e))(ValueError('It is not possible concatenate "{l_exp}" with "{r_exp}"'))
"""
        return code.strip().format(l_exp=l_exp, r_exp=r_exp)

    def visitLista(self, context):
        last_exp = context.exp(0)
        values = [self.visit(last_exp)]
        index = 0
        while last_exp:
            index += 1
            last_exp = context.exp(index)
            if last_exp:
                values.append(self.visit(last_exp))
        return "ListList([{}])".format(", ".join(values))
