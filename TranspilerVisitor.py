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
        return "{} + {}".format(
            self.visit(context.exp(0)),
            self.visit(context.exp(1))
        )

    def visitConcatenacao(self, context):
        return "{} + {}".format(
            self.visit(context.exp(0)),
            self.visit(context.exp(1))
        )

    def visitLista(self, context):
        last_exp = context.exp(0)
        values = [self.visit(last_exp)]
        index = 0
        while last_exp:
            index += 1
            last_exp = context.exp(index)
            if last_exp:
                values.append(self.visit(last_exp))
        return "[{}]".format(", ".join(values))
