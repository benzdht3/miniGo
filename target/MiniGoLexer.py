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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0201\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\6\5\u009f\n\5\r\5\16")
        buf.write("\5\u00a0\3\5\3\5\3\6\5\6\u00a6\n\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\38\38\58\u0161\n8\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3:\3;\3;\7;\u0170\n;\f;\16;")
        buf.write("\u0173\13;\3<\3<\3<\3<\5<\u0179\n<\3=\6=\u017c\n=\r=\16")
        buf.write("=\u017d\3=\3=\7=\u0182\n=\f=\16=\u0185\13=\3=\6=\u0188")
        buf.write("\n=\r=\16=\u0189\3=\3=\7=\u018e\n=\f=\16=\u0191\13=\3")
        buf.write("=\3=\5=\u0195\n=\3=\6=\u0198\n=\r=\16=\u0199\5=\u019c")
        buf.write("\n=\3>\3>\3>\6>\u01a1\n>\r>\16>\u01a2\5>\u01a5\n>\3?\3")
        buf.write("?\3?\6?\u01aa\n?\r?\16?\u01ab\3@\3@\3@\6@\u01b1\n@\r@")
        buf.write("\16@\u01b2\3A\3A\3A\6A\u01b8\nA\rA\16A\u01b9\3B\3B\3B")
        buf.write("\3B\7B\u01c0\nB\fB\16B\u01c3\13B\3B\3B\3C\3C\3C\3C\7C")
        buf.write("\u01cb\nC\fC\16C\u01ce\13C\3D\3D\3D\3D\7D\u01d4\nD\fD")
        buf.write("\16D\u01d7\13D\3D\3D\3D\3D\3D\3D\3D\5D\u01e0\nD\3D\3D")
        buf.write("\3E\3E\3E\3E\7E\u01e8\nE\fE\16E\u01eb\13E\3E\3E\3E\5E")
        buf.write("\u01f0\nE\3E\3E\3F\3F\3F\3F\7F\u01f8\nF\fF\16F\u01fb\13")
        buf.write("F\3F\3F\3G\3G\3G\2\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085")
        buf.write("\2\u0087D\u0089E\u008bF\u008dG\3\2\25\5\2\13\13\16\17")
        buf.write("\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--/")
        buf.write("/\3\2\63;\4\2ZZzz\5\2\62;CHch\4\2DDdd\4\2QQqq\3\2\629")
        buf.write("\7\2$$^^ppttvv\6\2\f\f\17\17$$^^\3\2,,\3\2\61\61\4\2\f")
        buf.write("\f\17\17\4\2$$^^\6\2\n\13\16\16\"#%\u0080\2\u021e\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0095\3\2\2\2\7\u0097")
        buf.write("\3\2\2\2\t\u009e\3\2\2\2\13\u00a5\3\2\2\2\r\u00aa\3\2")
        buf.write("\2\2\17\u00ac\3\2\2\2\21\u00ae\3\2\2\2\23\u00b0\3\2\2")
        buf.write("\2\25\u00b2\3\2\2\2\27\u00b4\3\2\2\2\31\u00b6\3\2\2\2")
        buf.write("\33\u00b8\3\2\2\2\35\u00ba\3\2\2\2\37\u00bc\3\2\2\2!\u00be")
        buf.write("\3\2\2\2#\u00c0\3\2\2\2%\u00c2\3\2\2\2\'\u00c4\3\2\2\2")
        buf.write(")\u00c6\3\2\2\2+\u00c8\3\2\2\2-\u00cb\3\2\2\2/\u00ce\3")
        buf.write("\2\2\2\61\u00d0\3\2\2\2\63\u00d3\3\2\2\2\65\u00d5\3\2")
        buf.write("\2\2\67\u00d8\3\2\2\29\u00db\3\2\2\2;\u00de\3\2\2\2=\u00e0")
        buf.write("\3\2\2\2?\u00e2\3\2\2\2A\u00e5\3\2\2\2C\u00e8\3\2\2\2")
        buf.write("E\u00eb\3\2\2\2G\u00ee\3\2\2\2I\u00f1\3\2\2\2K\u00f4\3")
        buf.write("\2\2\2M\u00f7\3\2\2\2O\u00fc\3\2\2\2Q\u0100\3\2\2\2S\u0107")
        buf.write("\3\2\2\2U\u010c\3\2\2\2W\u0111\3\2\2\2Y\u0118\3\2\2\2")
        buf.write("[\u0122\3\2\2\2]\u0129\3\2\2\2_\u012d\3\2\2\2a\u0133\3")
        buf.write("\2\2\2c\u013b\3\2\2\2e\u0141\3\2\2\2g\u0145\3\2\2\2i\u014e")
        buf.write("\3\2\2\2k\u0154\3\2\2\2m\u015a\3\2\2\2o\u0160\3\2\2\2")
        buf.write("q\u0162\3\2\2\2s\u0167\3\2\2\2u\u016d\3\2\2\2w\u0178\3")
        buf.write("\2\2\2y\u019b\3\2\2\2{\u01a4\3\2\2\2}\u01a6\3\2\2\2\177")
        buf.write("\u01ad\3\2\2\2\u0081\u01b4\3\2\2\2\u0083\u01bb\3\2\2\2")
        buf.write("\u0085\u01cc\3\2\2\2\u0087\u01df\3\2\2\2\u0089\u01e3\3")
        buf.write("\2\2\2\u008b\u01f3\3\2\2\2\u008d\u01fe\3\2\2\2\u008f\u0090")
        buf.write("\7k\2\2\u0090\u0091\7p\2\2\u0091\u0092\7f\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7z\2\2\u0094\4\3\2\2\2\u0095\u0096")
        buf.write("\7a\2\2\u0096\6\3\2\2\2\u0097\u0098\7x\2\2\u0098\u0099")
        buf.write("\7c\2\2\u0099\u009a\7n\2\2\u009a\u009b\7w\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\b\3\2\2\2\u009d\u009f\t\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\b\5\2\2")
        buf.write("\u00a3\n\3\2\2\2\u00a4\u00a6\7\17\2\2\u00a5\u00a4\3\2")
        buf.write("\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8")
        buf.write("\7\f\2\2\u00a8\u00a9\b\6\3\2\u00a9\f\3\2\2\2\u00aa\u00ab")
        buf.write("\7*\2\2\u00ab\16\3\2\2\2\u00ac\u00ad\7+\2\2\u00ad\20\3")
        buf.write("\2\2\2\u00ae\u00af\7}\2\2\u00af\22\3\2\2\2\u00b0\u00b1")
        buf.write("\7\177\2\2\u00b1\24\3\2\2\2\u00b2\u00b3\7]\2\2\u00b3\26")
        buf.write("\3\2\2\2\u00b4\u00b5\7_\2\2\u00b5\30\3\2\2\2\u00b6\u00b7")
        buf.write("\7.\2\2\u00b7\32\3\2\2\2\u00b8\u00b9\7=\2\2\u00b9\34\3")
        buf.write("\2\2\2\u00ba\u00bb\7<\2\2\u00bb\36\3\2\2\2\u00bc\u00bd")
        buf.write("\7\60\2\2\u00bd \3\2\2\2\u00be\u00bf\7-\2\2\u00bf\"\3")
        buf.write("\2\2\2\u00c0\u00c1\7/\2\2\u00c1$\3\2\2\2\u00c2\u00c3\7")
        buf.write(",\2\2\u00c3&\3\2\2\2\u00c4\u00c5\7\61\2\2\u00c5(\3\2\2")
        buf.write("\2\u00c6\u00c7\7\'\2\2\u00c7*\3\2\2\2\u00c8\u00c9\7?\2")
        buf.write("\2\u00c9\u00ca\7?\2\2\u00ca,\3\2\2\2\u00cb\u00cc\7#\2")
        buf.write("\2\u00cc\u00cd\7?\2\2\u00cd.\3\2\2\2\u00ce\u00cf\7>\2")
        buf.write("\2\u00cf\60\3\2\2\2\u00d0\u00d1\7>\2\2\u00d1\u00d2\7?")
        buf.write("\2\2\u00d2\62\3\2\2\2\u00d3\u00d4\7@\2\2\u00d4\64\3\2")
        buf.write("\2\2\u00d5\u00d6\7@\2\2\u00d6\u00d7\7?\2\2\u00d7\66\3")
        buf.write("\2\2\2\u00d8\u00d9\7(\2\2\u00d9\u00da\7(\2\2\u00da8\3")
        buf.write("\2\2\2\u00db\u00dc\7~\2\2\u00dc\u00dd\7~\2\2\u00dd:\3")
        buf.write("\2\2\2\u00de\u00df\7#\2\2\u00df<\3\2\2\2\u00e0\u00e1\7")
        buf.write("?\2\2\u00e1>\3\2\2\2\u00e2\u00e3\7<\2\2\u00e3\u00e4\7")
        buf.write("?\2\2\u00e4@\3\2\2\2\u00e5\u00e6\7-\2\2\u00e6\u00e7\7")
        buf.write("?\2\2\u00e7B\3\2\2\2\u00e8\u00e9\7/\2\2\u00e9\u00ea\7")
        buf.write("?\2\2\u00eaD\3\2\2\2\u00eb\u00ec\7,\2\2\u00ec\u00ed\7")
        buf.write("?\2\2\u00edF\3\2\2\2\u00ee\u00ef\7\61\2\2\u00ef\u00f0")
        buf.write("\7?\2\2\u00f0H\3\2\2\2\u00f1\u00f2\7\'\2\2\u00f2\u00f3")
        buf.write("\7?\2\2\u00f3J\3\2\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6")
        buf.write("\7h\2\2\u00f6L\3\2\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7u\2\2\u00fa\u00fb\7g\2\2\u00fbN\3")
        buf.write("\2\2\2\u00fc\u00fd\7h\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7t\2\2\u00ffP\3\2\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7v\2\2\u0103\u0104\7w\2\2\u0104\u0105")
        buf.write("\7t\2\2\u0105\u0106\7p\2\2\u0106R\3\2\2\2\u0107\u0108")
        buf.write("\7h\2\2\u0108\u0109\7w\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7e\2\2\u010bT\3\2\2\2\u010c\u010d\7v\2\2\u010d\u010e")
        buf.write("\7{\2\2\u010e\u010f\7r\2\2\u010f\u0110\7g\2\2\u0110V\3")
        buf.write("\2\2\2\u0111\u0112\7u\2\2\u0112\u0113\7v\2\2\u0113\u0114")
        buf.write("\7t\2\2\u0114\u0115\7w\2\2\u0115\u0116\7e\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117X\3\2\2\2\u0118\u0119\7k\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011a\u011b\7v\2\2\u011b\u011c\7g\2\2\u011c\u011d")
        buf.write("\7t\2\2\u011d\u011e\7h\2\2\u011e\u011f\7c\2\2\u011f\u0120")
        buf.write("\7e\2\2\u0120\u0121\7g\2\2\u0121Z\3\2\2\2\u0122\u0123")
        buf.write("\7u\2\2\u0123\u0124\7v\2\2\u0124\u0125\7t\2\2\u0125\u0126")
        buf.write("\7k\2\2\u0126\u0127\7p\2\2\u0127\u0128\7i\2\2\u0128\\")
        buf.write("\3\2\2\2\u0129\u012a\7k\2\2\u012a\u012b\7p\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c^\3\2\2\2\u012d\u012e\7h\2\2\u012e\u012f")
        buf.write("\7n\2\2\u012f\u0130\7q\2\2\u0130\u0131\7c\2\2\u0131\u0132")
        buf.write("\7v\2\2\u0132`\3\2\2\2\u0133\u0134\7d\2\2\u0134\u0135")
        buf.write("\7q\2\2\u0135\u0136\7q\2\2\u0136\u0137\7n\2\2\u0137\u0138")
        buf.write("\7g\2\2\u0138\u0139\7c\2\2\u0139\u013a\7p\2\2\u013ab\3")
        buf.write("\2\2\2\u013b\u013c\7e\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7p\2\2\u013e\u013f\7u\2\2\u013f\u0140\7v\2\2\u0140d\3")
        buf.write("\2\2\2\u0141\u0142\7x\2\2\u0142\u0143\7c\2\2\u0143\u0144")
        buf.write("\7t\2\2\u0144f\3\2\2\2\u0145\u0146\7e\2\2\u0146\u0147")
        buf.write("\7q\2\2\u0147\u0148\7p\2\2\u0148\u0149\7v\2\2\u0149\u014a")
        buf.write("\7k\2\2\u014a\u014b\7p\2\2\u014b\u014c\7w\2\2\u014c\u014d")
        buf.write("\7g\2\2\u014dh\3\2\2\2\u014e\u014f\7d\2\2\u014f\u0150")
        buf.write("\7t\2\2\u0150\u0151\7g\2\2\u0151\u0152\7c\2\2\u0152\u0153")
        buf.write("\7m\2\2\u0153j\3\2\2\2\u0154\u0155\7t\2\2\u0155\u0156")
        buf.write("\7c\2\2\u0156\u0157\7p\2\2\u0157\u0158\7i\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159l\3\2\2\2\u015a\u015b\7p\2\2\u015b\u015c")
        buf.write("\7k\2\2\u015c\u015d\7n\2\2\u015dn\3\2\2\2\u015e\u0161")
        buf.write("\5q9\2\u015f\u0161\5s:\2\u0160\u015e\3\2\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161p\3\2\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write("\7t\2\2\u0164\u0165\7w\2\2\u0165\u0166\7g\2\2\u0166r\3")
        buf.write("\2\2\2\u0167\u0168\7h\2\2\u0168\u0169\7c\2\2\u0169\u016a")
        buf.write("\7n\2\2\u016a\u016b\7u\2\2\u016b\u016c\7g\2\2\u016ct\3")
        buf.write("\2\2\2\u016d\u0171\t\3\2\2\u016e\u0170\t\4\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172v\3\2\2\2\u0173\u0171\3\2\2\2\u0174")
        buf.write("\u0179\5{>\2\u0175\u0179\5\177@\2\u0176\u0179\5\u0081")
        buf.write("A\2\u0177\u0179\5}?\2\u0178\u0174\3\2\2\2\u0178\u0175")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("x\3\2\2\2\u017a\u017c\t\5\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0183\5\37\20\2\u0180\u0182")
        buf.write("\t\5\2\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u019c\3\2\2\2")
        buf.write("\u0185\u0183\3\2\2\2\u0186\u0188\t\5\2\2\u0187\u0186\3")
        buf.write("\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018f\5\37\20\2\u018c")
        buf.write("\u018e\t\5\2\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2")
        buf.write("\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\3")
        buf.write("\2\2\2\u0191\u018f\3\2\2\2\u0192\u0194\t\6\2\2\u0193\u0195")
        buf.write("\t\7\2\2\u0194\u0193\3\2\2\2\u0194\u0195\3\2\2\2\u0195")
        buf.write("\u0197\3\2\2\2\u0196\u0198\t\5\2\2\u0197\u0196\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3")
        buf.write("\2\2\2\u019a\u019c\3\2\2\2\u019b\u017b\3\2\2\2\u019b\u0187")
        buf.write("\3\2\2\2\u019cz\3\2\2\2\u019d\u01a5\t\5\2\2\u019e\u01a0")
        buf.write("\t\b\2\2\u019f\u01a1\t\5\2\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a5\3\2\2\2\u01a4\u019d\3\2\2\2\u01a4\u019e\3")
        buf.write("\2\2\2\u01a5|\3\2\2\2\u01a6\u01a7\7\62\2\2\u01a7\u01a9")
        buf.write("\t\t\2\2\u01a8\u01aa\t\n\2\2\u01a9\u01a8\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac~\3\2\2\2\u01ad\u01ae\7\62\2\2\u01ae\u01b0\t\13")
        buf.write("\2\2\u01af\u01b1\4\62\63\2\u01b0\u01af\3\2\2\2\u01b1\u01b2")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u0080\3\2\2\2\u01b4\u01b5\7\62\2\2\u01b5\u01b7\t\f\2")
        buf.write("\2\u01b6\u01b8\t\r\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01b9")
        buf.write("\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u0082\3\2\2\2\u01bb\u01c1\7$\2\2\u01bc\u01bd\7^\2\2\u01bd")
        buf.write("\u01c0\t\16\2\2\u01be\u01c0\n\17\2\2\u01bf\u01bc\3\2\2")
        buf.write("\2\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c4\u01c5\7$\2\2\u01c5\u0084\3\2\2\2")
        buf.write("\u01c6\u01cb\n\20\2\2\u01c7\u01c8\7,\2\2\u01c8\u01cb\n")
        buf.write("\21\2\2\u01c9\u01cb\5\u0087D\2\u01ca\u01c6\3\2\2\2\u01ca")
        buf.write("\u01c7\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2")
        buf.write("\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u0086\3")
        buf.write("\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d0\7\61\2\2\u01d0")
        buf.write("\u01d1\7\61\2\2\u01d1\u01d5\3\2\2\2\u01d2\u01d4\n\22\2")
        buf.write("\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01e0\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01d9\7\61\2\2\u01d9\u01da\7,\2\2")
        buf.write("\u01da\u01db\3\2\2\2\u01db\u01dc\5\u0085C\2\u01dc\u01dd")
        buf.write("\7,\2\2\u01dd\u01de\7\61\2\2\u01de\u01e0\3\2\2\2\u01df")
        buf.write("\u01cf\3\2\2\2\u01df\u01d8\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01e2\bD\2\2\u01e2\u0088\3\2\2\2\u01e3\u01e9\7")
        buf.write("$\2\2\u01e4\u01e5\7^\2\2\u01e5\u01e8\t\16\2\2\u01e6\u01e8")
        buf.write("\n\23\2\2\u01e7\u01e4\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8")
        buf.write("\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2")
        buf.write("\u01ea\u01ef\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ed\7")
        buf.write("^\2\2\u01ed\u01f0\n\16\2\2\u01ee\u01f0\7^\2\2\u01ef\u01ec")
        buf.write("\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01f2\bE\4\2\u01f2\u008a\3\2\2\2\u01f3\u01f9\7$\2\2\u01f4")
        buf.write("\u01f8\t\24\2\2\u01f5\u01f6\7)\2\2\u01f6\u01f8\7$\2\2")
        buf.write("\u01f7\u01f4\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01fb\3")
        buf.write("\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc")
        buf.write("\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01fd\bF\5\2\u01fd")
        buf.write("\u008c\3\2\2\2\u01fe\u01ff\13\2\2\2\u01ff\u0200\bG\6\2")
        buf.write("\u0200\u008e\3\2\2\2\37\2\u00a0\u00a5\u0160\u0171\u0178")
        buf.write("\u017d\u0183\u0189\u018f\u0194\u0199\u019b\u01a2\u01a4")
        buf.write("\u01ab\u01b2\u01b9\u01bf\u01c1\u01ca\u01cc\u01d5\u01df")
        buf.write("\u01e7\u01e9\u01ef\u01f7\u01f9\7\b\2\2\3\6\2\3E\3\3F\4")
        buf.write("\3G\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    WS = 4
    NL = 5
    LB = 6
    RB = 7
    LC = 8
    RC = 9
    LP = 10
    RP = 11
    COMMA = 12
    SEMICOLON = 13
    COLON = 14
    DOT = 15
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
    INITOP = 30
    ASSIGN = 31
    ADDASS = 32
    SUBASS = 33
    MULASS = 34
    DIVASS = 35
    MODASS = 36
    IF = 37
    ELSE = 38
    FOR = 39
    RETURN = 40
    FUNC = 41
    TYPE = 42
    STRUCT = 43
    INTERFACE = 44
    STRING = 45
    INT = 46
    FLOAT = 47
    BOOLEAN = 48
    CONST = 49
    VAR = 50
    CONTINUE = 51
    BREAK = 52
    RANGE = 53
    NIL = 54
    BOOLLIT = 55
    TRUE = 56
    FALSE = 57
    ID = 58
    INTLIT = 59
    FLOATLIT = 60
    DECIMAL = 61
    HEXADECIMAL = 62
    BINARY = 63
    OCTAL = 64
    STRINGLIT = 65
    COMMENT = 66
    ILLEGAL_ESCAPE = 67
    UNCLOSE_STRING = 68
    ERROR_CHAR = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'index'", "'_'", "'value'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "';'", "':'", "'.'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", 
            "'||'", "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'" ]

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

    ruleNames = [ "T__0", "T__1", "T__2", "WS", "NL", "LB", "RB", "LC", 
                  "RC", "LP", "RP", "COMMA", "SEMICOLON", "COLON", "DOT", 
                  "ADD", "SUBTR", "MUL", "DIV", "MOD", "EQ", "UNEQ", "LESS", 
                  "LESSEQ", "GREATER", "GREATEREQ", "AND", "OR", "NOT", 
                  "INITOP", "ASSIGN", "ADDASS", "SUBASS", "MULASS", "DIVASS", 
                  "MODASS", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "BOOLLIT", 
                  "TRUE", "FALSE", "ID", "INTLIT", "FLOATLIT", "DECIMAL", 
                  "HEXADECIMAL", "BINARY", "OCTAL", "STRINGLIT", "COMMENT_CONTENT", 
                  "COMMENT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[4] = self.NL_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ERROR_CHAR_action 
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
     


