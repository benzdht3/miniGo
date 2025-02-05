# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u0237\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\7\2p\n\2\f\2\16\2s")
        buf.write("\13\2\3\2\3\2\7\2w\n\2\f\2\16\2z\13\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\5\4\u0085\n\4\3\5\7\5\u0088\n\5\f")
        buf.write("\5\16\5\u008b\13\5\3\5\3\5\3\5\3\5\5\5\u0091\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u009d\n\7\3\7\5")
        buf.write("\7\u00a0\n\7\3\7\3\7\3\b\3\b\3\t\6\t\u00a7\n\t\r\t\16")
        buf.write("\t\u00a8\3\t\3\t\5\t\u00ad\n\t\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\5\f\u00ba\n\f\3\r\3\r\3\r\7\r")
        buf.write("\u00bf\n\r\f\r\16\r\u00c2\13\r\3\r\3\r\3\r\3\16\7\16\u00c8")
        buf.write("\n\16\f\16\16\16\u00cb\13\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00d2\n\16\3\16\3\16\3\17\3\17\3\17\7\17\u00d9\n")
        buf.write("\17\f\17\16\17\u00dc\13\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\5\20\u00e4\n\20\3\20\3\20\3\20\5\20\u00e9\n\20\3\21")
        buf.write("\3\21\3\21\5\21\u00ee\n\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00f7\n\22\3\23\3\23\5\23\u00fb\n\23\3\23")
        buf.write("\3\23\3\23\7\23\u0100\n\23\f\23\16\23\u0103\13\23\3\23")
        buf.write("\3\23\7\23\u0107\n\23\f\23\16\23\u010a\13\23\7\23\u010c")
        buf.write("\n\23\f\23\16\23\u010f\13\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u0123\n\25\3\25\3\25\3\25\3\25\5\25\u0129")
        buf.write("\n\25\3\26\3\26\3\26\3\26\5\26\u012f\n\26\3\27\3\27\3")
        buf.write("\27\5\27\u0134\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u013d\n\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0145")
        buf.write("\n\31\f\31\16\31\u0148\13\31\3\31\7\31\u014b\n\31\f\31")
        buf.write("\16\31\u014e\13\31\3\31\3\31\5\31\u0152\n\31\3\32\3\32")
        buf.write("\3\32\3\32\7\32\u0158\n\32\f\32\16\32\u015b\13\32\3\32")
        buf.write("\7\32\u015e\n\32\f\32\16\32\u0161\13\32\3\32\5\32\u0164")
        buf.write("\n\32\3\33\3\33\3\33\3\33\5\33\u016a\n\33\3\33\3\33\7")
        buf.write("\33\u016e\n\33\f\33\16\33\u0171\13\33\3\33\7\33\u0174")
        buf.write("\n\33\f\33\16\33\u0177\13\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0180\n\34\3\34\5\34\u0183\n\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0192\n\35\3\36\3\36\3\37\3\37\3 \3 \5 \u019a")
        buf.write("\n \3!\3!\3!\3!\3!\3!\7!\u01a2\n!\f!\16!\u01a5\13!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\7\"\u01ad\n\"\f\"\16\"\u01b0\13\"")
        buf.write("\3#\3#\3#\3#\3#\3#\7#\u01b8\n#\f#\16#\u01bb\13#\3$\3$")
        buf.write("\3$\3$\3$\3$\7$\u01c3\n$\f$\16$\u01c6\13$\3%\3%\3%\3%")
        buf.write("\3%\3%\7%\u01ce\n%\f%\16%\u01d1\13%\3&\3&\3&\5&\u01d6")
        buf.write("\n&\3\'\3\'\3\'\5\'\u01db\n\'\3(\3(\6(\u01df\n(\r(\16")
        buf.write("(\u01e0\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\5+\u01ee\n+\3")
        buf.write(",\3,\3,\5,\u01f3\n,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\5.\u01ff")
        buf.write("\n.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\5\60\u020a\n")
        buf.write("\60\3\61\3\61\5\61\u020e\n\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u0217\n\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\5\64\u0224\n\64\3\65\3\65")
        buf.write("\3\65\5\65\u0229\n\65\3\65\3\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\67\3\67\3\67\5\67\u0235\n\67\3\67\2\7@BDFH8\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl\2\13\3\2,/\4\2\66\669")
        buf.write("9\4\2\16\16\67\67\3\2\3\4\3\2\4\5\3\2\25\32\3\2\20\21")
        buf.write("\3\2\22\24\4\2\21\21\35\35\2\u0257\2q\3\2\2\2\4}\3\2\2")
        buf.write("\2\6\u0084\3\2\2\2\b\u0090\3\2\2\2\n\u0092\3\2\2\2\f\u0098")
        buf.write("\3\2\2\2\16\u00a3\3\2\2\2\20\u00a6\3\2\2\2\22\u00ae\3")
        buf.write("\2\2\2\24\u00b2\3\2\2\2\26\u00b5\3\2\2\2\30\u00bb\3\2")
        buf.write("\2\2\32\u00c9\3\2\2\2\34\u00d5\3\2\2\2\36\u00e0\3\2\2")
        buf.write("\2 \u00ea\3\2\2\2\"\u00f6\3\2\2\2$\u00f8\3\2\2\2&\u0113")
        buf.write("\3\2\2\2(\u0122\3\2\2\2*\u012a\3\2\2\2,\u0133\3\2\2\2")
        buf.write(".\u013c\3\2\2\2\60\u013e\3\2\2\2\62\u0153\3\2\2\2\64\u0165")
        buf.write("\3\2\2\2\66\u0182\3\2\2\28\u0189\3\2\2\2:\u0193\3\2\2")
        buf.write("\2<\u0195\3\2\2\2>\u0197\3\2\2\2@\u019b\3\2\2\2B\u01a6")
        buf.write("\3\2\2\2D\u01b1\3\2\2\2F\u01bc\3\2\2\2H\u01c7\3\2\2\2")
        buf.write("J\u01d5\3\2\2\2L\u01da\3\2\2\2N\u01dc\3\2\2\2P\u01e2\3")
        buf.write("\2\2\2R\u01e6\3\2\2\2T\u01ed\3\2\2\2V\u01ef\3\2\2\2X\u01f6")
        buf.write("\3\2\2\2Z\u01fe\3\2\2\2\\\u0200\3\2\2\2^\u0209\3\2\2\2")
        buf.write("`\u020b\3\2\2\2b\u0216\3\2\2\2d\u0218\3\2\2\2f\u0223\3")
        buf.write("\2\2\2h\u0225\3\2\2\2j\u022c\3\2\2\2l\u0234\3\2\2\2np")
        buf.write("\7\67\2\2on\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3")
        buf.write("\2\2\2sq\3\2\2\2tx\5\4\3\2uw\7\67\2\2vu\3\2\2\2wz\3\2")
        buf.write("\2\2xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zx\3\2\2\2{|\7\2\2\3")
        buf.write("|\3\3\2\2\2}~\5\6\4\2~\177\5\b\5\2\177\5\3\2\2\2\u0080")
        buf.write("\u0085\5\n\6\2\u0081\u0085\5\f\7\2\u0082\u0085\5\26\f")
        buf.write("\2\u0083\u0085\5$\23\2\u0084\u0080\3\2\2\2\u0084\u0081")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085")
        buf.write("\7\3\2\2\2\u0086\u0088\7\67\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\5")
        buf.write("\6\4\2\u008d\u008e\5\b\5\2\u008e\u0091\3\2\2\2\u008f\u0091")
        buf.write("\3\2\2\2\u0090\u0089\3\2\2\2\u0090\u008f\3\2\2\2\u0091")
        buf.write("\t\3\2\2\2\u0092\u0093\7\60\2\2\u0093\u0094\7\66\2\2\u0094")
        buf.write("\u0095\7\36\2\2\u0095\u0096\5@!\2\u0096\u0097\7\16\2\2")
        buf.write("\u0097\13\3\2\2\2\u0098\u0099\7\61\2\2\u0099\u009c\7\66")
        buf.write("\2\2\u009a\u009d\5\20\t\2\u009b\u009d\5\16\b\2\u009c\u009a")
        buf.write("\3\2\2\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u009f\3\2\2\2\u009e\u00a0\5\24\13\2\u009f\u009e\3\2\2")
        buf.write("\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write("\7\16\2\2\u00a2\r\3\2\2\2\u00a3\u00a4\t\2\2\2\u00a4\17")
        buf.write("\3\2\2\2\u00a5\u00a7\5\22\n\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00ac\3\2\2\2\u00aa\u00ad\5\16\b\2\u00ab\u00ad")
        buf.write("\7*\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("\21\3\2\2\2\u00ae\u00af\7\13\2\2\u00af\u00b0\t\3\2\2\u00b0")
        buf.write("\u00b1\7\f\2\2\u00b1\23\3\2\2\2\u00b2\u00b3\7\36\2\2\u00b3")
        buf.write("\u00b4\5@!\2\u00b4\25\3\2\2\2\u00b5\u00b6\7)\2\2\u00b6")
        buf.write("\u00b9\7\66\2\2\u00b7\u00ba\5\30\r\2\u00b8\u00ba\5\34")
        buf.write("\17\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\27")
        buf.write("\3\2\2\2\u00bb\u00bc\7*\2\2\u00bc\u00c0\7\t\2\2\u00bd")
        buf.write("\u00bf\5\32\16\2\u00be\u00bd\3\2\2\2\u00bf\u00c2\3\2\2")
        buf.write("\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3")
        buf.write("\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\7\n\2\2\u00c4")
        buf.write("\u00c5\t\4\2\2\u00c5\31\3\2\2\2\u00c6\u00c8\7\67\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c9\3")
        buf.write("\2\2\2\u00cc\u00d1\7\66\2\2\u00cd\u00d2\5\16\b\2\u00ce")
        buf.write("\u00d2\5\30\r\2\u00cf\u00d2\5\20\t\2\u00d0\u00d2\5\34")
        buf.write("\17\2\u00d1\u00cd\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("\u00d4\t\4\2\2\u00d4\33\3\2\2\2\u00d5\u00d6\7+\2\2\u00d6")
        buf.write("\u00da\7\t\2\2\u00d7\u00d9\5\36\20\2\u00d8\u00d7\3\2\2")
        buf.write("\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db")
        buf.write("\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd")
        buf.write("\u00de\7\n\2\2\u00de\u00df\t\4\2\2\u00df\35\3\2\2\2\u00e0")
        buf.write("\u00e1\7\66\2\2\u00e1\u00e3\7\7\2\2\u00e2\u00e4\5 \21")
        buf.write("\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e8\7\b\2\2\u00e6\u00e9\5\16\b\2\u00e7")
        buf.write("\u00e9\5\20\t\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2")
        buf.write("\2\u00e8\u00e9\3\2\2\2\u00e9\37\3\2\2\2\u00ea\u00ed\7")
        buf.write("\66\2\2\u00eb\u00ee\5\16\b\2\u00ec\u00ee\5\20\t\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef\u00f0\5\"\22\2\u00f0!\3\2\2")
        buf.write("\2\u00f1\u00f2\7\r\2\2\u00f2\u00f3\5 \21\2\u00f3\u00f4")
        buf.write("\5\"\22\2\u00f4\u00f7\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f1\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7#\3\2\2\2\u00f8")
        buf.write("\u00fa\7(\2\2\u00f9\u00fb\5&\24\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\5")
        buf.write("\36\20\2\u00fd\u0101\7\t\2\2\u00fe\u0100\7\67\2\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u010d\3\2\2\2\u0103\u0101\3")
        buf.write("\2\2\2\u0104\u0108\5(\25\2\u0105\u0107\7\67\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3")
        buf.write("\2\2\2\u010b\u0104\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b")
        buf.write("\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0110\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u0110\u0111\7\n\2\2\u0111\u0112\7\67\2")
        buf.write("\2\u0112%\3\2\2\2\u0113\u0114\7\7\2\2\u0114\u0115\7\66")
        buf.write("\2\2\u0115\u0116\7\66\2\2\u0116\u0117\7\b\2\2\u0117\'")
        buf.write("\3\2\2\2\u0118\u0123\5\f\7\2\u0119\u0123\5\n\6\2\u011a")
        buf.write("\u0123\5*\26\2\u011b\u0123\5\60\31\2\u011c\u0123\5\64")
        buf.write("\33\2\u011d\u0123\5:\36\2\u011e\u0123\5<\37\2\u011f\u0123")
        buf.write("\5V,\2\u0120\u0123\5\\/\2\u0121\u0123\5> \2\u0122\u0118")
        buf.write("\3\2\2\2\u0122\u0119\3\2\2\2\u0122\u011a\3\2\2\2\u0122")
        buf.write("\u011b\3\2\2\2\u0122\u011c\3\2\2\2\u0122\u011d\3\2\2\2")
        buf.write("\u0122\u011e\3\2\2\2\u0122\u011f\3\2\2\2\u0122\u0120\3")
        buf.write("\2\2\2\u0122\u0121\3\2\2\2\u0123\u0128\3\2\2\2\u0124\u0125")
        buf.write("\7\16\2\2\u0125\u0129\7\67\2\2\u0126\u0129\7\16\2\2\u0127")
        buf.write("\u0129\7\67\2\2\u0128\u0124\3\2\2\2\u0128\u0126\3\2\2")
        buf.write("\2\u0128\u0127\3\2\2\2\u0129)\3\2\2\2\u012a\u012b\5,\27")
        buf.write("\2\u012b\u012e\5.\30\2\u012c\u012f\5@!\2\u012d\u012f\5")
        buf.write("`\61\2\u012e\u012c\3\2\2\2\u012e\u012d\3\2\2\2\u012f+")
        buf.write("\3\2\2\2\u0130\u0134\7\66\2\2\u0131\u0134\5N(\2\u0132")
        buf.write("\u0134\5R*\2\u0133\u0130\3\2\2\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134-\3\2\2\2\u0135\u0136\7\17\2\2\u0136")
        buf.write("\u013d\7\36\2\2\u0137\u013d\7\37\2\2\u0138\u013d\7 \2")
        buf.write("\2\u0139\u013d\7!\2\2\u013a\u013d\7\"\2\2\u013b\u013d")
        buf.write("\7#\2\2\u013c\u0135\3\2\2\2\u013c\u0137\3\2\2\2\u013c")
        buf.write("\u0138\3\2\2\2\u013c\u0139\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013d/\3\2\2\2\u013e\u013f\7$\2\2")
        buf.write("\u013f\u0140\7\7\2\2\u0140\u0141\5@!\2\u0141\u0142\7\b")
        buf.write("\2\2\u0142\u0146\7\t\2\2\u0143\u0145\7\67\2\2\u0144\u0143")
        buf.write("\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u014c\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0149\u014b\5(\25\2\u014a\u0149\3\2\2\2\u014b\u014e\3")
        buf.write("\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f")
        buf.write("\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0151\7\n\2\2\u0150")
        buf.write("\u0152\5\62\32\2\u0151\u0150\3\2\2\2\u0151\u0152\3\2\2")
        buf.write("\2\u0152\61\3\2\2\2\u0153\u0163\7%\2\2\u0154\u0164\5\60")
        buf.write("\31\2\u0155\u0159\7\t\2\2\u0156\u0158\7\67\2\2\u0157\u0156")
        buf.write("\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u015a\3\2\2\2\u015a\u015f\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015c\u015e\5(\25\2\u015d\u015c\3\2\2\2\u015e\u0161\3")
        buf.write("\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0164\7\n\2\2\u0163")
        buf.write("\u0154\3\2\2\2\u0163\u0155\3\2\2\2\u0164\63\3\2\2\2\u0165")
        buf.write("\u0169\7&\2\2\u0166\u016a\5@!\2\u0167\u016a\5\66\34\2")
        buf.write("\u0168\u016a\58\35\2\u0169\u0166\3\2\2\2\u0169\u0167\3")
        buf.write("\2\2\2\u0169\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016f")
        buf.write("\7\t\2\2\u016c\u016e\7\67\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0175\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0174\5")
        buf.write("(\25\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177")
        buf.write("\u0175\3\2\2\2\u0178\u0179\7\n\2\2\u0179\65\3\2\2\2\u017a")
        buf.write("\u0183\5*\26\2\u017b\u017c\7\61\2\2\u017c\u017f\7\66\2")
        buf.write("\2\u017d\u0180\5\16\b\2\u017e\u0180\5\20\t\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u0183\5\24\13\2\u0182\u017a\3\2\2")
        buf.write("\2\u0182\u017b\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185")
        buf.write("\7\16\2\2\u0185\u0186\5@!\2\u0186\u0187\7\16\2\2\u0187")
        buf.write("\u0188\5*\26\2\u0188\67\3\2\2\2\u0189\u018a\t\5\2\2\u018a")
        buf.write("\u018b\7\r\2\2\u018b\u018c\t\6\2\2\u018c\u018d\7\17\2")
        buf.write("\2\u018d\u018e\7\36\2\2\u018e\u0191\7\64\2\2\u018f\u0192")
        buf.write("\7\66\2\2\u0190\u0192\5d\63\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u01929\3\2\2\2\u0193\u0194\7\63\2\2\u0194")
        buf.write(";\3\2\2\2\u0195\u0196\7\62\2\2\u0196=\3\2\2\2\u0197\u0199")
        buf.write("\7\'\2\2\u0198\u019a\5@!\2\u0199\u0198\3\2\2\2\u0199\u019a")
        buf.write("\3\2\2\2\u019a?\3\2\2\2\u019b\u019c\b!\1\2\u019c\u019d")
        buf.write("\5B\"\2\u019d\u01a3\3\2\2\2\u019e\u019f\f\4\2\2\u019f")
        buf.write("\u01a0\7\34\2\2\u01a0\u01a2\5B\"\2\u01a1\u019e\3\2\2\2")
        buf.write("\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3")
        buf.write("\2\2\2\u01a4A\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7")
        buf.write("\b\"\1\2\u01a7\u01a8\5D#\2\u01a8\u01ae\3\2\2\2\u01a9\u01aa")
        buf.write("\f\4\2\2\u01aa\u01ab\7\33\2\2\u01ab\u01ad\5D#\2\u01ac")
        buf.write("\u01a9\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01afC\3\2\2\2\u01b0\u01ae\3\2\2")
        buf.write("\2\u01b1\u01b2\b#\1\2\u01b2\u01b3\5F$\2\u01b3\u01b9\3")
        buf.write("\2\2\2\u01b4\u01b5\f\4\2\2\u01b5\u01b6\t\7\2\2\u01b6\u01b8")
        buf.write("\5F$\2\u01b7\u01b4\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01b9\u01ba\3\2\2\2\u01baE\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bc\u01bd\b$\1\2\u01bd\u01be\5H%\2\u01be\u01c4")
        buf.write("\3\2\2\2\u01bf\u01c0\f\4\2\2\u01c0\u01c1\t\b\2\2\u01c1")
        buf.write("\u01c3\5H%\2\u01c2\u01bf\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5G\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c7\u01c8\b%\1\2\u01c8\u01c9\5J&\2\u01c9")
        buf.write("\u01cf\3\2\2\2\u01ca\u01cb\f\4\2\2\u01cb\u01cc\t\t\2\2")
        buf.write("\u01cc\u01ce\5J&\2\u01cd\u01ca\3\2\2\2\u01ce\u01d1\3\2")
        buf.write("\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0I\3")
        buf.write("\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\t\n\2\2\u01d3\u01d6")
        buf.write("\5L\'\2\u01d4\u01d6\5L\'\2\u01d5\u01d2\3\2\2\2\u01d5\u01d4")
        buf.write("\3\2\2\2\u01d6K\3\2\2\2\u01d7\u01db\5N(\2\u01d8\u01db")
        buf.write("\5R*\2\u01d9\u01db\5T+\2\u01da\u01d7\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01da\u01d9\3\2\2\2\u01dbM\3\2\2\2\u01dc\u01de")
        buf.write("\7\66\2\2\u01dd\u01df\5P)\2\u01de\u01dd\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1O\3\2\2\2\u01e2\u01e3\7\13\2\2\u01e3\u01e4\5@!\2")
        buf.write("\u01e4\u01e5\7\f\2\2\u01e5Q\3\2\2\2\u01e6\u01e7\7\66\2")
        buf.write("\2\u01e7\u01e8\7\6\2\2\u01e8\u01e9\7\66\2\2\u01e9S\3\2")
        buf.write("\2\2\u01ea\u01ee\5V,\2\u01eb\u01ee\5\\/\2\u01ec\u01ee")
        buf.write("\5^\60\2\u01ed\u01ea\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01eeU\3\2\2\2\u01ef\u01f0\7\66\2\2\u01f0")
        buf.write("\u01f2\7\7\2\2\u01f1\u01f3\5X-\2\u01f2\u01f1\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5\7\b\2\2")
        buf.write("\u01f5W\3\2\2\2\u01f6\u01f7\5@!\2\u01f7\u01f8\5Z.\2\u01f8")
        buf.write("Y\3\2\2\2\u01f9\u01fa\7\r\2\2\u01fa\u01fb\5@!\2\u01fb")
        buf.write("\u01fc\5Z.\2\u01fc\u01ff\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe")
        buf.write("\u01f9\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ff[\3\2\2\2\u0200")
        buf.write("\u0201\7\66\2\2\u0201\u0202\7\6\2\2\u0202\u0203\5V,\2")
        buf.write("\u0203]\3\2\2\2\u0204\u0205\7\7\2\2\u0205\u0206\5@!\2")
        buf.write("\u0206\u0207\7\b\2\2\u0207\u020a\3\2\2\2\u0208\u020a\5")
        buf.write("b\62\2\u0209\u0204\3\2\2\2\u0209\u0208\3\2\2\2\u020a_")
        buf.write("\3\2\2\2\u020b\u020d\5\20\t\2\u020c\u020e\5d\63\2\u020d")
        buf.write("\u020c\3\2\2\2\u020d\u020e\3\2\2\2\u020ea\3\2\2\2\u020f")
        buf.write("\u0217\79\2\2\u0210\u0217\7:\2\2\u0211\u0217\7>\2\2\u0212")
        buf.write("\u0217\7A\2\2\u0213\u0217\5d\63\2\u0214\u0217\5h\65\2")
        buf.write("\u0215\u0217\7\66\2\2\u0216\u020f\3\2\2\2\u0216\u0210")
        buf.write("\3\2\2\2\u0216\u0211\3\2\2\2\u0216\u0212\3\2\2\2\u0216")
        buf.write("\u0213\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2")
        buf.write("\u0217c\3\2\2\2\u0218\u0219\7\t\2\2\u0219\u021a\5b\62")
        buf.write("\2\u021a\u021b\5f\64\2\u021b\u021c\7\n\2\2\u021c\u021d")
        buf.write("\5f\64\2\u021de\3\2\2\2\u021e\u021f\7\r\2\2\u021f\u0220")
        buf.write("\5b\62\2\u0220\u0221\5f\64\2\u0221\u0224\3\2\2\2\u0222")
        buf.write("\u0224\3\2\2\2\u0223\u021e\3\2\2\2\u0223\u0222\3\2\2\2")
        buf.write("\u0224g\3\2\2\2\u0225\u0226\7\66\2\2\u0226\u0228\7\t\2")
        buf.write("\2\u0227\u0229\5j\66\2\u0228\u0227\3\2\2\2\u0228\u0229")
        buf.write("\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b\7\n\2\2\u022b")
        buf.write("i\3\2\2\2\u022c\u022d\7\66\2\2\u022d\u022e\7\17\2\2\u022e")
        buf.write("\u022f\5@!\2\u022f\u0230\5l\67\2\u0230k\3\2\2\2\u0231")
        buf.write("\u0232\7\r\2\2\u0232\u0235\5j\66\2\u0233\u0235\3\2\2\2")
        buf.write("\u0234\u0231\3\2\2\2\u0234\u0233\3\2\2\2\u0235m\3\2\2")
        buf.write("\2;qx\u0084\u0089\u0090\u009c\u009f\u00a8\u00ac\u00b9")
        buf.write("\u00c0\u00c9\u00d1\u00da\u00e3\u00e8\u00ed\u00f6\u00fa")
        buf.write("\u0101\u0108\u010d\u0122\u0128\u012e\u0133\u013c\u0146")
        buf.write("\u014c\u0151\u0159\u015f\u0163\u0169\u016f\u0175\u017f")
        buf.write("\u0182\u0191\u0199\u01a3\u01ae\u01b9\u01c4\u01cf\u01d5")
        buf.write("\u01da\u01e0\u01ed\u01f2\u01fe\u0209\u020d\u0216\u0223")
        buf.write("\u0228\u0234")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'index'", "'_'", "'value'", "'.'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
                     "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'if'", 
                     "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LB", "RB", "LC", "RC", "LP", "RP", "COMMA", 
                      "SEMICOLON", "COLON", "ADD", "SUBTR", "MUL", "DIV", 
                      "MOD", "EQ", "UNEQ", "LESS", "LESSEQ", "GREATER", 
                      "GREATEREQ", "AND", "OR", "NOT", "ASSIGN", "ADDASS", 
                      "SUBASS", "MULASS", "DIVASS", "MODASS", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
                      "CONTINUE", "BREAK", "RANGE", "NIL", "ID", "NL", "HEXADECIMAL", 
                      "INTLIT", "FLOATLIT", "DECIMAL", "BINARY", "OCTAL", 
                      "BOOLLIT", "TRUE", "FALSE", "STRINGLIT", "COMMENT", 
                      "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_declare = 2
    RULE_declareTail = 3
    RULE_constDeclare = 4
    RULE_varDeclare = 5
    RULE_varType = 6
    RULE_arrayType = 7
    RULE_dimensions = 8
    RULE_init = 9
    RULE_typeDeclare = 10
    RULE_structDeclare = 11
    RULE_field = 12
    RULE_interfaceDeclare = 13
    RULE_method = 14
    RULE_parameters = 15
    RULE_paraTail = 16
    RULE_funcDeclare = 17
    RULE_methodDeclare = 18
    RULE_stmt = 19
    RULE_assignment = 20
    RULE_lhs = 21
    RULE_assignOp = 22
    RULE_ifstmt = 23
    RULE_elsestmt = 24
    RULE_forstmt = 25
    RULE_initFor = 26
    RULE_rangeFor = 27
    RULE_breakstmt = 28
    RULE_contstmt = 29
    RULE_returnstmt = 30
    RULE_expr = 31
    RULE_expr1 = 32
    RULE_expr2 = 33
    RULE_expr3 = 34
    RULE_expr4 = 35
    RULE_expr5 = 36
    RULE_expr6 = 37
    RULE_arrayElement = 38
    RULE_index = 39
    RULE_structField = 40
    RULE_expr7 = 41
    RULE_funcCall = 42
    RULE_arguments = 43
    RULE_argTail = 44
    RULE_methodCall = 45
    RULE_expr8 = 46
    RULE_arrayInit = 47
    RULE_literal = 48
    RULE_arrayLit = 49
    RULE_literalTail = 50
    RULE_structLit = 51
    RULE_structElement = 52
    RULE_elementTail = 53

    ruleNames =  [ "program", "declarations", "declare", "declareTail", 
                   "constDeclare", "varDeclare", "varType", "arrayType", 
                   "dimensions", "init", "typeDeclare", "structDeclare", 
                   "field", "interfaceDeclare", "method", "parameters", 
                   "paraTail", "funcDeclare", "methodDeclare", "stmt", "assignment", 
                   "lhs", "assignOp", "ifstmt", "elsestmt", "forstmt", "initFor", 
                   "rangeFor", "breakstmt", "contstmt", "returnstmt", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "arrayElement", "index", "structField", "expr7", "funcCall", 
                   "arguments", "argTail", "methodCall", "expr8", "arrayInit", 
                   "literal", "arrayLit", "literalTail", "structLit", "structElement", 
                   "elementTail" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    LB=5
    RB=6
    LC=7
    RC=8
    LP=9
    RP=10
    COMMA=11
    SEMICOLON=12
    COLON=13
    ADD=14
    SUBTR=15
    MUL=16
    DIV=17
    MOD=18
    EQ=19
    UNEQ=20
    LESS=21
    LESSEQ=22
    GREATER=23
    GREATEREQ=24
    AND=25
    OR=26
    NOT=27
    ASSIGN=28
    ADDASS=29
    SUBASS=30
    MULASS=31
    DIVASS=32
    MODASS=33
    IF=34
    ELSE=35
    FOR=36
    RETURN=37
    FUNC=38
    TYPE=39
    STRUCT=40
    INTERFACE=41
    STRING=42
    INT=43
    FLOAT=44
    BOOLEAN=45
    CONST=46
    VAR=47
    CONTINUE=48
    BREAK=49
    RANGE=50
    NIL=51
    ID=52
    NL=53
    HEXADECIMAL=54
    INTLIT=55
    FLOATLIT=56
    DECIMAL=57
    BINARY=58
    OCTAL=59
    BOOLLIT=60
    TRUE=61
    FALSE=62
    STRINGLIT=63
    COMMENT=64
    WS=65
    ERROR_CHAR=66
    ILLEGAL_ESCAPE=67
    UNCLOSE_STRING=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarations(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationsContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 108
                self.match(MiniGoParser.NL)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.declarations()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 115
                self.match(MiniGoParser.NL)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(MiniGoParser.DeclareContext,0)


        def declareTail(self):
            return self.getTypedRuleContext(MiniGoParser.DeclareTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = MiniGoParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.declare()
            self.state = 124
            self.declareTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclareContext,0)


        def varDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclareContext,0)


        def typeDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclareContext,0)


        def funcDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclareContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = MiniGoParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.constDeclare()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.varDeclare()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.typeDeclare()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.funcDeclare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(MiniGoParser.DeclareContext,0)


        def declareTail(self):
            return self.getTypedRuleContext(MiniGoParser.DeclareTailContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_declareTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareTail" ):
                return visitor.visitDeclareTail(self)
            else:
                return visitor.visitChildren(self)




    def declareTail(self):

        localctx = MiniGoParser.DeclareTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declareTail)
        self._la = 0 # Token type
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 132
                    self.match(MiniGoParser.NL)
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 138
                self.declare()
                self.state = 139
                self.declareTail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDeclare" ):
                return visitor.visitConstDeclare(self)
            else:
                return visitor.visitChildren(self)




    def constDeclare(self):

        localctx = MiniGoParser.ConstDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(MiniGoParser.CONST)
            self.state = 145
            self.match(MiniGoParser.ID)
            self.state = 146
            self.match(MiniGoParser.ASSIGN)
            self.state = 147
            self.expr(0)
            self.state = 148
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclare" ):
                return visitor.visitVarDeclare(self)
            else:
                return visitor.visitChildren(self)




    def varDeclare(self):

        localctx = MiniGoParser.VarDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MiniGoParser.VAR)
            self.state = 151
            self.match(MiniGoParser.ID)
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.state = 152
                self.arrayType()
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 153
                self.varType()
                pass
            elif token in [MiniGoParser.SEMICOLON, MiniGoParser.ASSIGN]:
                pass
            else:
                pass
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 156
                self.init()


            self.state = 159
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_varType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarType" ):
                return visitor.visitVarType(self)
            else:
                return visitor.visitChildren(self)




    def varType(self):

        localctx = MiniGoParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def dimensions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DimensionsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DimensionsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 163
                self.dimensions()
                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LP):
                    break

            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 168
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 169
                self.match(MiniGoParser.STRUCT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MiniGoParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MiniGoParser.LP)
            self.state = 173
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTLIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 174
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MiniGoParser.ASSIGN)
            self.state = 177
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def structDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclareContext,0)


        def interfaceDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclareContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDeclare" ):
                return visitor.visitTypeDeclare(self)
            else:
                return visitor.visitChildren(self)




    def typeDeclare(self):

        localctx = MiniGoParser.TypeDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MiniGoParser.TYPE)
            self.state = 180
            self.match(MiniGoParser.ID)
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 181
                self.structDeclare()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 182
                self.interfaceDeclare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDeclare" ):
                return visitor.visitStructDeclare(self)
            else:
                return visitor.visitChildren(self)




    def structDeclare(self):

        localctx = MiniGoParser.StructDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(MiniGoParser.STRUCT)
            self.state = 186
            self.match(MiniGoParser.LC)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID or _la==MiniGoParser.NL:
                self.state = 187
                self.field()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self.match(MiniGoParser.RC)
            self.state = 194
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def structDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclareContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def interfaceDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclareContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 196
                self.match(MiniGoParser.NL)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(MiniGoParser.ID)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 203
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 204
                self.structDeclare()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 205
                self.arrayType()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 206
                self.interfaceDeclare()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 209
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MethodContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MethodContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclare" ):
                return visitor.visitInterfaceDeclare(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclare(self):

        localctx = MiniGoParser.InterfaceDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_interfaceDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(MiniGoParser.INTERFACE)
            self.state = 212
            self.match(MiniGoParser.LC)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 213
                self.method()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.match(MiniGoParser.RC)
            self.state = 220
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def parameters(self):
            return self.getTypedRuleContext(MiniGoParser.ParametersContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.ID)
            self.state = 223
            self.match(MiniGoParser.LB)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 224
                self.parameters()


            self.state = 227
            self.match(MiniGoParser.RB)
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 228
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 229
                self.arrayType()
                pass
            elif token in [MiniGoParser.LC, MiniGoParser.RC, MiniGoParser.ID]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def paraTail(self):
            return self.getTypedRuleContext(MiniGoParser.ParaTailContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = MiniGoParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MiniGoParser.ID)
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 233
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 234
                self.arrayType()
                pass
            elif token in [MiniGoParser.RB, MiniGoParser.COMMA]:
                pass
            else:
                pass
            self.state = 237
            self.paraTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameters(self):
            return self.getTypedRuleContext(MiniGoParser.ParametersContext,0)


        def paraTail(self):
            return self.getTypedRuleContext(MiniGoParser.ParaTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paraTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaTail" ):
                return visitor.visitParaTail(self)
            else:
                return visitor.visitChildren(self)




    def paraTail(self):

        localctx = MiniGoParser.ParaTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paraTail)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(MiniGoParser.COMMA)
                self.state = 240
                self.parameters()
                self.state = 241
                self.paraTail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def methodDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclareContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclare" ):
                return visitor.visitFuncDeclare(self)
            else:
                return visitor.visitChildren(self)




    def funcDeclare(self):

        localctx = MiniGoParser.FuncDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(MiniGoParser.FUNC)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LB:
                self.state = 247
                self.methodDeclare()


            self.state = 250
            self.method()
            self.state = 251
            self.match(MiniGoParser.LC)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 252
                self.match(MiniGoParser.NL)
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 258
                self.stmt()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 259
                    self.match(MiniGoParser.NL)
                    self.state = 264
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
            self.match(MiniGoParser.RC)
            self.state = 271
            self.match(MiniGoParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclare" ):
                return visitor.visitMethodDeclare(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclare(self):

        localctx = MiniGoParser.MethodDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_methodDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MiniGoParser.LB)
            self.state = 274
            self.match(MiniGoParser.ID)
            self.state = 275
            self.match(MiniGoParser.ID)
            self.state = 276
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclareContext,0)


        def constDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclareContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContstmtContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 278
                self.varDeclare()
                pass

            elif la_ == 2:
                self.state = 279
                self.constDeclare()
                pass

            elif la_ == 3:
                self.state = 280
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 281
                self.ifstmt()
                pass

            elif la_ == 5:
                self.state = 282
                self.forstmt()
                pass

            elif la_ == 6:
                self.state = 283
                self.breakstmt()
                pass

            elif la_ == 7:
                self.state = 284
                self.contstmt()
                pass

            elif la_ == 8:
                self.state = 285
                self.funcCall()
                pass

            elif la_ == 9:
                self.state = 286
                self.methodCall()
                pass

            elif la_ == 10:
                self.state = 287
                self.returnstmt()
                pass


            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 290
                self.match(MiniGoParser.SEMICOLON)
                self.state = 291
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 2:
                self.state = 292
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.state = 293
                self.match(MiniGoParser.NL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assignOp(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.lhs()
            self.state = 297
            self.assignOp()
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LB, MiniGoParser.LC, MiniGoParser.SUBTR, MiniGoParser.NOT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.BOOLLIT, MiniGoParser.STRINGLIT]:
                self.state = 298
                self.expr(0)
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 299
                self.arrayInit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def structField(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_lhs)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.arrayElement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.structField()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ADDASS(self):
            return self.getToken(MiniGoParser.ADDASS, 0)

        def SUBASS(self):
            return self.getToken(MiniGoParser.SUBASS, 0)

        def MULASS(self):
            return self.getToken(MiniGoParser.MULASS, 0)

        def DIVASS(self):
            return self.getToken(MiniGoParser.DIVASS, 0)

        def MODASS(self):
            return self.getToken(MiniGoParser.MODASS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignOp" ):
                return visitor.visitAssignOp(self)
            else:
                return visitor.visitChildren(self)




    def assignOp(self):

        localctx = MiniGoParser.AssignOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignOp)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(MiniGoParser.COLON)
                self.state = 308
                self.match(MiniGoParser.ASSIGN)
                pass
            elif token in [MiniGoParser.ADDASS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(MiniGoParser.ADDASS)
                pass
            elif token in [MiniGoParser.SUBASS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.match(MiniGoParser.SUBASS)
                pass
            elif token in [MiniGoParser.MULASS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 311
                self.match(MiniGoParser.MULASS)
                pass
            elif token in [MiniGoParser.DIVASS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 312
                self.match(MiniGoParser.DIVASS)
                pass
            elif token in [MiniGoParser.MODASS]:
                self.enterOuterAlt(localctx, 6)
                self.state = 313
                self.match(MiniGoParser.MODASS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def elsestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ElsestmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(MiniGoParser.IF)
            self.state = 317
            self.match(MiniGoParser.LB)
            self.state = 318
            self.expr(0)
            self.state = 319
            self.match(MiniGoParser.RB)
            self.state = 320
            self.match(MiniGoParser.LC)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 321
                self.match(MiniGoParser.NL)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 327
                self.stmt()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 333
            self.match(MiniGoParser.RC)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 334
                self.elsestmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = MiniGoParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elsestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MiniGoParser.ELSE)
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF]:
                self.state = 338
                self.ifstmt()
                pass
            elif token in [MiniGoParser.LC]:
                self.state = 339
                self.match(MiniGoParser.LC)
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 340
                    self.match(MiniGoParser.NL)
                    self.state = 345
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 346
                    self.stmt()
                    self.state = 351
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 352
                self.match(MiniGoParser.RC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def initFor(self):
            return self.getTypedRuleContext(MiniGoParser.InitForContext,0)


        def rangeFor(self):
            return self.getTypedRuleContext(MiniGoParser.RangeForContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(MiniGoParser.FOR)
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 356
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 357
                self.initFor()
                pass

            elif la_ == 3:
                self.state = 358
                self.rangeFor()
                pass


            self.state = 361
            self.match(MiniGoParser.LC)
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 362
                self.match(MiniGoParser.NL)
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 368
                self.stmt()
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
            self.match(MiniGoParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignmentContext,i)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initFor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitFor" ):
                return visitor.visitInitFor(self)
            else:
                return visitor.visitChildren(self)




    def initFor(self):

        localctx = MiniGoParser.InitForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_initFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 376
                self.assignment()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 377
                self.match(MiniGoParser.VAR)
                self.state = 378
                self.match(MiniGoParser.ID)
                self.state = 381
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 379
                    self.varType()
                    pass
                elif token in [MiniGoParser.LP]:
                    self.state = 380
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.ASSIGN]:
                    pass
                else:
                    pass
                self.state = 383
                self.init()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 386
            self.match(MiniGoParser.SEMICOLON)
            self.state = 387
            self.expr(0)
            self.state = 388
            self.match(MiniGoParser.SEMICOLON)
            self.state = 389
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rangeFor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeFor" ):
                return visitor.visitRangeFor(self)
            else:
                return visitor.visitChildren(self)




    def rangeFor(self):

        localctx = MiniGoParser.RangeForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_rangeFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 392
            self.match(MiniGoParser.COMMA)
            self.state = 393
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__1 or _la==MiniGoParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 394
            self.match(MiniGoParser.COLON)
            self.state = 395
            self.match(MiniGoParser.ASSIGN)
            self.state = 396
            self.match(MiniGoParser.RANGE)
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 397
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LC]:
                self.state = 398
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MiniGoParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_contstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContstmt" ):
                return visitor.visitContstmt(self)
            else:
                return visitor.visitChildren(self)




    def contstmt(self):

        localctx = MiniGoParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MiniGoParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(MiniGoParser.RETURN)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LC) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 406
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 412
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 413
                    self.match(MiniGoParser.OR)
                    self.state = 414
                    self.expr1(0) 
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 428
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 423
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 424
                    self.match(MiniGoParser.AND)
                    self.state = 425
                    self.expr2(0) 
                self.state = 430
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def UNEQ(self):
            return self.getToken(MiniGoParser.UNEQ, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESSEQ(self):
            return self.getToken(MiniGoParser.LESSEQ, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATEREQ(self):
            return self.getToken(MiniGoParser.GREATEREQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 434
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 435
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.UNEQ) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESSEQ) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATEREQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 436
                    self.expr3(0) 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUBTR(self):
            return self.getToken(MiniGoParser.SUBTR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 445
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 446
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUBTR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 447
                    self.expr4(0) 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 461
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 456
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 457
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 458
                    self.expr5() 
                self.state = 463
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUBTR(self):
            return self.getToken(MiniGoParser.SUBTR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUBTR, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 465
                self.expr6()
                pass
            elif token in [MiniGoParser.LB, MiniGoParser.LC, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.BOOLLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def structField(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldContext,0)


        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr6)
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.arrayElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.structField()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.expr7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElement" ):
                return visitor.visitArrayElement(self)
            else:
                return visitor.visitChildren(self)




    def arrayElement(self):

        localctx = MiniGoParser.ArrayElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniGoParser.ID)
            self.state = 476 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 475
                    self.index()

                else:
                    raise NoViableAltException(self)
                self.state = 478 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(MiniGoParser.LP)
            self.state = 481
            self.expr(0)
            self.state = 482
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructField" ):
                return visitor.visitStructField(self)
            else:
                return visitor.visitChildren(self)




    def structField(self):

        localctx = MiniGoParser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(MiniGoParser.ID)
            self.state = 485
            self.match(MiniGoParser.T__3)
            self.state = 486
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallContext,0)


        def expr8(self):
            return self.getTypedRuleContext(MiniGoParser.Expr8Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr7)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.methodCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 490
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = MiniGoParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(MiniGoParser.ID)
            self.state = 494
            self.match(MiniGoParser.LB)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LC) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 495
                self.arguments()


            self.state = 498
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def argTail(self):
            return self.getTypedRuleContext(MiniGoParser.ArgTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = MiniGoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.expr(0)
            self.state = 501
            self.argTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def argTail(self):
            return self.getTypedRuleContext(MiniGoParser.ArgTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgTail" ):
                return visitor.visitArgTail(self)
            else:
                return visitor.visitChildren(self)




    def argTail(self):

        localctx = MiniGoParser.ArgTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_argTail)
        try:
            self.state = 508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.match(MiniGoParser.COMMA)
                self.state = 504
                self.expr(0)
                self.state = 505
                self.argTail()
                pass
            elif token in [MiniGoParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = MiniGoParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(MiniGoParser.ID)
            self.state = 511
            self.match(MiniGoParser.T__3)
            self.state = 512
            self.funcCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = MiniGoParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr8)
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(MiniGoParser.LB)
                self.state = 515
                self.expr(0)
                self.state = 516
                self.match(MiniGoParser.RB)
                pass
            elif token in [MiniGoParser.LC, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.BOOLLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInit" ):
                return visitor.visitArrayInit(self)
            else:
                return visitor.visitChildren(self)




    def arrayInit(self):

        localctx = MiniGoParser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arrayInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.arrayType()
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 522
                self.arrayLit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literal)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 527
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 528
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 529
                self.arrayLit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 530
                self.structLit()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 531
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def literalTail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LiteralTailContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LiteralTailContext,i)


        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(MiniGoParser.LC)
            self.state = 535
            self.literal()
            self.state = 536
            self.literalTail()
            self.state = 537
            self.match(MiniGoParser.RC)
            self.state = 538
            self.literalTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def literalTail(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literalTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralTail" ):
                return visitor.visitLiteralTail(self)
            else:
                return visitor.visitChildren(self)




    def literalTail(self):

        localctx = MiniGoParser.LiteralTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literalTail)
        try:
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.match(MiniGoParser.COMMA)
                self.state = 541
                self.literal()
                self.state = 542
                self.literalTail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def structElement(self):
            return self.getTypedRuleContext(MiniGoParser.StructElementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLit" ):
                return visitor.visitStructLit(self)
            else:
                return visitor.visitChildren(self)




    def structLit(self):

        localctx = MiniGoParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_structLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(MiniGoParser.ID)
            self.state = 548
            self.match(MiniGoParser.LC)
            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 549
                self.structElement()


            self.state = 552
            self.match(MiniGoParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def elementTail(self):
            return self.getTypedRuleContext(MiniGoParser.ElementTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructElement" ):
                return visitor.visitStructElement(self)
            else:
                return visitor.visitChildren(self)




    def structElement(self):

        localctx = MiniGoParser.StructElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_structElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(MiniGoParser.ID)
            self.state = 555
            self.match(MiniGoParser.COLON)
            self.state = 556
            self.expr(0)
            self.state = 557
            self.elementTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structElement(self):
            return self.getTypedRuleContext(MiniGoParser.StructElementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elementTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementTail" ):
                return visitor.visitElementTail(self)
            else:
                return visitor.visitChildren(self)




    def elementTail(self):

        localctx = MiniGoParser.ElementTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_elementTail)
        try:
            self.state = 562
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.match(MiniGoParser.COMMA)
                self.state = 560
                self.structElement()
                pass
            elif token in [MiniGoParser.RC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expr_sempred
        self._predicates[32] = self.expr1_sempred
        self._predicates[33] = self.expr2_sempred
        self._predicates[34] = self.expr3_sempred
        self._predicates[35] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




