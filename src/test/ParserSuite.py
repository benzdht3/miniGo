import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = 1;","successful", 301))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = true;","successful", 302))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [5][0]string{1, \"string\"};","successful", 303))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [1.]ID{1, 3};","Error on line 1 col 17: 1.", 304))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = Person{name: \"Alice\", age: 30};","successful", 305))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", 306))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", 307))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = ca.foo(132) + b.c[2];","successful", 308))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = a.a.foo();","successful", 309))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.checkParser("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", 310))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.checkParser("""
            const VoTien = a.b() + 2;
        ""","successful", 311))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.checkParser("""
            func VoTien(x int, y int) int {}
            func VoTien1() [2][3] ID {}         
            func VoTien2() {}                                       
        ""","successful", 312))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) VoTien(x int) int {}  
            func (c Calculator) VoTien() ID {}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {}                                                      
        ""","successful", 313))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }
            type VoTien struct {}                                                                       
        ""","successful", 314))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }
            type VoTien struct {}                                                                       
        ""","successful", 315))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type VoTien interface {}                                                                       
        ""","successful", 316))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", 317))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", 318))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                if (x > 10) {} 
                if (x > 10) {
                  
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", 319))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                for i < 10 {}
                for i := 0; i < 10; i += 1 {}
                for index, value := range array {}
            }
        ""","successful", 320))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", 321))

    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 0b11;                         
        ""","successful", 322))

    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", 323))

    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2][3][a + 2];                         
        ""","successful", 324))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int{1};                         
        ""","Error on line 2 col 28: int", 325))

    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);                         
        ""","successful", 326))

    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = (a + 23) * 3 && (1 + 1);                         
        ""","successful", 327))

    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = ID {a : 2}.c[2] + 2[2] + true.foo() + (2).foo();                         
        ""","successful", 328))

    def test_029(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        ""","successful", 329))

    def test_030(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", 330))

    def test_031(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = a.foo()[2];
        ""","successful", 331))

    def test_032(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]ID
            ""","Error on line 2 col 28: \n", 332))

    def test_033(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y int) int  {};
