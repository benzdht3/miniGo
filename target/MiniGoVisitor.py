# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declarations.
    def visitDeclarations(self, ctx:MiniGoParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declare.
    def visitDeclare(self, ctx:MiniGoParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declareTail.
    def visitDeclareTail(self, ctx:MiniGoParser.DeclareTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDeclare.
    def visitConstDeclare(self, ctx:MiniGoParser.ConstDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDeclare.
    def visitVarDeclare(self, ctx:MiniGoParser.VarDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varType.
    def visitVarType(self, ctx:MiniGoParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init.
    def visitInit(self, ctx:MiniGoParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeDeclare.
    def visitTypeDeclare(self, ctx:MiniGoParser.TypeDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDeclare.
    def visitStructDeclare(self, ctx:MiniGoParser.StructDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceDeclare.
    def visitInterfaceDeclare(self, ctx:MiniGoParser.InterfaceDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameters.
    def visitParameters(self, ctx:MiniGoParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paraTail.
    def visitParaTail(self, ctx:MiniGoParser.ParaTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDeclare.
    def visitFuncDeclare(self, ctx:MiniGoParser.FuncDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDeclare.
    def visitMethodDeclare(self, ctx:MiniGoParser.MethodDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignOp.
    def visitAssignOp(self, ctx:MiniGoParser.AssignOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elsestmt.
    def visitElsestmt(self, ctx:MiniGoParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstmt.
    def visitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initFor.
    def visitInitFor(self, ctx:MiniGoParser.InitForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rangeFor.
    def visitRangeFor(self, ctx:MiniGoParser.RangeForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#contstmt.
    def visitContstmt(self, ctx:MiniGoParser.ContstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayElement.
    def visitArrayElement(self, ctx:MiniGoParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structField.
    def visitStructField(self, ctx:MiniGoParser.StructFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcCall.
    def visitFuncCall(self, ctx:MiniGoParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arguments.
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argTail.
    def visitArgTail(self, ctx:MiniGoParser.ArgTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodCall.
    def visitMethodCall(self, ctx:MiniGoParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr8.
    def visitExpr8(self, ctx:MiniGoParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayInit.
    def visitArrayInit(self, ctx:MiniGoParser.ArrayInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLit.
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literalTail.
    def visitLiteralTail(self, ctx:MiniGoParser.LiteralTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structLit.
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structElement.
    def visitStructElement(self, ctx:MiniGoParser.StructElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elementTail.
    def visitElementTail(self, ctx:MiniGoParser.ElementTailContext):
        return self.visitChildren(ctx)



del MiniGoParser