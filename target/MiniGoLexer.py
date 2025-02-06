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
        buf.write("\67\3\67\38\38\38\68\u0166\n8\r8\168\u0167\38\38\39\3")
        buf.write("9\39\69\u016f\n9\r9\169\u0170\39\39\3:\3:\3:\3:\5:\u0179")
        buf.write("\n:\3;\3;\3;\7;\u017e\n;\f;\16;\u0181\13;\5;\u0183\n;")
        buf.write("\3;\3;\7;\u0187\n;\f;\16;\u018a\13;\3;\3;\3;\7;\u018f")
        buf.write("\n;\f;\16;\u0192\13;\5;\u0194\n;\3;\3;\7;\u0198\n;\f;")
        buf.write("\16;\u019b\13;\3;\3;\5;\u019f\n;\3;\6;\u01a2\n;\r;\16")
        buf.write(";\u01a3\5;\u01a6\n;\3<\3<\3<\6<\u01ab\n<\r<\16<\u01ac")
        buf.write("\5<\u01af\n<\3=\3=\5=\u01b3\n=\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\3?\3?\3@\3@\3@\3@\7@\u01c4\n@\f@\16@\u01c7\13@\3")
        buf.write("@\3@\3@\3A\3A\3A\3A\7A\u01d0\nA\fA\16A\u01d3\13A\3B\3")
        buf.write("B\3B\3B\7B\u01d9\nB\fB\16B\u01dc\13B\3B\7B\u01df\nB\f")
        buf.write("B\16B\u01e2\13B\3B\3B\3B\3B\3B\3B\3B\5B\u01eb\nB\3B\3")
        buf.write("B\3C\6C\u01f0\nC\rC\16C\u01f1\3C\3C\3D\3D\3D\3E\3E\3E")
        buf.write("\3E\7E\u01fd\nE\fE\16E\u0200\13E\3E\3E\3E\5E\u0205\nE")
        buf.write("\3E\3E\3F\3F\3F\3F\7F\u020d\nF\fF\16F\u0210\13F\3F\7F")
        buf.write("\u0213\nF\fF\16F\u0216\13F\3F\3F\2\2G\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("\2\u0083B\u0085C\u0087D\u0089E\u008bF\3\2\25\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\4\2ZZzz\5\2\62;CHch\4\2DDdd\4\2QQqq")
        buf.write("\3\2\629\3\2\62;\3\2\63;\4\2GGgg\4\2--//\7\2$$^^ppttv")
        buf.write("v\6\2\f\f\17\17$$^^\3\2,,\3\2\61\61\4\2\f\f\17\17\5\2")
        buf.write("\n\13\16\16\"\"\4\2$$^^\6\2\n\f\16\17\"#%\u0080\2\u023b")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\3\u008d\3\2\2\2\5\u0093\3\2\2\2\7\u0095\3\2\2\2\t\u009b")
        buf.write("\3\2\2\2\13\u009d\3\2\2\2\r\u009f\3\2\2\2\17\u00a1\3\2")
        buf.write("\2\2\21\u00a3\3\2\2\2\23\u00a5\3\2\2\2\25\u00a7\3\2\2")
        buf.write("\2\27\u00a9\3\2\2\2\31\u00ab\3\2\2\2\33\u00ad\3\2\2\2")
        buf.write("\35\u00af\3\2\2\2\37\u00b1\3\2\2\2!\u00b3\3\2\2\2#\u00b5")
        buf.write("\3\2\2\2%\u00b7\3\2\2\2\'\u00b9\3\2\2\2)\u00bc\3\2\2\2")
        buf.write("+\u00bf\3\2\2\2-\u00c1\3\2\2\2/\u00c4\3\2\2\2\61\u00c6")
        buf.write("\3\2\2\2\63\u00c9\3\2\2\2\65\u00cc\3\2\2\2\67\u00cf\3")
        buf.write("\2\2\29\u00d1\3\2\2\2;\u00d3\3\2\2\2=\u00d6\3\2\2\2?\u00d9")
        buf.write("\3\2\2\2A\u00dc\3\2\2\2C\u00df\3\2\2\2E\u00e2\3\2\2\2")
        buf.write("G\u00e5\3\2\2\2I\u00ea\3\2\2\2K\u00ee\3\2\2\2M\u00f5\3")
        buf.write("\2\2\2O\u00fa\3\2\2\2Q\u00ff\3\2\2\2S\u0106\3\2\2\2U\u0110")
        buf.write("\3\2\2\2W\u0117\3\2\2\2Y\u011b\3\2\2\2[\u0121\3\2\2\2")
        buf.write("]\u0129\3\2\2\2_\u012f\3\2\2\2a\u0133\3\2\2\2c\u013c\3")
        buf.write("\2\2\2e\u0142\3\2\2\2g\u0148\3\2\2\2i\u014c\3\2\2\2k\u0157")
        buf.write("\3\2\2\2m\u0159\3\2\2\2o\u0162\3\2\2\2q\u016b\3\2\2\2")
        buf.write("s\u0178\3\2\2\2u\u01a5\3\2\2\2w\u01ae\3\2\2\2y\u01b2\3")
        buf.write("\2\2\2{\u01b4\3\2\2\2}\u01b9\3\2\2\2\177\u01bf\3\2\2\2")
        buf.write("\u0081\u01d1\3\2\2\2\u0083\u01ea\3\2\2\2\u0085\u01ef\3")
        buf.write("\2\2\2\u0087\u01f5\3\2\2\2\u0089\u01f8\3\2\2\2\u008b\u0208")
        buf.write("\3\2\2\2\u008d\u008e\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090")
        buf.write("\7f\2\2\u0090\u0091\7g\2\2\u0091\u0092\7z\2\2\u0092\4")
        buf.write("\3\2\2\2\u0093\u0094\7a\2\2\u0094\6\3\2\2\2\u0095\u0096")
        buf.write("\7x\2\2\u0096\u0097\7c\2\2\u0097\u0098\7n\2\2\u0098\u0099")
        buf.write("\7w\2\2\u0099\u009a\7g\2\2\u009a\b\3\2\2\2\u009b\u009c")
        buf.write("\7\60\2\2\u009c\n\3\2\2\2\u009d\u009e\7*\2\2\u009e\f\3")
        buf.write("\2\2\2\u009f\u00a0\7+\2\2\u00a0\16\3\2\2\2\u00a1\u00a2")
        buf.write("\7}\2\2\u00a2\20\3\2\2\2\u00a3\u00a4\7\177\2\2\u00a4\22")
        buf.write("\3\2\2\2\u00a5\u00a6\7]\2\2\u00a6\24\3\2\2\2\u00a7\u00a8")
        buf.write("\7_\2\2\u00a8\26\3\2\2\2\u00a9\u00aa\7.\2\2\u00aa\30\3")
        buf.write("\2\2\2\u00ab\u00ac\7=\2\2\u00ac\32\3\2\2\2\u00ad\u00ae")
        buf.write("\7<\2\2\u00ae\34\3\2\2\2\u00af\u00b0\7-\2\2\u00b0\36\3")
        buf.write("\2\2\2\u00b1\u00b2\7/\2\2\u00b2 \3\2\2\2\u00b3\u00b4\7")
        buf.write(",\2\2\u00b4\"\3\2\2\2\u00b5\u00b6\7\61\2\2\u00b6$\3\2")
        buf.write("\2\2\u00b7\u00b8\7\'\2\2\u00b8&\3\2\2\2\u00b9\u00ba\7")
        buf.write("?\2\2\u00ba\u00bb\7?\2\2\u00bb(\3\2\2\2\u00bc\u00bd\7")
        buf.write("#\2\2\u00bd\u00be\7?\2\2\u00be*\3\2\2\2\u00bf\u00c0\7")
        buf.write(">\2\2\u00c0,\3\2\2\2\u00c1\u00c2\7>\2\2\u00c2\u00c3\7")
        buf.write("?\2\2\u00c3.\3\2\2\2\u00c4\u00c5\7@\2\2\u00c5\60\3\2\2")
        buf.write("\2\u00c6\u00c7\7@\2\2\u00c7\u00c8\7?\2\2\u00c8\62\3\2")
        buf.write("\2\2\u00c9\u00ca\7(\2\2\u00ca\u00cb\7(\2\2\u00cb\64\3")
        buf.write("\2\2\2\u00cc\u00cd\7~\2\2\u00cd\u00ce\7~\2\2\u00ce\66")
        buf.write("\3\2\2\2\u00cf\u00d0\7#\2\2\u00d08\3\2\2\2\u00d1\u00d2")
        buf.write("\7?\2\2\u00d2:\3\2\2\2\u00d3\u00d4\7-\2\2\u00d4\u00d5")
        buf.write("\7?\2\2\u00d5<\3\2\2\2\u00d6\u00d7\7/\2\2\u00d7\u00d8")
        buf.write("\7?\2\2\u00d8>\3\2\2\2\u00d9\u00da\7,\2\2\u00da\u00db")
        buf.write("\7?\2\2\u00db@\3\2\2\2\u00dc\u00dd\7\61\2\2\u00dd\u00de")
        buf.write("\7?\2\2\u00deB\3\2\2\2\u00df\u00e0\7\'\2\2\u00e0\u00e1")
        buf.write("\7?\2\2\u00e1D\3\2\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4")
        buf.write("\7h\2\2\u00e4F\3\2\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7g\2\2\u00e9H\3")
        buf.write("\2\2\2\u00ea\u00eb\7h\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00edJ\3\2\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7p\2\2\u00f4L\3\2\2\2\u00f5\u00f6")
        buf.write("\7h\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7e\2\2\u00f9N\3\2\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc")
        buf.write("\7{\2\2\u00fc\u00fd\7r\2\2\u00fd\u00fe\7g\2\2\u00feP\3")
        buf.write("\2\2\2\u00ff\u0100\7u\2\2\u0100\u0101\7v\2\2\u0101\u0102")
        buf.write("\7t\2\2\u0102\u0103\7w\2\2\u0103\u0104\7e\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105R\3\2\2\2\u0106\u0107\7k\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7v\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7t\2\2\u010b\u010c\7h\2\2\u010c\u010d\7c\2\2\u010d\u010e")
        buf.write("\7e\2\2\u010e\u010f\7g\2\2\u010fT\3\2\2\2\u0110\u0111")
        buf.write("\7u\2\2\u0111\u0112\7v\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7k\2\2\u0114\u0115\7p\2\2\u0115\u0116\7i\2\2\u0116V\3")
        buf.write("\2\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011aX\3\2\2\2\u011b\u011c\7h\2\2\u011c\u011d")
        buf.write("\7n\2\2\u011d\u011e\7q\2\2\u011e\u011f\7c\2\2\u011f\u0120")
        buf.write("\7v\2\2\u0120Z\3\2\2\2\u0121\u0122\7d\2\2\u0122\u0123")
        buf.write("\7q\2\2\u0123\u0124\7q\2\2\u0124\u0125\7n\2\2\u0125\u0126")
        buf.write("\7g\2\2\u0126\u0127\7c\2\2\u0127\u0128\7p\2\2\u0128\\")
        buf.write("\3\2\2\2\u0129\u012a\7e\2\2\u012a\u012b\7q\2\2\u012b\u012c")
        buf.write("\7p\2\2\u012c\u012d\7u\2\2\u012d\u012e\7v\2\2\u012e^\3")
        buf.write("\2\2\2\u012f\u0130\7x\2\2\u0130\u0131\7c\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132`\3\2\2\2\u0133\u0134\7e\2\2\u0134\u0135")
        buf.write("\7q\2\2\u0135\u0136\7p\2\2\u0136\u0137\7v\2\2\u0137\u0138")
        buf.write("\7k\2\2\u0138\u0139\7p\2\2\u0139\u013a\7w\2\2\u013a\u013b")
        buf.write("\7g\2\2\u013bb\3\2\2\2\u013c\u013d\7d\2\2\u013d\u013e")
        buf.write("\7t\2\2\u013e\u013f\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141")
        buf.write("\7m\2\2\u0141d\3\2\2\2\u0142\u0143\7t\2\2\u0143\u0144")
        buf.write("\7c\2\2\u0144\u0145\7p\2\2\u0145\u0146\7i\2\2\u0146\u0147")
        buf.write("\7g\2\2\u0147f\3\2\2\2\u0148\u0149\7p\2\2\u0149\u014a")
        buf.write("\7k\2\2\u014a\u014b\7n\2\2\u014bh\3\2\2\2\u014c\u0150")
        buf.write("\t\2\2\2\u014d\u014f\t\3\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151j\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0158\7\f\2")
        buf.write("\2\u0154\u0155\7\17\2\2\u0155\u0158\7\f\2\2\u0156\u0158")
        buf.write("\7\17\2\2\u0157\u0153\3\2\2\2\u0157\u0154\3\2\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158l\3\2\2\2\u0159\u015a\7\62\2\2\u015a")
        buf.write("\u015c\t\4\2\2\u015b\u015d\t\5\2\2\u015c\u015b\3\2\2\2")
        buf.write("\u015d\u015e\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\b\67\2\2\u0161")
        buf.write("n\3\2\2\2\u0162\u0163\7\62\2\2\u0163\u0165\t\6\2\2\u0164")
        buf.write("\u0166\4\62\63\2\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2")
        buf.write("\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016a\b8\3\2\u016ap\3\2\2\2\u016b\u016c")
        buf.write("\7\62\2\2\u016c\u016e\t\7\2\2\u016d\u016f\t\b\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\b")
        buf.write("9\4\2\u0173r\3\2\2\2\u0174\u0179\5w<\2\u0175\u0179\5o")
        buf.write("8\2\u0176\u0179\5q9\2\u0177\u0179\5m\67\2\u0178\u0174")
        buf.write("\3\2\2\2\u0178\u0175\3\2\2\2\u0178\u0176\3\2\2\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179t\3\2\2\2\u017a\u0183\t\t\2\2\u017b")
        buf.write("\u017f\t\n\2\2\u017c\u017e\t\t\2\2\u017d\u017c\3\2\2\2")
        buf.write("\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3")
        buf.write("\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u017a")
        buf.write("\3\2\2\2\u0182\u017b\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0188\7\60\2\2\u0185\u0187\t\t\2\2\u0186\u0185\3\2\2")
        buf.write("\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u01a6\3\2\2\2\u018a\u0188\3\2\2\2\u018b")
        buf.write("\u0194\t\t\2\2\u018c\u0190\t\n\2\2\u018d\u018f\t\t\2\2")
        buf.write("\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0190\u0191\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0193\u018b\3\2\2\2\u0193\u018c\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0199\7\60\2\2\u0196\u0198\t\t\2")
        buf.write("\2\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019c\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019c\u019e\t\13\2\2\u019d\u019f\t\f\2")
        buf.write("\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1")
        buf.write("\3\2\2\2\u01a0\u01a2\t\t\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a6\3\2\2\2\u01a5\u0182\3\2\2\2\u01a5\u0193\3")
        buf.write("\2\2\2\u01a6v\3\2\2\2\u01a7\u01af\t\t\2\2\u01a8\u01aa")
        buf.write("\t\n\2\2\u01a9\u01ab\t\t\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u01af\3\2\2\2\u01ae\u01a7\3\2\2\2\u01ae\u01a8\3")
        buf.write("\2\2\2\u01afx\3\2\2\2\u01b0\u01b3\5{>\2\u01b1\u01b3\5")
        buf.write("}?\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3z\3")
        buf.write("\2\2\2\u01b4\u01b5\7v\2\2\u01b5\u01b6\7t\2\2\u01b6\u01b7")
        buf.write("\7w\2\2\u01b7\u01b8\7g\2\2\u01b8|\3\2\2\2\u01b9\u01ba")
        buf.write("\7h\2\2\u01ba\u01bb\7c\2\2\u01bb\u01bc\7n\2\2\u01bc\u01bd")
        buf.write("\7u\2\2\u01bd\u01be\7g\2\2\u01be~\3\2\2\2\u01bf\u01c5")
        buf.write("\7$\2\2\u01c0\u01c1\7^\2\2\u01c1\u01c4\t\r\2\2\u01c2\u01c4")
        buf.write("\n\16\2\2\u01c3\u01c0\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9\7")
        buf.write("$\2\2\u01c9\u01ca\b@\5\2\u01ca\u0080\3\2\2\2\u01cb\u01d0")
        buf.write("\n\17\2\2\u01cc\u01cd\7,\2\2\u01cd\u01d0\n\20\2\2\u01ce")
        buf.write("\u01d0\5\u0083B\2\u01cf\u01cb\3\2\2\2\u01cf\u01cc\3\2")
        buf.write("\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u0082\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d4\u01d5\7\61\2\2\u01d5\u01d6\7\61\2")
        buf.write("\2\u01d6\u01da\3\2\2\2\u01d7\u01d9\n\21\2\2\u01d8\u01d7")
        buf.write("\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01da")
        buf.write("\u01db\3\2\2\2\u01db\u01e0\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dd\u01df\t\21\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2")
        buf.write("\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u01eb\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\7\61\2")
        buf.write("\2\u01e4\u01e5\7,\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7")
        buf.write("\5\u0081A\2\u01e7\u01e8\7,\2\2\u01e8\u01e9\7\61\2\2\u01e9")
        buf.write("\u01eb\3\2\2\2\u01ea\u01d4\3\2\2\2\u01ea\u01e3\3\2\2\2")
        buf.write("\u01eb\u01ec\3\2\2\2\u01ec\u01ed\bB\6\2\u01ed\u0084\3")
        buf.write("\2\2\2\u01ee\u01f0\t\22\2\2\u01ef\u01ee\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f4\bC\6\2\u01f4\u0086\3")
        buf.write("\2\2\2\u01f5\u01f6\13\2\2\2\u01f6\u01f7\bD\7\2\u01f7\u0088")
        buf.write("\3\2\2\2\u01f8\u01fe\7$\2\2\u01f9\u01fa\7^\2\2\u01fa\u01fd")
        buf.write("\t\r\2\2\u01fb\u01fd\n\23\2\2\u01fc\u01f9\3\2\2\2\u01fc")
        buf.write("\u01fb\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2")
        buf.write("\u01fe\u01ff\3\2\2\2\u01ff\u0204\3\2\2\2\u0200\u01fe\3")
        buf.write("\2\2\2\u0201\u0202\7^\2\2\u0202\u0205\n\r\2\2\u0203\u0205")
        buf.write("\7^\2\2\u0204\u0201\3\2\2\2\u0204\u0203\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u0207\bE\b\2\u0207\u008a\3\2\2\2")
        buf.write("\u0208\u020e\7$\2\2\u0209\u020d\t\24\2\2\u020a\u020b\7")
        buf.write(")\2\2\u020b\u020d\7$\2\2\u020c\u0209\3\2\2\2\u020c\u020a")
        buf.write("\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e")
        buf.write("\u020f\3\2\2\2\u020f\u0214\3\2\2\2\u0210\u020e\3\2\2\2")
        buf.write("\u0211\u0213\t\21\2\2\u0212\u0211\3\2\2\2\u0213\u0216")
        buf.write("\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215")
        buf.write("\u0217\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0218\bF\t\2")
        buf.write("\u0218\u008c\3\2\2\2#\2\u0150\u0157\u015e\u0167\u0170")
        buf.write("\u0178\u017f\u0182\u0188\u0190\u0193\u0199\u019e\u01a3")
        buf.write("\u01a5\u01ac\u01ae\u01b2\u01c3\u01c5\u01cf\u01d1\u01da")
        buf.write("\u01e0\u01ea\u01f1\u01fc\u01fe\u0204\u020c\u020e\u0214")
        buf.write("\n\3\67\2\38\3\39\4\3@\5\b\2\2\3D\6\3E\7\3F\b")
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
    BINARY = 55
    OCTAL = 56
    INTLIT = 57
    FLOATLIT = 58
    DECIMAL = 59
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
            "NIL", "ID", "NL", "HEXADECIMAL", "BINARY", "OCTAL", "INTLIT", 
            "FLOATLIT", "DECIMAL", "BOOLLIT", "TRUE", "FALSE", "STRINGLIT", 
            "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "LB", "RB", "LC", "RC", 
                  "LP", "RP", "COMMA", "SEMICOLON", "COLON", "ADD", "SUBTR", 
                  "MUL", "DIV", "MOD", "EQ", "UNEQ", "LESS", "LESSEQ", "GREATER", 
                  "GREATEREQ", "AND", "OR", "NOT", "ASSIGN", "ADDASS", "SUBASS", 
                  "MULASS", "DIVASS", "MODASS", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "ID", "NL", "HEXADECIMAL", "BINARY", "OCTAL", 
                  "INTLIT", "FLOATLIT", "DECIMAL", "BOOLLIT", "TRUE", "FALSE", 
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
            actions[54] = self.BINARY_action 
            actions[55] = self.OCTAL_action 
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

     


