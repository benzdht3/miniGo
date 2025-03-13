from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

class ASTGeneration(MiniGoVisitor):
    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visit(ctx.declarations())


    # Visit a parse tree produced by MiniGoParser#declarations.
    def visitDeclarations(self, ctx:MiniGoParser.DeclarationsContext):
        return Program(self.visit(ctx.declare()) + self.visit(ctx.declareTail()))


    # Visit a parse tree produced by MiniGoParser#declare.
    def visitDeclare(self, ctx:MiniGoParser.DeclareContext):
        if ctx.constDeclare():
            return [self.visit(ctx.constDeclare())]
        elif ctx.varDeclare():
            return [self.visit(ctx.varDeclare())]
        elif ctx.typeDeclare():
            return [self.visit(ctx.typeDeclare())]
        elif ctx.funcDeclare():
            return [self.visit(ctx.funcDeclare())]


    # Visit a parse tree produced by MiniGoParser#declareTail.
    def visitDeclareTail(self, ctx:MiniGoParser.DeclareTailContext):
        if ctx.declare():
            return self.visit(ctx.declare()) + self.visit(ctx.declareTail())
        return []


    # Visit a parse tree produced by MiniGoParser#constDeclare.
    def visitConstDeclare(self, ctx:MiniGoParser.ConstDeclareContext):
        return ConstDecl(self.visit(ctx.identifier()), None, self.visit(ctx.init()))


    # Visit a parse tree produced by MiniGoParser#varDeclare.
    def visitVarDeclare(self, ctx:MiniGoParser.VarDeclareContext):
        varType, varInit = self.visit(ctx.modify())
        return varDeclare(self.visit(ctx.identifier()), varType, varInit)


    # Visit a parse tree produced by MiniGoParser#modify.
    def visitModify(self, ctx:MiniGoParser.ModifyContext):
        varType, varInit = None
        if ctx.arrayType(): varType = self.visit(ctx.arrayType())
        if ctx.varType(): varType = self.visit(ctx.varType())
        if ctx.identifier(): varType = self.visit(ctx.identifier())
        if ctx.init(): varInit = self.visit(ctx.init())

        return varType, varInit


    # Visit a parse tree produced by MiniGoParser#varType.
    def visitVarType(self, ctx:MiniGoParser.VarTypeContext):
        if ctx.INT: return IntType()
        if ctx.FLOAT: return FloatType()
        if ctx.STRING: return StringType()
        if ctx.BOOL: return BoolType()


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        eleType = None
        if ctx.varType(): eleType = self.visit(ctx.varType())
        if ctx.STRUCT: eleType = 'STRUCT'
        if ctx.identifier(): eleType = self.visit(ctx.identifier())

        return ArrayType([self.visit(dim) for dim in ctx.demensions], eleType)


    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        if ctx.INTLIT: return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.identifier(): return self.visit(ctx.identifier())


    # Visit a parse tree produced by MiniGoParser#init.
    def visitInit(self, ctx:MiniGoParser.InitContext):
        if ctx.expr(): return self.visit(ctx.expr())
        if ctx.arrayInit(): return self.visit(ctx.arrayInit)


    # Visit a parse tree produced by MiniGoParser#typeDeclare.
    def visitTypeDeclare(self, ctx:MiniGoParser.TypeDeclareContext):
        if ctx.structDeclare():
            structType = StructType(self.visit(ctx.identifier()), self.visit(ctx.structDeclare()), [])
            return ParamDecl(self.visit(ctx.identifier()), structType)
        if ctx.interfaceDeclare():
            interfaceType = InterfaceType(self.visit(ctx.identifier()), self.visit(ctx.interfaceDeclare()))
            return ParamDecl(self.visit(ctx.identifier()), interfaceType)


    # Visit a parse tree produced by MiniGoParser#structDeclare.
    def visitStructDeclare(self, ctx:MiniGoParser.StructDeclareContext):
        return [self.visit(f) for f in ctx.field()]


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        fieldType = None
        if ctx.varType(): fieldType = self.visit(ctx.varType())
        if ctx.structDeclare(): fieldType = self.visit(ctx.structDeclare())
        if ctx.arrayType(): fieldType = self.visit(ctx.arrayType())
        if ctx.interfaceDeclare(): fieldType = self.visit(ctx.interfaceDeclare())
        if ctx.identifier.size() == 2: fieldType = self.visit(ctx.identifier.get(1))

        return self.visit(ctx.identifier.get(0)), fieldType


    # Visit a parse tree produced by MiniGoParser#interfaceDeclare.
    def visitInterfaceDeclare(self, ctx:MiniGoParser.InterfaceDeclareContext):
        return [self.visit(prototype) for prototype in ctx.method]
    
    # Visit a parse tree produced by MiniGoParser#prototype.
    def visitPrototype(self, ctx:MiniGoParser.PrototypeContext):
        params = []
        retType = VoidType()
        if ctx.parameters(): params = self.visit(ctx.parameters()) + self.visit(ctx.paraTail())
        if ctx.varType(): retType = self.visit(ctx.varType()) 
        if ctx.arrayType(): retType = self.visit(ctx.arrayType())
        if ctx.identifier.size() == 2: retType = self.visit(ctx.identifier.get(1))

        return Prototype(self.visit(ctx.identifier.get(0)), params, retType)


    # Visit a parse tree produced by MiniGoParser#parameters.
    def visitParameters(self, ctx:MiniGoParser.ParametersContext):
        typs = []
        if ctx.varType(): typs = [self.visit(ctx.varType())] * (ctx.COMMA.size() + 1)
        if ctx.arrayType(): typs = [self.visit(ctx.arrayType())] * (ctx.COMMA.size() + 1)
        if ctx.identifier(): typs = [self.visit(ctx.identifier())] * (ctx.COMMA.size() + 1)

        return [([self.visit(id) for id in ctx.identifier()], typs)]

    # Visit a parse tree produced by MiniGoParser#paraTail.
    def visitParaTail(self, ctx:MiniGoParser.ParaTailContext):
        if ctx.parameters():
            return self.visit(ctx.parameters()) + self.visit(ctx.paraTail())
        
        return []


    # Visit a parse tree produced by MiniGoParser#funcDeclare.
    def visitFuncDeclare(self, ctx:MiniGoParser.FuncDeclareContext):
        name, params, retType = self.visit(ctx.method())
        body = []
        if ctx.stmt(): body = [self.visit(stmt) for stmt in ctx.stmt()]

        return FuncDecl(name, params, retType, Block(body))
    
    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        params = []
        retType = VoidType()
        if ctx.parameters(): params = self.visit(ctx.parameters()) + self.visit(ctx.paraTail())
        if ctx.varType(): retType = self.visit(ctx.varType()) 
        if ctx.arrayType(): retType = self.visit(ctx.arrayType())
        if ctx.identifier.size() == 2: retType = self.visit(ctx.identifier.get(1))

        return self.visit(ctx.identifier.get(0)), params, retType


    # Visit a parse tree produced by MiniGoParser#methodDeclare.
    def visitMethodDeclare(self, ctx:MiniGoParser.MethodDeclareContext):
        pass


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        if ctx.varDeclare(): return self.visit(ctx.varDeclare())
        if ctx.constDeclare(): return self.visit(ctx.constDeclare())
        if ctx.statement(): return self.visit(ctx.statement())



    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        if ctx.assignment(): return self.visit(ctx.assignment())
        if ctx.ifstmt(): return self.visit(ctx.ifstmt())
        if ctx.forstmt(): return self.visit(ctx.forstmt())
        if ctx.breakstmt(): return self.visit(ctx.breakstmt())
        if ctx.contstmt(): return self.visit(ctx.contstmt())
        if ctx.funcCall(): return self.visit(ctx.funcCall())
        if ctx.methodCall(): return self.visit(ctx.methodCall())
        if ctx.returnstmt(): return self.visit(ctx.returnstmt())


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        rhs = None
        if ctx.expr(): rhs = self.visit(ctx.rhs())
        else: rhs = self.visit(ctx.arrayInit())

        return Assign(self.visit(ctx.lhs()), rhs)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.DOT: 
            receiver = None
            if ctx.arrayCell(): receiver = self.visit(ctx.arrayReceiver())
            else: receiver = self.visit(ctx.identifier().get(0))
            fields = [self.visit(child) for child in ctx.getChildren() if isinstance(child, (MiniGoParser.IdentifierContext, MiniGoParser.ArrayCellContext))][1:]
             
            return reduce(lambda field, acc: FieldAccess(receiver, acc), reversed(fields), receiver)
        elif ctx.arrayCell(): return self.visit(ctx.arrayCell())
        else: return self.visit(ctx.identifier())

    

    # Visit a parse tree produced by MiniGoParser#arrayCell.
    def visitArrayCell(self, ctx:MiniGoParser.ArrayCellContext):
        return ArrayCell(self.visit(ctx.identifier()),[self.visit(idx) for idx in ctx.index()])


    # Visit a parse tree produced by MiniGoParser#assignOp.
    def visitAssignOp(self, ctx:MiniGoParser.AssignOpContext):
        pass


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        body = []
        if ctx.stmt(): body = [self.visit(stmt) for stmt in ctx.stmt()]
        elsestmt = None
        if ctx.elsestmt(): elsestmt = Block(self.visit(ctx.elsestmt()))

        return If(self.visit(ctx.expr()), Block(body), elsestmt)


    # Visit a parse tree produced by MiniGoParser#elsestmt.
    def visitElsestmt(self, ctx:MiniGoParser.ElsestmtContext):
        if ctx.ifstmt(): return [self.visit(ctx.ifstmt())]
        if ctx.stmt(): return [self.visit(stmt) for stmt in ctx.stmt()]
        
        return []


    # Visit a parse tree produced by MiniGoParser#forstmt.
    def visitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        body = []
        if ctx.stmt(): body = [self.visit(stmt) for stmt in ctx.stmt()]
        if ctx.expr(): return ForBasic(self.visit(ctx.expr()), Block(body))
        if ctx.initFor():
            init, cond, upda = self.visit(ctx.initFor())

            return ForStep(init, cond, upda, Block(body))
        else: 
            idx, value, arr = self.visit(ctx.rangeFor())

            return ForEach(idx, value, arr, Block(body))


    # Visit a parse tree produced by MiniGoParser#initFor.
    def visitInitFor(self, ctx:MiniGoParser.InitForContext):
        init = None
        if ctx.VAR:
            typ = None
            if ctx.varType(): typ = self.visit(ctx.varType())
            if ctx.arrayType(): typ = self.visit(ctx.arrayType())

            init = VarDecl(self.visit(ctx.identifier()), typ, self.visit(ctx.init()))
        else: init = self.visit(self.visit(ctx.assignment_for().get(0)))

        return init, self.visit(ctx.expr()), self.visit(ctx.assignment_for().get(1))


    # Visit a parse tree produced by MiniGoParser#assignment_for.
    def visitAssignment_for(self, ctx:MiniGoParser.Assignment_forContext):
        return Assign(self.visit(ctx.identifier()), self.visit(ctx.literal()))


    # Visit a parse tree produced by MiniGoParser#rangeFor.
    def visitRangeFor(self, ctx:MiniGoParser.RangeForContext):
        arr = None
        if ctx.literal(): arr = self.visit(ctx.arr())
        if ctx.arrayElement(): arr = self.visit(ctx.arrayElement())
        else: arr = self.visit(ctx.identifier().get(2))

        return self.visit(ctx.identifier().get(0)), self.visit(ctx.identifier().get(1)), arr


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#contstmt.
    def visitContstmt(self, ctx:MiniGoParser.ContstmtContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        exp = None
        if ctx.expr():  exp = self.visit(ctx.expr())

        return Return(exp)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        if ctx.expr(): return BinaryOp(ctx.OR.getText(), self.visit(ctx.expr()), self.visit(ctx.expr1()))
        
        return self.visit(ctx.expr1())


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        if ctx.expr1(): return BinaryOp(ctx.AND.getText(), self.visit(ctx.expr1()), self.visit(ctx.expr2()))
        
        return self.visit(ctx.expr2())


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        if ctx.expr2(): 
            op = ''
            if ctx.EQ: op = ctx.EQ.getText()
            if ctx.UNEQ: op = ctx.UNEQ.getText()
            if ctx.LESS: op = ctx.LESS.getText()
            if ctx.LESSEQ: op = ctx.LESSEQ.getText()
            if ctx.GREATER: op = ctx.GREATER.getText()
            if ctx.GREATEREQ: op = ctx.GREATEREQ.getText()

            return BinaryOp(op, self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        
        return self.visit(ctx.expr3())


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        if ctx.expr3(): 
            op = ''
            if ctx.ADD: op = ctx.ADD.getText()
            if ctx.SUBTR: op = ctx.SUBTR.getText()

            return BinaryOp(op, self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        
        return self.visit(ctx.expr4())


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        if ctx.expr4(): 
            op = ''
            if ctx.MUL: op = ctx.MUL.getText()
            if ctx.DIV: op = ctx.DIV.getText()
            if ctx.MOD: op = ctx.MOD.getText()

            return BinaryOp(op, self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        
        return self.visit(ctx.expr5())


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        unary_ops = [] 
        if ctx.NOT or ctx.SUBTR: 
            unary_ops = [op.getText() for op in ctx.getChildren() if op.getText() in [ctx.NOT, ctx.SUBTR]]
            return reduce(lambda acc, op: UnaryOp(op, acc), reversed(unary_ops), self.visit(ctx.expr6()))
        
        return self.visit(ctx.expr6())


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        if ctx.arrayElement(): return self.visit(self.visit(ctx.arrayElement()))
        if ctx.methodCallExpr(): return self.visit(self.visit(ctx.methodCallExpr()))
        if ctx.expr7(): return self.visit(self.visit(ctx.expr7()))


    # Visit a parse tree produced by MiniGoParser#arrayElement.
    def visitArrayElement(self, ctx:MiniGoParser.ArrayElementContext):
        arr = None
        if ctx.expr8(): arr = self.visit(ctx.expr8())
        else: arr = self.visit(ctx.funcCall())

        return self.visit(arr, [self.visit(idx) for idx in ctx.index()])


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MiniGoParser#structField.
    def visitStructField(self, ctx:MiniGoParser.StructFieldContext):
        receiver = None
        if ctx.arrayElement(): receiver = self.visit(ctx.arrayElement())
        elif ctx.structLit(): receiver = self.visit(ctx.structLit())
        elif ctx.expr(): receiver = self.visit(ctx.expr())
        elif ctx.BOOLIT: receiver = self.visit(ctx.BOOLIT.getText())
        elif ctx.funcCallReceiver(): receiver = self.visit(ctx.funcCallReceiver())
        else: receiver = self.visit(ctx.identifier().get(0))
        fields = [self.visit(child) for child in ctx.getChildren() 
              if isinstance(child, (MiniGoParser.IdentifierContext, 
                                    MiniGoParser.FuncCallContext, 
                                    MiniGoParser.ArrayCellContext, 
                                    MiniGoParser.FuncArrayCellContext))][1:]

        return reduce(lambda acc, field: FieldAccess(receiver, acc), reversed(fields), receiver)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        if ctx.structField(): return self.visit(ctx.structField())
        if ctx.funcCall(): return self.visit(ctx.funcCall())
        if ctx.expr8(): return self.visit(ctx.expr8())
    
    
    # Visit a parse tree produced by MiniGoParser#funcArrayCell.
    def visitFuncArrayCell(self, ctx:MiniGoParser.FuncArrayCellContext):
        return ArrayCell(self.visit(ctx.funcCall()), [self.visit(idx) for idx in ctx.index()])


    # Visit a parse tree produced by MiniGoParser#funcCall.
    def visitFuncCall(self, ctx:MiniGoParser.FuncCallContext):
        args = []
        if ctx.arguments(): args = self.visit(ctx.args())

        return FuncCall(self.visit(ctx.identifier()), args)
    
    
     # Visit a parse tree produced by MiniGoParser#funcCallReceiver.
    def visitFuncCallReceiver(self, ctx:MiniGoParser.FuncCallReceiverContext):
        args = []
        if ctx.arguments(): args = self.visit(ctx.args())

        return FuncCall(self.visit(ctx.identifier()), args)


    # Visit a parse tree produced by MiniGoParser#arguments.
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.argTail())


    # Visit a parse tree produced by MiniGoParser#argTail.
    def visitArgTail(self, ctx:MiniGoParser.ArgTailContext):
        if ctx.expr(): return [self.visit(ctx.expr())] + self.visit(ctx.argTail())

        return []


    # Visit a parse tree produced by MiniGoParser#methodCallExpr.
    def visitMethodCallExpr(self, ctx:MiniGoParser.MethodCallExprContext):
        metName, args = self.visit(ctx.funcCallMeth())
        return MethCall(self.visit(ctx.identifier()), metName, args)
    
    
     # Visit a parse tree produced by MiniGoParser#funcCallMeth.
    def visitFuncCallMeth(self, ctx:MiniGoParser.FuncCallMethContext):
        args = []
        if ctx.arguments(): args = self.visit(ctx.args())

        return self.visit(ctx.identifier()), args



    # Visit a parse tree produced by MiniGoParser#methodCall.
    def visitMethodCall(self, ctx:MiniGoParser.MethodCallContext):
        metName, args = self.visit(ctx.funcCallMeth())
        receiver = None
        if ctx.identifier(): receiver = self.visit(ctx.identifier())
        else: receiver = self.visit(ctx.arrayCell())

        return MethCall(receiver, metName, args)


    # Visit a parse tree produced by MiniGoParser#expr8.
    def visitExpr8(self, ctx:MiniGoParser.Expr8Context):
        if ctx.expr(): return self.visit(ctx.expr())
        if ctx.literal(): return self.visit(ctx.literal())
        if ctx.arrayInit(): return self.visit(ctx.arrayInit())


    # Visit a parse tree produced by MiniGoParser#arrayInit.
    def visitArrayInit(self, ctx:MiniGoParser.ArrayInitContext):
        dimens, eleType = self.visit(ctx.arrayTypeInit)
        value = []
        if ctx.arrayLit(): value = self.visit(ctx.arrayLit())

        return ArrayLiteral(dimens, eleType, value)
    

    # Visit a parse tree produced by MiniGoParser#arrayTypeInit.
    def visitArrayTypeInit(self, ctx:MiniGoParser.ArrayTypeInitContext):
        eleType = None
        if ctx.varType(): eleType = self.visit(ctx.varType())
        if ctx.STRUCT: eleType = 'STRUCT'
        if ctx.identifier(): eleType = self.visit(ctx.identifier())

        return [self.visit(dim) for dim in ctx.demensions], eleType


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INTLIT: return IntLiteral(int(ctx.INTLIT.getText()))
        if ctx.DECIMAL: return IntLiteral(int(ctx.DECIMAL.getText()))
        if ctx.BINARY: return IntLiteral(int(ctx.BINARY.getText()))
        if ctx.OCTAL: return IntLiteral(int(ctx.OCTAL.getText()))
        if ctx.HEXADECIMAL: return IntLiteral(int(ctx.HEXADECIMAL.getText()))
        if ctx.FLOATLIT: return FloatLiteral(float(ctx.FLOATLIT.getText()))
        if ctx.BOOLLIT: return BooleanLiteral(bool(ctx.BOOLLIT.getText()))
        if ctx.STRINGLIT: return StringLiteral(ctx.STRINGLIT.getText())
        if ctx.structLit: 
            name, elements = self.visit(ctx.structLit())
            return StructLiteral(name, elements)
        if ctx.identifier: return self.visit(ctx.identifier())
        if ctx.NIL: return NilLiteral()


    # Visit a parse tree produced by MiniGoParser#arrayLit.
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        val = []
        if ctx.literal(): val = [self.visit(ctx.literal())]
        else: val = [self.visit(ctx.arrayLit())]
        
        return val  + self.visit(ctx.literalTail()) 


    # Visit a parse tree produced by MiniGoParser#literalTail.
    def visitLiteralTail(self, ctx:MiniGoParser.LiteralTailContext):
        if ctx.literalTail():
            val = []
            if ctx.literal(): val = [self.visit(ctx.literal())]
            elif ctx.arrayLit(): 
                val = [self.visit(ctx.arrayLit())]
            
            return val  + self.visit(ctx.literalTail())
        
        return []


    # Visit a parse tree produced by MiniGoParser#structLit.
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        elements = []
        if ctx.structElement(): elements = self.visit(ctx.structElement())

        return StructLiteral(self.visit(ctx.identifier()), elements)


    # Visit a parse tree produced by MiniGoParser#structElement.
    def visitStructElement(self, ctx:MiniGoParser.StructElementContext):
        return [(self.visit(ctx.identifier()), self.visit(ctx.expr()))] + self.visit(ctx.elementTail())


    # Visit a parse tree produced by MiniGoParser#elementTail.
    def visitElementTail(self, ctx:MiniGoParser.ElementTailContext):
        if ctx.structElement():
            return [(self.visit(ctx.identifier()), self.visit(ctx.expr()))] + self.visit(ctx.elementTail())
        
        return []


    # Visit a parse tree produced by MiniGoParser#identifier.
    def visitIdentifier(self, ctx:MiniGoParser.IdentifierContext):
        return Id(ctx.ID.getText())


    # Visit a parse tree produced by MiniGoParser#endStmt.
    def visitEndStmt(self, ctx:MiniGoParser.EndStmtContext):
        pass



