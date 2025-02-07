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
        buf.write("\u02b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\7\2t\n")
        buf.write("\2\f\2\16\2w\13\2\3\2\3\2\7\2{\n\2\f\2\16\2~\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u0089\n\4\3\5\7\5")
        buf.write("\u008c\n\5\f\5\16\5\u008f\13\5\3\5\3\5\7\5\u0093\n\5\f")
        buf.write("\5\16\5\u0096\13\5\3\5\3\5\3\5\5\5\u009b\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u00a8\n\7\3\7\5")
        buf.write("\7\u00ab\n\7\3\7\3\7\3\7\5\7\u00b0\n\7\3\b\3\b\3\t\6\t")
        buf.write("\u00b5\n\t\r\t\16\t\u00b6\3\t\3\t\3\t\5\t\u00bc\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13\u00c5\n\13\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00cb\n\f\3\r\3\r\3\r\7\r\u00d0\n\r\f\r\16")
        buf.write("\r\u00d3\13\r\3\r\7\r\u00d6\n\r\f\r\16\r\u00d9\13\r\3")
        buf.write("\r\3\r\3\r\3\16\7\16\u00df\n\16\f\16\16\16\u00e2\13\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ea\n\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u00f0\n\16\3\17\3\17\3\17\7\17\u00f5")
        buf.write("\n\17\f\17\16\17\u00f8\13\17\3\17\7\17\u00fb\n\17\f\17")
        buf.write("\16\17\u00fe\13\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20")
        buf.write("\u0106\n\20\3\20\3\20\3\20\3\20\5\20\u010c\n\20\3\20\3")
        buf.write("\20\3\20\3\20\7\20\u0112\n\20\f\20\16\20\u0115\13\20\3")
        buf.write("\21\3\21\3\21\5\21\u011a\n\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u0123\n\22\3\23\3\23\5\23\u0127\n\23\3")
        buf.write("\23\3\23\3\23\5\23\u012c\n\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u0132\n\23\3\23\3\23\3\23\3\23\7\23\u0138\n\23\f\23\16")
        buf.write("\23\u013b\13\23\3\23\3\23\7\23\u013f\n\23\f\23\16\23\u0142")
        buf.write("\13\23\3\23\3\23\5\23\u0146\n\23\7\23\u0148\n\23\f\23")
        buf.write("\16\23\u014b\13\23\3\23\3\23\5\23\u014f\n\23\3\24\3\24")
        buf.write("\3\24\5\24\u0154\n\24\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u015d\n\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u016e\n")
        buf.write("\27\3\27\3\27\3\27\3\27\5\27\u0174\n\27\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u017a\n\30\3\31\3\31\3\31\5\31\u017f\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0188\n\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\7\33\u018f\n\33\f\33\16\33\u0192")
        buf.write("\13\33\3\33\3\33\7\33\u0196\n\33\f\33\16\33\u0199\13\33")
        buf.write("\3\33\7\33\u019c\n\33\f\33\16\33\u019f\13\33\3\33\3\33")
        buf.write("\5\33\u01a3\n\33\3\33\5\33\u01a6\n\33\3\34\3\34\3\34\7")
        buf.write("\34\u01ab\n\34\f\34\16\34\u01ae\13\34\3\34\3\34\7\34\u01b2")
        buf.write("\n\34\f\34\16\34\u01b5\13\34\3\34\7\34\u01b8\n\34\f\34")
        buf.write("\16\34\u01bb\13\34\3\34\3\34\7\34\u01bf\n\34\f\34\16\34")
        buf.write("\u01c2\13\34\5\34\u01c4\n\34\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u01ca\n\35\3\35\3\35\7\35\u01ce\n\35\f\35\16\35\u01d1")
        buf.write("\13\35\3\35\7\35\u01d4\n\35\f\35\16\35\u01d7\13\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u01e0\n\36\3\36\5")
        buf.write("\36\u01e3\n\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u01f3\n\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\5\"\u01fb\n\"\3#\3#\3#\3#\3#\3#\7#\u0203")
        buf.write("\n#\f#\16#\u0206\13#\3$\3$\3$\3$\3$\3$\7$\u020e\n$\f$")
        buf.write("\16$\u0211\13$\3%\3%\3%\3%\3%\3%\7%\u0219\n%\f%\16%\u021c")
        buf.write("\13%\3&\3&\3&\3&\3&\3&\7&\u0224\n&\f&\16&\u0227\13&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\7\'\u022f\n\'\f\'\16\'\u0232\13")
        buf.write("\'\3(\7(\u0235\n(\f(\16(\u0238\13(\3(\3(\5(\u023c\n(\3")
        buf.write(")\3)\3)\5)\u0241\n)\3*\3*\5*\u0245\n*\3*\6*\u0248\n*\r")
        buf.write("*\16*\u0249\3+\3+\3+\3+\3,\3,\5,\u0252\n,\3,\3,\3,\3,")
        buf.write("\5,\u0258\n,\3-\3-\3-\5-\u025d\n-\3.\3.\3.\5.\u0262\n")
        buf.write(".\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\5\60\u026e\n")
        buf.write("\60\3\61\5\61\u0271\n\61\3\61\3\61\3\61\3\61\5\61\u0277")
        buf.write("\n\61\3\61\5\61\u027a\n\61\3\61\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\5\62\u0284\n\62\3\63\3\63\5\63\u0288\n\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\5\64\u0296\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\5\66\u02a3\n\66\3\67\3\67\3\67")
        buf.write("\5\67\u02a8\n\67\3\67\3\67\38\38\38\38\38\39\39\39\59")
        buf.write("\u02b4\n9\39\4\u0113\u0139\7DFHJL:\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnp\2\13\3\2.\61\4\288<<\4\2\b\b\20\20\3")
        buf.write("\2\3\4\3\2\4\5\3\2\27\34\3\2\22\23\3\2\24\26\4\2\23\23")
        buf.write("\37\37\2\u0300\2u\3\2\2\2\4\u0081\3\2\2\2\6\u0088\3\2")
        buf.write("\2\2\b\u009a\3\2\2\2\n\u009c\3\2\2\2\f\u00a2\3\2\2\2\16")
        buf.write("\u00b1\3\2\2\2\20\u00b4\3\2\2\2\22\u00bd\3\2\2\2\24\u00c1")
        buf.write("\3\2\2\2\26\u00c6\3\2\2\2\30\u00cc\3\2\2\2\32\u00e0\3")
        buf.write("\2\2\2\34\u00f1\3\2\2\2\36\u0102\3\2\2\2 \u0116\3\2\2")
        buf.write("\2\"\u0122\3\2\2\2$\u0124\3\2\2\2&\u0150\3\2\2\2(\u015c")
        buf.write("\3\2\2\2*\u015e\3\2\2\2,\u016d\3\2\2\2.\u0175\3\2\2\2")
        buf.write("\60\u017e\3\2\2\2\62\u0187\3\2\2\2\64\u0189\3\2\2\2\66")
        buf.write("\u01a7\3\2\2\28\u01c5\3\2\2\2:\u01e2\3\2\2\2<\u01e9\3")
        buf.write("\2\2\2>\u01f4\3\2\2\2@\u01f6\3\2\2\2B\u01f8\3\2\2\2D\u01fc")
        buf.write("\3\2\2\2F\u0207\3\2\2\2H\u0212\3\2\2\2J\u021d\3\2\2\2")
        buf.write("L\u0228\3\2\2\2N\u023b\3\2\2\2P\u0240\3\2\2\2R\u0244\3")
        buf.write("\2\2\2T\u024b\3\2\2\2V\u0251\3\2\2\2X\u025c\3\2\2\2Z\u025e")
        buf.write("\3\2\2\2\\\u0265\3\2\2\2^\u026d\3\2\2\2`\u0270\3\2\2\2")
        buf.write("b\u0283\3\2\2\2d\u0285\3\2\2\2f\u0295\3\2\2\2h\u0297\3")
        buf.write("\2\2\2j\u02a2\3\2\2\2l\u02a4\3\2\2\2n\u02ab\3\2\2\2p\u02b3")
        buf.write("\3\2\2\2rt\7\b\2\2sr\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2")
        buf.write("\2\2vx\3\2\2\2wu\3\2\2\2x|\5\4\3\2y{\7\b\2\2zy\3\2\2\2")
        buf.write("{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|\3\2\2\2")
        buf.write("\177\u0080\7\2\2\3\u0080\3\3\2\2\2\u0081\u0082\5\6\4\2")
        buf.write("\u0082\u0083\5\b\5\2\u0083\5\3\2\2\2\u0084\u0089\5\n\6")
        buf.write("\2\u0085\u0089\5\f\7\2\u0086\u0089\5\26\f\2\u0087\u0089")
        buf.write("\5$\23\2\u0088\u0084\3\2\2\2\u0088\u0085\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089\7\3\2\2\2\u008a")
        buf.write("\u008c\7\b\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0090\3")
        buf.write("\2\2\2\u008f\u008d\3\2\2\2\u0090\u0094\5\6\4\2\u0091\u0093")
        buf.write("\7\b\2\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2")
        buf.write("\u0096\u0094\3\2\2\2\u0097\u0098\5\b\5\2\u0098\u009b\3")
        buf.write("\2\2\2\u0099\u009b\3\2\2\2\u009a\u008d\3\2\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\t\3\2\2\2\u009c\u009d\7\62\2\2\u009d\u009e")
        buf.write("\78\2\2\u009e\u009f\7 \2\2\u009f\u00a0\5D#\2\u00a0\u00a1")
        buf.write("\7\20\2\2\u00a1\13\3\2\2\2\u00a2\u00a3\7\63\2\2\u00a3")
        buf.write("\u00a7\78\2\2\u00a4\u00a8\5\20\t\2\u00a5\u00a8\5\16\b")
        buf.write("\2\u00a6\u00a8\78\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00ab\5\24\13\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00ab\u00af\3\2\2\2\u00ac\u00b0")
        buf.write("\7\20\2\2\u00ad\u00ae\7\20\2\2\u00ae\u00b0\7\b\2\2\u00af")
        buf.write("\u00ac\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\r\3\2\2\2\u00b1")
        buf.write("\u00b2\t\2\2\2\u00b2\17\3\2\2\2\u00b3\u00b5\5\22\n\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00bb\3\2\2\2\u00b8\u00bc\5")
        buf.write("\16\b\2\u00b9\u00bc\7,\2\2\u00ba\u00bc\78\2\2\u00bb\u00b8")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc")
        buf.write("\21\3\2\2\2\u00bd\u00be\7\r\2\2\u00be\u00bf\t\3\2\2\u00bf")
        buf.write("\u00c0\7\16\2\2\u00c0\23\3\2\2\2\u00c1\u00c4\7 \2\2\u00c2")
        buf.write("\u00c5\5D#\2\u00c3\u00c5\5d\63\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\25\3\2\2\2\u00c6\u00c7\7+\2\2\u00c7")
        buf.write("\u00ca\78\2\2\u00c8\u00cb\5\30\r\2\u00c9\u00cb\5\34\17")
        buf.write("\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\27\3")
        buf.write("\2\2\2\u00cc\u00cd\7,\2\2\u00cd\u00d1\7\13\2\2\u00ce\u00d0")
        buf.write("\7\b\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d7\3\2\2\2")
        buf.write("\u00d3\u00d1\3\2\2\2\u00d4\u00d6\5\32\16\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00da\u00db\7\f\2\2\u00db\u00dc\t\4\2\2\u00dc\31\3\2")
        buf.write("\2\2\u00dd\u00df\7\b\2\2\u00de\u00dd\3\2\2\2\u00df\u00e2")
        buf.write("\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e9\78\2\2")
        buf.write("\u00e4\u00ea\5\16\b\2\u00e5\u00ea\5\30\r\2\u00e6\u00ea")
        buf.write("\5\20\t\2\u00e7\u00ea\5\34\17\2\u00e8\u00ea\78\2\2\u00e9")
        buf.write("\u00e4\3\2\2\2\u00e9\u00e5\3\2\2\2\u00e9\u00e6\3\2\2\2")
        buf.write("\u00e9\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00ef\3")
        buf.write("\2\2\2\u00eb\u00f0\7\20\2\2\u00ec\u00f0\7\b\2\2\u00ed")
        buf.write("\u00ee\7\20\2\2\u00ee\u00f0\7\b\2\2\u00ef\u00eb\3\2\2")
        buf.write("\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\33\3")
        buf.write("\2\2\2\u00f1\u00f2\7-\2\2\u00f2\u00f6\7\13\2\2\u00f3\u00f5")
        buf.write("\7\b\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00fc\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f9\u00fb\5\36\20\2\u00fa\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc")
        buf.write("\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3\2\2\2")
        buf.write("\u00ff\u0100\7\f\2\2\u0100\u0101\t\4\2\2\u0101\35\3\2")
        buf.write("\2\2\u0102\u0103\78\2\2\u0103\u0105\7\t\2\2\u0104\u0106")
        buf.write("\5 \21\2\u0105\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u010b\7\n\2\2\u0108\u010c\5\16\b")
        buf.write("\2\u0109\u010c\5\20\t\2\u010a\u010c\78\2\2\u010b\u0108")
        buf.write("\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c\u0113\3\2\2\2\u010d\u0112\7\20\2")
        buf.write("\2\u010e\u0112\7\b\2\2\u010f\u0110\7\20\2\2\u0110\u0112")
        buf.write("\7\b\2\2\u0111\u010d\3\2\2\2\u0111\u010e\3\2\2\2\u0111")
        buf.write("\u010f\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0114\37\3\2\2\2\u0115\u0113\3\2")
        buf.write("\2\2\u0116\u0119\78\2\2\u0117\u011a\5\16\b\2\u0118\u011a")
        buf.write("\5\20\t\2\u0119\u0117\3\2\2\2\u0119\u0118\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\5\"\22")
        buf.write("\2\u011c!\3\2\2\2\u011d\u011e\7\17\2\2\u011e\u011f\5 ")
        buf.write("\21\2\u011f\u0120\5\"\22\2\u0120\u0123\3\2\2\2\u0121\u0123")
        buf.write("\3\2\2\2\u0122\u011d\3\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("#\3\2\2\2\u0124\u0126\7*\2\2\u0125\u0127\5*\26\2\u0126")
        buf.write("\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\u0129\78\2\2\u0129\u012b\7\t\2\2\u012a\u012c\5")
        buf.write("&\24\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u0131\7\n\2\2\u012e\u0132\5\16\b\2\u012f")
        buf.write("\u0132\5\20\t\2\u0130\u0132\78\2\2\u0131\u012e\3\2\2\2")
        buf.write("\u0131\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0131\u0132\3")
        buf.write("\2\2\2\u0132\u0139\3\2\2\2\u0133\u0138\7\20\2\2\u0134")
        buf.write("\u0138\7\b\2\2\u0135\u0136\7\20\2\2\u0136\u0138\7\b\2")
        buf.write("\2\u0137\u0133\3\2\2\2\u0137\u0134\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u013a\3\2\2\2\u0139")
        buf.write("\u0137\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013c\u0140\7\13\2\2\u013d\u013f\7\b\2\2\u013e\u013d")
        buf.write("\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140")
        buf.write("\u0141\3\2\2\2\u0141\u0149\3\2\2\2\u0142\u0140\3\2\2\2")
        buf.write("\u0143\u0145\5,\27\2\u0144\u0146\7\b\2\2\u0145\u0144\3")
        buf.write("\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0143")
        buf.write("\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u0149\3\2\2\2")
        buf.write("\u014c\u014e\7\f\2\2\u014d\u014f\7\b\2\2\u014e\u014d\3")
        buf.write("\2\2\2\u014e\u014f\3\2\2\2\u014f%\3\2\2\2\u0150\u0153")
        buf.write("\78\2\2\u0151\u0154\5\16\b\2\u0152\u0154\5\20\t\2\u0153")
        buf.write("\u0151\3\2\2\2\u0153\u0152\3\2\2\2\u0154\u0155\3\2\2\2")
        buf.write("\u0155\u0156\5(\25\2\u0156\'\3\2\2\2\u0157\u0158\7\17")
        buf.write("\2\2\u0158\u0159\5&\24\2\u0159\u015a\5(\25\2\u015a\u015d")
        buf.write("\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u0157\3\2\2\2\u015c")
        buf.write("\u015b\3\2\2\2\u015d)\3\2\2\2\u015e\u015f\7\t\2\2\u015f")
        buf.write("\u0160\78\2\2\u0160\u0161\78\2\2\u0161\u0162\7\n\2\2\u0162")
        buf.write("+\3\2\2\2\u0163\u016e\5\f\7\2\u0164\u016e\5\n\6\2\u0165")
        buf.write("\u016e\5.\30\2\u0166\u016e\5\64\33\2\u0167\u016e\58\35")
        buf.write("\2\u0168\u016e\5> \2\u0169\u016e\5@!\2\u016a\u016e\5Z")
        buf.write(".\2\u016b\u016e\5`\61\2\u016c\u016e\5B\"\2\u016d\u0163")
        buf.write("\3\2\2\2\u016d\u0164\3\2\2\2\u016d\u0165\3\2\2\2\u016d")
        buf.write("\u0166\3\2\2\2\u016d\u0167\3\2\2\2\u016d\u0168\3\2\2\2")
        buf.write("\u016d\u0169\3\2\2\2\u016d\u016a\3\2\2\2\u016d\u016b\3")
        buf.write("\2\2\2\u016d\u016c\3\2\2\2\u016e\u0173\3\2\2\2\u016f\u0174")
        buf.write("\7\b\2\2\u0170\u0174\7\20\2\2\u0171\u0172\7\20\2\2\u0172")
        buf.write("\u0174\7\b\2\2\u0173\u016f\3\2\2\2\u0173\u0170\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0174-\3\2\2\2\u0175\u0176\5\60\31")
        buf.write("\2\u0176\u0179\5\62\32\2\u0177\u017a\5D#\2\u0178\u017a")
        buf.write("\5d\63\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("/\3\2\2\2\u017b\u017f\78\2\2\u017c\u017f\5R*\2\u017d\u017f")
        buf.write("\5V,\2\u017e\u017b\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017d")
        buf.write("\3\2\2\2\u017f\61\3\2\2\2\u0180\u0181\7\21\2\2\u0181\u0188")
        buf.write("\7 \2\2\u0182\u0188\7!\2\2\u0183\u0188\7\"\2\2\u0184\u0188")
        buf.write("\7#\2\2\u0185\u0188\7$\2\2\u0186\u0188\7%\2\2\u0187\u0180")
        buf.write("\3\2\2\2\u0187\u0182\3\2\2\2\u0187\u0183\3\2\2\2\u0187")
        buf.write("\u0184\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2")
        buf.write("\u0188\63\3\2\2\2\u0189\u018a\7&\2\2\u018a\u018b\7\t\2")
        buf.write("\2\u018b\u018c\5D#\2\u018c\u0190\7\n\2\2\u018d\u018f\7")
        buf.write("\b\2\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u0197\7\13\2\2\u0194\u0196\7\b\2")
        buf.write("\2\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019d\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u019a\u019c\5,\27\2\u019b\u019a\3\2\2\2")
        buf.write("\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3")
        buf.write("\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a2")
        buf.write("\7\f\2\2\u01a1\u01a3\7\b\2\2\u01a2\u01a1\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3\u01a5\3\2\2\2\u01a4\u01a6\5\66\34")
        buf.write("\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\65\3")
        buf.write("\2\2\2\u01a7\u01c3\7\'\2\2\u01a8\u01c4\5\64\33\2\u01a9")
        buf.write("\u01ab\7\b\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2")
        buf.write("\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01af\3")
        buf.write("\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b3\7\13\2\2\u01b0")
        buf.write("\u01b2\7\b\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2")
        buf.write("\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b9\3")
        buf.write("\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b8\5,\27\2\u01b7\u01b6")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01bc\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bc\u01c0\7\f\2\2\u01bd\u01bf\7\b\2\2\u01be\u01bd\3")
        buf.write("\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3")
        buf.write("\u01a8\3\2\2\2\u01c3\u01ac\3\2\2\2\u01c4\67\3\2\2\2\u01c5")
        buf.write("\u01c9\7(\2\2\u01c6\u01ca\5D#\2\u01c7\u01ca\5:\36\2\u01c8")
        buf.write("\u01ca\5<\37\2\u01c9\u01c6\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cf\7")
        buf.write("\13\2\2\u01cc\u01ce\7\b\2\2\u01cd\u01cc\3\2\2\2\u01ce")
        buf.write("\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2")
        buf.write("\u01d0\u01d5\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d4\5")
        buf.write(",\27\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01d9\7\f\2\2\u01d99\3\2\2\2\u01da")
        buf.write("\u01e3\5.\30\2\u01db\u01dc\7\63\2\2\u01dc\u01df\78\2\2")
        buf.write("\u01dd\u01e0\5\16\b\2\u01de\u01e0\5\20\t\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01df\u01de\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u01e1\3\2\2\2\u01e1\u01e3\5\24\13\2\u01e2\u01da\3\2\2")
        buf.write("\2\u01e2\u01db\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5")
        buf.write("\7\20\2\2\u01e5\u01e6\5D#\2\u01e6\u01e7\7\20\2\2\u01e7")
        buf.write("\u01e8\5.\30\2\u01e8;\3\2\2\2\u01e9\u01ea\t\5\2\2\u01ea")
        buf.write("\u01eb\7\17\2\2\u01eb\u01ec\t\6\2\2\u01ec\u01ed\7\21\2")
        buf.write("\2\u01ed\u01ee\7 \2\2\u01ee\u01f2\7\66\2\2\u01ef\u01f3")
        buf.write("\78\2\2\u01f0\u01f3\5h\65\2\u01f1\u01f3\5R*\2\u01f2\u01ef")
        buf.write("\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3")
        buf.write("=\3\2\2\2\u01f4\u01f5\7\65\2\2\u01f5?\3\2\2\2\u01f6\u01f7")
        buf.write("\7\64\2\2\u01f7A\3\2\2\2\u01f8\u01fa\7)\2\2\u01f9\u01fb")
        buf.write("\5D#\2\u01fa\u01f9\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fbC")
        buf.write("\3\2\2\2\u01fc\u01fd\b#\1\2\u01fd\u01fe\5F$\2\u01fe\u0204")
        buf.write("\3\2\2\2\u01ff\u0200\f\4\2\2\u0200\u0201\7\36\2\2\u0201")
        buf.write("\u0203\5F$\2\u0202\u01ff\3\2\2\2\u0203\u0206\3\2\2\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205E\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0207\u0208\b$\1\2\u0208\u0209\5H%\2\u0209")
        buf.write("\u020f\3\2\2\2\u020a\u020b\f\4\2\2\u020b\u020c\7\35\2")
        buf.write("\2\u020c\u020e\5H%\2\u020d\u020a\3\2\2\2\u020e\u0211\3")
        buf.write("\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210G")
        buf.write("\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0213\b%\1\2\u0213")
        buf.write("\u0214\5J&\2\u0214\u021a\3\2\2\2\u0215\u0216\f\4\2\2\u0216")
        buf.write("\u0217\t\7\2\2\u0217\u0219\5J&\2\u0218\u0215\3\2\2\2\u0219")
        buf.write("\u021c\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2")
        buf.write("\u021bI\3\2\2\2\u021c\u021a\3\2\2\2\u021d\u021e\b&\1\2")
        buf.write("\u021e\u021f\5L\'\2\u021f\u0225\3\2\2\2\u0220\u0221\f")
        buf.write("\4\2\2\u0221\u0222\t\b\2\2\u0222\u0224\5L\'\2\u0223\u0220")
        buf.write("\3\2\2\2\u0224\u0227\3\2\2\2\u0225\u0223\3\2\2\2\u0225")
        buf.write("\u0226\3\2\2\2\u0226K\3\2\2\2\u0227\u0225\3\2\2\2\u0228")
        buf.write("\u0229\b\'\1\2\u0229\u022a\5N(\2\u022a\u0230\3\2\2\2\u022b")
        buf.write("\u022c\f\4\2\2\u022c\u022d\t\t\2\2\u022d\u022f\5N(\2\u022e")
        buf.write("\u022b\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231M\3\2\2\2\u0232\u0230\3\2\2")
        buf.write("\2\u0233\u0235\t\n\2\2\u0234\u0233\3\2\2\2\u0235\u0238")
        buf.write("\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237")
        buf.write("\u0239\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023c\5P)\2\u023a")
        buf.write("\u023c\5P)\2\u023b\u0236\3\2\2\2\u023b\u023a\3\2\2\2\u023c")
        buf.write("O\3\2\2\2\u023d\u0241\5R*\2\u023e\u0241\5`\61\2\u023f")
        buf.write("\u0241\5X-\2\u0240\u023d\3\2\2\2\u0240\u023e\3\2\2\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241Q\3\2\2\2\u0242\u0245\5f\64\2\u0243")
        buf.write("\u0245\5Z.\2\u0244\u0242\3\2\2\2\u0244\u0243\3\2\2\2\u0245")
        buf.write("\u0247\3\2\2\2\u0246\u0248\5T+\2\u0247\u0246\3\2\2\2\u0248")
        buf.write("\u0249\3\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2")
        buf.write("\u024aS\3\2\2\2\u024b\u024c\7\r\2\2\u024c\u024d\5D#\2")
        buf.write("\u024d\u024e\7\16\2\2\u024eU\3\2\2\2\u024f\u0252\5f\64")
        buf.write("\2\u0250\u0252\5R*\2\u0251\u024f\3\2\2\2\u0251\u0250\3")
        buf.write("\2\2\2\u0252\u0253\3\2\2\2\u0253\u0257\7\6\2\2\u0254\u0258")
        buf.write("\5V,\2\u0255\u0258\5f\64\2\u0256\u0258\5R*\2\u0257\u0254")
        buf.write("\3\2\2\2\u0257\u0255\3\2\2\2\u0257\u0256\3\2\2\2\u0258")
        buf.write("W\3\2\2\2\u0259\u025d\5Z.\2\u025a\u025d\5V,\2\u025b\u025d")
        buf.write("\5b\62\2\u025c\u0259\3\2\2\2\u025c\u025a\3\2\2\2\u025c")
        buf.write("\u025b\3\2\2\2\u025dY\3\2\2\2\u025e\u025f\78\2\2\u025f")
        buf.write("\u0261\7\t\2\2\u0260\u0262\5\\/\2\u0261\u0260\3\2\2\2")
        buf.write("\u0261\u0262\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\7")
        buf.write("\n\2\2\u0264[\3\2\2\2\u0265\u0266\5D#\2\u0266\u0267\5")
        buf.write("^\60\2\u0267]\3\2\2\2\u0268\u0269\7\17\2\2\u0269\u026a")
        buf.write("\5D#\2\u026a\u026b\5^\60\2\u026b\u026e\3\2\2\2\u026c\u026e")
        buf.write("\3\2\2\2\u026d\u0268\3\2\2\2\u026d\u026c\3\2\2\2\u026e")
        buf.write("_\3\2\2\2\u026f\u0271\7\t\2\2\u0270\u026f\3\2\2\2\u0270")
        buf.write("\u0271\3\2\2\2\u0271\u0276\3\2\2\2\u0272\u0277\5f\64\2")
        buf.write("\u0273\u0277\5Z.\2\u0274\u0277\5R*\2\u0275\u0277\78\2")
        buf.write("\2\u0276\u0272\3\2\2\2\u0276\u0273\3\2\2\2\u0276\u0274")
        buf.write("\3\2\2\2\u0276\u0275\3\2\2\2\u0277\u0279\3\2\2\2\u0278")
        buf.write("\u027a\7\n\2\2\u0279\u0278\3\2\2\2\u0279\u027a\3\2\2\2")
        buf.write("\u027a\u027b\3\2\2\2\u027b\u027c\7\6\2\2\u027c\u027d\5")
        buf.write("D#\2\u027da\3\2\2\2\u027e\u027f\7\t\2\2\u027f\u0280\5")
        buf.write("D#\2\u0280\u0281\7\n\2\2\u0281\u0284\3\2\2\2\u0282\u0284")
        buf.write("\5f\64\2\u0283\u027e\3\2\2\2\u0283\u0282\3\2\2\2\u0284")
        buf.write("c\3\2\2\2\u0285\u0287\5\20\t\2\u0286\u0288\5h\65\2\u0287")
        buf.write("\u0286\3\2\2\2\u0287\u0288\3\2\2\2\u0288e\3\2\2\2\u0289")
        buf.write("\u0296\7<\2\2\u028a\u0296\7>\2\2\u028b\u0296\7:\2\2\u028c")
        buf.write("\u0296\7;\2\2\u028d\u0296\79\2\2\u028e\u0296\7=\2\2\u028f")
        buf.write("\u0296\7?\2\2\u0290\u0296\7B\2\2\u0291\u0296\5h\65\2\u0292")
        buf.write("\u0296\5l\67\2\u0293\u0296\78\2\2\u0294\u0296\5d\63\2")
        buf.write("\u0295\u0289\3\2\2\2\u0295\u028a\3\2\2\2\u0295\u028b\3")
        buf.write("\2\2\2\u0295\u028c\3\2\2\2\u0295\u028d\3\2\2\2\u0295\u028e")
        buf.write("\3\2\2\2\u0295\u028f\3\2\2\2\u0295\u0290\3\2\2\2\u0295")
        buf.write("\u0291\3\2\2\2\u0295\u0292\3\2\2\2\u0295\u0293\3\2\2\2")
        buf.write("\u0295\u0294\3\2\2\2\u0296g\3\2\2\2\u0297\u0298\7\13\2")
        buf.write("\2\u0298\u0299\5f\64\2\u0299\u029a\5j\66\2\u029a\u029b")
        buf.write("\7\f\2\2\u029b\u029c\5j\66\2\u029ci\3\2\2\2\u029d\u029e")
        buf.write("\7\17\2\2\u029e\u029f\5f\64\2\u029f\u02a0\5j\66\2\u02a0")
        buf.write("\u02a3\3\2\2\2\u02a1\u02a3\3\2\2\2\u02a2\u029d\3\2\2\2")
        buf.write("\u02a2\u02a1\3\2\2\2\u02a3k\3\2\2\2\u02a4\u02a5\78\2\2")
        buf.write("\u02a5\u02a7\7\13\2\2\u02a6\u02a8\5n8\2\u02a7\u02a6\3")
        buf.write("\2\2\2\u02a7\u02a8\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02aa")
        buf.write("\7\f\2\2\u02aam\3\2\2\2\u02ab\u02ac\78\2\2\u02ac\u02ad")
        buf.write("\7\21\2\2\u02ad\u02ae\5D#\2\u02ae\u02af\5p9\2\u02afo\3")
        buf.write("\2\2\2\u02b0\u02b1\7\17\2\2\u02b1\u02b4\5n8\2\u02b2\u02b4")
        buf.write("\3\2\2\2\u02b3\u02b0\3\2\2\2\u02b3\u02b2\3\2\2\2\u02b4")
        buf.write("q\3\2\2\2Uu|\u0088\u008d\u0094\u009a\u00a7\u00aa\u00af")
        buf.write("\u00b6\u00bb\u00c4\u00ca\u00d1\u00d7\u00e0\u00e9\u00ef")
        buf.write("\u00f6\u00fc\u0105\u010b\u0111\u0113\u0119\u0122\u0126")
        buf.write("\u012b\u0131\u0137\u0139\u0140\u0145\u0149\u014e\u0153")
        buf.write("\u015c\u016d\u0173\u0179\u017e\u0187\u0190\u0197\u019d")
        buf.write("\u01a2\u01a5\u01ac\u01b3\u01b9\u01c0\u01c3\u01c9\u01cf")
        buf.write("\u01d5\u01df\u01e2\u01f2\u01fa\u0204\u020f\u021a\u0225")
        buf.write("\u0230\u0236\u023b\u0240\u0244\u0249\u0251\u0257\u025c")
        buf.write("\u0261\u026d\u0270\u0276\u0279\u0283\u0287\u0295\u02a2")
        buf.write("\u02a7\u02b3")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'index'", "'_'", "'value'", "'.'", "<INVALID>", 
                     "'\n'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'", "':'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "NL", "LB", "RB", "LC", "RC", "LP", 
                      "RP", "COMMA", "SEMICOLON", "COLON", "ADD", "SUBTR", 
                      "MUL", "DIV", "MOD", "EQ", "UNEQ", "LESS", "LESSEQ", 
                      "GREATER", "GREATEREQ", "AND", "OR", "NOT", "ASSIGN", 
                      "ADDASS", "SUBASS", "MULASS", "DIVASS", "MODASS", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "ID", "HEXADECIMAL", "BINARY", "OCTAL", "INTLIT", 
                      "FLOATLIT", "DECIMAL", "BOOLLIT", "TRUE", "FALSE", 
                      "STRINGLIT", "COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

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
    RULE_funcParams = 18
    RULE_funcParamTail = 19
    RULE_methodDeclare = 20
    RULE_stmt = 21
    RULE_assignment = 22
    RULE_lhs = 23
    RULE_assignOp = 24
    RULE_ifstmt = 25
    RULE_elsestmt = 26
    RULE_forstmt = 27
    RULE_initFor = 28
    RULE_rangeFor = 29
    RULE_breakstmt = 30
    RULE_contstmt = 31
    RULE_returnstmt = 32
    RULE_expr = 33
    RULE_expr1 = 34
    RULE_expr2 = 35
    RULE_expr3 = 36
    RULE_expr4 = 37
    RULE_expr5 = 38
    RULE_expr6 = 39
    RULE_arrayElement = 40
    RULE_index = 41
    RULE_structField = 42
    RULE_expr7 = 43
    RULE_funcCall = 44
    RULE_arguments = 45
    RULE_argTail = 46
    RULE_methodCall = 47
    RULE_expr8 = 48
    RULE_arrayInit = 49
    RULE_literal = 50
    RULE_arrayLit = 51
    RULE_literalTail = 52
    RULE_structLit = 53
    RULE_structElement = 54
    RULE_elementTail = 55

    ruleNames =  [ "program", "declarations", "declare", "declareTail", 
                   "constDeclare", "varDeclare", "varType", "arrayType", 
                   "dimensions", "init", "typeDeclare", "structDeclare", 
                   "field", "interfaceDeclare", "method", "parameters", 
                   "paraTail", "funcDeclare", "funcParams", "funcParamTail", 
                   "methodDeclare", "stmt", "assignment", "lhs", "assignOp", 
                   "ifstmt", "elsestmt", "forstmt", "initFor", "rangeFor", 
                   "breakstmt", "contstmt", "returnstmt", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "arrayElement", 
                   "index", "structField", "expr7", "funcCall", "arguments", 
                   "argTail", "methodCall", "expr8", "arrayInit", "literal", 
                   "arrayLit", "literalTail", "structLit", "structElement", 
                   "elementTail" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WS=5
    NL=6
    LB=7
    RB=8
    LC=9
    RC=10
    LP=11
    RP=12
    COMMA=13
    SEMICOLON=14
    COLON=15
    ADD=16
    SUBTR=17
    MUL=18
    DIV=19
    MOD=20
    EQ=21
    UNEQ=22
    LESS=23
    LESSEQ=24
    GREATER=25
    GREATEREQ=26
    AND=27
    OR=28
    NOT=29
    ASSIGN=30
    ADDASS=31
    SUBASS=32
    MULASS=33
    DIVASS=34
    MODASS=35
    IF=36
    ELSE=37
    FOR=38
    RETURN=39
    FUNC=40
    TYPE=41
    STRUCT=42
    INTERFACE=43
    STRING=44
    INT=45
    FLOAT=46
    BOOLEAN=47
    CONST=48
    VAR=49
    CONTINUE=50
    BREAK=51
    RANGE=52
    NIL=53
    ID=54
    HEXADECIMAL=55
    BINARY=56
    OCTAL=57
    INTLIT=58
    FLOATLIT=59
    DECIMAL=60
    BOOLLIT=61
    TRUE=62
    FALSE=63
    STRINGLIT=64
    COMMENT=65
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
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 112
                self.match(MiniGoParser.NL)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.declarations()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 119
                self.match(MiniGoParser.NL)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
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
            self.state = 127
            self.declare()
            self.state = 128
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
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.constDeclare()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.varDeclare()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.typeDeclare()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 136
                    self.match(MiniGoParser.NL)
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 142
                self.declare()
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 143
                        self.match(MiniGoParser.NL) 
                    self.state = 148
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 149
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
            self.state = 154
            self.match(MiniGoParser.CONST)
            self.state = 155
            self.match(MiniGoParser.ID)
            self.state = 156
            self.match(MiniGoParser.ASSIGN)
            self.state = 157
            self.expr(0)
            self.state = 158
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

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
            self.state = 160
            self.match(MiniGoParser.VAR)
            self.state = 161
            self.match(MiniGoParser.ID)
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.state = 162
                self.arrayType()
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 163
                self.varType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 164
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.SEMICOLON, MiniGoParser.ASSIGN]:
                pass
            else:
                pass
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 167
                self.init()


            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 170
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.state = 171
                self.match(MiniGoParser.SEMICOLON)
                self.state = 172
                self.match(MiniGoParser.NL)
                pass


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
            self.state = 175
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
            self.state = 178 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 177
                self.dimensions()
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LP):
                    break

            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 182
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 183
                self.match(MiniGoParser.STRUCT)
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 184
                self.match(MiniGoParser.ID)
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
            self.state = 187
            self.match(MiniGoParser.LP)
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTLIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 189
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


        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


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
            self.state = 191
            self.match(MiniGoParser.ASSIGN)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 192
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 193
                self.arrayInit()
                pass


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
            self.state = 196
            self.match(MiniGoParser.TYPE)
            self.state = 197
            self.match(MiniGoParser.ID)
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 198
                self.structDeclare()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 199
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

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

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
            self.state = 202
            self.match(MiniGoParser.STRUCT)
            self.state = 203
            self.match(MiniGoParser.LC)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 204
                    self.match(MiniGoParser.NL) 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL or _la==MiniGoParser.ID:
                self.state = 210
                self.field()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(MiniGoParser.RC)
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def structDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclareContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def interfaceDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclareContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

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
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 219
                self.match(MiniGoParser.NL)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self.match(MiniGoParser.ID)
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 226
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 227
                self.structDeclare()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 228
                self.arrayType()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 229
                self.interfaceDeclare()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 230
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 233
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.state = 234
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 3:
                self.state = 235
                self.match(MiniGoParser.SEMICOLON)
                self.state = 236
                self.match(MiniGoParser.NL)
                pass


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

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

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
            self.state = 239
            self.match(MiniGoParser.INTERFACE)
            self.state = 240
            self.match(MiniGoParser.LC)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 241
                self.match(MiniGoParser.NL)
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 247
                self.method()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
            self.match(MiniGoParser.RC)
            self.state = 254
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

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


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

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
            self.state = 256
            self.match(MiniGoParser.ID)
            self.state = 257
            self.match(MiniGoParser.LB)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 258
                self.parameters()


            self.state = 261
            self.match(MiniGoParser.RB)
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 262
                self.varType()

            elif la_ == 2:
                self.state = 263
                self.arrayType()

            elif la_ == 3:
                self.state = 264
                self.match(MiniGoParser.ID)


            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 271
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        self.state = 267
                        self.match(MiniGoParser.SEMICOLON)
                        pass

                    elif la_ == 2:
                        self.state = 268
                        self.match(MiniGoParser.NL)
                        pass

                    elif la_ == 3:
                        self.state = 269
                        self.match(MiniGoParser.SEMICOLON)
                        self.state = 270
                        self.match(MiniGoParser.NL)
                        pass

             
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 276
            self.match(MiniGoParser.ID)
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 277
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 278
                self.arrayType()
                pass
            elif token in [MiniGoParser.RB, MiniGoParser.COMMA]:
                pass
            else:
                pass
            self.state = 281
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
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(MiniGoParser.COMMA)
                self.state = 284
                self.parameters()
                self.state = 285
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def methodDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclareContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

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
            self.state = 290
            self.match(MiniGoParser.FUNC)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LB:
                self.state = 291
                self.methodDeclare()


            self.state = 294
            self.match(MiniGoParser.ID)
            self.state = 295
            self.match(MiniGoParser.LB)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 296
                self.funcParams()


            self.state = 299
            self.match(MiniGoParser.RB)
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 300
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 301
                self.arrayType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 302
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.NL, MiniGoParser.LC, MiniGoParser.SEMICOLON]:
                pass
            else:
                pass
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 309
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 305
                        self.match(MiniGoParser.SEMICOLON)
                        pass

                    elif la_ == 2:
                        self.state = 306
                        self.match(MiniGoParser.NL)
                        pass

                    elif la_ == 3:
                        self.state = 307
                        self.match(MiniGoParser.SEMICOLON)
                        self.state = 308
                        self.match(MiniGoParser.NL)
                        pass

             
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 314
            self.match(MiniGoParser.LC)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 315
                self.match(MiniGoParser.NL)
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (MiniGoParser.LB - 7)) | (1 << (MiniGoParser.LC - 7)) | (1 << (MiniGoParser.LP - 7)) | (1 << (MiniGoParser.IF - 7)) | (1 << (MiniGoParser.FOR - 7)) | (1 << (MiniGoParser.RETURN - 7)) | (1 << (MiniGoParser.CONST - 7)) | (1 << (MiniGoParser.VAR - 7)) | (1 << (MiniGoParser.CONTINUE - 7)) | (1 << (MiniGoParser.BREAK - 7)) | (1 << (MiniGoParser.ID - 7)) | (1 << (MiniGoParser.HEXADECIMAL - 7)) | (1 << (MiniGoParser.BINARY - 7)) | (1 << (MiniGoParser.OCTAL - 7)) | (1 << (MiniGoParser.INTLIT - 7)) | (1 << (MiniGoParser.FLOATLIT - 7)) | (1 << (MiniGoParser.DECIMAL - 7)) | (1 << (MiniGoParser.BOOLLIT - 7)) | (1 << (MiniGoParser.STRINGLIT - 7)))) != 0):
                self.state = 321
                self.stmt()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NL:
                    self.state = 322
                    self.match(MiniGoParser.NL)


                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 330
            self.match(MiniGoParser.RC)
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 331
                self.match(MiniGoParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcParamTail(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamTailContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParams" ):
                return visitor.visitFuncParams(self)
            else:
                return visitor.visitChildren(self)




    def funcParams(self):

        localctx = MiniGoParser.FuncParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(MiniGoParser.ID)
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 335
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 336
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 339
            self.funcParamTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def funcParamTail(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParamTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParamTail" ):
                return visitor.visitFuncParamTail(self)
            else:
                return visitor.visitChildren(self)




    def funcParamTail(self):

        localctx = MiniGoParser.FuncParamTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funcParamTail)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(MiniGoParser.COMMA)
                self.state = 342
                self.funcParams()
                self.state = 343
                self.funcParamTail()
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
        self.enterRule(localctx, 40, self.RULE_methodDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(MiniGoParser.LB)
            self.state = 349
            self.match(MiniGoParser.ID)
            self.state = 350
            self.match(MiniGoParser.ID)
            self.state = 351
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


        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 353
                self.varDeclare()
                pass

            elif la_ == 2:
                self.state = 354
                self.constDeclare()
                pass

            elif la_ == 3:
                self.state = 355
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 356
                self.ifstmt()
                pass

            elif la_ == 5:
                self.state = 357
                self.forstmt()
                pass

            elif la_ == 6:
                self.state = 358
                self.breakstmt()
                pass

            elif la_ == 7:
                self.state = 359
                self.contstmt()
                pass

            elif la_ == 8:
                self.state = 360
                self.funcCall()
                pass

            elif la_ == 9:
                self.state = 361
                self.methodCall()
                pass

            elif la_ == 10:
                self.state = 362
                self.returnstmt()
                pass


            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 365
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 2:
                self.state = 366
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.state = 367
                self.match(MiniGoParser.SEMICOLON)
                self.state = 368
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
        self.enterRule(localctx, 44, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.lhs()
            self.state = 372
            self.assignOp()
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 373
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 374
                self.arrayInit()
                pass


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
        self.enterRule(localctx, 46, self.RULE_lhs)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.arrayElement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
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
        self.enterRule(localctx, 48, self.RULE_assignOp)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(MiniGoParser.COLON)
                self.state = 383
                self.match(MiniGoParser.ASSIGN)
                pass
            elif token in [MiniGoParser.ADDASS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.match(MiniGoParser.ADDASS)
                pass
            elif token in [MiniGoParser.SUBASS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
                self.match(MiniGoParser.SUBASS)
                pass
            elif token in [MiniGoParser.MULASS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 386
                self.match(MiniGoParser.MULASS)
                pass
            elif token in [MiniGoParser.DIVASS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 387
                self.match(MiniGoParser.DIVASS)
                pass
            elif token in [MiniGoParser.MODASS]:
                self.enterOuterAlt(localctx, 6)
                self.state = 388
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
        self.enterRule(localctx, 50, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(MiniGoParser.IF)
            self.state = 392
            self.match(MiniGoParser.LB)
            self.state = 393
            self.expr(0)
            self.state = 394
            self.match(MiniGoParser.RB)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 395
                self.match(MiniGoParser.NL)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 401
            self.match(MiniGoParser.LC)
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 402
                self.match(MiniGoParser.NL)
                self.state = 407
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (MiniGoParser.LB - 7)) | (1 << (MiniGoParser.LC - 7)) | (1 << (MiniGoParser.LP - 7)) | (1 << (MiniGoParser.IF - 7)) | (1 << (MiniGoParser.FOR - 7)) | (1 << (MiniGoParser.RETURN - 7)) | (1 << (MiniGoParser.CONST - 7)) | (1 << (MiniGoParser.VAR - 7)) | (1 << (MiniGoParser.CONTINUE - 7)) | (1 << (MiniGoParser.BREAK - 7)) | (1 << (MiniGoParser.ID - 7)) | (1 << (MiniGoParser.HEXADECIMAL - 7)) | (1 << (MiniGoParser.BINARY - 7)) | (1 << (MiniGoParser.OCTAL - 7)) | (1 << (MiniGoParser.INTLIT - 7)) | (1 << (MiniGoParser.FLOATLIT - 7)) | (1 << (MiniGoParser.DECIMAL - 7)) | (1 << (MiniGoParser.BOOLLIT - 7)) | (1 << (MiniGoParser.STRINGLIT - 7)))) != 0):
                self.state = 408
                self.stmt()
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 414
            self.match(MiniGoParser.RC)
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 415
                self.match(MiniGoParser.NL)


            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 418
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
        self.enterRule(localctx, 52, self.RULE_elsestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MiniGoParser.ELSE)
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF]:
                self.state = 422
                self.ifstmt()
                pass
            elif token in [MiniGoParser.NL, MiniGoParser.LC]:
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 423
                    self.match(MiniGoParser.NL)
                    self.state = 428
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 429
                self.match(MiniGoParser.LC)
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 430
                    self.match(MiniGoParser.NL)
                    self.state = 435
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (MiniGoParser.LB - 7)) | (1 << (MiniGoParser.LC - 7)) | (1 << (MiniGoParser.LP - 7)) | (1 << (MiniGoParser.IF - 7)) | (1 << (MiniGoParser.FOR - 7)) | (1 << (MiniGoParser.RETURN - 7)) | (1 << (MiniGoParser.CONST - 7)) | (1 << (MiniGoParser.VAR - 7)) | (1 << (MiniGoParser.CONTINUE - 7)) | (1 << (MiniGoParser.BREAK - 7)) | (1 << (MiniGoParser.ID - 7)) | (1 << (MiniGoParser.HEXADECIMAL - 7)) | (1 << (MiniGoParser.BINARY - 7)) | (1 << (MiniGoParser.OCTAL - 7)) | (1 << (MiniGoParser.INTLIT - 7)) | (1 << (MiniGoParser.FLOATLIT - 7)) | (1 << (MiniGoParser.DECIMAL - 7)) | (1 << (MiniGoParser.BOOLLIT - 7)) | (1 << (MiniGoParser.STRINGLIT - 7)))) != 0):
                    self.state = 436
                    self.stmt()
                    self.state = 441
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 442
                self.match(MiniGoParser.RC)
                self.state = 446
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 443
                        self.match(MiniGoParser.NL) 
                    self.state = 448
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(MiniGoParser.FOR)
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 452
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 453
                self.initFor()
                pass

            elif la_ == 3:
                self.state = 454
                self.rangeFor()
                pass


            self.state = 457
            self.match(MiniGoParser.LC)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 458
                self.match(MiniGoParser.NL)
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (MiniGoParser.LB - 7)) | (1 << (MiniGoParser.LC - 7)) | (1 << (MiniGoParser.LP - 7)) | (1 << (MiniGoParser.IF - 7)) | (1 << (MiniGoParser.FOR - 7)) | (1 << (MiniGoParser.RETURN - 7)) | (1 << (MiniGoParser.CONST - 7)) | (1 << (MiniGoParser.VAR - 7)) | (1 << (MiniGoParser.CONTINUE - 7)) | (1 << (MiniGoParser.BREAK - 7)) | (1 << (MiniGoParser.ID - 7)) | (1 << (MiniGoParser.HEXADECIMAL - 7)) | (1 << (MiniGoParser.BINARY - 7)) | (1 << (MiniGoParser.OCTAL - 7)) | (1 << (MiniGoParser.INTLIT - 7)) | (1 << (MiniGoParser.FLOATLIT - 7)) | (1 << (MiniGoParser.DECIMAL - 7)) | (1 << (MiniGoParser.BOOLLIT - 7)) | (1 << (MiniGoParser.STRINGLIT - 7)))) != 0):
                self.state = 464
                self.stmt()
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 470
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
        self.enterRule(localctx, 56, self.RULE_initFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LC, MiniGoParser.LP, MiniGoParser.ID, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.BOOLLIT, MiniGoParser.STRINGLIT]:
                self.state = 472
                self.assignment()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 473
                self.match(MiniGoParser.VAR)
                self.state = 474
                self.match(MiniGoParser.ID)
                self.state = 477
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 475
                    self.varType()
                    pass
                elif token in [MiniGoParser.LP]:
                    self.state = 476
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.ASSIGN]:
                    pass
                else:
                    pass
                self.state = 479
                self.init()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 482
            self.match(MiniGoParser.SEMICOLON)
            self.state = 483
            self.expr(0)
            self.state = 484
            self.match(MiniGoParser.SEMICOLON)
            self.state = 485
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


        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rangeFor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeFor" ):
                return visitor.visitRangeFor(self)
            else:
                return visitor.visitChildren(self)




    def rangeFor(self):

        localctx = MiniGoParser.RangeForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_rangeFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 488
            self.match(MiniGoParser.COMMA)
            self.state = 489
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__1 or _la==MiniGoParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 490
            self.match(MiniGoParser.COLON)
            self.state = 491
            self.match(MiniGoParser.ASSIGN)
            self.state = 492
            self.match(MiniGoParser.RANGE)
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 493
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 494
                self.arrayLit()
                pass

            elif la_ == 3:
                self.state = 495
                self.arrayElement()
                pass


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
        self.enterRule(localctx, 60, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
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
        self.enterRule(localctx, 62, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
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
        self.enterRule(localctx, 64, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(MiniGoParser.RETURN)
            self.state = 504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (MiniGoParser.LB - 7)) | (1 << (MiniGoParser.LC - 7)) | (1 << (MiniGoParser.LP - 7)) | (1 << (MiniGoParser.SUBTR - 7)) | (1 << (MiniGoParser.NOT - 7)) | (1 << (MiniGoParser.ID - 7)) | (1 << (MiniGoParser.HEXADECIMAL - 7)) | (1 << (MiniGoParser.BINARY - 7)) | (1 << (MiniGoParser.OCTAL - 7)) | (1 << (MiniGoParser.INTLIT - 7)) | (1 << (MiniGoParser.FLOATLIT - 7)) | (1 << (MiniGoParser.DECIMAL - 7)) | (1 << (MiniGoParser.BOOLLIT - 7)) | (1 << (MiniGoParser.STRINGLIT - 7)))) != 0):
                self.state = 503
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 514
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 509
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 510
                    self.match(MiniGoParser.OR)
                    self.state = 511
                    self.expr1(0) 
                self.state = 516
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 525
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 520
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 521
                    self.match(MiniGoParser.AND)
                    self.state = 522
                    self.expr2(0) 
                self.state = 527
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 536
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 531
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 532
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.UNEQ) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESSEQ) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATEREQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 533
                    self.expr3(0) 
                self.state = 538
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 547
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 542
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 543
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUBTR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 544
                    self.expr4(0) 
                self.state = 549
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 558
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 553
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 554
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 555
                    self.expr5() 
                self.state = 560
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)

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


        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NOT)
            else:
                return self.getToken(MiniGoParser.NOT, i)

        def SUBTR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SUBTR)
            else:
                return self.getToken(MiniGoParser.SUBTR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT:
                    self.state = 561
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 566
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 567
                self.expr6()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.expr6()
                pass


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


        def methodCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallContext,0)


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
        self.enterRule(localctx, 78, self.RULE_expr6)
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 571
                self.arrayElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
                self.methodCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 573
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

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


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
        self.enterRule(localctx, 80, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 576
                self.literal()
                pass

            elif la_ == 2:
                self.state = 577
                self.funcCall()
                pass


            self.state = 581 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 580
                    self.index()

                else:
                    raise NoViableAltException(self)
                self.state = 583 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(MiniGoParser.LP)
            self.state = 586
            self.expr(0)
            self.state = 587
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

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LiteralContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LiteralContext,i)


        def arrayElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArrayElementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,i)


        def structField(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructField" ):
                return visitor.visitStructField(self)
            else:
                return visitor.visitChildren(self)




    def structField(self):

        localctx = MiniGoParser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 589
                self.literal()
                pass

            elif la_ == 2:
                self.state = 590
                self.arrayElement()
                pass


            self.state = 593
            self.match(MiniGoParser.T__3)
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.state = 594
                self.structField()
                pass

            elif la_ == 2:
                self.state = 595
                self.literal()
                pass

            elif la_ == 3:
                self.state = 596
                self.arrayElement()
                pass


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


        def structField(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldContext,0)


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
        self.enterRule(localctx, 86, self.RULE_expr7)
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 599
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.structField()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 601
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
        self.enterRule(localctx, 88, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.ID)
            self.state = 605
            self.match(MiniGoParser.LB)
            self.state = 607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (MiniGoParser.LB - 7)) | (1 << (MiniGoParser.LC - 7)) | (1 << (MiniGoParser.LP - 7)) | (1 << (MiniGoParser.SUBTR - 7)) | (1 << (MiniGoParser.NOT - 7)) | (1 << (MiniGoParser.ID - 7)) | (1 << (MiniGoParser.HEXADECIMAL - 7)) | (1 << (MiniGoParser.BINARY - 7)) | (1 << (MiniGoParser.OCTAL - 7)) | (1 << (MiniGoParser.INTLIT - 7)) | (1 << (MiniGoParser.FLOATLIT - 7)) | (1 << (MiniGoParser.DECIMAL - 7)) | (1 << (MiniGoParser.BOOLLIT - 7)) | (1 << (MiniGoParser.STRINGLIT - 7)))) != 0):
                self.state = 606
                self.arguments()


            self.state = 609
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
        self.enterRule(localctx, 90, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.expr(0)
            self.state = 612
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
        self.enterRule(localctx, 92, self.RULE_argTail)
        try:
            self.state = 619
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.match(MiniGoParser.COMMA)
                self.state = 615
                self.expr(0)
                self.state = 616
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = MiniGoParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LB:
                self.state = 621
                self.match(MiniGoParser.LB)


            self.state = 628
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 624
                self.literal()
                pass

            elif la_ == 2:
                self.state = 625
                self.funcCall()
                pass

            elif la_ == 3:
                self.state = 626
                self.arrayElement()
                pass

            elif la_ == 4:
                self.state = 627
                self.match(MiniGoParser.ID)
                pass


            self.state = 631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.RB:
                self.state = 630
                self.match(MiniGoParser.RB)


            self.state = 633
            self.match(MiniGoParser.T__3)
            self.state = 634
            self.expr(0)
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
        self.enterRule(localctx, 96, self.RULE_expr8)
        try:
            self.state = 641
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.match(MiniGoParser.LB)
                self.state = 637
                self.expr(0)
                self.state = 638
                self.match(MiniGoParser.RB)
                pass
            elif token in [MiniGoParser.LC, MiniGoParser.LP, MiniGoParser.ID, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.BOOLLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 640
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
        self.enterRule(localctx, 98, self.RULE_arrayInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.arrayType()
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 644
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

        def DECIMAL(self):
            return self.getToken(MiniGoParser.DECIMAL, 0)

        def BINARY(self):
            return self.getToken(MiniGoParser.BINARY, 0)

        def OCTAL(self):
            return self.getToken(MiniGoParser.OCTAL, 0)

        def HEXADECIMAL(self):
            return self.getToken(MiniGoParser.HEXADECIMAL, 0)

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

        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literal)
        try:
            self.state = 659
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 647
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 648
                self.match(MiniGoParser.DECIMAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 649
                self.match(MiniGoParser.BINARY)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 650
                self.match(MiniGoParser.OCTAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 651
                self.match(MiniGoParser.HEXADECIMAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 652
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 653
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 654
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 655
                self.arrayLit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 656
                self.structLit()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 657
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 658
                self.arrayInit()
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
        self.enterRule(localctx, 102, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.match(MiniGoParser.LC)
            self.state = 662
            self.literal()
            self.state = 663
            self.literalTail()
            self.state = 664
            self.match(MiniGoParser.RC)
            self.state = 665
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
        self.enterRule(localctx, 104, self.RULE_literalTail)
        try:
            self.state = 672
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.match(MiniGoParser.COMMA)
                self.state = 668
                self.literal()
                self.state = 669
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
        self.enterRule(localctx, 106, self.RULE_structLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
            self.match(MiniGoParser.ID)
            self.state = 675
            self.match(MiniGoParser.LC)
            self.state = 677
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 676
                self.structElement()


            self.state = 679
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
        self.enterRule(localctx, 108, self.RULE_structElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.match(MiniGoParser.ID)
            self.state = 682
            self.match(MiniGoParser.COLON)
            self.state = 683
            self.expr(0)
            self.state = 684
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
        self.enterRule(localctx, 110, self.RULE_elementTail)
        try:
            self.state = 689
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 686
                self.match(MiniGoParser.COMMA)
                self.state = 687
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
        self._predicates[33] = self.expr_sempred
        self._predicates[34] = self.expr1_sempred
        self._predicates[35] = self.expr2_sempred
        self._predicates[36] = self.expr3_sempred
        self._predicates[37] = self.expr4_sempred
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
         




