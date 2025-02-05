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
        buf.write("\u0213\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\65\3\65\7\65\u014f\n\65\f")
        buf.write("\65\16\65\u0152\13\65\3\66\3\66\3\66\3\66\5\66\u0158\n")
        buf.write("\66\3\67\3\67\3\67\6\67\u015d\n\67\r\67\16\67\u015e\3")
        buf.write("\67\3\67\38\38\38\38\58\u0167\n8\39\39\39\79\u016c\n9")
        buf.write("\f9\169\u016f\139\59\u0171\n9\39\39\79\u0175\n9\f9\16")
        buf.write("9\u0178\139\39\39\39\79\u017d\n9\f9\169\u0180\139\59\u0182")
        buf.write("\n9\39\39\79\u0186\n9\f9\169\u0189\139\39\39\59\u018d")
        buf.write("\n9\39\69\u0190\n9\r9\169\u0191\59\u0194\n9\3:\3:\3:\6")
        buf.write(":\u0199\n:\r:\16:\u019a\5:\u019d\n:\3;\3;\3;\6;\u01a2")
        buf.write("\n;\r;\16;\u01a3\3<\3<\3<\6<\u01a9\n<\r<\16<\u01aa\3=")
        buf.write("\3=\5=\u01af\n=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3@\3")
        buf.write("@\3@\3@\7@\u01c0\n@\f@\16@\u01c3\13@\3@\3@\3@\3A\3A\3")
        buf.write("A\3A\7A\u01cc\nA\fA\16A\u01cf\13A\3B\3B\3B\3B\7B\u01d5")
        buf.write("\nB\fB\16B\u01d8\13B\3B\6B\u01db\nB\rB\16B\u01dc\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\5B\u01e6\nB\3B\3B\3C\6C\u01eb\nC\rC\16")
        buf.write("C\u01ec\3C\3C\3D\3D\3D\3E\3E\3E\3E\7E\u01f8\nE\fE\16E")
        buf.write("\u01fb\13E\3E\3E\3E\5E\u0200\nE\3E\3E\3F\3F\3F\3F\7F\u0208")
        buf.write("\nF\fF\16F\u020b\13F\3F\6F\u020e\nF\rF\16F\u020f\3F\3")
        buf.write("F\2\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081\2\u0083B\u0085C\u0087D\u0089")
        buf.write("E\u008bF\3\2\25\5\2C\\aac|\6\2\62;C\\aac|\4\2ZZzz\5\2")
        buf.write("\62;CHch\3\2\62;\3\2\63;\4\2GGgg\4\2--//\4\2DDdd\4\2Q")
        buf.write("Qqq\3\2\629\7\2$$^^ppttvv\6\2\f\f\17\17$$^^\3\2,,\3\2")
        buf.write("\61\61\4\2\f\f\17\17\5\2\n\13\16\16\"\"\4\2$$^^\6\2\n")
        buf.write("\f\16\17\"#%\u0080\2\u0235\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u0093")
        buf.write("\3\2\2\2\7\u0095\3\2\2\2\t\u009b\3\2\2\2\13\u009d\3\2")
        buf.write("\2\2\r\u009f\3\2\2\2\17\u00a1\3\2\2\2\21\u00a3\3\2\2\2")
        buf.write("\23\u00a5\3\2\2\2\25\u00a7\3\2\2\2\27\u00a9\3\2\2\2\31")
        buf.write("\u00ab\3\2\2\2\33\u00ad\3\2\2\2\35\u00af\3\2\2\2\37\u00b1")
        buf.write("\3\2\2\2!\u00b3\3\2\2\2#\u00b5\3\2\2\2%\u00b7\3\2\2\2")
        buf.write("\'\u00b9\3\2\2\2)\u00bc\3\2\2\2+\u00bf\3\2\2\2-\u00c1")
        buf.write("\3\2\2\2/\u00c4\3\2\2\2\61\u00c6\3\2\2\2\63\u00c9\3\2")
        buf.write("\2\2\65\u00cc\3\2\2\2\67\u00cf\3\2\2\29\u00d1\3\2\2\2")
        buf.write(";\u00d3\3\2\2\2=\u00d6\3\2\2\2?\u00d9\3\2\2\2A\u00dc\3")
        buf.write("\2\2\2C\u00df\3\2\2\2E\u00e2\3\2\2\2G\u00e5\3\2\2\2I\u00ea")
        buf.write("\3\2\2\2K\u00ee\3\2\2\2M\u00f5\3\2\2\2O\u00fa\3\2\2\2")
        buf.write("Q\u00ff\3\2\2\2S\u0106\3\2\2\2U\u0110\3\2\2\2W\u0117\3")
        buf.write("\2\2\2Y\u011b\3\2\2\2[\u0121\3\2\2\2]\u0129\3\2\2\2_\u012f")
        buf.write("\3\2\2\2a\u0133\3\2\2\2c\u013c\3\2\2\2e\u0142\3\2\2\2")
        buf.write("g\u0148\3\2\2\2i\u014c\3\2\2\2k\u0157\3\2\2\2m\u0159\3")
        buf.write("\2\2\2o\u0166\3\2\2\2q\u0193\3\2\2\2s\u019c\3\2\2\2u\u019e")
        buf.write("\3\2\2\2w\u01a5\3\2\2\2y\u01ae\3\2\2\2{\u01b0\3\2\2\2")
        buf.write("}\u01b5\3\2\2\2\177\u01bb\3\2\2\2\u0081\u01cd\3\2\2\2")
        buf.write("\u0083\u01e5\3\2\2\2\u0085\u01ea\3\2\2\2\u0087\u01f0\3")
        buf.write("\2\2\2\u0089\u01f3\3\2\2\2\u008b\u0203\3\2\2\2\u008d\u008e")
        buf.write("\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090\7f\2\2\u0090\u0091")
        buf.write("\7g\2\2\u0091\u0092\7z\2\2\u0092\4\3\2\2\2\u0093\u0094")
        buf.write("\7a\2\2\u0094\6\3\2\2\2\u0095\u0096\7x\2\2\u0096\u0097")
        buf.write("\7c\2\2\u0097\u0098\7n\2\2\u0098\u0099\7w\2\2\u0099\u009a")
        buf.write("\7g\2\2\u009a\b\3\2\2\2\u009b\u009c\7\60\2\2\u009c\n\3")
        buf.write("\2\2\2\u009d\u009e\7*\2\2\u009e\f\3\2\2\2\u009f\u00a0")
        buf.write("\7+\2\2\u00a0\16\3\2\2\2\u00a1\u00a2\7}\2\2\u00a2\20\3")
        buf.write("\2\2\2\u00a3\u00a4\7\177\2\2\u00a4\22\3\2\2\2\u00a5\u00a6")
        buf.write("\7]\2\2\u00a6\24\3\2\2\2\u00a7\u00a8\7_\2\2\u00a8\26\3")
        buf.write("\2\2\2\u00a9\u00aa\7.\2\2\u00aa\30\3\2\2\2\u00ab\u00ac")
        buf.write("\7=\2\2\u00ac\32\3\2\2\2\u00ad\u00ae\7<\2\2\u00ae\34\3")
        buf.write("\2\2\2\u00af\u00b0\7-\2\2\u00b0\36\3\2\2\2\u00b1\u00b2")
        buf.write("\7/\2\2\u00b2 \3\2\2\2\u00b3\u00b4\7,\2\2\u00b4\"\3\2")
        buf.write("\2\2\u00b5\u00b6\7\61\2\2\u00b6$\3\2\2\2\u00b7\u00b8\7")
        buf.write("\'\2\2\u00b8&\3\2\2\2\u00b9\u00ba\7?\2\2\u00ba\u00bb\7")
        buf.write("?\2\2\u00bb(\3\2\2\2\u00bc\u00bd\7#\2\2\u00bd\u00be\7")
        buf.write("?\2\2\u00be*\3\2\2\2\u00bf\u00c0\7>\2\2\u00c0,\3\2\2\2")
        buf.write("\u00c1\u00c2\7>\2\2\u00c2\u00c3\7?\2\2\u00c3.\3\2\2\2")
        buf.write("\u00c4\u00c5\7@\2\2\u00c5\60\3\2\2\2\u00c6\u00c7\7@\2")
        buf.write("\2\u00c7\u00c8\7?\2\2\u00c8\62\3\2\2\2\u00c9\u00ca\7(")
        buf.write("\2\2\u00ca\u00cb\7(\2\2\u00cb\64\3\2\2\2\u00cc\u00cd\7")
        buf.write("~\2\2\u00cd\u00ce\7~\2\2\u00ce\66\3\2\2\2\u00cf\u00d0")
        buf.write("\7#\2\2\u00d08\3\2\2\2\u00d1\u00d2\7?\2\2\u00d2:\3\2\2")
        buf.write("\2\u00d3\u00d4\7-\2\2\u00d4\u00d5\7?\2\2\u00d5<\3\2\2")
        buf.write("\2\u00d6\u00d7\7/\2\2\u00d7\u00d8\7?\2\2\u00d8>\3\2\2")
        buf.write("\2\u00d9\u00da\7,\2\2\u00da\u00db\7?\2\2\u00db@\3\2\2")
        buf.write("\2\u00dc\u00dd\7\61\2\2\u00dd\u00de\7?\2\2\u00deB\3\2")
        buf.write("\2\2\u00df\u00e0\7\'\2\2\u00e0\u00e1\7?\2\2\u00e1D\3\2")
        buf.write("\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7h\2\2\u00e4F\3\2")
        buf.write("\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7u\2\2\u00e8\u00e9\7g\2\2\u00e9H\3\2\2\2\u00ea\u00eb")
        buf.write("\7h\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7t\2\2\u00edJ\3")
        buf.write("\2\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4L\3\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7")
        buf.write("\7w\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7e\2\2\u00f9N\3")
        buf.write("\2\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7{\2\2\u00fc\u00fd")
        buf.write("\7r\2\2\u00fd\u00fe\7g\2\2\u00feP\3\2\2\2\u00ff\u0100")
        buf.write("\7u\2\2\u0100\u0101\7v\2\2\u0101\u0102\7t\2\2\u0102\u0103")
        buf.write("\7w\2\2\u0103\u0104\7e\2\2\u0104\u0105\7v\2\2\u0105R\3")
        buf.write("\2\2\2\u0106\u0107\7k\2\2\u0107\u0108\7p\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109\u010a\7g\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7h\2\2\u010c\u010d\7c\2\2\u010d\u010e\7e\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010fT\3\2\2\2\u0110\u0111\7u\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7t\2\2\u0113\u0114\7k\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\u0116\7i\2\2\u0116V\3\2\2\2\u0117\u0118")
        buf.write("\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a\7v\2\2\u011aX\3")
        buf.write("\2\2\2\u011b\u011c\7h\2\2\u011c\u011d\7n\2\2\u011d\u011e")
        buf.write("\7q\2\2\u011e\u011f\7c\2\2\u011f\u0120\7v\2\2\u0120Z\3")
        buf.write("\2\2\2\u0121\u0122\7d\2\2\u0122\u0123\7q\2\2\u0123\u0124")
        buf.write("\7q\2\2\u0124\u0125\7n\2\2\u0125\u0126\7g\2\2\u0126\u0127")
        buf.write("\7c\2\2\u0127\u0128\7p\2\2\u0128\\\3\2\2\2\u0129\u012a")
        buf.write("\7e\2\2\u012a\u012b\7q\2\2\u012b\u012c\7p\2\2\u012c\u012d")
        buf.write("\7u\2\2\u012d\u012e\7v\2\2\u012e^\3\2\2\2\u012f\u0130")
        buf.write("\7x\2\2\u0130\u0131\7c\2\2\u0131\u0132\7t\2\2\u0132`\3")
        buf.write("\2\2\2\u0133\u0134\7e\2\2\u0134\u0135\7q\2\2\u0135\u0136")
        buf.write("\7p\2\2\u0136\u0137\7v\2\2\u0137\u0138\7k\2\2\u0138\u0139")
        buf.write("\7p\2\2\u0139\u013a\7w\2\2\u013a\u013b\7g\2\2\u013bb\3")
        buf.write("\2\2\2\u013c\u013d\7d\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141\7m\2\2\u0141d\3")
        buf.write("\2\2\2\u0142\u0143\7t\2\2\u0143\u0144\7c\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145\u0146\7i\2\2\u0146\u0147\7g\2\2\u0147f\3")
        buf.write("\2\2\2\u0148\u0149\7p\2\2\u0149\u014a\7k\2\2\u014a\u014b")
        buf.write("\7n\2\2\u014bh\3\2\2\2\u014c\u0150\t\2\2\2\u014d\u014f")
        buf.write("\t\3\2\2\u014e\u014d\3\2\2\2\u014f\u0152\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151j\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0153\u0158\7\f\2\2\u0154\u0155\7\17\2")
        buf.write("\2\u0155\u0158\7\f\2\2\u0156\u0158\7\17\2\2\u0157\u0153")
        buf.write("\3\2\2\2\u0157\u0154\3\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("l\3\2\2\2\u0159\u015a\7\62\2\2\u015a\u015c\t\4\2\2\u015b")
        buf.write("\u015d\t\5\2\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3")
        buf.write("\2\2\2\u0160\u0161\b\67\2\2\u0161n\3\2\2\2\u0162\u0167")
        buf.write("\5s:\2\u0163\u0167\5u;\2\u0164\u0167\5w<\2\u0165\u0167")
        buf.write("\5m\67\2\u0166\u0162\3\2\2\2\u0166\u0163\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0166\u0165\3\2\2\2\u0167p\3\2\2\2\u0168")
        buf.write("\u0171\t\6\2\2\u0169\u016d\t\7\2\2\u016a\u016c\t\6\2\2")
        buf.write("\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d")
        buf.write("\3\2\2\2\u0170\u0168\3\2\2\2\u0170\u0169\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0176\7\60\2\2\u0173\u0175\t\6\2")
        buf.write("\2\u0174\u0173\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0194\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0179\u0182\t\6\2\2\u017a\u017e\t\7\2\2")
        buf.write("\u017b\u017d\t\6\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3")
        buf.write("\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0182")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0179\3\2\2\2\u0181")
        buf.write("\u017a\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0187\7\60\2")
        buf.write("\2\u0184\u0186\t\6\2\2\u0185\u0184\3\2\2\2\u0186\u0189")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u018a\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018c\t\b\2\2")
        buf.write("\u018b\u018d\t\t\2\2\u018c\u018b\3\2\2\2\u018c\u018d\3")
        buf.write("\2\2\2\u018d\u018f\3\2\2\2\u018e\u0190\t\6\2\2\u018f\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0194\3\2\2\2\u0193\u0170\3\2\2\2")
        buf.write("\u0193\u0181\3\2\2\2\u0194r\3\2\2\2\u0195\u019d\t\6\2")
        buf.write("\2\u0196\u0198\t\7\2\2\u0197\u0199\t\6\2\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u0195\3\2\2\2")
        buf.write("\u019c\u0196\3\2\2\2\u019dt\3\2\2\2\u019e\u019f\7\62\2")
        buf.write("\2\u019f\u01a1\t\n\2\2\u01a0\u01a2\4\62\63\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4v\3\2\2\2\u01a5\u01a6\7\62\2\2\u01a6")
        buf.write("\u01a8\t\13\2\2\u01a7\u01a9\t\f\2\2\u01a8\u01a7\3\2\2")
        buf.write("\2\u01a9\u01aa\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01abx\3\2\2\2\u01ac\u01af\5{>\2\u01ad\u01af")
        buf.write("\5}?\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad\3\2\2\2\u01afz")
        buf.write("\3\2\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3")
        buf.write("\7w\2\2\u01b3\u01b4\7g\2\2\u01b4|\3\2\2\2\u01b5\u01b6")
        buf.write("\7h\2\2\u01b6\u01b7\7c\2\2\u01b7\u01b8\7n\2\2\u01b8\u01b9")
        buf.write("\7u\2\2\u01b9\u01ba\7g\2\2\u01ba~\3\2\2\2\u01bb\u01c1")
        buf.write("\7$\2\2\u01bc\u01bd\7^\2\2\u01bd\u01c0\t\r\2\2\u01be\u01c0")
        buf.write("\n\16\2\2\u01bf\u01bc\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0")
        buf.write("\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\7")
        buf.write("$\2\2\u01c5\u01c6\b@\3\2\u01c6\u0080\3\2\2\2\u01c7\u01cc")
        buf.write("\n\17\2\2\u01c8\u01c9\7,\2\2\u01c9\u01cc\n\20\2\2\u01ca")
        buf.write("\u01cc\5\u0083B\2\u01cb\u01c7\3\2\2\2\u01cb\u01c8\3\2")
        buf.write("\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u0082\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01d0\u01d1\7\61\2\2\u01d1\u01d2\7\61\2")
        buf.write("\2\u01d2\u01d6\3\2\2\2\u01d3\u01d5\n\21\2\2\u01d4\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2")
        buf.write("\u01d9\u01db\t\21\2\2\u01da\u01d9\3\2\2\2\u01db\u01dc")
        buf.write("\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write("\u01e6\3\2\2\2\u01de\u01df\7\61\2\2\u01df\u01e0\7,\2\2")
        buf.write("\u01e0\u01e1\3\2\2\2\u01e1\u01e2\5\u0081A\2\u01e2\u01e3")
        buf.write("\7,\2\2\u01e3\u01e4\7\61\2\2\u01e4\u01e6\3\2\2\2\u01e5")
        buf.write("\u01d0\3\2\2\2\u01e5\u01de\3\2\2\2\u01e6\u01e7\3\2\2\2")
        buf.write("\u01e7\u01e8\bB\4\2\u01e8\u0084\3\2\2\2\u01e9\u01eb\t")
        buf.write("\22\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01ef\bC\4\2\u01ef\u0086\3\2\2\2\u01f0\u01f1\13")
        buf.write("\2\2\2\u01f1\u01f2\bD\5\2\u01f2\u0088\3\2\2\2\u01f3\u01f9")
        buf.write("\7$\2\2\u01f4\u01f5\7^\2\2\u01f5\u01f8\t\r\2\2\u01f6\u01f8")
        buf.write("\n\23\2\2\u01f7\u01f4\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8")
        buf.write("\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2")
        buf.write("\u01fa\u01ff\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01fd\7")
        buf.write("^\2\2\u01fd\u0200\n\r\2\2\u01fe\u0200\7^\2\2\u01ff\u01fc")
        buf.write("\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201")
        buf.write("\u0202\bE\6\2\u0202\u008a\3\2\2\2\u0203\u0209\7$\2\2\u0204")
        buf.write("\u0208\t\24\2\2\u0205\u0206\7)\2\2\u0206\u0208\7$\2\2")
        buf.write("\u0207\u0204\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u020b\3")
        buf.write("\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020d")
        buf.write("\3\2\2\2\u020b\u0209\3\2\2\2\u020c\u020e\t\21\2\2\u020d")
        buf.write("\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u020d\3\2\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212\b")
        buf.write("F\7\2\u0212\u008c\3\2\2\2#\2\u0150\u0157\u015e\u0166\u016d")
        buf.write("\u0170\u0176\u017e\u0181\u0187\u018c\u0191\u0193\u019a")
        buf.write("\u019c\u01a3\u01aa\u01ae\u01bf\u01c1\u01cb\u01cd\u01d6")
        buf.write("\u01dc\u01e5\u01ec\u01f7\u01f9\u01ff\u0207\u0209\u020f")
        buf.write("\b\3\67\2\3@\3\b\2\2\3D\4\3E\5\3F\6")
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
    HEXADECIMAL = 54
    INTLIT = 55
    FLOATLIT = 56
    DECIMAL = 57
    BINARY = 58
    OCTAL = 59
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
            "NIL", "ID", "NL", "HEXADECIMAL", "INTLIT", "FLOATLIT", "DECIMAL", 
            "BINARY", "OCTAL", "BOOLLIT", "TRUE", "FALSE", "STRINGLIT", 
            "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "LB", "RB", "LC", "RC", 
                  "LP", "RP", "COMMA", "SEMICOLON", "COLON", "ADD", "SUBTR", 
                  "MUL", "DIV", "MOD", "EQ", "UNEQ", "LESS", "LESSEQ", "GREATER", 
                  "GREATEREQ", "AND", "OR", "NOT", "ASSIGN", "ADDASS", "SUBASS", 
                  "MULASS", "DIVASS", "MODASS", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "ID", "NL", "HEXADECIMAL", "INTLIT", "FLOATLIT", 
                  "DECIMAL", "BINARY", "OCTAL", "BOOLLIT", "TRUE", "FALSE", 
                  "STRINGLIT", "COMMENT_CONTENT", "COMMENT", "WS", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
            actions[53] = self.HEXADECIMAL_action 
            actions[62] = self.STRINGLIT_action 
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
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise IllegalEscape(self.text[1:]) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.text = self.text[1:]
                self.text = self.text.replace('\n','')
                self.text = self.text.replace('\r','')
                raise UncloseString(self.text)

     


