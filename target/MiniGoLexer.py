# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u01fb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\7\65\u014d\n\65\f\65\16")
        buf.write("\65\u0150\13\65\3\66\3\66\3\66\3\66\5\66\u0156\n\66\3")
        buf.write("\67\3\67\3\67\3\67\5\67\u015c\n\67\38\38\38\78\u0161\n")
        buf.write("8\f8\168\u0164\138\58\u0166\n8\38\38\78\u016a\n8\f8\16")
        buf.write("8\u016d\138\38\38\38\78\u0172\n8\f8\168\u0175\138\58\u0177")
        buf.write("\n8\38\38\38\38\58\u017d\n8\38\68\u0180\n8\r8\168\u0181")
        buf.write("\58\u0184\n8\39\39\39\69\u0189\n9\r9\169\u018a\59\u018d")
        buf.write("\n9\3:\3:\3:\6:\u0192\n:\r:\16:\u0193\3;\3;\3;\6;\u0199")
        buf.write("\n;\r;\16;\u019a\3<\3<\3<\6<\u01a0\n<\r<\16<\u01a1\3=")
        buf.write("\3=\5=\u01a6\n=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3@\3")
        buf.write("@\3@\3@\7@\u01b7\n@\f@\16@\u01ba\13@\3@\3@\3@\3A\3A\3")
        buf.write("A\3A\7A\u01c3\nA\fA\16A\u01c6\13A\3A\3A\3A\3A\7A\u01cc")
        buf.write("\nA\fA\16A\u01cf\13A\3A\3A\5A\u01d3\nA\3A\3A\3B\6B\u01d8")
        buf.write("\nB\rB\16B\u01d9\3B\3B\3C\3C\3C\3D\3D\3D\3D\7D\u01e5\n")
        buf.write("D\fD\16D\u01e8\13D\3D\3D\3D\5D\u01ed\nD\3D\3D\3E\3E\3")
        buf.write("E\3E\7E\u01f5\nE\fE\16E\u01f8\13E\3E\3E\3\u01cd\2F\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\3\2\22")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2GGgg\4\2")
        buf.write("--//\4\2DDdd\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\7\2$")
        buf.write("$^^ppttvv\4\2$$^^\3\2\f\f\5\2\n\13\16\16\"\"\6\2\n\13")
        buf.write("\16\16\"#%\u0080\2\u0219\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u0091")
        buf.write("\3\2\2\2\7\u0093\3\2\2\2\t\u0099\3\2\2\2\13\u009b\3\2")
        buf.write("\2\2\r\u009d\3\2\2\2\17\u009f\3\2\2\2\21\u00a1\3\2\2\2")
        buf.write("\23\u00a3\3\2\2\2\25\u00a5\3\2\2\2\27\u00a7\3\2\2\2\31")
        buf.write("\u00a9\3\2\2\2\33\u00ab\3\2\2\2\35\u00ad\3\2\2\2\37\u00af")
        buf.write("\3\2\2\2!\u00b1\3\2\2\2#\u00b3\3\2\2\2%\u00b5\3\2\2\2")
        buf.write("\'\u00b7\3\2\2\2)\u00ba\3\2\2\2+\u00bd\3\2\2\2-\u00bf")
        buf.write("\3\2\2\2/\u00c2\3\2\2\2\61\u00c4\3\2\2\2\63\u00c7\3\2")
        buf.write("\2\2\65\u00ca\3\2\2\2\67\u00cd\3\2\2\29\u00cf\3\2\2\2")
        buf.write(";\u00d1\3\2\2\2=\u00d4\3\2\2\2?\u00d7\3\2\2\2A\u00da\3")
        buf.write("\2\2\2C\u00dd\3\2\2\2E\u00e0\3\2\2\2G\u00e3\3\2\2\2I\u00e8")
        buf.write("\3\2\2\2K\u00ec\3\2\2\2M\u00f3\3\2\2\2O\u00f8\3\2\2\2")
        buf.write("Q\u00fd\3\2\2\2S\u0104\3\2\2\2U\u010e\3\2\2\2W\u0115\3")
        buf.write("\2\2\2Y\u0119\3\2\2\2[\u011f\3\2\2\2]\u0127\3\2\2\2_\u012d")
        buf.write("\3\2\2\2a\u0131\3\2\2\2c\u013a\3\2\2\2e\u0140\3\2\2\2")
        buf.write("g\u0146\3\2\2\2i\u014a\3\2\2\2k\u0155\3\2\2\2m\u015b\3")
        buf.write("\2\2\2o\u0183\3\2\2\2q\u018c\3\2\2\2s\u018e\3\2\2\2u\u0195")
        buf.write("\3\2\2\2w\u019c\3\2\2\2y\u01a5\3\2\2\2{\u01a7\3\2\2\2")
        buf.write("}\u01ac\3\2\2\2\177\u01b2\3\2\2\2\u0081\u01d2\3\2\2\2")
        buf.write("\u0083\u01d7\3\2\2\2\u0085\u01dd\3\2\2\2\u0087\u01e0\3")
        buf.write("\2\2\2\u0089\u01f0\3\2\2\2\u008b\u008c\7k\2\2\u008c\u008d")
        buf.write("\7p\2\2\u008d\u008e\7f\2\2\u008e\u008f\7g\2\2\u008f\u0090")
        buf.write("\7z\2\2\u0090\4\3\2\2\2\u0091\u0092\7a\2\2\u0092\6\3\2")
        buf.write("\2\2\u0093\u0094\7x\2\2\u0094\u0095\7c\2\2\u0095\u0096")
        buf.write("\7n\2\2\u0096\u0097\7w\2\2\u0097\u0098\7g\2\2\u0098\b")
        buf.write("\3\2\2\2\u0099\u009a\7\60\2\2\u009a\n\3\2\2\2\u009b\u009c")
        buf.write("\7*\2\2\u009c\f\3\2\2\2\u009d\u009e\7+\2\2\u009e\16\3")
        buf.write("\2\2\2\u009f\u00a0\7}\2\2\u00a0\20\3\2\2\2\u00a1\u00a2")
        buf.write("\7\177\2\2\u00a2\22\3\2\2\2\u00a3\u00a4\7]\2\2\u00a4\24")
        buf.write("\3\2\2\2\u00a5\u00a6\7_\2\2\u00a6\26\3\2\2\2\u00a7\u00a8")
        buf.write("\7.\2\2\u00a8\30\3\2\2\2\u00a9\u00aa\7=\2\2\u00aa\32\3")
        buf.write("\2\2\2\u00ab\u00ac\7<\2\2\u00ac\34\3\2\2\2\u00ad\u00ae")
        buf.write("\7-\2\2\u00ae\36\3\2\2\2\u00af\u00b0\7/\2\2\u00b0 \3\2")
        buf.write("\2\2\u00b1\u00b2\7,\2\2\u00b2\"\3\2\2\2\u00b3\u00b4\7")
        buf.write("\61\2\2\u00b4$\3\2\2\2\u00b5\u00b6\7\'\2\2\u00b6&\3\2")
        buf.write("\2\2\u00b7\u00b8\7?\2\2\u00b8\u00b9\7?\2\2\u00b9(\3\2")
        buf.write("\2\2\u00ba\u00bb\7#\2\2\u00bb\u00bc\7?\2\2\u00bc*\3\2")
        buf.write("\2\2\u00bd\u00be\7>\2\2\u00be,\3\2\2\2\u00bf\u00c0\7>")
        buf.write("\2\2\u00c0\u00c1\7?\2\2\u00c1.\3\2\2\2\u00c2\u00c3\7@")
        buf.write("\2\2\u00c3\60\3\2\2\2\u00c4\u00c5\7@\2\2\u00c5\u00c6\7")
        buf.write("?\2\2\u00c6\62\3\2\2\2\u00c7\u00c8\7(\2\2\u00c8\u00c9")
        buf.write("\7(\2\2\u00c9\64\3\2\2\2\u00ca\u00cb\7~\2\2\u00cb\u00cc")
        buf.write("\7~\2\2\u00cc\66\3\2\2\2\u00cd\u00ce\7#\2\2\u00ce8\3\2")
        buf.write("\2\2\u00cf\u00d0\7?\2\2\u00d0:\3\2\2\2\u00d1\u00d2\7-")
        buf.write("\2\2\u00d2\u00d3\7?\2\2\u00d3<\3\2\2\2\u00d4\u00d5\7/")
        buf.write("\2\2\u00d5\u00d6\7?\2\2\u00d6>\3\2\2\2\u00d7\u00d8\7,")
        buf.write("\2\2\u00d8\u00d9\7?\2\2\u00d9@\3\2\2\2\u00da\u00db\7\61")
        buf.write("\2\2\u00db\u00dc\7?\2\2\u00dcB\3\2\2\2\u00dd\u00de\7\'")
        buf.write("\2\2\u00de\u00df\7?\2\2\u00dfD\3\2\2\2\u00e0\u00e1\7k")
        buf.write("\2\2\u00e1\u00e2\7h\2\2\u00e2F\3\2\2\2\u00e3\u00e4\7g")
        buf.write("\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7H\3\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7t\2\2\u00ebJ\3\2\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7w\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7p\2\2\u00f2L\3")
        buf.write("\2\2\2\u00f3\u00f4\7h\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7e\2\2\u00f7N\3\2\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9\u00fa\7{\2\2\u00fa\u00fb\7r\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fcP\3\2\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7w\2\2\u0101\u0102")
        buf.write("\7e\2\2\u0102\u0103\7v\2\2\u0103R\3\2\2\2\u0104\u0105")
        buf.write("\7k\2\2\u0105\u0106\7p\2\2\u0106\u0107\7v\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\u0109\7t\2\2\u0109\u010a\7h\2\2\u010a\u010b")
        buf.write("\7c\2\2\u010b\u010c\7e\2\2\u010c\u010d\7g\2\2\u010dT\3")
        buf.write("\2\2\2\u010e\u010f\7u\2\2\u010f\u0110\7v\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111\u0112\7k\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7i\2\2\u0114V\3\2\2\2\u0115\u0116\7k\2\2\u0116\u0117")
        buf.write("\7p\2\2\u0117\u0118\7v\2\2\u0118X\3\2\2\2\u0119\u011a")
        buf.write("\7h\2\2\u011a\u011b\7n\2\2\u011b\u011c\7q\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7v\2\2\u011eZ\3\2\2\2\u011f\u0120")
        buf.write("\7d\2\2\u0120\u0121\7q\2\2\u0121\u0122\7q\2\2\u0122\u0123")
        buf.write("\7n\2\2\u0123\u0124\7g\2\2\u0124\u0125\7c\2\2\u0125\u0126")
        buf.write("\7p\2\2\u0126\\\3\2\2\2\u0127\u0128\7e\2\2\u0128\u0129")
        buf.write("\7q\2\2\u0129\u012a\7p\2\2\u012a\u012b\7u\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c^\3\2\2\2\u012d\u012e\7x\2\2\u012e\u012f")
        buf.write("\7c\2\2\u012f\u0130\7t\2\2\u0130`\3\2\2\2\u0131\u0132")
        buf.write("\7e\2\2\u0132\u0133\7q\2\2\u0133\u0134\7p\2\2\u0134\u0135")
        buf.write("\7v\2\2\u0135\u0136\7k\2\2\u0136\u0137\7p\2\2\u0137\u0138")
        buf.write("\7w\2\2\u0138\u0139\7g\2\2\u0139b\3\2\2\2\u013a\u013b")
        buf.write("\7d\2\2\u013b\u013c\7t\2\2\u013c\u013d\7g\2\2\u013d\u013e")
        buf.write("\7c\2\2\u013e\u013f\7m\2\2\u013fd\3\2\2\2\u0140\u0141")
        buf.write("\7t\2\2\u0141\u0142\7c\2\2\u0142\u0143\7p\2\2\u0143\u0144")
        buf.write("\7i\2\2\u0144\u0145\7g\2\2\u0145f\3\2\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\u0148\7k\2\2\u0148\u0149\7n\2\2\u0149h\3")
        buf.write("\2\2\2\u014a\u014e\t\2\2\2\u014b\u014d\t\3\2\2\u014c\u014b")
        buf.write("\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014fj\3\2\2\2\u0150\u014e\3\2\2\2\u0151")
        buf.write("\u0156\7\f\2\2\u0152\u0153\7\17\2\2\u0153\u0156\7\f\2")
        buf.write("\2\u0154\u0156\7\17\2\2\u0155\u0151\3\2\2\2\u0155\u0152")
        buf.write("\3\2\2\2\u0155\u0154\3\2\2\2\u0156l\3\2\2\2\u0157\u015c")
        buf.write("\5q9\2\u0158\u015c\5s:\2\u0159\u015c\5u;\2\u015a\u015c")
        buf.write("\5w<\2\u015b\u0157\3\2\2\2\u015b\u0158\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015cn\3\2\2\2\u015d\u0166")
        buf.write("\t\4\2\2\u015e\u0162\t\5\2\2\u015f\u0161\t\4\2\2\u0160")
        buf.write("\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0165\u015d\3\2\2\2\u0165\u015e\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u016b\7\60\2\2\u0168\u016a\t\4\2\2\u0169")
        buf.write("\u0168\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2")
        buf.write("\u016b\u016c\3\2\2\2\u016c\u0184\3\2\2\2\u016d\u016b\3")
        buf.write("\2\2\2\u016e\u0177\t\4\2\2\u016f\u0173\t\5\2\2\u0170\u0172")
        buf.write("\t\4\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0177\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0176\u016e\3\2\2\2\u0176\u016f\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\7\60\2\2\u0179")
        buf.write("\u017a\t\4\2\2\u017a\u017c\t\6\2\2\u017b\u017d\t\7\2\2")
        buf.write("\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\3")
        buf.write("\2\2\2\u017e\u0180\t\4\2\2\u017f\u017e\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0165\3\2\2\2\u0183\u0176\3\2\2\2")
        buf.write("\u0184p\3\2\2\2\u0185\u018d\t\4\2\2\u0186\u0188\t\5\2")
        buf.write("\2\u0187\u0189\t\4\2\2\u0188\u0187\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u018d\3\2\2\2\u018c\u0185\3\2\2\2\u018c\u0186\3\2\2\2")
        buf.write("\u018dr\3\2\2\2\u018e\u018f\7\62\2\2\u018f\u0191\t\b\2")
        buf.write("\2\u0190\u0192\4\62\63\2\u0191\u0190\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("t\3\2\2\2\u0195\u0196\7\62\2\2\u0196\u0198\t\t\2\2\u0197")
        buf.write("\u0199\t\n\2\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019bv\3\2\2")
        buf.write("\2\u019c\u019d\7\62\2\2\u019d\u019f\t\13\2\2\u019e\u01a0")
        buf.write("\t\f\2\2\u019f\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2x\3\2\2\2\u01a3")
        buf.write("\u01a6\5{>\2\u01a4\u01a6\5}?\2\u01a5\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a4\3\2\2\2\u01a6z\3\2\2\2\u01a7\u01a8\7v\2\2\u01a8")
        buf.write("\u01a9\7t\2\2\u01a9\u01aa\7w\2\2\u01aa\u01ab\7g\2\2\u01ab")
        buf.write("|\3\2\2\2\u01ac\u01ad\7h\2\2\u01ad\u01ae\7c\2\2\u01ae")
        buf.write("\u01af\7n\2\2\u01af\u01b0\7u\2\2\u01b0\u01b1\7g\2\2\u01b1")
        buf.write("~\3\2\2\2\u01b2\u01b8\7$\2\2\u01b3\u01b4\7^\2\2\u01b4")
        buf.write("\u01b7\t\r\2\2\u01b5\u01b7\n\16\2\2\u01b6\u01b3\3\2\2")
        buf.write("\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01bb\u01bc\7$\2\2\u01bc\u01bd\b@\2\2\u01bd")
        buf.write("\u0080\3\2\2\2\u01be\u01bf\7\61\2\2\u01bf\u01c0\7\61\2")
        buf.write("\2\u01c0\u01c4\3\2\2\2\u01c1\u01c3\n\17\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5\u01d3\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c7\u01c8\7\61\2\2\u01c8\u01c9\7,\2\2\u01c9\u01cd\3")
        buf.write("\2\2\2\u01ca\u01cc\13\2\2\2\u01cb\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cf\3\2\2\2\u01cd\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01ce\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1\7")
        buf.write(",\2\2\u01d1\u01d3\7\61\2\2\u01d2\u01be\3\2\2\2\u01d2\u01c7")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\bA\3\2\u01d5")
        buf.write("\u0082\3\2\2\2\u01d6\u01d8\t\20\2\2\u01d7\u01d6\3\2\2")
        buf.write("\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\bB\3\2\u01dc")
        buf.write("\u0084\3\2\2\2\u01dd\u01de\13\2\2\2\u01de\u01df\bC\4\2")
        buf.write("\u01df\u0086\3\2\2\2\u01e0\u01e6\7$\2\2\u01e1\u01e2\7")
        buf.write("^\2\2\u01e2\u01e5\t\r\2\2\u01e3\u01e5\n\16\2\2\u01e4\u01e1")
        buf.write("\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01ec\3\2\2\2")
        buf.write("\u01e8\u01e6\3\2\2\2\u01e9\u01ea\7^\2\2\u01ea\u01ed\n")
        buf.write("\r\2\2\u01eb\u01ed\7^\2\2\u01ec\u01e9\3\2\2\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\bD\5\2\u01ef")
        buf.write("\u0088\3\2\2\2\u01f0\u01f6\7$\2\2\u01f1\u01f5\t\21\2\2")
        buf.write("\u01f2\u01f3\7)\2\2\u01f3\u01f5\7$\2\2\u01f4\u01f1\3\2")
        buf.write("\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f9\u01fa\bE\6\2\u01fa\u008a\3\2\2\2")
        buf.write("\37\2\u014e\u0155\u015b\u0162\u0165\u016b\u0173\u0176")
        buf.write("\u017c\u0181\u0183\u018a\u018c\u0193\u019a\u01a1\u01a5")
        buf.write("\u01b6\u01b8\u01c4\u01cd\u01d2\u01d9\u01e4\u01e6\u01ec")
        buf.write("\u01f4\u01f6\7\3@\2\b\2\2\3C\3\3D\4\3E\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    LB = 5
    RB = 6
    LC = 7
    RC = 8
    LP = 9
    RP = 10
    COMMA = 11
    SEMICOLON = 12
    COLON = 13
    ADD = 14
    SUBTR = 15
    MUL = 16
    DIV = 17
    MOD = 18
    EQ = 19
    UNEQ = 20
    LESS = 21
    LESSEQ = 22
    GREATER = 23
    GREATEREQ = 24
    AND = 25
    OR = 26
    NOT = 27
    ASSIGN = 28
    ADDASS = 29
    SUBASS = 30
    MULASS = 31
    DIVASS = 32
    MODASS = 33
    IF = 34
    ELSE = 35
    FOR = 36
    RETURN = 37
    FUNC = 38
    TYPE = 39
    STRUCT = 40
    INTERFACE = 41
    STRING = 42
    INT = 43
    FLOAT = 44
    BOOLEAN = 45
    CONST = 46
    VAR = 47
    CONTINUE = 48
    BREAK = 49
    RANGE = 50
    NIL = 51
    ID = 52
    NL = 53
    INTLIT = 54
    FLOATLIT = 55
    DECIMAL = 56
    BINARY = 57
    OCTAL = 58
    HEXADECIMAL = 59
    BOOLLIT = 60
    TRUE = 61
    FALSE = 62
    STRINGLIT = 63
    COMMENT = 64
    WS = 65
    ERROR_CHAR = 66
    ILLEGAL_ESCAPE = 67
    UNCLOSE_STRING = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'index'", "'_'", "'value'", "'.'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "','", "';'", "':'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", 
            "'||'", "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LC", "RC", "LP", "RP", "COMMA", "SEMICOLON", "COLON", 
            "ADD", "SUBTR", "MUL", "DIV", "MOD", "EQ", "UNEQ", "LESS", "LESSEQ", 
            "GREATER", "GREATEREQ", "AND", "OR", "NOT", "ASSIGN", "ADDASS", 
            "SUBASS", "MULASS", "DIVASS", "MODASS", "IF", "ELSE", "FOR", 
            "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
            "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
            "NIL", "ID", "NL", "INTLIT", "FLOATLIT", "DECIMAL", "BINARY", 
            "OCTAL", "HEXADECIMAL", "BOOLLIT", "TRUE", "FALSE", "STRINGLIT", 
            "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "LB", "RB", "LC", "RC", 
                  "LP", "RP", "COMMA", "SEMICOLON", "COLON", "ADD", "SUBTR", 
                  "MUL", "DIV", "MOD", "EQ", "UNEQ", "LESS", "LESSEQ", "GREATER", 
                  "GREATEREQ", "AND", "OR", "NOT", "ASSIGN", "ADDASS", "SUBASS", 
                  "MULASS", "DIVASS", "MODASS", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "ID", "NL", "INTLIT", "FLOATLIT", "DECIMAL", 
                  "BINARY", "OCTAL", "HEXADECIMAL", "BOOLLIT", "TRUE", "FALSE", 
                  "STRINGLIT", "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.STRINGLIT_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text[1:]) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     