""","Error on line 2 col 43: ;", 333))
        
    def test_034(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x, c int) {}
""","Error on line 2 col 29: ,", 334))
        
    def test_035(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {};
""","Error on line 2 col 37: ;", 335))
        
    def test_036(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    }""","successful", 336))
    
    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2, 3];                         
        ""","Error on line 2 col 31: ,", 337))

    def test_038(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{};                         
        ""","Error on line 2 col 35: }", 338))

    def test_039(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {};                         
        ""","successful", 339))

    def test_040(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
""","Error on line 4 col 23: a", 340))
        
    def test_041(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo() += 2;       
                                    }""","Error on line 3 col 49: +=", 341))
        
    def test_042(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2].b := 2;       
                                    }""","successful", 342))
        
    def test_043(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) 
                                        {
                                            if (){}
                                        } 
                                    }""","Error on line 5 col 49: )", 343))
    
    def test_044(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) 
                                        {
                                            if (1){} else {}

                                        } else if(2)
                                        {
                                        }
                                    }""","successful", 344))
        
    def test_045(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) 
                                        {
                                        } else if(1)
                                        {
                                        }else if(1)
                                        {
                                        }else if(2)
                                        {
                                        }else 
                                        {
                                        }
                                    }""","successful", 345))
        
    def test_046(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true {}
                                    }""","successful", 346))
        
    def test_047(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for const i = 0; i < 10; i += 1 {
                                            // loop body
                                        }
                                    }""","Error on line 3 col 45: const", 347))
        
    def test_048(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                            // loop body
                                        }
                                    }""","successful", 348))
        
    def test_049(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr[2] {
                                        }
                                    }""","successful", 349))
    
    def test_050(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    }""","successful", 350))
       
    def test_051(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {}
                                        else if(2) {return string;}
                                        else if(3) {reutrn int;}
                                    }""","Error on line 4 col 60: string", 351))

    def test_simpler_program(self):
        input = [
        """func main() { return 1; }
        """,#1
        #variable declaration
        #booltype
        """var a boolean ;
        """,#2
        """var a boolean = true ;
        """,#3
        """var a boolean = false ;
        """,#4
        """var 1a boolean ;
        """,#5
        """var true boolean ;
        """,#6
        """var a boolean = "true" ;
        """,#7
        """var a boolean -> true ;
        """,#8
        """var a boolean == true ;
        """,#9
        #numbertype
        """var 1 int ;
        """,#10
        #211-220
        """var a int ;
        """,#11
        """var a int = 1 ;
        """,#12
        """var a int a = 1.1e123 ;
        """,#13
        """var int a = true ;
        """,#14
        """var a int = "string things" ;
        """,#15
        """var a int <-> 1 ;
        """,#16
        """var int int ;
        """,#17
        #stringtype
        """var string string ;
        """,#18
        """var a string ;
        """,#19
        """var a string = 123 ;
        """,#20
        """var a string = string ;
        """,#21
        """var a string = int ;
        """,#22
        """var a string = boolean ;
        """,#23
        """var a string = "string" ;
        """,#24
        """var a string = true ;
        """,#25
        #variable declare without semicolon
        """var a int""",#26
        """var a string""",#27
        """var a boolean""",#28
        #vartype and arraytype
        """var a ;""",#29
        """var a = 1 ;
        """,#30
        """var a = string ;
        """,#31
        """var a = "string things" ;
        """,#32
        """var a = true ;
        """,#33
        """var a = var ;
        """,#34
        """var a = dynamic ;
        """,#35
        """var dynamic var ;
        """,#36
        """var a struct ;
        """,#37
        """var a struct a = 1 ;
        """,#38
        """var dynamic struct = b ;
        """,#39
        ##array
        """var a []int ;
        """,#40
        """var a [1]int ;
        """,#41
        """var a [abc]int ;
        """,#42
        """var a [1]int = {1,2,3} ;
        """,#43
        """var a [1][2]int = {{1,2},{1,2}} ;
        """,#44
        """var a [1][3]int = {{abc,"string",1},123,{"a b c",123}} ;
        """,#45
        """var a [1]int = {123 ;""",#46
        """var a (1)int ;
        """,#47
        #arithmetic expression
        """var a = a+b ;
        """,#48
        """var a = a-b*c/1%-1 ;
        """,#49
        #logic
        """var a = a && b ;
        """,#50
        """var a = !b ;
        """,#51
        """var a = a ! b ;
        """,#52
        """var a = a || !b ;
        """,#53
        #struct
        """var a = a.a ;
        """,#54
        #function call
        """var a = foo() ;
        """,#55
        """var a = foo(a,b,c,d,e,f) ;
        """,#56
        """var a = foo1(foo2(foo3(1,a,"string"))) ;
        """,#57
        #function declaration
        """func foo() {} 
        """,#58
        """FUNC foo() {}
        """,#59
        """func 1foo() {}
        """,#60
        """func foo()""",#61
        """func isPrime(x int) {}
        """,#62
        """func foo(x int, y string, z boolean) {}
        """,#63
        """func foo(x var) {}
        """,#64
        """func foo(x int, y string) int {
            return x + y ;
        }
        """,#65
        """func foo(x int, y string) {
            x := 1;
        }
        """,#66
        #assignment
        """func main() {
            aPI := 3.14 ;
            l[3] += val * aPI ;
        }
        """,#67
        """func main() {
            a /= 1 ;
            str *= "Nguyen Van A" ;
            "abc" %= 1 ;
        }
        """,#68
        """func main() {
            a := 1 b := 2
        }
        """,#69
        #if
        """func main() {
            if (areDivisor(num1,num2)) { writeString("yes"); }
        }
        """,#70
        """func main() {
            if (areDivisor(num1,num2)) {
                writeString("yes")
            } else {
                writeString("no")
            }
        }
        """,#71
        """func main() {
            if (areDivisor(num1,num2)) {
                writeString("yes");
            } else if (areDivisor(num1,num2)) {
                if(num1 < num2) { doNothing(); }
            } else { writeString("no"); }
        }
        """,#72
        """func main() {
            if a < b { donothing(); }
        }
        """,#73
        """func main() {
            if ((a<b)) { donothing(); }
        }
        """,#74
        """func main() {
            if ((a<b)(a<c)) {
                donothing()
            }
        }""",#75
        """func main() {
            IF (a<b) { donthing(); }
        }
        """,#76
        #for
        """func main() {
            for i := 0; i >= 0; i += 1 {
                writeNumber(i) ;
            }
        }
        """,#77
        """func main() {
            for i > x / 2 {
                if (x/i==0) {return false;}
            }
        }
        """,#78
        """func main() {
            fOr i := 0, i > x / 2, i -= 1 {
                donothing()
            }
        }
        """,#79
        """func main() {
            for index, value := range {1,2,3} {
                donothing()
            }
        }
        """,#80
        #Break
        """func main() {
            for index, value := range {1,2,3} {
                donothing()
                if (i>y) { break; }
            }
        }
        """,#81
        """break ;
        """,#82
        """func main() {
            break ;
        }
        """,#83
        """func main() {
            break ;
        }
        """,#84
        """func main() {
            break; break; break;
        }
        """,#85
        """func main() {
            break
            break
            break
        }
        """,#86
        #continue
        """continue ;
        """,#87
        """func main() {
            continue
        }
        """,#88
        """func main() {
            if (x>y) {
                continue
            } else { break ; }
        }
        """,#89
        """func main() {
            continue ,
        }
        """,#90
        #return
        """func main() {
            return ; }
        """,#91
        """func main() {
            return a + b * c -d / z + "string"
        }
        """,#92
        """func main() {
            return ,
        }
        """,#93
        """func main() {
            return}""",#94
        """func areDivisors(num1 int, num2 int) {
            return ((num1 % num2 == 0) || (num2 % num1 == 0))
        }
        """,#95
        """func main() {
            var num1 = readNumber() ;
            var num2 = readNumber() ;

            if (areDivisors(num1, num2)) {
                writeString("Yes")
            } else {
                writeString("No")
            }
        }
        """,#96
        """func isPrime(x int) {}
        func main() {
            var x int = readNumber() ;
            if (isPrime(x)) {
                writeString("Yes")
            } else { writeString("No"); }
        }
        func isPrime(x int) {
            if (x <= 1) { return false; }
            var i = 2 ;
            for var i int = 0; i > x / 2; i += 1 {
                if (x / i == 0) {return false;}
            }
            return true
        }
        """
        ]
        expect = [

            "successful",#1
            "successful",#2
            "successful",#3
            "successful",#4
            "Error on line 1 col 5: 1",#5
            "successful",#6
            "successful",#7
            "Error on line 1 col 15: -",#8
            "Error on line 1 col 15: ==",#9
            "Error on line 1 col 5: 1",#10
            #211-220
            "successful",#11
            "successful",#12
            "Error on line 1 col 11: a",#13
            "Error on line 1 col 5: int",#14
            "successful",#15
            "Error on line 1 col 11: <",#16
            "Error on line 1 col 5: int",#17
            "Error on line 1 col 5: string",#18
            "successful",#19
            "successful",#20
            "Error on line 1 col 16: string",#21
            "Error on line 1 col 16: int",#22
            "Error on line 1 col 16: boolean",#23
            "successful",#24
            "successful",#25
            "Error on line 1 col 10: <EOF>",#26
            "Error on line 1 col 13: <EOF>",#27
            "Error on line 1 col 14: <EOF>",#28
            "successful",#29
            "successful",#30
            "Error on line 1 col 9: string",#31
            "successful",#32
            "successful",#33
            "Error on line 1 col 9: var",#34
            "successful",#35
            "Error on line 1 col 13: var",#36
            "Error on line 1 col 7: struct",#37
            "Error on line 1 col 7: struct",#38
            "Error on line 1 col 13: struct",#39
            "Error on line 1 col 8: ]",#40
            "successful",#41
            "successful",#42
            "successful",#43
            "successful",#44
            "successful",#45
            "Error on line 1 col 21: ;",#46
            "Error on line 1 col 7: (",#47
            "successful",#48
            "successful",#49
            "successful",#50
            "successful",#51
            "Error on line 1 col 11: !",#52
            "successful",#53
            "successful",#54
            "successful",#55
            "successful",#56
            "successful",#57
            "successful",#58
            "Error on line 1 col 1: FUNC",#59
            "Error on line 1 col 6: 1",#60
            "Error on line 1 col 11: <EOF>",#61
            "successful",#62
            "successful",#63
            "Error on line 1 col 12: var",#64
            "successful",#65
            "successful",#66
            "successful",#67
            "Error on line 4 col 19: %=",#68
            "Error on line 2 col 20: b",#69
            "successful",#70
            "successful",#71
            "successful",#72
            "Error on line 2 col 16: a",#73
            "successful",#74
            "Error on line 2 col 22: (",#75
            "Error on line 2 col 22: {",#76
            "successful",#77
            "successful",#78
            "Error on line 2 col 17: i",#79
            "successful",#80
            "successful",#81
            "Error on line 1 col 1: break",#82
            "successful",#83
            "successful",#84
            "successful",#85
            "successful",#86
            "Error on line 1 col 1: continue",#87
            "successful",#88
            "successful",#89
            "Error on line 2 col 22: ,",#90
            "successful",#91
            "successful",#92
            "Error on line 2 col 20: ,",#93
            "Error on line 2 col 19: }",#94
            "successful",#95
            "successful",#96
            "successful",#97
        ]
        for i in range(0,len(input),1):
            self.assertTrue(TestParser.checkParser(input[i],expect[i],200+i+1))

