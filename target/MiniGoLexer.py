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
        buf.write("\u0219\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\6\6\u009f\n\6\r\6\16")
        buf.write("\6\u00a0\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\7\67")
        buf.write("\u0158\n\67\f\67\16\67\u015b\13\67\38\38\38\68\u0160\n")
        buf.write("8\r8\168\u0161\38\38\39\39\39\69\u0169\n9\r9\169\u016a")
        buf.write("\39\39\3:\3:\3:\6:\u0172\n:\r:\16:\u0173\3:\3:\3;\3;\3")
        buf.write(";\3;\5;\u017c\n;\3<\3<\3<\7<\u0181\n<\f<\16<\u0184\13")
        buf.write("<\5<\u0186\n<\3<\3<\7<\u018a\n<\f<\16<\u018d\13<\3<\3")
        buf.write("<\3<\7<\u0192\n<\f<\16<\u0195\13<\5<\u0197\n<\3<\3<\7")
        buf.write("<\u019b\n<\f<\16<\u019e\13<\3<\3<\5<\u01a2\n<\3<\3<\3")
        buf.write("<\6<\u01a7\n<\r<\16<\u01a8\5<\u01ab\n<\5<\u01ad\n<\3=")
        buf.write("\3=\3=\6=\u01b2\n=\r=\16=\u01b3\5=\u01b6\n=\3>\3>\5>\u01ba")
        buf.write("\n>\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\7A\u01cb")
        buf.write("\nA\fA\16A\u01ce\13A\3A\3A\3A\3B\3B\3B\3B\7B\u01d7\nB")
        buf.write("\fB\16B\u01da\13B\3C\3C\3C\3C\7C\u01e0\nC\fC\16C\u01e3")
        buf.write("\13C\3C\5C\u01e6\nC\3C\3C\3C\3C\3C\3C\3C\3C\5C\u01f0\n")
        buf.write("C\5C\u01f2\nC\3C\3C\3D\3D\3D\3E\3E\3E\3E\7E\u01fd\nE\f")
        buf.write("E\16E\u0200\13E\3E\3E\3E\5E\u0205\nE\3E\3E\3F\3F\3F\3")
        buf.write("F\7F\u020d\nF\fF\16F\u0210\13F\3F\7F\u0213\nF\fF\16F\u0216")
        buf.write("\13F\3F\3F\2\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083\2\u0085C")
        buf.write("\u0087D\u0089E\u008bF\3\2\25\5\2\13\13\16\17\"\"\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\4\2ZZzz\5\2\62;CHch\4\2DDdd\4\2")
        buf.write("QQqq\3\2\629\3\2\62;\3\2\63;\4\2GGgg\4\2--//\7\2$$^^p")
        buf.write("pttvv\6\2\f\f\17\17$$^^\3\2,,\3\2\61\61\4\2\f\f\17\17")
        buf.write("\4\2$$^^\6\2\n\f\16\17\"#%\u0080\2\u023b\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d")
        buf.write("\3\2\2\2\5\u0093\3\2\2\2\7\u0095\3\2\2\2\t\u009b\3\2\2")
        buf.write("\2\13\u009e\3\2\2\2\r\u00a4\3\2\2\2\17\u00a6\3\2\2\2\21")
        buf.write("\u00a8\3\2\2\2\23\u00aa\3\2\2\2\25\u00ac\3\2\2\2\27\u00ae")
        buf.write("\3\2\2\2\31\u00b0\3\2\2\2\33\u00b2\3\2\2\2\35\u00b4\3")
        buf.write("\2\2\2\37\u00b6\3\2\2\2!\u00b8\3\2\2\2#\u00ba\3\2\2\2")
        buf.write("%\u00bc\3\2\2\2\'\u00be\3\2\2\2)\u00c0\3\2\2\2+\u00c2")
        buf.write("\3\2\2\2-\u00c5\3\2\2\2/\u00c8\3\2\2\2\61\u00ca\3\2\2")
        buf.write("\2\63\u00cd\3\2\2\2\65\u00cf\3\2\2\2\67\u00d2\3\2\2\2")
        buf.write("9\u00d5\3\2\2\2;\u00d8\3\2\2\2=\u00da\3\2\2\2?\u00dc\3")
        buf.write("\2\2\2A\u00df\3\2\2\2C\u00e2\3\2\2\2E\u00e5\3\2\2\2G\u00e8")
        buf.write("\3\2\2\2I\u00eb\3\2\2\2K\u00ee\3\2\2\2M\u00f3\3\2\2\2")
        buf.write("O\u00f7\3\2\2\2Q\u00fe\3\2\2\2S\u0103\3\2\2\2U\u0108\3")
        buf.write("\2\2\2W\u010f\3\2\2\2Y\u0119\3\2\2\2[\u0120\3\2\2\2]\u0124")
        buf.write("\3\2\2\2_\u012a\3\2\2\2a\u0132\3\2\2\2c\u0138\3\2\2\2")
        buf.write("e\u013c\3\2\2\2g\u0145\3\2\2\2i\u014b\3\2\2\2k\u0151\3")
        buf.write("\2\2\2m\u0155\3\2\2\2o\u015c\3\2\2\2q\u0165\3\2\2\2s\u016e")
        buf.write("\3\2\2\2u\u017b\3\2\2\2w\u01ac\3\2\2\2y\u01b5\3\2\2\2")
        buf.write("{\u01b9\3\2\2\2}\u01bb\3\2\2\2\177\u01c0\3\2\2\2\u0081")
        buf.write("\u01c6\3\2\2\2\u0083\u01d8\3\2\2\2\u0085\u01f1\3\2\2\2")
        buf.write("\u0087\u01f5\3\2\2\2\u0089\u01f8\3\2\2\2\u008b\u0208\3")
        buf.write("\2\2\2\u008d\u008e\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090")
        buf.write("\7f\2\2\u0090\u0091\7g\2\2\u0091\u0092\7z\2\2\u0092\4")
        buf.write("\3\2\2\2\u0093\u0094\7a\2\2\u0094\6\3\2\2\2\u0095\u0096")
        buf.write("\7x\2\2\u0096\u0097\7c\2\2\u0097\u0098\7n\2\2\u0098\u0099")
        buf.write("\7w\2\2\u0099\u009a\7g\2\2\u009a\b\3\2\2\2\u009b\u009c")
        buf.write("\7\60\2\2\u009c\n\3\2\2\2\u009d\u009f\t\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\b\6\2\2")
        buf.write("\u00a3\f\3\2\2\2\u00a4\u00a5\7\f\2\2\u00a5\16\3\2\2\2")
        buf.write("\u00a6\u00a7\7*\2\2\u00a7\20\3\2\2\2\u00a8\u00a9\7+\2")
        buf.write("\2\u00a9\22\3\2\2\2\u00aa\u00ab\7}\2\2\u00ab\24\3\2\2")
        buf.write("\2\u00ac\u00ad\7\177\2\2\u00ad\26\3\2\2\2\u00ae\u00af")
        buf.write("\7]\2\2\u00af\30\3\2\2\2\u00b0\u00b1\7_\2\2\u00b1\32\3")
        buf.write("\2\2\2\u00b2\u00b3\7.\2\2\u00b3\34\3\2\2\2\u00b4\u00b5")
        buf.write("\7=\2\2\u00b5\36\3\2\2\2\u00b6\u00b7\7<\2\2\u00b7 \3\2")
        buf.write("\2\2\u00b8\u00b9\7-\2\2\u00b9\"\3\2\2\2\u00ba\u00bb\7")
        buf.write("/\2\2\u00bb$\3\2\2\2\u00bc\u00bd\7,\2\2\u00bd&\3\2\2\2")
        buf.write("\u00be\u00bf\7\61\2\2\u00bf(\3\2\2\2\u00c0\u00c1\7\'\2")
        buf.write("\2\u00c1*\3\2\2\2\u00c2\u00c3\7?\2\2\u00c3\u00c4\7?\2")
        buf.write("\2\u00c4,\3\2\2\2\u00c5\u00c6\7#\2\2\u00c6\u00c7\7?\2")
        buf.write("\2\u00c7.\3\2\2\2\u00c8\u00c9\7>\2\2\u00c9\60\3\2\2\2")
        buf.write("\u00ca\u00cb\7>\2\2\u00cb\u00cc\7?\2\2\u00cc\62\3\2\2")
        buf.write("\2\u00cd\u00ce\7@\2\2\u00ce\64\3\2\2\2\u00cf\u00d0\7@")
        buf.write("\2\2\u00d0\u00d1\7?\2\2\u00d1\66\3\2\2\2\u00d2\u00d3\7")
        buf.write("(\2\2\u00d3\u00d4\7(\2\2\u00d48\3\2\2\2\u00d5\u00d6\7")
        buf.write("~\2\2\u00d6\u00d7\7~\2\2\u00d7:\3\2\2\2\u00d8\u00d9\7")
        buf.write("#\2\2\u00d9<\3\2\2\2\u00da\u00db\7?\2\2\u00db>\3\2\2\2")
        buf.write("\u00dc\u00dd\7-\2\2\u00dd\u00de\7?\2\2\u00de@\3\2\2\2")
        buf.write("\u00df\u00e0\7/\2\2\u00e0\u00e1\7?\2\2\u00e1B\3\2\2\2")
        buf.write("\u00e2\u00e3\7,\2\2\u00e3\u00e4\7?\2\2\u00e4D\3\2\2\2")
        buf.write("\u00e5\u00e6\7\61\2\2\u00e6\u00e7\7?\2\2\u00e7F\3\2\2")
        buf.write("\2\u00e8\u00e9\7\'\2\2\u00e9\u00ea\7?\2\2\u00eaH\3\2\2")
        buf.write("\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7h\2\2\u00edJ\3\2\2")
        buf.write("\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7")
        buf.write("u\2\2\u00f1\u00f2\7g\2\2\u00f2L\3\2\2\2\u00f3\u00f4\7")
        buf.write("h\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7t\2\2\u00f6N\3\2")
        buf.write("\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fdP\3\2\2\2\u00fe\u00ff\7h\2\2\u00ff\u0100")
        buf.write("\7w\2\2\u0100\u0101\7p\2\2\u0101\u0102\7e\2\2\u0102R\3")
        buf.write("\2\2\2\u0103\u0104\7v\2\2\u0104\u0105\7{\2\2\u0105\u0106")
        buf.write("\7r\2\2\u0106\u0107\7g\2\2\u0107T\3\2\2\2\u0108\u0109")
        buf.write("\7u\2\2\u0109\u010a\7v\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7w\2\2\u010c\u010d\7e\2\2\u010d\u010e\7v\2\2\u010eV\3")
        buf.write("\2\2\2\u010f\u0110\7k\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7g\2\2\u0113\u0114\7t\2\2\u0114\u0115")
        buf.write("\7h\2\2\u0115\u0116\7c\2\2\u0116\u0117\7e\2\2\u0117\u0118")
        buf.write("\7g\2\2\u0118X\3\2\2\2\u0119\u011a\7u\2\2\u011a\u011b")
        buf.write("\7v\2\2\u011b\u011c\7t\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7i\2\2\u011fZ\3\2\2\2\u0120\u0121")
        buf.write("\7k\2\2\u0121\u0122\7p\2\2\u0122\u0123\7v\2\2\u0123\\")
        buf.write("\3\2\2\2\u0124\u0125\7h\2\2\u0125\u0126\7n\2\2\u0126\u0127")
        buf.write("\7q\2\2\u0127\u0128\7c\2\2\u0128\u0129\7v\2\2\u0129^\3")
        buf.write("\2\2\2\u012a\u012b\7d\2\2\u012b\u012c\7q\2\2\u012c\u012d")
        buf.write("\7q\2\2\u012d\u012e\7n\2\2\u012e\u012f\7g\2\2\u012f\u0130")
        buf.write("\7c\2\2\u0130\u0131\7p\2\2\u0131`\3\2\2\2\u0132\u0133")
        buf.write("\7e\2\2\u0133\u0134\7q\2\2\u0134\u0135\7p\2\2\u0135\u0136")
        buf.write("\7u\2\2\u0136\u0137\7v\2\2\u0137b\3\2\2\2\u0138\u0139")
        buf.write("\7x\2\2\u0139\u013a\7c\2\2\u013a\u013b\7t\2\2\u013bd\3")
        buf.write("\2\2\2\u013c\u013d\7e\2\2\u013d\u013e\7q\2\2\u013e\u013f")
        buf.write("\7p\2\2\u013f\u0140\7v\2\2\u0140\u0141\7k\2\2\u0141\u0142")
        buf.write("\7p\2\2\u0142\u0143\7w\2\2\u0143\u0144\7g\2\2\u0144f\3")
        buf.write("\2\2\2\u0145\u0146\7d\2\2\u0146\u0147\7t\2\2\u0147\u0148")
        buf.write("\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a\7m\2\2\u014ah\3")
        buf.write("\2\2\2\u014b\u014c\7t\2\2\u014c\u014d\7c\2\2\u014d\u014e")
        buf.write("\7p\2\2\u014e\u014f\7i\2\2\u014f\u0150\7g\2\2\u0150j\3")
        buf.write("\2\2\2\u0151\u0152\7p\2\2\u0152\u0153\7k\2\2\u0153\u0154")
        buf.write("\7n\2\2\u0154l\3\2\2\2\u0155\u0159\t\3\2\2\u0156\u0158")
        buf.write("\t\4\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015an\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015c\u015d\7\62\2\2\u015d\u015f\t\5\2")
        buf.write("\2\u015e\u0160\t\6\2\2\u015f\u015e\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0164\b8\3\2\u0164p\3\2\2\2\u0165")
        buf.write("\u0166\7\62\2\2\u0166\u0168\t\7\2\2\u0167\u0169\4\62\63")
        buf.write("\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016d\b9\4\2\u016dr\3\2\2\2\u016e\u016f\7\62\2\2\u016f")
        buf.write("\u0171\t\b\2\2\u0170\u0172\t\t\2\2\u0171\u0170\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3")
        buf.write("\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\b:\5\2\u0176t\3")
        buf.write("\2\2\2\u0177\u017c\5y=\2\u0178\u017c\5q9\2\u0179\u017c")
        buf.write("\5s:\2\u017a\u017c\5o8\2\u017b\u0177\3\2\2\2\u017b\u0178")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("v\3\2\2\2\u017d\u0186\t\n\2\2\u017e\u0182\t\13\2\2\u017f")
        buf.write("\u0181\t\n\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0186\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u017d\3\2\2\2\u0185\u017e")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u018b\7\60\2\2\u0188")
        buf.write("\u018a\t\n\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u01ad\3")
        buf.write("\2\2\2\u018d\u018b\3\2\2\2\u018e\u0197\t\n\2\2\u018f\u0193")
        buf.write("\t\13\2\2\u0190\u0192\t\n\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u018e\3")
        buf.write("\2\2\2\u0196\u018f\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019c")
        buf.write("\7\60\2\2\u0199\u019b\t\n\2\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019d\u019f\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1\t")
        buf.write("\f\2\2\u01a0\u01a2\t\r\2\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01aa\3\2\2\2\u01a3\u01ab\t\n\2\2\u01a4")
        buf.write("\u01a6\t\13\2\2\u01a5\u01a7\t\n\2\2\u01a6\u01a5\3\2\2")
        buf.write("\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a3\3\2\2\2\u01aa")
        buf.write("\u01a4\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u0185\3\2\2\2")
        buf.write("\u01ac\u0196\3\2\2\2\u01adx\3\2\2\2\u01ae\u01b6\t\n\2")
        buf.write("\2\u01af\u01b1\t\13\2\2\u01b0\u01b2\t\n\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01ae\3\2\2\2")
        buf.write("\u01b5\u01af\3\2\2\2\u01b6z\3\2\2\2\u01b7\u01ba\5}?\2")
        buf.write("\u01b8\u01ba\5\177@\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01ba|\3\2\2\2\u01bb\u01bc\7v\2\2\u01bc\u01bd")
        buf.write("\7t\2\2\u01bd\u01be\7w\2\2\u01be\u01bf\7g\2\2\u01bf~\3")
        buf.write("\2\2\2\u01c0\u01c1\7h\2\2\u01c1\u01c2\7c\2\2\u01c2\u01c3")
        buf.write("\7n\2\2\u01c3\u01c4\7u\2\2\u01c4\u01c5\7g\2\2\u01c5\u0080")
        buf.write("\3\2\2\2\u01c6\u01cc\7$\2\2\u01c7\u01c8\7^\2\2\u01c8\u01cb")
        buf.write("\t\16\2\2\u01c9\u01cb\n\17\2\2\u01ca\u01c7\3\2\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3")
        buf.write("\2\2\2\u01cf\u01d0\7$\2\2\u01d0\u01d1\bA\6\2\u01d1\u0082")
        buf.write("\3\2\2\2\u01d2\u01d7\n\20\2\2\u01d3\u01d4\7,\2\2\u01d4")
        buf.write("\u01d7\n\21\2\2\u01d5\u01d7\5\u0085C\2\u01d6\u01d2\3\2")
        buf.write("\2\2\u01d6\u01d3\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u0084\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dc\7\61\2")
        buf.write("\2\u01dc\u01dd\7\61\2\2\u01dd\u01e1\3\2\2\2\u01de\u01e0")
        buf.write("\n\22\2\2\u01df\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e5\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e4\u01e6\7\17\2\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01f2\3\2\2\2\u01e7")
        buf.write("\u01e8\7\61\2\2\u01e8\u01e9\7,\2\2\u01e9\u01ea\3\2\2\2")
        buf.write("\u01ea\u01eb\5\u0083B\2\u01eb\u01ec\7,\2\2\u01ec\u01ed")
        buf.write("\7\61\2\2\u01ed\u01ef\3\2\2\2\u01ee\u01f0\7\17\2\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2")
        buf.write("\u01f1\u01db\3\2\2\2\u01f1\u01e7\3\2\2\2\u01f2\u01f3\3")
        buf.write("\2\2\2\u01f3\u01f4\bC\2\2\u01f4\u0086\3\2\2\2\u01f5\u01f6")
        buf.write("\13\2\2\2\u01f6\u01f7\bD\7\2\u01f7\u0088\3\2\2\2\u01f8")
        buf.write("\u01fe\7$\2\2\u01f9\u01fa\7^\2\2\u01fa\u01fd\t\16\2\2")
        buf.write("\u01fb\u01fd\n\23\2\2\u01fc\u01f9\3\2\2\2\u01fc\u01fb")
        buf.write("\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0204\3\2\2\2\u0200\u01fe\3\2\2\2")
        buf.write("\u0201\u0202\7^\2\2\u0202\u0205\n\16\2\2\u0203\u0205\7")
        buf.write("^\2\2\u0204\u0201\3\2\2\2\u0204\u0203\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u0207\bE\b\2\u0207\u008a\3\2\2\2\u0208")
        buf.write("\u020e\7$\2\2\u0209\u020d\t\24\2\2\u020a\u020b\7)\2\2")
        buf.write("\u020b\u020d\7$\2\2\u020c\u0209\3\2\2\2\u020c\u020a\3")
        buf.write("\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020f\u0214\3\2\2\2\u0210\u020e\3\2\2\2\u0211")
        buf.write("\u0213\t\22\2\2\u0212\u0211\3\2\2\2\u0213\u0216\3\2\2")
        buf.write("\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0217")
        buf.write("\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0218\bF\t\2\u0218")
        buf.write("\u008c\3\2\2\2$\2\u00a0\u0159\u0161\u016a\u0173\u017b")
        buf.write("\u0182\u0185\u018b\u0193\u0196\u019c\u01a1\u01a8\u01aa")
        buf.write("\u01ac\u01b3\u01b5\u01b9\u01ca\u01cc\u01d6\u01d8\u01e1")
        buf.write("\u01e5\u01ef\u01f1\u01fc\u01fe\u0204\u020c\u020e\u0214")
        buf.write("\n\b\2\2\38\2\39\3\3:\4\3A\5\3D\6\3E\7\3F\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    WS = 5
    NL = 6
    LB = 7
    RB = 8
    LC = 9
    RC = 10
    LP = 11
    RP = 12
    COMMA = 13
    SEMICOLON = 14
    COLON = 15
    ADD = 16
    SUBTR = 17
    MUL = 18
    DIV = 19
    MOD = 20
    EQ = 21
    UNEQ = 22
    LESS = 23
    LESSEQ = 24
    GREATER = 25
    GREATEREQ = 26
    AND = 27
    OR = 28
    NOT = 29
    ASSIGN = 30
    ADDASS = 31
    SUBASS = 32
    MULASS = 33
    DIVASS = 34
    MODASS = 35
    IF = 36
    ELSE = 37
    FOR = 38
    RETURN = 39
    FUNC = 40
    TYPE = 41
    STRUCT = 42
    INTERFACE = 43
    STRING = 44
    INT = 45
    FLOAT = 46
    BOOLEAN = 47
    CONST = 48
    VAR = 49
    CONTINUE = 50
    BREAK = 51
    RANGE = 52
    NIL = 53
    ID = 54
    HEXADECIMAL = 55
    BINARY = 56
    OCTAL = 57
    INTLIT = 58
    FLOATLIT = 59
    DECIMAL = 60
    BOOLLIT = 61
    TRUE = 62
    FALSE = 63
    STRINGLIT = 64
    COMMENT = 65
    ERROR_CHAR = 66
    ILLEGAL_ESCAPE = 67
    UNCLOSE_STRING = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'index'", "'_'", "'value'", "'.'", "'\n'", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "','", "';'", "':'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'&&'", "'||'", "'!'", "'='", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "NL", "LB", "RB", "LC", "RC", "LP", "RP", "COMMA", "SEMICOLON", 
            "COLON", "ADD", "SUBTR", "MUL", "DIV", "MOD", "EQ", "UNEQ", 
            "LESS", "LESSEQ", "GREATER", "GREATEREQ", "AND", "OR", "NOT", 
            "ASSIGN", "ADDASS", "SUBASS", "MULASS", "DIVASS", "MODASS", 
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "ID", "HEXADECIMAL", "BINARY", "OCTAL", 
            "INTLIT", "FLOATLIT", "DECIMAL", "BOOLLIT", "TRUE", "FALSE", 
            "STRINGLIT", "COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "WS", "NL", "LB", "RB", 
                  "LC", "RC", "LP", "RP", "COMMA", "SEMICOLON", "COLON", 
                  "ADD", "SUBTR", "MUL", "DIV", "MOD", "EQ", "UNEQ", "LESS", 
                  "LESSEQ", "GREATER", "GREATEREQ", "AND", "OR", "NOT", 
                  "ASSIGN", "ADDASS", "SUBASS", "MULASS", "DIVASS", "MODASS", 
                  "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "ID", "HEXADECIMAL", 
                  "BINARY", "OCTAL", "INTLIT", "FLOATLIT", "DECIMAL", "BOOLLIT", 
                  "TRUE", "FALSE", "STRINGLIT", "COMMENT_CONTENT", "COMMENT", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
            actions[54] = self.HEXADECIMAL_action 
            actions[55] = self.BINARY_action 
            actions[56] = self.OCTAL_action 
            actions[63] = self.STRINGLIT_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def HEXADECIMAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = str(int(self.text, 16)) 
     

    def BINARY_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = str(int(self.text, 2)) 
     

    def OCTAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = str(int(self.text, 8)) 
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
             raise IllegalEscape(self.text[1:]) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                self.text = self.text[1:]
                self.text = self.text.replace('\n','')
                self.text = self.text.replace('\r','')
                raise UncloseString(self.text)

     


