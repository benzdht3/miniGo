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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01ed\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\6\2\u008b\n\2\r\2\16\2\u008c\3\2\3\2\3\3\5")
        buf.write("\3\u0092\n\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\5\65")
        buf.write("\u014d\n\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\38\38\78\u015c\n8\f8\168\u015f\138\39\3")
        buf.write("9\39\39\59\u0165\n9\3:\6:\u0168\n:\r:\16:\u0169\3:\3:")
        buf.write("\7:\u016e\n:\f:\16:\u0171\13:\3:\6:\u0174\n:\r:\16:\u0175")
        buf.write("\3:\3:\7:\u017a\n:\f:\16:\u017d\13:\3:\3:\5:\u0181\n:")
        buf.write("\3:\6:\u0184\n:\r:\16:\u0185\5:\u0188\n:\3;\3;\3;\6;\u018d")
        buf.write("\n;\r;\16;\u018e\5;\u0191\n;\3<\3<\3<\6<\u0196\n<\r<\16")
        buf.write("<\u0197\3=\3=\3=\6=\u019d\n=\r=\16=\u019e\3>\3>\3>\6>")
        buf.write("\u01a4\n>\r>\16>\u01a5\3?\3?\3?\3?\7?\u01ac\n?\f?\16?")
        buf.write("\u01af\13?\3?\3?\3@\3@\3@\3@\7@\u01b7\n@\f@\16@\u01ba")
        buf.write("\13@\3A\3A\3A\3A\7A\u01c0\nA\fA\16A\u01c3\13A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\5A\u01cc\nA\3A\3A\3B\3B\3B\3B\7B\u01d4\n")
        buf.write("B\fB\16B\u01d7\13B\3B\3B\3B\5B\u01dc\nB\3B\3B\3C\3C\3")
        buf.write("C\3C\7C\u01e4\nC\fC\16C\u01e7\13C\3C\3C\3D\3D\3D\2\2E")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;")
        buf.write("u<w=y>{?}@\177\2\u0081A\u0083B\u0085C\u0087D\3\2\25\5")
        buf.write("\2\13\13\16\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\3\2\63;\4\2ZZzz\5\2\62;CHch\4\2DDdd\4\2")
        buf.write("QQqq\3\2\629\7\2$$^^ppttvv\6\2\f\f\17\17$$^^\3\2,,\3\2")
        buf.write("\61\61\4\2\f\f\17\17\4\2$$^^\6\2\n\13\16\16\"#%\u0080")
        buf.write("\2\u020a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u008a\3\2\2")
        buf.write("\2\5\u0091\3\2\2\2\7\u0096\3\2\2\2\t\u0098\3\2\2\2\13")
        buf.write("\u009a\3\2\2\2\r\u009c\3\2\2\2\17\u009e\3\2\2\2\21\u00a0")
        buf.write("\3\2\2\2\23\u00a2\3\2\2\2\25\u00a4\3\2\2\2\27\u00a6\3")
        buf.write("\2\2\2\31\u00a8\3\2\2\2\33\u00aa\3\2\2\2\35\u00ac\3\2")
        buf.write("\2\2\37\u00ae\3\2\2\2!\u00b0\3\2\2\2#\u00b2\3\2\2\2%\u00b4")
        buf.write("\3\2\2\2\'\u00b7\3\2\2\2)\u00ba\3\2\2\2+\u00bc\3\2\2\2")
        buf.write("-\u00bf\3\2\2\2/\u00c1\3\2\2\2\61\u00c4\3\2\2\2\63\u00c7")
        buf.write("\3\2\2\2\65\u00ca\3\2\2\2\67\u00cc\3\2\2\29\u00ce\3\2")
        buf.write("\2\2;\u00d1\3\2\2\2=\u00d4\3\2\2\2?\u00d7\3\2\2\2A\u00da")
        buf.write("\3\2\2\2C\u00dd\3\2\2\2E\u00e0\3\2\2\2G\u00e3\3\2\2\2")
        buf.write("I\u00e8\3\2\2\2K\u00ec\3\2\2\2M\u00f3\3\2\2\2O\u00f8\3")
        buf.write("\2\2\2Q\u00fd\3\2\2\2S\u0104\3\2\2\2U\u010e\3\2\2\2W\u0115")
        buf.write("\3\2\2\2Y\u0119\3\2\2\2[\u011f\3\2\2\2]\u0127\3\2\2\2")
        buf.write("_\u012d\3\2\2\2a\u0131\3\2\2\2c\u013a\3\2\2\2e\u0140\3")
        buf.write("\2\2\2g\u0146\3\2\2\2i\u014c\3\2\2\2k\u014e\3\2\2\2m\u0153")
        buf.write("\3\2\2\2o\u0159\3\2\2\2q\u0164\3\2\2\2s\u0187\3\2\2\2")
        buf.write("u\u0190\3\2\2\2w\u0192\3\2\2\2y\u0199\3\2\2\2{\u01a0\3")
        buf.write("\2\2\2}\u01a7\3\2\2\2\177\u01b8\3\2\2\2\u0081\u01cb\3")
        buf.write("\2\2\2\u0083\u01cf\3\2\2\2\u0085\u01df\3\2\2\2\u0087\u01ea")
        buf.write("\3\2\2\2\u0089\u008b\t\2\2\2\u008a\u0089\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u008f\b\2\2\2\u008f\4\3\2\2")
        buf.write("\2\u0090\u0092\7\17\2\2\u0091\u0090\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\7\f\2\2\u0094")
        buf.write("\u0095\b\3\3\2\u0095\6\3\2\2\2\u0096\u0097\7*\2\2\u0097")
        buf.write("\b\3\2\2\2\u0098\u0099\7+\2\2\u0099\n\3\2\2\2\u009a\u009b")
        buf.write("\7}\2\2\u009b\f\3\2\2\2\u009c\u009d\7\177\2\2\u009d\16")
        buf.write("\3\2\2\2\u009e\u009f\7]\2\2\u009f\20\3\2\2\2\u00a0\u00a1")
        buf.write("\7_\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\7.\2\2\u00a3\24\3")
        buf.write("\2\2\2\u00a4\u00a5\7=\2\2\u00a5\26\3\2\2\2\u00a6\u00a7")
        buf.write("\7<\2\2\u00a7\30\3\2\2\2\u00a8\u00a9\7\60\2\2\u00a9\32")
        buf.write("\3\2\2\2\u00aa\u00ab\7-\2\2\u00ab\34\3\2\2\2\u00ac\u00ad")
        buf.write("\7/\2\2\u00ad\36\3\2\2\2\u00ae\u00af\7,\2\2\u00af \3\2")
        buf.write("\2\2\u00b0\u00b1\7\61\2\2\u00b1\"\3\2\2\2\u00b2\u00b3")
        buf.write("\7\'\2\2\u00b3$\3\2\2\2\u00b4\u00b5\7?\2\2\u00b5\u00b6")
        buf.write("\7?\2\2\u00b6&\3\2\2\2\u00b7\u00b8\7#\2\2\u00b8\u00b9")
        buf.write("\7?\2\2\u00b9(\3\2\2\2\u00ba\u00bb\7>\2\2\u00bb*\3\2\2")
        buf.write("\2\u00bc\u00bd\7>\2\2\u00bd\u00be\7?\2\2\u00be,\3\2\2")
        buf.write("\2\u00bf\u00c0\7@\2\2\u00c0.\3\2\2\2\u00c1\u00c2\7@\2")
        buf.write("\2\u00c2\u00c3\7?\2\2\u00c3\60\3\2\2\2\u00c4\u00c5\7(")
        buf.write("\2\2\u00c5\u00c6\7(\2\2\u00c6\62\3\2\2\2\u00c7\u00c8\7")
        buf.write("~\2\2\u00c8\u00c9\7~\2\2\u00c9\64\3\2\2\2\u00ca\u00cb")
        buf.write("\7#\2\2\u00cb\66\3\2\2\2\u00cc\u00cd\7?\2\2\u00cd8\3\2")
        buf.write("\2\2\u00ce\u00cf\7<\2\2\u00cf\u00d0\7?\2\2\u00d0:\3\2")
        buf.write("\2\2\u00d1\u00d2\7-\2\2\u00d2\u00d3\7?\2\2\u00d3<\3\2")
        buf.write("\2\2\u00d4\u00d5\7/\2\2\u00d5\u00d6\7?\2\2\u00d6>\3\2")
        buf.write("\2\2\u00d7\u00d8\7,\2\2\u00d8\u00d9\7?\2\2\u00d9@\3\2")
        buf.write("\2\2\u00da\u00db\7\61\2\2\u00db\u00dc\7?\2\2\u00dcB\3")
        buf.write("\2\2\2\u00dd\u00de\7\'\2\2\u00de\u00df\7?\2\2\u00dfD\3")
        buf.write("\2\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7h\2\2\u00e2F\3")
        buf.write("\2\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6")
        buf.write("\7u\2\2\u00e6\u00e7\7g\2\2\u00e7H\3\2\2\2\u00e8\u00e9")
        buf.write("\7h\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7t\2\2\u00ebJ\3")
        buf.write("\2\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2L\3\2\2\2\u00f3\u00f4\7h\2\2\u00f4\u00f5")
        buf.write("\7w\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7e\2\2\u00f7N\3")
        buf.write("\2\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7{\2\2\u00fa\u00fb")
        buf.write("\7r\2\2\u00fb\u00fc\7g\2\2\u00fcP\3\2\2\2\u00fd\u00fe")
        buf.write("\7u\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7e\2\2\u0102\u0103\7v\2\2\u0103R\3")
        buf.write("\2\2\2\u0104\u0105\7k\2\2\u0105\u0106\7p\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\u0108\7g\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7h\2\2\u010a\u010b\7c\2\2\u010b\u010c\7e\2\2\u010c\u010d")
        buf.write("\7g\2\2\u010dT\3\2\2\2\u010e\u010f\7u\2\2\u010f\u0110")
        buf.write("\7v\2\2\u0110\u0111\7t\2\2\u0111\u0112\7k\2\2\u0112\u0113")
        buf.write("\7p\2\2\u0113\u0114\7i\2\2\u0114V\3\2\2\2\u0115\u0116")
        buf.write("\7k\2\2\u0116\u0117\7p\2\2\u0117\u0118\7v\2\2\u0118X\3")
        buf.write("\2\2\2\u0119\u011a\7h\2\2\u011a\u011b\7n\2\2\u011b\u011c")
        buf.write("\7q\2\2\u011c\u011d\7c\2\2\u011d\u011e\7v\2\2\u011eZ\3")
        buf.write("\2\2\2\u011f\u0120\7d\2\2\u0120\u0121\7q\2\2\u0121\u0122")
        buf.write("\7q\2\2\u0122\u0123\7n\2\2\u0123\u0124\7g\2\2\u0124\u0125")
        buf.write("\7c\2\2\u0125\u0126\7p\2\2\u0126\\\3\2\2\2\u0127\u0128")
        buf.write("\7e\2\2\u0128\u0129\7q\2\2\u0129\u012a\7p\2\2\u012a\u012b")
        buf.write("\7u\2\2\u012b\u012c\7v\2\2\u012c^\3\2\2\2\u012d\u012e")
        buf.write("\7x\2\2\u012e\u012f\7c\2\2\u012f\u0130\7t\2\2\u0130`\3")
        buf.write("\2\2\2\u0131\u0132\7e\2\2\u0132\u0133\7q\2\2\u0133\u0134")
        buf.write("\7p\2\2\u0134\u0135\7v\2\2\u0135\u0136\7k\2\2\u0136\u0137")
        buf.write("\7p\2\2\u0137\u0138\7w\2\2\u0138\u0139\7g\2\2\u0139b\3")
        buf.write("\2\2\2\u013a\u013b\7d\2\2\u013b\u013c\7t\2\2\u013c\u013d")
        buf.write("\7g\2\2\u013d\u013e\7c\2\2\u013e\u013f\7m\2\2\u013fd\3")
        buf.write("\2\2\2\u0140\u0141\7t\2\2\u0141\u0142\7c\2\2\u0142\u0143")
        buf.write("\7p\2\2\u0143\u0144\7i\2\2\u0144\u0145\7g\2\2\u0145f\3")
        buf.write("\2\2\2\u0146\u0147\7p\2\2\u0147\u0148\7k\2\2\u0148\u0149")
        buf.write("\7n\2\2\u0149h\3\2\2\2\u014a\u014d\5k\66\2\u014b\u014d")
        buf.write("\5m\67\2\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d")
        buf.write("j\3\2\2\2\u014e\u014f\7v\2\2\u014f\u0150\7t\2\2\u0150")
        buf.write("\u0151\7w\2\2\u0151\u0152\7g\2\2\u0152l\3\2\2\2\u0153")
        buf.write("\u0154\7h\2\2\u0154\u0155\7c\2\2\u0155\u0156\7n\2\2\u0156")
        buf.write("\u0157\7u\2\2\u0157\u0158\7g\2\2\u0158n\3\2\2\2\u0159")
        buf.write("\u015d\t\3\2\2\u015a\u015c\t\4\2\2\u015b\u015a\3\2\2\2")
        buf.write("\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3")
        buf.write("\2\2\2\u015ep\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0165")
        buf.write("\5u;\2\u0161\u0165\5y=\2\u0162\u0165\5{>\2\u0163\u0165")
        buf.write("\5w<\2\u0164\u0160\3\2\2\2\u0164\u0161\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0163\3\2\2\2\u0165r\3\2\2\2\u0166\u0168")
        buf.write("\t\5\2\2\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016f\5\31\r\2\u016c\u016e\t\5\2\2\u016d\u016c")
        buf.write("\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0188\3\2\2\2\u0171\u016f\3\2\2\2")
        buf.write("\u0172\u0174\t\5\2\2\u0173\u0172\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u017b\5\31\r\2\u0178\u017a\t\5\2\2\u0179")
        buf.write("\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u017b\3")
        buf.write("\2\2\2\u017e\u0180\t\6\2\2\u017f\u0181\t\7\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182")
        buf.write("\u0184\t\5\2\2\u0183\u0182\3\2\2\2\u0184\u0185\3\2\2\2")
        buf.write("\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188\3")
        buf.write("\2\2\2\u0187\u0167\3\2\2\2\u0187\u0173\3\2\2\2\u0188t")
        buf.write("\3\2\2\2\u0189\u0191\t\5\2\2\u018a\u018c\t\b\2\2\u018b")
        buf.write("\u018d\t\5\2\2\u018c\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\3")
        buf.write("\2\2\2\u0190\u0189\3\2\2\2\u0190\u018a\3\2\2\2\u0191v")
        buf.write("\3\2\2\2\u0192\u0193\7\62\2\2\u0193\u0195\t\t\2\2\u0194")
        buf.write("\u0196\t\n\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198x\3\2\2")
        buf.write("\2\u0199\u019a\7\62\2\2\u019a\u019c\t\13\2\2\u019b\u019d")
        buf.write("\4\62\63\2\u019c\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019fz\3\2\2\2\u01a0")
        buf.write("\u01a1\7\62\2\2\u01a1\u01a3\t\f\2\2\u01a2\u01a4\t\r\2")
        buf.write("\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6|\3\2\2\2\u01a7\u01ad")
        buf.write("\7$\2\2\u01a8\u01a9\7^\2\2\u01a9\u01ac\t\16\2\2\u01aa")
        buf.write("\u01ac\n\17\2\2\u01ab\u01a8\3\2\2\2\u01ab\u01aa\3\2\2")
        buf.write("\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0")
        buf.write("\u01b1\7$\2\2\u01b1~\3\2\2\2\u01b2\u01b7\n\20\2\2\u01b3")
        buf.write("\u01b4\7,\2\2\u01b4\u01b7\n\21\2\2\u01b5\u01b7\5\u0081")
        buf.write("A\2\u01b6\u01b2\3\2\2\2\u01b6\u01b3\3\2\2\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u0080\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01bb\u01bc\7\61\2\2\u01bc\u01bd\7\61\2\2\u01bd\u01c1")
        buf.write("\3\2\2\2\u01be\u01c0\n\22\2\2\u01bf\u01be\3\2\2\2\u01c0")
        buf.write("\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01cc\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\7")
        buf.write("\61\2\2\u01c5\u01c6\7,\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8")
        buf.write("\5\177@\2\u01c8\u01c9\7,\2\2\u01c9\u01ca\7\61\2\2\u01ca")
        buf.write("\u01cc\3\2\2\2\u01cb\u01bb\3\2\2\2\u01cb\u01c4\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01ce\bA\2\2\u01ce\u0082\3")
        buf.write("\2\2\2\u01cf\u01d5\7$\2\2\u01d0\u01d1\7^\2\2\u01d1\u01d4")
        buf.write("\t\16\2\2\u01d2\u01d4\n\23\2\2\u01d3\u01d0\3\2\2\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d6\3\2\2\2\u01d6\u01db\3\2\2\2\u01d7\u01d5\3")
        buf.write("\2\2\2\u01d8\u01d9\7^\2\2\u01d9\u01dc\n\16\2\2\u01da\u01dc")
        buf.write("\7^\2\2\u01db\u01d8\3\2\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01de\bB\4\2\u01de\u0084\3\2\2\2")
        buf.write("\u01df\u01e5\7$\2\2\u01e0\u01e4\t\24\2\2\u01e1\u01e2\7")
        buf.write(")\2\2\u01e2\u01e4\7$\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e8\u01e9\bC\5\2\u01e9\u0086\3\2\2\2\u01ea\u01eb\13")
        buf.write("\2\2\2\u01eb\u01ec\bD\6\2\u01ec\u0088\3\2\2\2\37\2\u008c")
        buf.write("\u0091\u014c\u015d\u0164\u0169\u016f\u0175\u017b\u0180")
        buf.write("\u0185\u0187\u018e\u0190\u0197\u019e\u01a5\u01ab\u01ad")
        buf.write("\u01b6\u01b8\u01c1\u01cb\u01d3\u01d5\u01db\u01e3\u01e5")
        buf.write("\7\b\2\2\3\3\2\3B\3\3C\4\3D\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    NL = 2
    LB = 3
    RB = 4
    LC = 5
    RC = 6
    LP = 7
    RP = 8
    COMMA = 9
    SEMICOLON = 10
    COLON = 11
    DOT = 12
    ADD = 13
    SUBTR = 14
    MUL = 15
    DIV = 16
    MOD = 17
    EQ = 18
    UNEQ = 19
    LESS = 20
    LESSEQ = 21
    GREATER = 22
    GREATEREQ = 23
    AND = 24
    OR = 25
    NOT = 26
    INITOP = 27
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
    BOOLLIT = 52
    TRUE = 53
    FALSE = 54
    ID = 55
    INTLIT = 56
    FLOATLIT = 57
    DECIMAL = 58
    HEXADECIMAL = 59
    BINARY = 60
    OCTAL = 61
    STRINGLIT = 62
    COMMENT = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'", 
            "'.'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", 
            "'+='", "'-='", "'*='", "'/='", "'%='", "'if'", "'else'", "'for'", 
            "'return'", "'func'", "'type'", "'struct'", "'interface'", "'string'", 
            "'int'", "'float'", "'boolean'", "'const'", "'var'", "'continue'", 
            "'break'", "'range'", "'nil'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "NL", "LB", "RB", "LC", "RC", "LP", "RP", "COMMA", "SEMICOLON", 
            "COLON", "DOT", "ADD", "SUBTR", "MUL", "DIV", "MOD", "EQ", "UNEQ", 
            "LESS", "LESSEQ", "GREATER", "GREATEREQ", "AND", "OR", "NOT", 
            "INITOP", "ASSIGN", "ADDASS", "SUBASS", "MULASS", "DIVASS", 
            "MODASS", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
            "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
            "CONTINUE", "BREAK", "RANGE", "NIL", "BOOLLIT", "TRUE", "FALSE", 
            "ID", "INTLIT", "FLOATLIT", "DECIMAL", "HEXADECIMAL", "BINARY", 
            "OCTAL", "STRINGLIT", "COMMENT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "WS", "NL", "LB", "RB", "LC", "RC", "LP", "RP", "COMMA", 
                  "SEMICOLON", "COLON", "DOT", "ADD", "SUBTR", "MUL", "DIV", 
                  "MOD", "EQ", "UNEQ", "LESS", "LESSEQ", "GREATER", "GREATEREQ", 
                  "AND", "OR", "NOT", "INITOP", "ASSIGN", "ADDASS", "SUBASS", 
                  "MULASS", "DIVASS", "MODASS", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "BOOLLIT", "TRUE", "FALSE", "ID", "INTLIT", 
                  "FLOATLIT", "DECIMAL", "HEXADECIMAL", "BINARY", "OCTAL", 
                  "STRINGLIT", "COMMENT_CONTENT", "COMMENT", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        self.preType = tk;
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
            actions[1] = self.NL_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.preType in [self.ID, self.INTLIT, self.FLOATLIT, self.STRINGLIT, self.BOOLLIT, self.RETURN, self.BREAK, self.CONTINUE, self.RB, self.RC, self.RP, self.NIL, self.STRING, self.INT, self.FLOAT, self.BOOLEAN]: self.text = ';'
                else: self.skip()

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise IllegalEscape(self.text) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise UncloseString(self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


