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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u02fa\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\7")
        buf.write("\2v\n\2\f\2\16\2y\13\2\3\2\3\2\7\2}\n\2\f\2\16\2\u0080")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u008b\n")
        buf.write("\4\3\5\7\5\u008e\n\5\f\5\16\5\u0091\13\5\3\5\3\5\7\5\u0095")
        buf.write("\n\5\f\5\16\5\u0098\13\5\3\5\3\5\3\5\5\5\u009d\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00a6\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u00af\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00b6")
        buf.write("\n\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00be\n\b\3\b\5\b\u00c1")
        buf.write("\n\b\3\t\3\t\3\n\6\n\u00c6\n\n\r\n\16\n\u00c7\3\n\3\n")
        buf.write("\3\n\5\n\u00cd\n\n\3\13\3\13\3\13\5\13\u00d2\n\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\5\f\u00d9\n\f\3\r\3\r\3\r\3\r\5\r\u00df")
        buf.write("\n\r\3\16\3\16\3\16\6\16\u00e4\n\16\r\16\16\16\u00e5\3")
        buf.write("\16\3\16\3\16\3\16\3\16\5\16\u00ed\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00f7\n\17\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u00fd\n\17\3\20\3\20\3\20\7\20\u0102\n\20")
        buf.write("\f\20\16\20\u0105\13\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u010c\n\20\6\20\u010e\n\20\r\20\16\20\u010f\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u011a\n\21\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u0120\n\21\3\22\3\22\3\22\7\22\u0125")
        buf.write("\n\22\f\22\16\22\u0128\13\22\3\22\3\22\3\22\5\22\u012d")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u0134\n\23\3\24\3")
        buf.write("\24\5\24\u0138\n\24\3\24\3\24\3\24\7\24\u013d\n\24\f\24")
        buf.write("\16\24\u0140\13\24\3\24\7\24\u0143\n\24\f\24\16\24\u0146")
        buf.write("\13\24\3\24\3\24\3\24\3\24\3\24\5\24\u014d\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\26\3\26\5\26\u0156\n\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0160\n\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u0166\n\26\5\26\u0168\n\26\3\27\3\27")
        buf.write("\6\27\u016c\n\27\r\27\16\27\u016d\3\27\3\27\5\27\u0172")
        buf.write("\n\27\3\30\3\30\7\30\u0176\n\30\f\30\16\30\u0179\13\30")
        buf.write("\3\30\3\30\3\30\6\30\u017e\n\30\r\30\16\30\u017f\5\30")
        buf.write("\u0182\n\30\3\30\3\30\3\30\7\30\u0187\n\30\f\30\16\30")
        buf.write("\u018a\13\30\6\30\u018c\n\30\r\30\16\30\u018d\5\30\u0190")
        buf.write("\n\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32\7\32\u0199\n")
        buf.write("\32\f\32\16\32\u019c\13\32\3\32\3\32\7\32\u01a0\n\32\f")
        buf.write("\32\16\32\u01a3\13\32\3\32\7\32\u01a6\n\32\f\32\16\32")
        buf.write("\u01a9\13\32\3\32\3\32\5\32\u01ad\n\32\3\33\3\33\3\33")
        buf.write("\7\33\u01b2\n\33\f\33\16\33\u01b5\13\33\3\33\3\33\7\33")
        buf.write("\u01b9\n\33\f\33\16\33\u01bc\13\33\3\33\7\33\u01bf\n\33")
        buf.write("\f\33\16\33\u01c2\13\33\3\33\3\33\7\33\u01c6\n\33\f\33")
        buf.write("\16\33\u01c9\13\33\5\33\u01cb\n\33\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u01d1\n\34\3\34\3\34\7\34\u01d5\n\34\f\34\16\34")
        buf.write("\u01d8\13\34\3\34\7\34\u01db\n\34\f\34\16\34\u01de\13")
        buf.write("\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\5\35\u01e7\n\35")
        buf.write("\3\35\5\35\u01ea\n\35\3\35\3\35\3\35\3\35\3\35\3\36\3")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u01fd\n\37\3 \3 \3!\3!\3\"\3\"\5\"\u0205\n\"\3#")
        buf.write("\3#\3#\3#\3#\3#\7#\u020d\n#\f#\16#\u0210\13#\3$\3$\3$")
        buf.write("\3$\3$\3$\7$\u0218\n$\f$\16$\u021b\13$\3%\3%\3%\3%\3%")
        buf.write("\3%\7%\u0223\n%\f%\16%\u0226\13%\3&\3&\3&\3&\3&\3&\7&")
        buf.write("\u022e\n&\f&\16&\u0231\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'")
        buf.write("\u0239\n\'\f\'\16\'\u023c\13\'\3(\7(\u023f\n(\f(\16(\u0242")
        buf.write("\13(\3(\3(\5(\u0246\n(\3)\3)\3)\5)\u024b\n)\3*\3*\5*\u024f")
        buf.write("\n*\3*\6*\u0252\n*\r*\16*\u0253\3+\3+\3+\3+\3,\3,\3,\6")
        buf.write(",\u025d\n,\r,\16,\u025e\5,\u0261\n,\3,\3,\3,\5,\u0266")
        buf.write("\n,\3,\7,\u0269\n,\f,\16,\u026c\13,\6,\u026e\n,\r,\16")
        buf.write(",\u026f\3-\3-\3-\5-\u0275\n-\3.\3.\3.\5.\u027a\n.\3.\3")
        buf.write(".\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\5\60\u0286\n\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0290\n\61")
        buf.write("\3\61\6\61\u0293\n\61\r\61\16\61\u0294\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u029d\n\61\3\61\3\61\3\61\3\61\7")
        buf.write("\61\u02a3\n\61\f\61\16\61\u02a6\13\61\3\61\5\61\u02a9")
        buf.write("\n\61\3\62\3\62\7\62\u02ad\n\62\f\62\16\62\u02b0\13\62")
        buf.write("\3\62\3\62\5\62\u02b4\n\62\3\62\3\62\3\62\5\62\u02b9\n")
        buf.write("\62\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u02c1\n\63\3\64")
        buf.write("\3\64\5\64\u02c5\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u02d4\n\65\3\66")
        buf.write("\3\66\3\66\5\66\u02d9\n\66\3\66\3\66\3\66\3\66\3\67\3")
        buf.write("\67\3\67\5\67\u02e2\n\67\3\67\3\67\3\67\5\67\u02e7\n\67")
        buf.write("\38\38\38\58\u02ec\n8\38\38\39\39\39\39\39\3:\3:\3:\5")
        buf.write(":\u02f8\n:\3:\2\7DFHJL;\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnpr\2\f\4\2\3\4<<\3\2/\62\4\2\7\7\17\17\3\2!&\3\2")
        buf.write("\4\5\4\2\3\3\5\5\3\2\27\34\3\2\22\23\3\2\24\26\4\2\23")
        buf.write("\23\37\37\2\u0359\2w\3\2\2\2\4\u0083\3\2\2\2\6\u008a\3")
        buf.write("\2\2\2\b\u009c\3\2\2\2\n\u009e\3\2\2\2\f\u00a7\3\2\2\2")
        buf.write("\16\u00c0\3\2\2\2\20\u00c2\3\2\2\2\22\u00c5\3\2\2\2\24")
        buf.write("\u00ce\3\2\2\2\26\u00d5\3\2\2\2\30\u00da\3\2\2\2\32\u00e0")
        buf.write("\3\2\2\2\34\u00ee\3\2\2\2\36\u00fe\3\2\2\2 \u0114\3\2")
        buf.write("\2\2\"\u0121\3\2\2\2$\u0133\3\2\2\2&\u0135\3\2\2\2(\u014e")
        buf.write("\3\2\2\2*\u0167\3\2\2\2,\u0169\3\2\2\2.\u018f\3\2\2\2")
        buf.write("\60\u0191\3\2\2\2\62\u0193\3\2\2\2\64\u01ae\3\2\2\2\66")
        buf.write("\u01cc\3\2\2\28\u01e9\3\2\2\2:\u01f0\3\2\2\2<\u01f4\3")
        buf.write("\2\2\2>\u01fe\3\2\2\2@\u0200\3\2\2\2B\u0202\3\2\2\2D\u0206")
        buf.write("\3\2\2\2F\u0211\3\2\2\2H\u021c\3\2\2\2J\u0227\3\2\2\2")
        buf.write("L\u0232\3\2\2\2N\u0245\3\2\2\2P\u024a\3\2\2\2R\u024e\3")
        buf.write("\2\2\2T\u0255\3\2\2\2V\u0260\3\2\2\2X\u0274\3\2\2\2Z\u0276")
        buf.write("\3\2\2\2\\\u027d\3\2\2\2^\u0285\3\2\2\2`\u029c\3\2\2\2")
        buf.write("b\u02b3\3\2\2\2d\u02c0\3\2\2\2f\u02c2\3\2\2\2h\u02d3\3")
        buf.write("\2\2\2j\u02d5\3\2\2\2l\u02e6\3\2\2\2n\u02e8\3\2\2\2p\u02ef")
        buf.write("\3\2\2\2r\u02f7\3\2\2\2tv\7\7\2\2ut\3\2\2\2vy\3\2\2\2")
        buf.write("wu\3\2\2\2wx\3\2\2\2xz\3\2\2\2yw\3\2\2\2z~\5\4\3\2{}\7")
        buf.write("\7\2\2|{\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2")
        buf.write("\177\u0081\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\7\2\2\3")
        buf.write("\u0082\3\3\2\2\2\u0083\u0084\5\6\4\2\u0084\u0085\5\b\5")
        buf.write("\2\u0085\5\3\2\2\2\u0086\u008b\5\n\6\2\u0087\u008b\5\f")
        buf.write("\7\2\u0088\u008b\5\30\r\2\u0089\u008b\5&\24\2\u008a\u0086")
        buf.write("\3\2\2\2\u008a\u0087\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\7\3\2\2\2\u008c\u008e\7\7\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0092\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0092\u0096\5\6\4\2\u0093\u0095\7\7\2\2\u0094\u0093")
        buf.write("\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2\2")
        buf.write("\u0099\u009a\5\b\5\2\u009a\u009d\3\2\2\2\u009b\u009d\3")
        buf.write("\2\2\2\u009c\u008f\3\2\2\2\u009c\u009b\3\2\2\2\u009d\t")
        buf.write("\3\2\2\2\u009e\u009f\7\63\2\2\u009f\u00a0\t\2\2\2\u00a0")
        buf.write("\u00a5\5\26\f\2\u00a1\u00a6\7\7\2\2\u00a2\u00a6\7\17\2")
        buf.write("\2\u00a3\u00a4\7\17\2\2\u00a4\u00a6\7\7\2\2\u00a5\u00a1")
        buf.write("\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6")
        buf.write("\13\3\2\2\2\u00a7\u00a8\7\64\2\2\u00a8\u00a9\t\2\2\2\u00a9")
        buf.write("\u00ae\5\16\b\2\u00aa\u00af\7\7\2\2\u00ab\u00af\7\17\2")
        buf.write("\2\u00ac\u00ad\7\17\2\2\u00ad\u00af\7\7\2\2\u00ae\u00aa")
        buf.write("\3\2\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af")
        buf.write("\r\3\2\2\2\u00b0\u00b6\5\22\n\2\u00b1\u00b6\5\20\t\2\u00b2")
        buf.write("\u00b6\7<\2\2\u00b3\u00b6\7\3\2\2\u00b4\u00b6\7\4\2\2")
        buf.write("\u00b5\u00b0\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5\u00b2\3")
        buf.write("\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00c1")
        buf.write("\3\2\2\2\u00b7\u00c1\5\26\f\2\u00b8\u00be\5\22\n\2\u00b9")
        buf.write("\u00be\5\20\t\2\u00ba\u00be\7<\2\2\u00bb\u00be\7\3\2\2")
        buf.write("\u00bc\u00be\7\4\2\2\u00bd\u00b8\3\2\2\2\u00bd\u00b9\3")
        buf.write("\2\2\2\u00bd\u00ba\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\5\26\f\2\u00c0")
        buf.write("\u00b5\3\2\2\2\u00c0\u00b7\3\2\2\2\u00c0\u00bd\3\2\2\2")
        buf.write("\u00c1\17\3\2\2\2\u00c2\u00c3\t\3\2\2\u00c3\21\3\2\2\2")
        buf.write("\u00c4\u00c6\5\24\13\2\u00c5\u00c4\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00cc\3\2\2\2\u00c9\u00cd\5\20\t\2\u00ca\u00cd\7-\2\2")
        buf.write("\u00cb\u00cd\t\2\2\2\u00cc\u00c9\3\2\2\2\u00cc\u00ca\3")
        buf.write("\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\23\3\2\2\2\u00ce\u00d1")
        buf.write("\7\f\2\2\u00cf\u00d2\7=\2\2\u00d0\u00d2\t\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3\u00d4\7\r\2\2\u00d4\25\3\2\2\2\u00d5\u00d8\7 \2")
        buf.write("\2\u00d6\u00d9\5D#\2\u00d7\u00d9\5f\64\2\u00d8\u00d6\3")
        buf.write("\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\27\3\2\2\2\u00da\u00db")
        buf.write("\7,\2\2\u00db\u00de\t\2\2\2\u00dc\u00df\5\32\16\2\u00dd")
        buf.write("\u00df\5\36\20\2\u00de\u00dc\3\2\2\2\u00de\u00dd\3\2\2")
        buf.write("\2\u00df\31\3\2\2\2\u00e0\u00e1\7-\2\2\u00e1\u00e3\7\n")
        buf.write("\2\2\u00e2\u00e4\5\34\17\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00ec\7\13\2\2\u00e8\u00ed\7\17\2")
        buf.write("\2\u00e9\u00ed\7\7\2\2\u00ea\u00eb\7\17\2\2\u00eb\u00ed")
        buf.write("\7\7\2\2\u00ec\u00e8\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ed\33\3\2\2\2\u00ee\u00f6\t\2\2\2\u00ef")
        buf.write("\u00f7\5\20\t\2\u00f0\u00f7\5\32\16\2\u00f1\u00f7\5\22")
        buf.write("\n\2\u00f2\u00f7\5\36\20\2\u00f3\u00f7\7<\2\2\u00f4\u00f7")
        buf.write("\7\3\2\2\u00f5\u00f7\7\4\2\2\u00f6\u00ef\3\2\2\2\u00f6")
        buf.write("\u00f0\3\2\2\2\u00f6\u00f1\3\2\2\2\u00f6\u00f2\3\2\2\2")
        buf.write("\u00f6\u00f3\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3")
        buf.write("\2\2\2\u00f7\u00fc\3\2\2\2\u00f8\u00fd\7\17\2\2\u00f9")
        buf.write("\u00fd\7\7\2\2\u00fa\u00fb\7\17\2\2\u00fb\u00fd\7\7\2")
        buf.write("\2\u00fc\u00f8\3\2\2\2\u00fc\u00f9\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\35\3\2\2\2\u00fe\u00ff\7.\2\2\u00ff\u0103")
        buf.write("\7\n\2\2\u0100\u0102\7\7\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u010d\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u010b\5")
        buf.write(" \21\2\u0107\u010c\7\17\2\2\u0108\u010c\7\7\2\2\u0109")
        buf.write("\u010a\7\17\2\2\u010a\u010c\7\7\2\2\u010b\u0107\3\2\2")
        buf.write("\2\u010b\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010e")
        buf.write("\3\2\2\2\u010d\u0106\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0112\7\13\2\2\u0112\u0113\t\4\2\2\u0113\37\3\2")
        buf.write("\2\2\u0114\u0115\t\2\2\2\u0115\u0119\7\b\2\2\u0116\u0117")
        buf.write("\5\"\22\2\u0117\u0118\5$\23\2\u0118\u011a\3\2\2\2\u0119")
        buf.write("\u0116\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2\2\2")
        buf.write("\u011b\u011f\7\t\2\2\u011c\u0120\5\20\t\2\u011d\u0120")
        buf.write("\5\22\n\2\u011e\u0120\t\2\2\2\u011f\u011c\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120!\3\2\2\2\u0121\u0126\t\2\2\2\u0122\u0123\7\16\2")
        buf.write("\2\u0123\u0125\t\2\2\2\u0124\u0122\3\2\2\2\u0125\u0128")
        buf.write("\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u012c\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012d\5\20\t")
        buf.write("\2\u012a\u012d\5\22\n\2\u012b\u012d\t\2\2\2\u012c\u0129")
        buf.write("\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d")
        buf.write("#\3\2\2\2\u012e\u012f\7\16\2\2\u012f\u0130\5\"\22\2\u0130")
        buf.write("\u0131\5$\23\2\u0131\u0134\3\2\2\2\u0132\u0134\3\2\2\2")
        buf.write("\u0133\u012e\3\2\2\2\u0133\u0132\3\2\2\2\u0134%\3\2\2")
        buf.write("\2\u0135\u0137\7+\2\2\u0136\u0138\5(\25\2\u0137\u0136")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("\u013a\5 \21\2\u013a\u013e\7\n\2\2\u013b\u013d\7\7\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3")
        buf.write("\2\2\2\u013e\u013f\3\2\2\2\u013f\u0144\3\2\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0141\u0143\5*\26\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0147\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u014c\7")
        buf.write("\13\2\2\u0148\u014d\7\7\2\2\u0149\u014d\7\17\2\2\u014a")
        buf.write("\u014b\7\17\2\2\u014b\u014d\7\7\2\2\u014c\u0148\3\2\2")
        buf.write("\2\u014c\u0149\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014d\'\3\2\2\2\u014e\u014f\7\b\2\2\u014f\u0150")
        buf.write("\t\2\2\2\u0150\u0151\t\2\2\2\u0151\u0152\7\t\2\2\u0152")
        buf.write(")\3\2\2\2\u0153\u0156\5\f\7\2\u0154\u0156\5\n\6\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u0168\3\2\2\2")
        buf.write("\u0157\u0160\5,\27\2\u0158\u0160\5\62\32\2\u0159\u0160")
        buf.write("\5\66\34\2\u015a\u0160\5> \2\u015b\u0160\5@!\2\u015c\u0160")
        buf.write("\5Z.\2\u015d\u0160\5b\62\2\u015e\u0160\5B\"\2\u015f\u0157")
        buf.write("\3\2\2\2\u015f\u0158\3\2\2\2\u015f\u0159\3\2\2\2\u015f")
        buf.write("\u015a\3\2\2\2\u015f\u015b\3\2\2\2\u015f\u015c\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u0165\3")
        buf.write("\2\2\2\u0161\u0166\7\7\2\2\u0162\u0166\7\17\2\2\u0163")
        buf.write("\u0164\7\17\2\2\u0164\u0166\7\7\2\2\u0165\u0161\3\2\2")
        buf.write("\2\u0165\u0162\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0168")
        buf.write("\3\2\2\2\u0167\u0155\3\2\2\2\u0167\u015f\3\2\2\2\u0168")
        buf.write("+\3\2\2\2\u0169\u016b\5.\30\2\u016a\u016c\5\60\31\2\u016b")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u0172\5")
        buf.write("D#\2\u0170\u0172\5f\64\2\u0171\u016f\3\2\2\2\u0171\u0170")
        buf.write("\3\2\2\2\u0172-\3\2\2\2\u0173\u0177\t\2\2\2\u0174\u0176")
        buf.write("\5T+\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0190\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u0182\t\2\2\2\u017b\u017d\t\2\2\2")
        buf.write("\u017c\u017e\5T+\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2")
        buf.write("\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0182")
        buf.write("\3\2\2\2\u0181\u017a\3\2\2\2\u0181\u017b\3\2\2\2\u0182")
        buf.write("\u018b\3\2\2\2\u0183\u0184\7\21\2\2\u0184\u0188\t\2\2")
        buf.write("\2\u0185\u0187\5T+\2\u0186\u0185\3\2\2\2\u0187\u018a\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018c")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u0183\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018e\u0190\3\2\2\2\u018f\u0173\3\2\2\2\u018f\u0181\3")
        buf.write("\2\2\2\u0190/\3\2\2\2\u0191\u0192\t\5\2\2\u0192\61\3\2")
        buf.write("\2\2\u0193\u0194\7\'\2\2\u0194\u0195\7\b\2\2\u0195\u0196")
        buf.write("\5D#\2\u0196\u019a\7\t\2\2\u0197\u0199\7\7\2\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019d\u01a1\7\n\2\2\u019e\u01a0\7\7\2\2\u019f\u019e\3")
        buf.write("\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01a7\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4")
        buf.write("\u01a6\5*\26\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2")
        buf.write("\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3")
        buf.write("\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ac\7\13\2\2\u01ab")
        buf.write("\u01ad\5\64\33\2\u01ac\u01ab\3\2\2\2\u01ac\u01ad\3\2\2")
        buf.write("\2\u01ad\63\3\2\2\2\u01ae\u01ca\7(\2\2\u01af\u01cb\5\62")
        buf.write("\32\2\u01b0\u01b2\7\7\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01ba\7\n\2\2")
        buf.write("\u01b7\u01b9\7\7\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc\3")
        buf.write("\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01c0")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01bf\5*\26\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01c0\3")
        buf.write("\2\2\2\u01c3\u01c7\7\13\2\2\u01c4\u01c6\7\7\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c8\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3")
        buf.write("\2\2\2\u01ca\u01af\3\2\2\2\u01ca\u01b3\3\2\2\2\u01cb\65")
        buf.write("\3\2\2\2\u01cc\u01d0\7)\2\2\u01cd\u01d1\5D#\2\u01ce\u01d1")
        buf.write("\58\35\2\u01cf\u01d1\5<\37\2\u01d0\u01cd\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2\u01d6\7\n\2\2\u01d3\u01d5\7\7\2\2\u01d4\u01d3\3")
        buf.write("\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01dc\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9")
        buf.write("\u01db\5*\26\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3")
        buf.write("\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0\7\13\2\2\u01e0")
        buf.write("\67\3\2\2\2\u01e1\u01ea\5:\36\2\u01e2\u01e3\7\64\2\2\u01e3")
        buf.write("\u01e6\t\2\2\2\u01e4\u01e7\5\20\t\2\u01e5\u01e7\5\22\n")
        buf.write("\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e6\u01e7")
        buf.write("\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01ea\5\26\f\2\u01e9")
        buf.write("\u01e1\3\2\2\2\u01e9\u01e2\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01eb\u01ec\t\4\2\2\u01ec\u01ed\5D#\2\u01ed\u01ee\t\4")
        buf.write("\2\2\u01ee\u01ef\5:\36\2\u01ef9\3\2\2\2\u01f0\u01f1\7")
        buf.write("<\2\2\u01f1\u01f2\5\60\31\2\u01f2\u01f3\5h\65\2\u01f3")
        buf.write(";\3\2\2\2\u01f4\u01f5\t\6\2\2\u01f5\u01f6\7\16\2\2\u01f6")
        buf.write("\u01f7\t\7\2\2\u01f7\u01f8\7!\2\2\u01f8\u01fc\7\67\2\2")
        buf.write("\u01f9\u01fd\t\2\2\2\u01fa\u01fd\5h\65\2\u01fb\u01fd\5")
        buf.write("R*\2\u01fc\u01f9\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fb")
        buf.write("\3\2\2\2\u01fd=\3\2\2\2\u01fe\u01ff\7\66\2\2\u01ff?\3")
        buf.write("\2\2\2\u0200\u0201\7\65\2\2\u0201A\3\2\2\2\u0202\u0204")
        buf.write("\7*\2\2\u0203\u0205\5D#\2\u0204\u0203\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205C\3\2\2\2\u0206\u0207\b#\1\2\u0207\u0208")
        buf.write("\5F$\2\u0208\u020e\3\2\2\2\u0209\u020a\f\4\2\2\u020a\u020b")
        buf.write("\7\36\2\2\u020b\u020d\5F$\2\u020c\u0209\3\2\2\2\u020d")
        buf.write("\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2")
        buf.write("\u020fE\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0212\b$\1\2")
        buf.write("\u0212\u0213\5H%\2\u0213\u0219\3\2\2\2\u0214\u0215\f\4")
        buf.write("\2\2\u0215\u0216\7\35\2\2\u0216\u0218\5H%\2\u0217\u0214")
        buf.write("\3\2\2\2\u0218\u021b\3\2\2\2\u0219\u0217\3\2\2\2\u0219")
        buf.write("\u021a\3\2\2\2\u021aG\3\2\2\2\u021b\u0219\3\2\2\2\u021c")
        buf.write("\u021d\b%\1\2\u021d\u021e\5J&\2\u021e\u0224\3\2\2\2\u021f")
        buf.write("\u0220\f\4\2\2\u0220\u0221\t\b\2\2\u0221\u0223\5J&\2\u0222")
        buf.write("\u021f\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0224\u0225\3\2\2\2\u0225I\3\2\2\2\u0226\u0224\3\2\2")
        buf.write("\2\u0227\u0228\b&\1\2\u0228\u0229\5L\'\2\u0229\u022f\3")
        buf.write("\2\2\2\u022a\u022b\f\4\2\2\u022b\u022c\t\t\2\2\u022c\u022e")
        buf.write("\5L\'\2\u022d\u022a\3\2\2\2\u022e\u0231\3\2\2\2\u022f")
        buf.write("\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230K\3\2\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0232\u0233\b\'\1\2\u0233\u0234\5N(\2\u0234")
        buf.write("\u023a\3\2\2\2\u0235\u0236\f\4\2\2\u0236\u0237\t\n\2\2")
        buf.write("\u0237\u0239\5N(\2\u0238\u0235\3\2\2\2\u0239\u023c\3\2")
        buf.write("\2\2\u023a\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023bM\3")
        buf.write("\2\2\2\u023c\u023a\3\2\2\2\u023d\u023f\t\13\2\2\u023e")
        buf.write("\u023d\3\2\2\2\u023f\u0242\3\2\2\2\u0240\u023e\3\2\2\2")
        buf.write("\u0240\u0241\3\2\2\2\u0241\u0243\3\2\2\2\u0242\u0240\3")
        buf.write("\2\2\2\u0243\u0246\5P)\2\u0244\u0246\5P)\2\u0245\u0240")
        buf.write("\3\2\2\2\u0245\u0244\3\2\2\2\u0246O\3\2\2\2\u0247\u024b")
        buf.write("\5R*\2\u0248\u024b\5`\61\2\u0249\u024b\5X-\2\u024a\u0247")
        buf.write("\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u0249\3\2\2\2\u024b")
        buf.write("Q\3\2\2\2\u024c\u024f\5d\63\2\u024d\u024f\5Z.\2\u024e")
        buf.write("\u024c\3\2\2\2\u024e\u024d\3\2\2\2\u024f\u0251\3\2\2\2")
        buf.write("\u0250\u0252\5T+\2\u0251\u0250\3\2\2\2\u0252\u0253\3\2")
        buf.write("\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254S\3")
        buf.write("\2\2\2\u0255\u0256\7\f\2\2\u0256\u0257\5D#\2\u0257\u0258")
        buf.write("\7\r\2\2\u0258U\3\2\2\2\u0259\u0261\t\2\2\2\u025a\u025c")
        buf.write("\t\2\2\2\u025b\u025d\5T+\2\u025c\u025b\3\2\2\2\u025d\u025e")
        buf.write("\3\2\2\2\u025e\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f")
        buf.write("\u0261\3\2\2\2\u0260\u0259\3\2\2\2\u0260\u025a\3\2\2\2")
        buf.write("\u0261\u026d\3\2\2\2\u0262\u0265\7\21\2\2\u0263\u0266")
        buf.write("\7<\2\2\u0264\u0266\5Z.\2\u0265\u0263\3\2\2\2\u0265\u0264")
        buf.write("\3\2\2\2\u0266\u026a\3\2\2\2\u0267\u0269\5T+\2\u0268\u0267")
        buf.write("\3\2\2\2\u0269\u026c\3\2\2\2\u026a\u0268\3\2\2\2\u026a")
        buf.write("\u026b\3\2\2\2\u026b\u026e\3\2\2\2\u026c\u026a\3\2\2\2")
        buf.write("\u026d\u0262\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u026d\3")
        buf.write("\2\2\2\u026f\u0270\3\2\2\2\u0270W\3\2\2\2\u0271\u0275")
        buf.write("\5V,\2\u0272\u0275\5Z.\2\u0273\u0275\5d\63\2\u0274\u0271")
        buf.write("\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0273\3\2\2\2\u0275")
        buf.write("Y\3\2\2\2\u0276\u0277\t\2\2\2\u0277\u0279\7\b\2\2\u0278")
        buf.write("\u027a\5\\/\2\u0279\u0278\3\2\2\2\u0279\u027a\3\2\2\2")
        buf.write("\u027a\u027b\3\2\2\2\u027b\u027c\7\t\2\2\u027c[\3\2\2")
        buf.write("\2\u027d\u027e\5D#\2\u027e\u027f\5^\60\2\u027f]\3\2\2")
        buf.write("\2\u0280\u0281\7\16\2\2\u0281\u0282\5D#\2\u0282\u0283")
        buf.write("\5^\60\2\u0283\u0286\3\2\2\2\u0284\u0286\3\2\2\2\u0285")
        buf.write("\u0280\3\2\2\2\u0285\u0284\3\2\2\2\u0286_\3\2\2\2\u0287")
        buf.write("\u029d\5Z.\2\u0288\u029d\7<\2\2\u0289\u029d\7\3\2\2\u028a")
        buf.write("\u029d\7\4\2\2\u028b\u0290\7<\2\2\u028c\u0290\7\3\2\2")
        buf.write("\u028d\u0290\7\4\2\2\u028e\u0290\5f\64\2\u028f\u028b\3")
        buf.write("\2\2\2\u028f\u028c\3\2\2\2\u028f\u028d\3\2\2\2\u028f\u028e")
        buf.write("\3\2\2\2\u0290\u0292\3\2\2\2\u0291\u0293\5T+\2\u0292\u0291")
        buf.write("\3\2\2\2\u0293\u0294\3\2\2\2\u0294\u0292\3\2\2\2\u0294")
        buf.write("\u0295\3\2\2\2\u0295\u029d\3\2\2\2\u0296\u029d\5n8\2\u0297")
        buf.write("\u029d\79\2\2\u0298\u0299\7\b\2\2\u0299\u029a\5D#\2\u029a")
        buf.write("\u029b\7\t\2\2\u029b\u029d\3\2\2\2\u029c\u0287\3\2\2\2")
        buf.write("\u029c\u0288\3\2\2\2\u029c\u0289\3\2\2\2\u029c\u028a\3")
        buf.write("\2\2\2\u029c\u028f\3\2\2\2\u029c\u0296\3\2\2\2\u029c\u0297")
        buf.write("\3\2\2\2\u029c\u0298\3\2\2\2\u029d\u029e\3\2\2\2\u029e")
        buf.write("\u02a8\7\21\2\2\u029f\u02a9\5Z.\2\u02a0\u02a4\7<\2\2\u02a1")
        buf.write("\u02a3\5T+\2\u02a2\u02a1\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4")
        buf.write("\u02a2\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a9\3\2\2\2")
        buf.write("\u02a6\u02a4\3\2\2\2\u02a7\u02a9\5`\61\2\u02a8\u029f\3")
        buf.write("\2\2\2\u02a8\u02a0\3\2\2\2\u02a8\u02a7\3\2\2\2\u02a9a")
        buf.write("\3\2\2\2\u02aa\u02ae\7<\2\2\u02ab\u02ad\5T+\2\u02ac\u02ab")
        buf.write("\3\2\2\2\u02ad\u02b0\3\2\2\2\u02ae\u02ac\3\2\2\2\u02ae")
        buf.write("\u02af\3\2\2\2\u02af\u02b4\3\2\2\2\u02b0\u02ae\3\2\2\2")
        buf.write("\u02b1\u02b4\7\3\2\2\u02b2\u02b4\7\4\2\2\u02b3\u02aa\3")
        buf.write("\2\2\2\u02b3\u02b1\3\2\2\2\u02b3\u02b2\3\2\2\2\u02b4\u02b5")
        buf.write("\3\2\2\2\u02b5\u02b6\7\21\2\2\u02b6\u02b8\5D#\2\u02b7")
        buf.write("\u02b9\7\17\2\2\u02b8\u02b7\3\2\2\2\u02b8\u02b9\3\2\2")
        buf.write("\2\u02b9c\3\2\2\2\u02ba\u02bb\7\b\2\2\u02bb\u02bc\5D#")
        buf.write("\2\u02bc\u02bd\7\t\2\2\u02bd\u02c1\3\2\2\2\u02be\u02c1")
        buf.write("\5h\65\2\u02bf\u02c1\5f\64\2\u02c0\u02ba\3\2\2\2\u02c0")
        buf.write("\u02be\3\2\2\2\u02c0\u02bf\3\2\2\2\u02c1e\3\2\2\2\u02c2")
        buf.write("\u02c4\5\22\n\2\u02c3\u02c5\5j\66\2\u02c4\u02c3\3\2\2")
        buf.write("\2\u02c4\u02c5\3\2\2\2\u02c5g\3\2\2\2\u02c6\u02d4\7=\2")
        buf.write("\2\u02c7\u02d4\7?\2\2\u02c8\u02d4\7A\2\2\u02c9\u02d4\7")
        buf.write("B\2\2\u02ca\u02d4\7@\2\2\u02cb\u02d4\7>\2\2\u02cc\u02d4")
        buf.write("\79\2\2\u02cd\u02d4\7C\2\2\u02ce\u02d4\5n8\2\u02cf\u02d4")
        buf.write("\7<\2\2\u02d0\u02d4\7\3\2\2\u02d1\u02d4\7\4\2\2\u02d2")
        buf.write("\u02d4\78\2\2\u02d3\u02c6\3\2\2\2\u02d3\u02c7\3\2\2\2")
        buf.write("\u02d3\u02c8\3\2\2\2\u02d3\u02c9\3\2\2\2\u02d3\u02ca\3")
        buf.write("\2\2\2\u02d3\u02cb\3\2\2\2\u02d3\u02cc\3\2\2\2\u02d3\u02cd")
        buf.write("\3\2\2\2\u02d3\u02ce\3\2\2\2\u02d3\u02cf\3\2\2\2\u02d3")
        buf.write("\u02d0\3\2\2\2\u02d3\u02d1\3\2\2\2\u02d3\u02d2\3\2\2\2")
        buf.write("\u02d4i\3\2\2\2\u02d5\u02d8\7\n\2\2\u02d6\u02d9\5h\65")
        buf.write("\2\u02d7\u02d9\5j\66\2\u02d8\u02d6\3\2\2\2\u02d8\u02d7")
        buf.write("\3\2\2\2\u02d9\u02da\3\2\2\2\u02da\u02db\5l\67\2\u02db")
        buf.write("\u02dc\7\13\2\2\u02dc\u02dd\5l\67\2\u02ddk\3\2\2\2\u02de")
        buf.write("\u02e1\7\16\2\2\u02df\u02e2\5h\65\2\u02e0\u02e2\5j\66")
        buf.write("\2\u02e1\u02df\3\2\2\2\u02e1\u02e0\3\2\2\2\u02e2\u02e3")
        buf.write("\3\2\2\2\u02e3\u02e4\5l\67\2\u02e4\u02e7\3\2\2\2\u02e5")
        buf.write("\u02e7\3\2\2\2\u02e6\u02de\3\2\2\2\u02e6\u02e5\3\2\2\2")
        buf.write("\u02e7m\3\2\2\2\u02e8\u02e9\t\2\2\2\u02e9\u02eb\7\n\2")
        buf.write("\2\u02ea\u02ec\5p9\2\u02eb\u02ea\3\2\2\2\u02eb\u02ec\3")
        buf.write("\2\2\2\u02ec\u02ed\3\2\2\2\u02ed\u02ee\7\13\2\2\u02ee")
        buf.write("o\3\2\2\2\u02ef\u02f0\t\2\2\2\u02f0\u02f1\7\20\2\2\u02f1")
        buf.write("\u02f2\5D#\2\u02f2\u02f3\5r:\2\u02f3q\3\2\2\2\u02f4\u02f5")
        buf.write("\7\16\2\2\u02f5\u02f8\5p9\2\u02f6\u02f8\3\2\2\2\u02f7")
        buf.write("\u02f4\3\2\2\2\u02f7\u02f6\3\2\2\2\u02f8s\3\2\2\2`w~\u008a")
        buf.write("\u008f\u0096\u009c\u00a5\u00ae\u00b5\u00bd\u00c0\u00c7")
        buf.write("\u00cc\u00d1\u00d8\u00de\u00e5\u00ec\u00f6\u00fc\u0103")
        buf.write("\u010b\u010f\u0119\u011f\u0126\u012c\u0133\u0137\u013e")
        buf.write("\u0144\u014c\u0155\u015f\u0165\u0167\u016d\u0171\u0177")
        buf.write("\u017f\u0181\u0188\u018d\u018f\u019a\u01a1\u01a7\u01ac")
        buf.write("\u01b3\u01ba\u01c0\u01c7\u01ca\u01d0\u01d6\u01dc\u01e6")
        buf.write("\u01e9\u01fc\u0204\u020e\u0219\u0224\u022f\u023a\u0240")
        buf.write("\u0245\u024a\u024e\u0253\u025e\u0260\u0265\u026a\u026f")
        buf.write("\u0274\u0279\u0285\u028f\u0294\u029c\u02a4\u02a8\u02ae")
        buf.write("\u02b3\u02b8\u02c0\u02c4\u02d3\u02d8\u02e1\u02e6\u02eb")
        buf.write("\u02f7")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'value'", "'index'", "'_'", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'", "'.'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'='", "':='", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "'nil'", 
                     "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "NL", "LB", "RB", "LC", "RC", "LP", "RP", "COMMA", 
                      "SEMICOLON", "COLON", "DOT", "ADD", "SUBTR", "MUL", 
                      "DIV", "MOD", "EQ", "UNEQ", "LESS", "LESSEQ", "GREATER", 
                      "GREATEREQ", "AND", "OR", "NOT", "INITOP", "ASSIGN", 
                      "ADDASS", "SUBASS", "MULASS", "DIVASS", "MODASS", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "BOOLLIT", "TRUE", "FALSE", "ID", "INTLIT", "FLOATLIT", 
                      "DECIMAL", "HEXADECIMAL", "BINARY", "OCTAL", "STRINGLIT", 
                      "COMMENT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_declare = 2
    RULE_declareTail = 3
    RULE_constDeclare = 4
    RULE_varDeclare = 5
    RULE_modify = 6
    RULE_varType = 7
    RULE_arrayType = 8
    RULE_dimensions = 9
    RULE_init = 10
    RULE_typeDeclare = 11
    RULE_structDeclare = 12
    RULE_field = 13
    RULE_interfaceDeclare = 14
    RULE_method = 15
    RULE_parameters = 16
    RULE_paraTail = 17
    RULE_funcDeclare = 18
    RULE_methodDeclare = 19
    RULE_stmt = 20
    RULE_assignment = 21
    RULE_lhs = 22
    RULE_assignOp = 23
    RULE_ifstmt = 24
    RULE_elsestmt = 25
    RULE_forstmt = 26
    RULE_initFor = 27
    RULE_assignment_for = 28
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
    RULE_methodCallExpr = 47
    RULE_methodCall = 48
    RULE_expr8 = 49
    RULE_arrayInit = 50
    RULE_literal = 51
    RULE_arrayLit = 52
    RULE_literalTail = 53
    RULE_structLit = 54
    RULE_structElement = 55
    RULE_elementTail = 56

    ruleNames =  [ "program", "declarations", "declare", "declareTail", 
                   "constDeclare", "varDeclare", "modify", "varType", "arrayType", 
                   "dimensions", "init", "typeDeclare", "structDeclare", 
                   "field", "interfaceDeclare", "method", "parameters", 
                   "paraTail", "funcDeclare", "methodDeclare", "stmt", "assignment", 
                   "lhs", "assignOp", "ifstmt", "elsestmt", "forstmt", "initFor", 
                   "assignment_for", "rangeFor", "breakstmt", "contstmt", 
                   "returnstmt", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "arrayElement", "index", "structField", 
                   "expr7", "funcCall", "arguments", "argTail", "methodCallExpr", 
                   "methodCall", "expr8", "arrayInit", "literal", "arrayLit", 
                   "literalTail", "structLit", "structElement", "elementTail" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4
    NL=5
    LB=6
    RB=7
    LC=8
    RC=9
    LP=10
    RP=11
    COMMA=12
    SEMICOLON=13
    COLON=14
    DOT=15
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
    INITOP=30
    ASSIGN=31
    ADDASS=32
    SUBASS=33
    MULASS=34
    DIVASS=35
    MODASS=36
    IF=37
    ELSE=38
    FOR=39
    RETURN=40
    FUNC=41
    TYPE=42
    STRUCT=43
    INTERFACE=44
    STRING=45
    INT=46
    FLOAT=47
    BOOLEAN=48
    CONST=49
    VAR=50
    CONTINUE=51
    BREAK=52
    RANGE=53
    NIL=54
    BOOLLIT=55
    TRUE=56
    FALSE=57
    ID=58
    INTLIT=59
    FLOATLIT=60
    DECIMAL=61
    HEXADECIMAL=62
    BINARY=63
    OCTAL=64
    STRINGLIT=65
    COMMENT=66
    ILLEGAL_ESCAPE=67
    UNCLOSE_STRING=68
    ERROR_CHAR=69

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
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 114
                self.match(MiniGoParser.NL)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.declarations()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 121
                self.match(MiniGoParser.NL)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
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
            self.state = 129
            self.declare()
            self.state = 130
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
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.constDeclare()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.varDeclare()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.typeDeclare()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
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
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 138
                    self.match(MiniGoParser.NL)
                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 144
                self.declare()
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 145
                        self.match(MiniGoParser.NL) 
                    self.state = 150
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 151
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

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MiniGoParser.CONST)
            self.state = 157
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 158
            self.init()
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 159
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 2:
                self.state = 160
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.state = 161
                self.match(MiniGoParser.SEMICOLON)
                self.state = 162
                self.match(MiniGoParser.NL)
                pass


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

        def modify(self):
            return self.getTypedRuleContext(MiniGoParser.ModifyContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
            self.state = 165
            self.match(MiniGoParser.VAR)
            self.state = 166
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 167
            self.modify()
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 168
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 2:
                self.state = 169
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.state = 170
                self.match(MiniGoParser.SEMICOLON)
                self.state = 171
                self.match(MiniGoParser.NL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_modify

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModify" ):
                return visitor.visitModify(self)
            else:
                return visitor.visitChildren(self)




    def modify(self):

        localctx = MiniGoParser.ModifyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_modify)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LP]:
                    self.state = 174
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 175
                    self.varType()
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 176
                    self.match(MiniGoParser.ID)
                    pass
                elif token in [MiniGoParser.T__0]:
                    self.state = 177
                    self.match(MiniGoParser.T__0)
                    pass
                elif token in [MiniGoParser.T__1]:
                    self.state = 178
                    self.match(MiniGoParser.T__1)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LP]:
                    self.state = 182
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 183
                    self.varType()
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 184
                    self.match(MiniGoParser.ID)
                    pass
                elif token in [MiniGoParser.T__0]:
                    self.state = 185
                    self.match(MiniGoParser.T__0)
                    pass
                elif token in [MiniGoParser.T__1]:
                    self.state = 186
                    self.match(MiniGoParser.T__1)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 189
                self.init()
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
        self.enterRule(localctx, 14, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
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


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 194
                self.dimensions()
                self.state = 197 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LP):
                    break

            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 199
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 200
                self.match(MiniGoParser.STRUCT)
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__1, MiniGoParser.ID]:
                self.state = 201
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self.enterRule(localctx, 18, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.LP)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTLIT]:
                self.state = 205
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__1, MiniGoParser.ID]:
                self.state = 206
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 209
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

        def INITOP(self):
            return self.getToken(MiniGoParser.INITOP, 0)

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
        self.enterRule(localctx, 20, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(MiniGoParser.INITOP)
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 212
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 213
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
        self.enterRule(localctx, 22, self.RULE_typeDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MiniGoParser.TYPE)
            self.state = 217
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 218
                self.structDeclare()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 219
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

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
        self.enterRule(localctx, 24, self.RULE_structDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.STRUCT)
            self.state = 223
            self.match(MiniGoParser.LC)
            self.state = 225 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 224
                self.field()
                self.state = 227 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 229
            self.match(MiniGoParser.RC)
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 230
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.state = 231
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 3:
                self.state = 232
                self.match(MiniGoParser.SEMICOLON)
                self.state = 233
                self.match(MiniGoParser.NL)
                pass


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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 237
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 238
                self.structDeclare()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 239
                self.arrayType()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 240
                self.interfaceDeclare()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 241
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.T__0]:
                self.state = 242
                self.match(MiniGoParser.T__0)
                pass
            elif token in [MiniGoParser.T__1]:
                self.state = 243
                self.match(MiniGoParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 246
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.state = 247
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 3:
                self.state = 248
                self.match(MiniGoParser.SEMICOLON)
                self.state = 249
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
        self.enterRule(localctx, 28, self.RULE_interfaceDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(MiniGoParser.INTERFACE)
            self.state = 253
            self.match(MiniGoParser.LC)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 254
                self.match(MiniGoParser.NL)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 267 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 260
                self.method()
                self.state = 265
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 261
                    self.match(MiniGoParser.SEMICOLON)
                    pass

                elif la_ == 2:
                    self.state = 262
                    self.match(MiniGoParser.NL)
                    pass

                elif la_ == 3:
                    self.state = 263
                    self.match(MiniGoParser.SEMICOLON)
                    self.state = 264
                    self.match(MiniGoParser.NL)
                    pass


                self.state = 269 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 271
            self.match(MiniGoParser.RC)
            self.state = 272
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

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def parameters(self):
            return self.getTypedRuleContext(MiniGoParser.ParametersContext,0)


        def paraTail(self):
            return self.getTypedRuleContext(MiniGoParser.ParaTailContext,0)


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
        self.enterRule(localctx, 30, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 275
            self.match(MiniGoParser.LB)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0):
                self.state = 276
                self.parameters()
                self.state = 277
                self.paraTail()


            self.state = 281
            self.match(MiniGoParser.RB)
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 282
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 283
                self.arrayType()
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__1, MiniGoParser.ID]:
                self.state = 284
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [MiniGoParser.NL, MiniGoParser.LC, MiniGoParser.SEMICOLON]:
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = MiniGoParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 288
                self.match(MiniGoParser.COMMA)
                self.state = 289
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 295
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 296
                self.arrayType()
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__1, MiniGoParser.ID]:
                self.state = 297
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self.enterRule(localctx, 34, self.RULE_paraTail)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(MiniGoParser.COMMA)
                self.state = 301
                self.parameters()
                self.state = 302
                self.paraTail()
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

        def methodDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclareContext,0)


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


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclare" ):
                return visitor.visitFuncDeclare(self)
            else:
                return visitor.visitChildren(self)




    def funcDeclare(self):

        localctx = MiniGoParser.FuncDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(MiniGoParser.FUNC)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LB:
                self.state = 308
                self.methodDeclare()


            self.state = 311
            self.method()
            self.state = 312
            self.match(MiniGoParser.LC)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 313
                self.match(MiniGoParser.NL)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 319
                self.stmt()
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 325
            self.match(MiniGoParser.RC)
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 326
                self.match(MiniGoParser.NL)

            elif la_ == 2:
                self.state = 327
                self.match(MiniGoParser.SEMICOLON)

            elif la_ == 3:
                self.state = 328
                self.match(MiniGoParser.SEMICOLON)
                self.state = 329
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

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclare" ):
                return visitor.visitMethodDeclare(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclare(self):

        localctx = MiniGoParser.MethodDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_methodDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(MiniGoParser.LB)
            self.state = 333
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 334
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 335
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
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.VAR]:
                    self.state = 337
                    self.varDeclare()
                    pass
                elif token in [MiniGoParser.CONST]:
                    self.state = 338
                    self.constDeclare()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__1, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 341
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 342
                    self.ifstmt()
                    pass

                elif la_ == 3:
                    self.state = 343
                    self.forstmt()
                    pass

                elif la_ == 4:
                    self.state = 344
                    self.breakstmt()
                    pass

                elif la_ == 5:
                    self.state = 345
                    self.contstmt()
                    pass

                elif la_ == 6:
                    self.state = 346
                    self.funcCall()
                    pass

                elif la_ == 7:
                    self.state = 347
                    self.methodCall()
                    pass

                elif la_ == 8:
                    self.state = 348
                    self.returnstmt()
                    pass


                self.state = 355
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 351
                    self.match(MiniGoParser.NL)
                    pass

                elif la_ == 2:
                    self.state = 352
                    self.match(MiniGoParser.SEMICOLON)
                    pass

                elif la_ == 3:
                    self.state = 353
                    self.match(MiniGoParser.SEMICOLON)
                    self.state = 354
                    self.match(MiniGoParser.NL)
                    pass


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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


        def assignOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignOpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignOpContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.lhs()
            self.state = 361 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 360
                self.assignOp()
                self.state = 363 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADDASS) | (1 << MiniGoParser.SUBASS) | (1 << MiniGoParser.MULASS) | (1 << MiniGoParser.DIVASS) | (1 << MiniGoParser.MODASS))) != 0)):
                    break

            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 365
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 366
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.LP:
                    self.state = 370
                    self.index()
                    self.state = 375
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 376
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass

                elif la_ == 2:
                    self.state = 377
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 379 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 378
                        self.index()
                        self.state = 381 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==MiniGoParser.LP):
                            break

                    pass


                self.state = 393 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 385
                    self.match(MiniGoParser.DOT)

                    self.state = 386
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 390
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MiniGoParser.LP:
                        self.state = 387
                        self.index()
                        self.state = 392
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 395 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.DOT):
                        break

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
        self.enterRule(localctx, 46, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADDASS) | (1 << MiniGoParser.SUBASS) | (1 << MiniGoParser.MULASS) | (1 << MiniGoParser.DIVASS) | (1 << MiniGoParser.MODASS))) != 0)):
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
        self.enterRule(localctx, 48, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MiniGoParser.IF)
            self.state = 402
            self.match(MiniGoParser.LB)
            self.state = 403
            self.expr(0)
            self.state = 404
            self.match(MiniGoParser.RB)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 405
                self.match(MiniGoParser.NL)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 411
            self.match(MiniGoParser.LC)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 412
                self.match(MiniGoParser.NL)
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 418
                self.stmt()
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 424
            self.match(MiniGoParser.RC)
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 425
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
        self.enterRule(localctx, 50, self.RULE_elsestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(MiniGoParser.ELSE)
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF]:
                self.state = 429
                self.ifstmt()
                pass
            elif token in [MiniGoParser.NL, MiniGoParser.LC]:
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 430
                    self.match(MiniGoParser.NL)
                    self.state = 435
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 436
                self.match(MiniGoParser.LC)
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 437
                    self.match(MiniGoParser.NL)
                    self.state = 442
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 443
                    self.stmt()
                    self.state = 448
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 449
                self.match(MiniGoParser.RC)
                self.state = 453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 450
                        self.match(MiniGoParser.NL) 
                    self.state = 455
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        self.enterRule(localctx, 52, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MiniGoParser.FOR)
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 459
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 460
                self.initFor()
                pass

            elif la_ == 3:
                self.state = 461
                self.rangeFor()
                pass


            self.state = 464
            self.match(MiniGoParser.LC)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 465
                self.match(MiniGoParser.NL)
                self.state = 470
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 471
                self.stmt()
                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 477
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assignment_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_forContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_forContext,i)


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

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
        self.enterRule(localctx, 54, self.RULE_initFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 479
                self.assignment_for()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 480
                self.match(MiniGoParser.VAR)
                self.state = 481
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 484
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 482
                    self.varType()
                    pass
                elif token in [MiniGoParser.LP]:
                    self.state = 483
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.INITOP]:
                    pass
                else:
                    pass
                self.state = 486
                self.init()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 489
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 490
            self.expr(0)
            self.state = 491
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 492
            self.assignment_for()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignOp(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOpContext,0)


        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_for" ):
                return visitor.visitAssignment_for(self)
            else:
                return visitor.visitChildren(self)




    def assignment_for(self):

        localctx = MiniGoParser.Assignment_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignment_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(MiniGoParser.ID)
            self.state = 495
            self.assignOp()
            self.state = 496
            self.literal()
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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
            self.state = 498
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__1 or _la==MiniGoParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 499
            self.match(MiniGoParser.COMMA)
            self.state = 500
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 501
            self.match(MiniGoParser.ASSIGN)
            self.state = 502
            self.match(MiniGoParser.RANGE)
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 503
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.state = 504
                self.literal()
                pass

            elif la_ == 3:
                self.state = 505
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
            self.state = 508
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
            self.state = 510
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
            self.state = 512
            self.match(MiniGoParser.RETURN)
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY))) != 0) or _la==MiniGoParser.OCTAL or _la==MiniGoParser.STRINGLIT:
                self.state = 513
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
            self.state = 517
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 524
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 519
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 520
                    self.match(MiniGoParser.OR)
                    self.state = 521
                    self.expr1(0) 
                self.state = 526
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

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
            self.state = 528
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 535
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 530
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 531
                    self.match(MiniGoParser.AND)
                    self.state = 532
                    self.expr2(0) 
                self.state = 537
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

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
            self.state = 539
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 546
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 541
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 542
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.UNEQ) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESSEQ) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATEREQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 543
                    self.expr3(0) 
                self.state = 548
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

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
            self.state = 550
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 557
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 552
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 553
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUBTR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 554
                    self.expr4(0) 
                self.state = 559
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)

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
            self.state = 561
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 568
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 563
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 564
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 565
                    self.expr5() 
                self.state = 570
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT:
                    self.state = 571
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 576
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 577
                self.expr6()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
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


        def methodCallExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallExprContext,0)


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
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.arrayElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.methodCallExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 583
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

        def expr8(self):
            return self.getTypedRuleContext(MiniGoParser.Expr8Context,0)


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
            self.state = 588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.state = 586
                self.expr8()
                pass

            elif la_ == 2:
                self.state = 587
                self.funcCall()
                pass


            self.state = 591 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 590
                    self.index()

                else:
                    raise NoViableAltException(self)
                self.state = 593 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

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
            self.state = 595
            self.match(MiniGoParser.LP)
            self.state = 596
            self.expr(0)
            self.state = 597
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

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def funcCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncCallContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncCallContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.state = 599
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.state = 600
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 602 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 601
                    self.index()
                    self.state = 604 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LP):
                        break

                pass


            self.state = 619 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 608
                    self.match(MiniGoParser.DOT)

                    self.state = 611
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
                    if la_ == 1:
                        self.state = 609
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 610
                        self.funcCall()
                        pass


                    self.state = 616
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 613
                            self.index() 
                        self.state = 618
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,73,self._ctx)


                else:
                    raise NoViableAltException(self)
                self.state = 621 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

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

        def structField(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


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
            self.state = 626
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 623
                self.structField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 624
                self.funcCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 625
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

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
            self.state = 628
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 629
            self.match(MiniGoParser.LB)
            self.state = 631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY))) != 0) or _la==MiniGoParser.OCTAL or _la==MiniGoParser.STRINGLIT:
                self.state = 630
                self.arguments()


            self.state = 633
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
            self.state = 635
            self.expr(0)
            self.state = 636
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
            self.state = 643
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 638
                self.match(MiniGoParser.COMMA)
                self.state = 639
                self.expr(0)
                self.state = 640
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


    class MethodCallExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def funcCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncCallContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncCallContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def methodCallExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallExprContext,0)


        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCallExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallExpr" ):
                return visitor.visitMethodCallExpr(self)
            else:
                return visitor.visitChildren(self)




    def methodCallExpr(self):

        localctx = MiniGoParser.MethodCallExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_methodCallExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.state = 645
                self.funcCall()
                pass

            elif la_ == 2:
                self.state = 646
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.state = 647
                self.match(MiniGoParser.T__0)
                pass

            elif la_ == 4:
                self.state = 648
                self.match(MiniGoParser.T__1)
                pass

            elif la_ == 5:
                self.state = 653
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ID]:
                    self.state = 649
                    self.match(MiniGoParser.ID)
                    pass
                elif token in [MiniGoParser.T__0]:
                    self.state = 650
                    self.match(MiniGoParser.T__0)
                    pass
                elif token in [MiniGoParser.T__1]:
                    self.state = 651
                    self.match(MiniGoParser.T__1)
                    pass
                elif token in [MiniGoParser.LP]:
                    self.state = 652
                    self.arrayInit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 656 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 655
                    self.index()
                    self.state = 658 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LP):
                        break

                pass

            elif la_ == 6:
                self.state = 660
                self.structLit()
                pass

            elif la_ == 7:
                self.state = 661
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 8:
                self.state = 662
                self.match(MiniGoParser.LB)
                self.state = 663
                self.expr(0)
                self.state = 664
                self.match(MiniGoParser.RB)
                pass


            self.state = 668
            self.match(MiniGoParser.DOT)
            self.state = 678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.state = 669
                self.funcCall()
                pass

            elif la_ == 2:
                self.state = 670
                self.match(MiniGoParser.ID)
                self.state = 674
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 671
                        self.index() 
                    self.state = 676
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

                pass

            elif la_ == 3:
                self.state = 677
                self.methodCallExpr()
                pass


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

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = MiniGoParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 680
                self.match(MiniGoParser.ID)
                self.state = 684
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.LP:
                    self.state = 681
                    self.index()
                    self.state = 686
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [MiniGoParser.T__0]:
                self.state = 687
                self.match(MiniGoParser.T__0)
                pass
            elif token in [MiniGoParser.T__1]:
                self.state = 688
                self.match(MiniGoParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 691
            self.match(MiniGoParser.DOT)
            self.state = 692
            self.expr(0)
            self.state = 694
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.state = 693
                self.match(MiniGoParser.SEMICOLON)


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


        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = MiniGoParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr8)
        try:
            self.state = 702
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 696
                self.match(MiniGoParser.LB)
                self.state = 697
                self.expr(0)
                self.state = 698
                self.match(MiniGoParser.RB)
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__1, MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 700
                self.literal()
                pass
            elif token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 701
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
        self.enterRule(localctx, 100, self.RULE_arrayInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 704
            self.arrayType()
            self.state = 706
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.state = 705
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

        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_literal)
        try:
            self.state = 721
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 708
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 709
                self.match(MiniGoParser.DECIMAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 710
                self.match(MiniGoParser.BINARY)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 711
                self.match(MiniGoParser.OCTAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 712
                self.match(MiniGoParser.HEXADECIMAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 713
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 714
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 715
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 716
                self.structLit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 717
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 718
                self.match(MiniGoParser.T__0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 719
                self.match(MiniGoParser.T__1)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 720
                self.match(MiniGoParser.NIL)
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

        def literalTail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LiteralTailContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LiteralTailContext,i)


        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 723
            self.match(MiniGoParser.LC)
            self.state = 726
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__0, MiniGoParser.T__1, MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                self.state = 724
                self.literal()
                pass
            elif token in [MiniGoParser.LC]:
                self.state = 725
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 728
            self.literalTail()
            self.state = 729
            self.match(MiniGoParser.RC)
            self.state = 730
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

        def literalTail(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralTailContext,0)


        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literalTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralTail" ):
                return visitor.visitLiteralTail(self)
            else:
                return visitor.visitChildren(self)




    def literalTail(self):

        localctx = MiniGoParser.LiteralTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_literalTail)
        try:
            self.state = 740
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 732
                self.match(MiniGoParser.COMMA)
                self.state = 735
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.T__0, MiniGoParser.T__1, MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                    self.state = 733
                    self.literal()
                    pass
                elif token in [MiniGoParser.LC]:
                    self.state = 734
                    self.arrayLit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 737
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

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
        self.enterRule(localctx, 108, self.RULE_structLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 743
            self.match(MiniGoParser.LC)
            self.state = 745
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0):
                self.state = 744
                self.structElement()


            self.state = 747
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

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def elementTail(self):
            return self.getTypedRuleContext(MiniGoParser.ElementTailContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructElement" ):
                return visitor.visitStructElement(self)
            else:
                return visitor.visitChildren(self)




    def structElement(self):

        localctx = MiniGoParser.StructElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_structElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 749
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 750
            self.match(MiniGoParser.COLON)
            self.state = 751
            self.expr(0)
            self.state = 752
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
        self.enterRule(localctx, 112, self.RULE_elementTail)
        try:
            self.state = 757
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 754
                self.match(MiniGoParser.COMMA)
                self.state = 755
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
         




