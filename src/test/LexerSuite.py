import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>",85))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>",86))
        
    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>",87))
        
    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_VOTien","_VOTien,<EOF>",88))
        
    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("12","12,<EOF>",89))
        
    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.checkLexeme("0x11","17,<EOF>",90))
    
    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>",91))
    
    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>",92))
        
    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("// VOTIEN\n","<EOF>",93))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>",94))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^",110))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\n" ""","Unclosed string: VOTIEN",95))
    
    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f",96))

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",97))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",98))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",99))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",100))

    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("// This is a single comment.","<EOF>",101))
        self.assertTrue(TestLexer.checkLexeme("abc //Comment next to id","abc,<EOF>",102))
        self.assertTrue(TestLexer.checkLexeme(" //Comment before assignment a <- 5","<EOF>",103))
        self.assertTrue(TestLexer.checkLexeme("/*This is a /* nested comment. */ n","n,<EOF>",104))

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",105))
        self.assertTrue(TestLexer.checkLexeme("ABC","ABC,<EOF>",106))
        self.assertTrue(TestLexer.checkLexeme("_aAbBcC","_aAbBcC,<EOF>",107))
        self.assertTrue(TestLexer.checkLexeme("a___123","a___123,<EOF>",108))
        self.assertTrue(TestLexer.checkLexeme("123abc","123,abc,<EOF>",109))
        self.assertTrue(TestLexer.checkLexeme("?abc","ErrorToken ?",110))

    def test_keyword(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",111))
        self.assertTrue(TestLexer.checkLexeme("return","return,<EOF>",112))
        self.assertTrue(TestLexer.checkLexeme("Return","Return,<EOF>",113))

    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("+-*/","+,-,*,/,<EOF>",114))
        self.assertTrue(TestLexer.checkLexeme("><",">,<,<EOF>",115))

    def test_seperator(self):
        """test seperator"""
        self.assertTrue(TestLexer.checkLexeme("()[],","(,),[,],,,<EOF>",116))
        self.assertTrue(TestLexer.checkLexeme("'","ErrorToken '",117))

    def test_number(self):
        """test number"""
        self.assertTrue(TestLexer.checkLexeme("0","0,<EOF>",118))
        self.assertTrue(TestLexer.checkLexeme("01","0,1,<EOF>",119))
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",120))
        self.assertTrue(TestLexer.checkLexeme("123.1.","123.1,.,<EOF>",121))
        self.assertTrue(TestLexer.checkLexeme("123.-1","123.,-,1,<EOF>",122))
        self.assertTrue(TestLexer.checkLexeme("123.1e123","123.1e123,<EOF>",123))
        self.assertTrue(TestLexer.checkLexeme("1.1e.123","1.1,e,.,123,<EOF>",124))
        self.assertTrue(TestLexer.checkLexeme("123e","123,e,<EOF>",125))
        self.assertTrue(TestLexer.checkLexeme("123.e123","123.e123,<EOF>",126))
        self.assertTrue(TestLexer.checkLexeme("123.0e-001","123.0e-001,<EOF>",127))
        self.assertTrue(TestLexer.checkLexeme("123.0e+123","123.0e+123,<EOF>",128))
        self.assertTrue(TestLexer.checkLexeme("123E-e","123,E,-,e,<EOF>",129))
        self.assertTrue(TestLexer.checkLexeme("123.456","123.456,<EOF>",130))
        self.assertTrue(TestLexer.checkLexeme("-1","-,1,<EOF>",131))

    def test_boolean(self):
        """test boolean"""
        self.assertTrue(TestLexer.checkLexeme("true false","true,false,<EOF>",132))
        self.assertTrue(TestLexer.checkLexeme("TRUE","TRUE,<EOF>",133))

    def test_string(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc sdajw jpsdaf" ""","abc sdajw jpsdaf,<EOF>",134))
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \t" ""","This is a string containing tab \t,<EOF>",135))
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: Where is John?" ""","He asked me: Where is John?,<EOF>",136))
        self.assertTrue(TestLexer.checkLexeme(""" "Nguyen""Van""A" ""","Nguyen,Van,A,<EOF>",137))
        self.assertTrue(TestLexer.checkLexeme(""" "Nguyen Van A ""","Unclosed string: Nguyen Van A ",138))
        self.assertTrue(TestLexer.checkLexeme(""" "Nguyen"" ""","Nguyen,Unclosed string:  ",139))
        self.assertTrue(TestLexer.checkLexeme(""" "String with illegal escape \\y" ""","Illegal escape in string: String with illegal escape \\y",140))
        self.assertTrue(TestLexer.checkLexeme(""" "String with double quote \\"" ""","String with double quote \\\",<EOF>",141))
        self.assertTrue(TestLexer.checkLexeme(""" "String with backslash \\\\" ""","String with backslash \\\\,<EOF>",142))
        self.assertTrue(TestLexer.checkLexeme(""" "String with newline \n" ""","Unclosed string: String with newline ",143))
        self.assertTrue(TestLexer.checkLexeme(""" "String with illegal escape \\a" ""","Illegal escape in string: String with illegal escape \\a",144))
        self.assertTrue(TestLexer.checkLexeme(""" "String with illegal escape \\x" ""","Illegal escape in string: String with illegal escape \\x",145))
        self.assertTrue(TestLexer.checkLexeme(""" "String with a lot special characters: !#$%^&**%^#$%!" ""","String with a lot special characters: !#$%^&**%^#$%!,<EOF>",146))
        self.assertTrue(TestLexer.checkLexeme(""" "Double quote without slash "" ""","Double quote without slash ,Unclosed string:  ",147))

        """Some more test"""
        self.assertTrue(TestLexer.checkLexeme(""" "Nguyen Van A" 123456789 ""","Nguyen Van A,123456789,<EOF>",148))
        self.assertTrue(TestLexer.checkLexeme(""" "Nguyen Van A" mssv 123456789 HCMUT CSE ""","Nguyen Van A,mssv,123456789,HCMUT,CSE,<EOF>",149))

    def test_errorToken(self):
        """test error tokens"""
        self.assertTrue(TestLexer.checkLexeme("?abc","ErrorToken ?",150))
        self.assertTrue(TestLexer.checkLexeme("!abc","!,abc,<EOF>",151))
        self.assertTrue(TestLexer.checkLexeme("#abc","ErrorToken #",152))
        self.assertTrue(TestLexer.checkLexeme("$abc","ErrorToken $",153))
        self.assertTrue(TestLexer.checkLexeme("'abc","ErrorToken '",154))
        self.assertTrue(TestLexer.checkLexeme("^abc","ErrorToken ^",155))
        self.assertTrue(TestLexer.checkLexeme("&abc","ErrorToken &",156))
        self.assertTrue(TestLexer.checkLexeme("|abc","ErrorToken |",157))
        self.assertTrue(TestLexer.checkLexeme(":abc",":,abc,<EOF>",158))
        self.assertTrue(TestLexer.checkLexeme(";abc",";,abc,<EOF>",159))
        self.assertTrue(TestLexer.checkLexeme(".abc",".,abc,<EOF>",160))

        self.assertTrue(TestLexer.checkLexeme("Assignment 1 MiniGo SPECIFICATION","Assignment,1,MiniGo,SPECIFICATION,<EOF>",161))
        self.assertTrue(TestLexer.checkLexeme("1234 4321 0000","1234,4321,0,0,0,0,<EOF>",162))
        self.assertTrue(TestLexer.checkLexeme("00.0e0","0,0.0e0,<EOF>",163))
        self.assertTrue(TestLexer.checkLexeme("00.0e+-*/0","0,0.0,e,+,-,*,/,0,<EOF>",164))
        self.assertTrue(TestLexer.checkLexeme("1+2=3","1,+,2,=,3,<EOF>",165))
        self.assertTrue(TestLexer.checkLexeme("func ABCD","func,ABCD,<EOF>",166))
        self.assertTrue(TestLexer.checkLexeme("func ABCD()","func,ABCD,(,),<EOF>",167))
        self.assertTrue(TestLexer.checkLexeme("ErrorToken","ErrorToken,<EOF>",168))
        self.assertTrue(TestLexer.checkLexeme("abc,asd","abc,,,asd,<EOF>",169))
        self.assertTrue(TestLexer.checkLexeme("<-","<,-,<EOF>",170))
        self.assertTrue(TestLexer.checkLexeme("# # Cannot comment","ErrorToken #",171))
        self.assertTrue(TestLexer.checkLexeme(""" foo(abc,123,"ok") ""","foo,(,abc,,,123,,,ok,),<EOF>",172))
        self.assertTrue(TestLexer.checkLexeme("return true","return,true,<EOF>",173))
        self.assertTrue(TestLexer.checkLexeme("return 0","return,0,<EOF>",174))
        self.assertTrue(TestLexer.checkLexeme("if (x=0) do nothing","if,(,x,=,0,),do,nothing,<EOF>",175))
        self.assertTrue(TestLexer.checkLexeme("for i until x by y","for,i,until,x,by,y,<EOF>",176))
        self.assertTrue(TestLexer.checkLexeme("var x <- 1","var,x,<,-,1,<EOF>",177))
        self.assertTrue(TestLexer.checkLexeme("number x[1]","number,x,[,1,],<EOF>",178))
        self.assertTrue(TestLexer.checkLexeme("bool things <- TRUE","bool,things,<,-,TRUE,<EOF>",179))
        self.assertTrue(TestLexer.checkLexeme(""" string str <- "String things" ""","string,str,<,-,String things,<EOF>",180))
        self.assertTrue(TestLexer.checkLexeme(""" "this string contains all available escape sequence \t\n\r" ""","Unclosed string: this string contains all available escape sequence \t",181))
        self.assertTrue(TestLexer.checkLexeme(""" "this string contains all available escape sequence \t\n\r until reach illegal escape \\x" ""","Illegal escape in string: this string contains all available escape sequence \t\n\n\n until reach illegal escape \\x",182))
        self.assertTrue(TestLexer.checkLexeme(""" "multiple strings""first string""second string" ""","multiple strings,first string,second string,<EOF>",183))
        self.assertTrue(TestLexer.checkLexeme(""" "string type" 123 TRUE ""","string type,123,TRUE,<EOF>",184))
        self.assertTrue(TestLexer.checkLexeme(""" "number in string type 123.e123" ""","number in string type 123.e123,<EOF>",185))
        self.assertTrue(TestLexer.checkLexeme(""" number a <- "ha ha ha" ""","number,a,<,-,ha ha ha,<EOF>",186))
        self.assertTrue(TestLexer.checkLexeme(""" DeprecationWarning: ""","DeprecationWarning,:,<EOF>",187))
        self.assertTrue(TestLexer.checkLexeme(""" "DeprecationWarning: no more error ha ha ^.^" ""","DeprecationWarning: no more error ha ha ^.^,<EOF>",188))
        self.assertTrue(TestLexer.checkLexeme(""" Too tired hjc T.T ""","Too,tired,hjc,T,.,T,<EOF>",189))
        self.assertTrue(TestLexer.checkLexeme(""" "Too tired hjc T.T" ""","Too tired hjc T.T,<EOF>",190))
        self.assertTrue(TestLexer.checkLexeme(""" class Regex() pass ""","class,Regex,(,),pass,<EOF>",191))
        self.assertTrue(TestLexer.checkLexeme(""" __main__ ""","__main__,<EOF>",192))
        self.assertTrue(TestLexer.checkLexeme(""" from x import y ""","from,x,import,y,<EOF>",193))
        self.assertTrue(TestLexer.checkLexeme(""" "##Comment but not a comment" ""","##Comment but not a comment,<EOF>",194))
        self.assertTrue(TestLexer.checkLexeme(""" "Arrrrrggg I want to say that..." ##Haha u are muted ""","Arrrrrggg I want to say that...,ErrorToken #",195))
        self.assertTrue(TestLexer.checkLexeme(""" ">_< >.< :3 => =< :> :< :) :(" """,">_< >.< :3 => =< :> :< :) :(,<EOF>",195))
        self.assertTrue(TestLexer.checkLexeme(""" 0798666xyz "call me" ""","0,798666,xyz,call me,<EOF>",196))
        self.assertTrue(TestLexer.checkLexeme(""" EOF ""","EOF,<EOF>",197))
        self.assertTrue(TestLexer.checkLexeme(""" "3 more to actual EOF" ""","3 more to actual EOF,<EOF>",198))
        self.assertTrue(TestLexer.checkLexeme(""" "Now <EOF>" ""","Now <EOF>,<EOF>",199))
        self.assertTrue(TestLexer.checkLexeme(""" "just kidding, now" <EOF> ""","just kidding, now,<,EOF,>,<EOF>",200))
