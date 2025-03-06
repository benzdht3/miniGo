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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u033e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\7\2\u0096\n")
        buf.write("\2\f\2\16\2\u0099\13\2\3\2\3\2\7\2\u009d\n\2\f\2\16\2")
        buf.write("\u00a0\13\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u00ab")
        buf.write("\n\4\3\5\7\5\u00ae\n\5\f\5\16\5\u00b1\13\5\3\5\3\5\7\5")
        buf.write("\u00b5\n\5\f\5\16\5\u00b8\13\5\3\5\3\5\3\5\5\5\u00bd\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\5\b\u00cc\n\b\3\b\3\b\3\b\3\b\5\b\u00d2\n\b\3\b\3\b\5")
        buf.write("\b\u00d6\n\b\3\t\3\t\3\n\6\n\u00db\n\n\r\n\16\n\u00dc")
        buf.write("\3\n\3\n\3\n\5\n\u00e2\n\n\3\13\3\13\3\13\5\13\u00e7\n")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\5\f\u00ee\n\f\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u00f4\n\r\3\16\3\16\3\16\6\16\u00f9\n\16\r\16\16")
        buf.write("\16\u00fa\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u0106\n\17\3\17\3\17\3\20\3\20\3\20\7\20\u010d\n")
        buf.write("\20\f\20\16\20\u0110\13\20\3\20\6\20\u0113\n\20\r\20\16")
        buf.write("\20\u0114\3\20\6\20\u0118\n\20\r\20\16\20\u0119\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u0124\n\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u012a\n\21\3\21\7\21\u012d\n\21\f")
        buf.write("\21\16\21\u0130\13\21\3\22\3\22\3\22\7\22\u0135\n\22\f")
        buf.write("\22\16\22\u0138\13\22\3\22\3\22\5\22\u013c\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u0143\n\23\3\24\3\24\5\24\u0147")
        buf.write("\n\24\3\24\3\24\3\24\7\24\u014c\n\24\f\24\16\24\u014f")
        buf.write("\13\24\3\24\7\24\u0152\n\24\f\24\16\24\u0155\13\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u015f\n\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u0165\n\25\3\25\7\25\u0168\n\25")
        buf.write("\f\25\16\25\u016b\13\25\3\26\3\26\3\26\7\26\u0170\n\26")
        buf.write("\f\26\16\26\u0173\13\26\3\26\3\26\3\26\5\26\u0178\n\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u017f\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\5\31\u0188\n\31\3\31\3\31\3\31")
        buf.write("\5\31\u018d\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\5\32\u0197\n\32\3\33\3\33\3\33\3\33\5\33\u019d\n\33")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u01a3\n\34\3\35\3\35\6\35\u01a7")
        buf.write("\n\35\r\35\16\35\u01a8\3\36\3\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\7\37\u01b2\n\37\f\37\16\37\u01b5\13\37\3\37\3\37\7")
        buf.write("\37\u01b9\n\37\f\37\16\37\u01bc\13\37\3\37\7\37\u01bf")
        buf.write("\n\37\f\37\16\37\u01c2\13\37\3\37\3\37\5\37\u01c6\n\37")
        buf.write("\3 \3 \3 \7 \u01cb\n \f \16 \u01ce\13 \3 \3 \7 \u01d2")
        buf.write("\n \f \16 \u01d5\13 \3 \7 \u01d8\n \f \16 \u01db\13 \3")
        buf.write(" \3 \7 \u01df\n \f \16 \u01e2\13 \5 \u01e4\n \3!\3!\3")
        buf.write("!\3!\5!\u01ea\n!\3!\3!\7!\u01ee\n!\f!\16!\u01f1\13!\3")
        buf.write("!\7!\u01f4\n!\f!\16!\u01f7\13!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\5\"\u0200\n\"\3\"\3\"\5\"\u0204\n\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0217\n$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\5\'\u021f\n\'\3(\3(\3(\3(\3(\3(\7(")
        buf.write("\u0227\n(\f(\16(\u022a\13(\3)\3)\3)\3)\3)\3)\7)\u0232")
        buf.write("\n)\f)\16)\u0235\13)\3*\3*\3*\3*\3*\3*\7*\u023d\n*\f*")
        buf.write("\16*\u0240\13*\3+\3+\3+\3+\3+\3+\7+\u0248\n+\f+\16+\u024b")
        buf.write("\13+\3,\3,\3,\3,\3,\3,\7,\u0253\n,\f,\16,\u0256\13,\3")
        buf.write("-\7-\u0259\n-\f-\16-\u025c\13-\3-\3-\5-\u0260\n-\3.\3")
        buf.write(".\3.\5.\u0265\n.\3/\3/\5/\u0269\n/\3/\6/\u026c\n/\r/\16")
        buf.write("/\u026d\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\7\61\u0278")
        buf.write("\n\61\f\61\16\61\u027b\13\61\3\61\3\61\3\61\5\61\u0280")
        buf.write("\n\61\6\61\u0282\n\61\r\61\16\61\u0283\3\61\7\61\u0287")
        buf.write("\n\61\f\61\16\61\u028a\13\61\5\61\u028c\n\61\3\61\3\61")
        buf.write("\5\61\u0290\n\61\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u02a2")
        buf.write("\n\65\3\66\3\66\3\66\5\66\u02a7\n\66\3\67\3\67\6\67\u02ab")
        buf.write("\n\67\r\67\16\67\u02ac\38\38\38\58\u02b2\n8\38\38\39\3")
        buf.write("9\39\59\u02b9\n9\39\39\3:\3:\3:\3;\3;\3;\3;\3;\5;\u02c5")
        buf.write("\n;\3<\3<\3<\3<\3<\6<\u02cc\n<\r<\16<\u02cd\3<\3<\3<\3")
        buf.write("<\3<\5<\u02d5\n<\3<\3<\3<\5<\u02da\n<\3=\3=\3=\5=\u02df")
        buf.write("\n=\3=\3=\3>\3>\3>\5>\u02e6\n>\3>\3>\3>\5>\u02eb\n>\3")
        buf.write("?\3?\3?\3?\3?\3?\5?\u02f3\n?\3@\3@\5@\u02f7\n@\3A\6A\u02fa")
        buf.write("\nA\rA\16A\u02fb\3A\3A\5A\u0300\nA\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\5B\u030d\nB\3C\3C\3D\3D\3D\5D\u0314\nD\3")
        buf.write("D\3D\3D\3E\3E\3E\5E\u031c\nE\3E\3E\3E\5E\u0321\nE\3F\3")
        buf.write("F\3F\5F\u0326\nF\3F\3F\3G\3G\3G\3G\3G\3H\3H\3H\3H\3H\5")
        buf.write("H\u0334\nH\3I\3I\3J\3J\3J\3J\5J\u033c\nJ\3J\2\7NPRTVK")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\2\b\3")
        buf.write("\2,/\3\2\36#\3\2\24\31\3\2\17\20\3\2\21\23\4\2\20\20\34")
        buf.write("\34\2\u037e\2\u0097\3\2\2\2\4\u00a3\3\2\2\2\6\u00aa\3")
        buf.write("\2\2\2\b\u00bc\3\2\2\2\n\u00be\3\2\2\2\f\u00c3\3\2\2\2")
        buf.write("\16\u00d5\3\2\2\2\20\u00d7\3\2\2\2\22\u00da\3\2\2\2\24")
        buf.write("\u00e3\3\2\2\2\26\u00ea\3\2\2\2\30\u00ef\3\2\2\2\32\u00f5")
        buf.write("\3\2\2\2\34\u00ff\3\2\2\2\36\u0109\3\2\2\2 \u011e\3\2")
        buf.write("\2\2\"\u0131\3\2\2\2$\u0142\3\2\2\2&\u0144\3\2\2\2(\u0159")
        buf.write("\3\2\2\2*\u016c\3\2\2\2,\u017e\3\2\2\2.\u0180\3\2\2\2")
        buf.write("\60\u018c\3\2\2\2\62\u0196\3\2\2\2\64\u0198\3\2\2\2\66")
        buf.write("\u01a2\3\2\2\28\u01a4\3\2\2\2:\u01aa\3\2\2\2<\u01ac\3")
        buf.write("\2\2\2>\u01c7\3\2\2\2@\u01e5\3\2\2\2B\u0203\3\2\2\2D\u020a")
        buf.write("\3\2\2\2F\u020e\3\2\2\2H\u0218\3\2\2\2J\u021a\3\2\2\2")
        buf.write("L\u021c\3\2\2\2N\u0220\3\2\2\2P\u022b\3\2\2\2R\u0236\3")
        buf.write("\2\2\2T\u0241\3\2\2\2V\u024c\3\2\2\2X\u025f\3\2\2\2Z\u0264")
        buf.write("\3\2\2\2\\\u0268\3\2\2\2^\u026f\3\2\2\2`\u0273\3\2\2\2")
        buf.write("b\u0291\3\2\2\2d\u0293\3\2\2\2f\u0297\3\2\2\2h\u02a1\3")
        buf.write("\2\2\2j\u02a6\3\2\2\2l\u02a8\3\2\2\2n\u02ae\3\2\2\2p\u02b5")
        buf.write("\3\2\2\2r\u02bc\3\2\2\2t\u02c4\3\2\2\2v\u02d9\3\2\2\2")
        buf.write("x\u02db\3\2\2\2z\u02e5\3\2\2\2|\u02f2\3\2\2\2~\u02f4\3")
        buf.write("\2\2\2\u0080\u02f9\3\2\2\2\u0082\u030c\3\2\2\2\u0084\u030e")
        buf.write("\3\2\2\2\u0086\u0310\3\2\2\2\u0088\u0320\3\2\2\2\u008a")
        buf.write("\u0322\3\2\2\2\u008c\u0329\3\2\2\2\u008e\u0333\3\2\2\2")
        buf.write("\u0090\u0335\3\2\2\2\u0092\u033b\3\2\2\2\u0094\u0096\7")
        buf.write("\4\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099")
        buf.write("\u0097\3\2\2\2\u009a\u009e\5\4\3\2\u009b\u009d\7\4\2\2")
        buf.write("\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3")
        buf.write("\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a1\u00a2\7\2\2\3\u00a2\3\3\2\2\2\u00a3\u00a4")
        buf.write("\5\6\4\2\u00a4\u00a5\5\b\5\2\u00a5\5\3\2\2\2\u00a6\u00ab")
        buf.write("\5\n\6\2\u00a7\u00ab\5\f\7\2\u00a8\u00ab\5\30\r\2\u00a9")
        buf.write("\u00ab\5&\24\2\u00aa\u00a6\3\2\2\2\u00aa\u00a7\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\7\3\2\2")
        buf.write("\2\u00ac\u00ae\7\4\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b6\5\6\4\2")
        buf.write("\u00b3\u00b5\7\4\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3")
        buf.write("\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9")
        buf.write("\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ba\5\b\5\2\u00ba")
        buf.write("\u00bd\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00af\3\2\2\2")
        buf.write("\u00bc\u00bb\3\2\2\2\u00bd\t\3\2\2\2\u00be\u00bf\7\60")
        buf.write("\2\2\u00bf\u00c0\5\u0090I\2\u00c0\u00c1\5\26\f\2\u00c1")
        buf.write("\u00c2\5\u0092J\2\u00c2\13\3\2\2\2\u00c3\u00c4\7\61\2")
        buf.write("\2\u00c4\u00c5\5\u0090I\2\u00c5\u00c6\5\16\b\2\u00c6\u00c7")
        buf.write("\5\u0092J\2\u00c7\r\3\2\2\2\u00c8\u00cc\5\22\n\2\u00c9")
        buf.write("\u00cc\5\20\t\2\u00ca\u00cc\5\u0084C\2\u00cb\u00c8\3\2")
        buf.write("\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00d6")
        buf.write("\3\2\2\2\u00cd\u00d6\5\26\f\2\u00ce\u00d2\5\22\n\2\u00cf")
        buf.write("\u00d2\5\20\t\2\u00d0\u00d2\5\u0084C\2\u00d1\u00ce\3\2")
        buf.write("\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00d4\5\26\f\2\u00d4\u00d6\3\2\2\2\u00d5")
        buf.write("\u00cb\3\2\2\2\u00d5\u00cd\3\2\2\2\u00d5\u00d1\3\2\2\2")
        buf.write("\u00d6\17\3\2\2\2\u00d7\u00d8\t\2\2\2\u00d8\21\3\2\2\2")
        buf.write("\u00d9\u00db\5\24\13\2\u00da\u00d9\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd")
        buf.write("\u00e1\3\2\2\2\u00de\u00e2\5\20\t\2\u00df\u00e2\7*\2\2")
        buf.write("\u00e0\u00e2\5\u0084C\2\u00e1\u00de\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2\23\3\2\2\2\u00e3\u00e6")
        buf.write("\7\t\2\2\u00e4\u00e7\7:\2\2\u00e5\u00e7\5\u0084C\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\7\n\2\2\u00e9\25\3\2\2\2\u00ea\u00ed\7\35")
        buf.write("\2\2\u00eb\u00ee\5N(\2\u00ec\u00ee\5~@\2\u00ed\u00eb\3")
        buf.write("\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\27\3\2\2\2\u00ef\u00f0")
        buf.write("\7)\2\2\u00f0\u00f3\5\u0090I\2\u00f1\u00f4\5\32\16\2\u00f2")
        buf.write("\u00f4\5\36\20\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2")
        buf.write("\2\u00f4\31\3\2\2\2\u00f5\u00f6\7*\2\2\u00f6\u00f8\7\7")
        buf.write("\2\2\u00f7\u00f9\5\34\17\2\u00f8\u00f7\3\2\2\2\u00f9\u00fa")
        buf.write("\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fd\7\b\2\2\u00fd\u00fe\5\u0092")
        buf.write("J\2\u00fe\33\3\2\2\2\u00ff\u0105\5\u0090I\2\u0100\u0106")
        buf.write("\5\20\t\2\u0101\u0106\5\32\16\2\u0102\u0106\5\22\n\2\u0103")
        buf.write("\u0106\5\36\20\2\u0104\u0106\5\u0084C\2\u0105\u0100\3")
        buf.write("\2\2\2\u0105\u0101\3\2\2\2\u0105\u0102\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0105\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107")
        buf.write("\u0108\5\u0092J\2\u0108\35\3\2\2\2\u0109\u010a\7+\2\2")
        buf.write("\u010a\u010e\7\7\2\2\u010b\u010d\7\4\2\2\u010c\u010b\3")
        buf.write("\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0111")
        buf.write("\u0113\5 \21\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3")
        buf.write("\2\2\2\u0116\u0118\5\u0092J\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b\u011c\7\b\2\2\u011c\u011d\5")
        buf.write("\u0092J\2\u011d\37\3\2\2\2\u011e\u011f\5\u0090I\2\u011f")
        buf.write("\u0123\7\5\2\2\u0120\u0121\5\"\22\2\u0121\u0122\5$\23")
        buf.write("\2\u0122\u0124\3\2\2\2\u0123\u0120\3\2\2\2\u0123\u0124")
        buf.write("\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0129\7\6\2\2\u0126")
        buf.write("\u012a\5\20\t\2\u0127\u012a\5\22\n\2\u0128\u012a\5\u0084")
        buf.write("C\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u0128")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012e\3\2\2\2\u012b")
        buf.write("\u012d\5\u0092J\2\u012c\u012b\3\2\2\2\u012d\u0130\3\2")
        buf.write("\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f!\3")
        buf.write("\2\2\2\u0130\u012e\3\2\2\2\u0131\u0136\5\u0090I\2\u0132")
        buf.write("\u0133\7\13\2\2\u0133\u0135\5\u0090I\2\u0134\u0132\3\2")
        buf.write("\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u013b\3\2\2\2\u0138\u0136\3\2\2\2\u0139")
        buf.write("\u013c\5\20\t\2\u013a\u013c\5\22\n\2\u013b\u0139\3\2\2")
        buf.write("\2\u013b\u013a\3\2\2\2\u013c#\3\2\2\2\u013d\u013e\7\13")
        buf.write("\2\2\u013e\u013f\5\"\22\2\u013f\u0140\5$\23\2\u0140\u0143")
        buf.write("\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u013d\3\2\2\2\u0142")
        buf.write("\u0141\3\2\2\2\u0143%\3\2\2\2\u0144\u0146\7(\2\2\u0145")
        buf.write("\u0147\5.\30\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148\u0149\5(\25\2\u0149\u014d\7")
        buf.write("\7\2\2\u014a\u014c\7\4\2\2\u014b\u014a\3\2\2\2\u014c\u014f")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("\u0153\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0152\5\60\31")
        buf.write("\2\u0151\u0150\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151")
        buf.write("\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0156\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0156\u0157\7\b\2\2\u0157\u0158\5\u0092")
        buf.write("J\2\u0158\'\3\2\2\2\u0159\u015a\5\u0090I\2\u015a\u015e")
        buf.write("\7\5\2\2\u015b\u015c\5*\26\2\u015c\u015d\5,\27\2\u015d")
        buf.write("\u015f\3\2\2\2\u015e\u015b\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160\u0164\7\6\2\2\u0161\u0165\5")
        buf.write("\20\t\2\u0162\u0165\5\22\n\2\u0163\u0165\5\u0090I\2\u0164")
        buf.write("\u0161\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0169\3\2\2\2\u0166\u0168\5")
        buf.write("\u0092J\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a)\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u0171\5\u0090I\2\u016d\u016e\7\13")
        buf.write("\2\2\u016e\u0170\5\u0090I\2\u016f\u016d\3\2\2\2\u0170")
        buf.write("\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2")
        buf.write("\u0172\u0177\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0178\5")
        buf.write("\20\t\2\u0175\u0178\5\22\n\2\u0176\u0178\5\u0084C\2\u0177")
        buf.write("\u0174\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0176\3\2\2\2")
        buf.write("\u0178+\3\2\2\2\u0179\u017a\7\13\2\2\u017a\u017b\5*\26")
        buf.write("\2\u017b\u017c\5,\27\2\u017c\u017f\3\2\2\2\u017d\u017f")
        buf.write("\3\2\2\2\u017e\u0179\3\2\2\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("-\3\2\2\2\u0180\u0181\7\5\2\2\u0181\u0182\5\u0090I\2\u0182")
        buf.write("\u0183\5\u0090I\2\u0183\u0184\7\6\2\2\u0184/\3\2\2\2\u0185")
        buf.write("\u0188\5\f\7\2\u0186\u0188\5\n\6\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0186\3\2\2\2\u0188\u018d\3\2\2\2\u0189\u018a\5")
        buf.write("\62\32\2\u018a\u018b\5\u0092J\2\u018b\u018d\3\2\2\2\u018c")
        buf.write("\u0187\3\2\2\2\u018c\u0189\3\2\2\2\u018d\61\3\2\2\2\u018e")
        buf.write("\u0197\5\64\33\2\u018f\u0197\5<\37\2\u0190\u0197\5@!\2")
        buf.write("\u0191\u0197\5H%\2\u0192\u0197\5J&\2\u0193\u0197\5n8\2")
        buf.write("\u0194\u0197\5z>\2\u0195\u0197\5L\'\2\u0196\u018e\3\2")
        buf.write("\2\2\u0196\u018f\3\2\2\2\u0196\u0190\3\2\2\2\u0196\u0191")
        buf.write("\3\2\2\2\u0196\u0192\3\2\2\2\u0196\u0193\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197\63\3\2\2\2\u0198")
        buf.write("\u0199\5\66\34\2\u0199\u019c\5:\36\2\u019a\u019d\5N(\2")
        buf.write("\u019b\u019d\5~@\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2")
        buf.write("\2\2\u019d\65\3\2\2\2\u019e\u01a3\5\u0084C\2\u019f\u01a3")
        buf.write("\5\\/\2\u01a0\u01a3\5`\61\2\u01a1\u01a3\5v<\2\u01a2\u019e")
        buf.write("\3\2\2\2\u01a2\u019f\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3\67\3\2\2\2\u01a4\u01a6\5\u0084C\2")
        buf.write("\u01a5\u01a7\5^\60\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3")
        buf.write("\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a99")
        buf.write("\3\2\2\2\u01aa\u01ab\t\3\2\2\u01ab;\3\2\2\2\u01ac\u01ad")
        buf.write("\7$\2\2\u01ad\u01ae\7\5\2\2\u01ae\u01af\5N(\2\u01af\u01b3")
        buf.write("\7\6\2\2\u01b0\u01b2\7\4\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01ba\7")
        buf.write("\7\2\2\u01b7\u01b9\7\4\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc")
        buf.write("\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01c0\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01bf\5\60\31")
        buf.write("\2\u01be\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c3\3\2\2\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c3\u01c5\7\b\2\2\u01c4\u01c6\5> \2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6=\3\2\2\2\u01c7")
        buf.write("\u01e3\7%\2\2\u01c8\u01e4\5<\37\2\u01c9\u01cb\7\4\2\2")
        buf.write("\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01cf\u01d3\7\7\2\2\u01d0\u01d2\7\4\2\2\u01d1")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2")
        buf.write("\u01d3\u01d4\3\2\2\2\u01d4\u01d9\3\2\2\2\u01d5\u01d3\3")
        buf.write("\2\2\2\u01d6\u01d8\5\60\31\2\u01d7\u01d6\3\2\2\2\u01d8")
        buf.write("\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2")
        buf.write("\u01da\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01e0\7")
        buf.write("\b\2\2\u01dd\u01df\7\4\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2")
        buf.write("\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01c8\3\2\2\2")
        buf.write("\u01e3\u01cc\3\2\2\2\u01e4?\3\2\2\2\u01e5\u01e9\7&\2\2")
        buf.write("\u01e6\u01ea\5N(\2\u01e7\u01ea\5B\"\2\u01e8\u01ea\5F$")
        buf.write("\2\u01e9\u01e6\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8")
        buf.write("\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ef\7\7\2\2\u01ec")
        buf.write("\u01ee\7\4\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2")
        buf.write("\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f5\3")
        buf.write("\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f4\5\60\31\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7\u01f5\3")
        buf.write("\2\2\2\u01f8\u01f9\7\b\2\2\u01f9A\3\2\2\2\u01fa\u0204")
        buf.write("\5D#\2\u01fb\u01fc\7\61\2\2\u01fc\u01ff\5\u0090I\2\u01fd")
        buf.write("\u0200\5\20\t\2\u01fe\u0200\5\22\n\2\u01ff\u01fd\3\2\2")
        buf.write("\2\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201")
        buf.write("\3\2\2\2\u0201\u0202\5\26\f\2\u0202\u0204\3\2\2\2\u0203")
        buf.write("\u01fa\3\2\2\2\u0203\u01fb\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0206\5\u0092J\2\u0206\u0207\5N(\2\u0207\u0208")
        buf.write("\5\u0092J\2\u0208\u0209\5D#\2\u0209C\3\2\2\2\u020a\u020b")
        buf.write("\5\u0084C\2\u020b\u020c\5:\36\2\u020c\u020d\5N(\2\u020d")
        buf.write("E\3\2\2\2\u020e\u020f\5\u0084C\2\u020f\u0210\7\13\2\2")
        buf.write("\u0210\u0211\5\u0084C\2\u0211\u0212\7\36\2\2\u0212\u0216")
        buf.write("\7\64\2\2\u0213\u0217\5\u0082B\2\u0214\u0217\5~@\2\u0215")
        buf.write("\u0217\5\\/\2\u0216\u0213\3\2\2\2\u0216\u0214\3\2\2\2")
        buf.write("\u0216\u0215\3\2\2\2\u0217G\3\2\2\2\u0218\u0219\7\63\2")
        buf.write("\2\u0219I\3\2\2\2\u021a\u021b\7\62\2\2\u021bK\3\2\2\2")
        buf.write("\u021c\u021e\7\'\2\2\u021d\u021f\5N(\2\u021e\u021d\3\2")
        buf.write("\2\2\u021e\u021f\3\2\2\2\u021fM\3\2\2\2\u0220\u0221\b")
        buf.write("(\1\2\u0221\u0222\5P)\2\u0222\u0228\3\2\2\2\u0223\u0224")
        buf.write("\f\4\2\2\u0224\u0225\7\33\2\2\u0225\u0227\5P)\2\u0226")
        buf.write("\u0223\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229O\3\2\2\2\u022a\u0228\3\2\2")
        buf.write("\2\u022b\u022c\b)\1\2\u022c\u022d\5R*\2\u022d\u0233\3")
        buf.write("\2\2\2\u022e\u022f\f\4\2\2\u022f\u0230\7\32\2\2\u0230")
        buf.write("\u0232\5R*\2\u0231\u022e\3\2\2\2\u0232\u0235\3\2\2\2\u0233")
        buf.write("\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234Q\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0236\u0237\b*\1\2\u0237\u0238\5T+\2\u0238")
        buf.write("\u023e\3\2\2\2\u0239\u023a\f\4\2\2\u023a\u023b\t\4\2\2")
        buf.write("\u023b\u023d\5T+\2\u023c\u0239\3\2\2\2\u023d\u0240\3\2")
        buf.write("\2\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023fS\3")
        buf.write("\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242\b+\1\2\u0242\u0243")
        buf.write("\5V,\2\u0243\u0249\3\2\2\2\u0244\u0245\f\4\2\2\u0245\u0246")
        buf.write("\t\5\2\2\u0246\u0248\5V,\2\u0247\u0244\3\2\2\2\u0248\u024b")
        buf.write("\3\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a")
        buf.write("U\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024d\b,\1\2\u024d")
        buf.write("\u024e\5X-\2\u024e\u0254\3\2\2\2\u024f\u0250\f\4\2\2\u0250")
        buf.write("\u0251\t\6\2\2\u0251\u0253\5X-\2\u0252\u024f\3\2\2\2\u0253")
        buf.write("\u0256\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2")
        buf.write("\u0255W\3\2\2\2\u0256\u0254\3\2\2\2\u0257\u0259\t\7\2")
        buf.write("\2\u0258\u0257\3\2\2\2\u0259\u025c\3\2\2\2\u025a\u0258")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025d\3\2\2\2\u025c")
        buf.write("\u025a\3\2\2\2\u025d\u0260\5Z.\2\u025e\u0260\5Z.\2\u025f")
        buf.write("\u025a\3\2\2\2\u025f\u025e\3\2\2\2\u0260Y\3\2\2\2\u0261")
        buf.write("\u0265\5\\/\2\u0262\u0265\5v<\2\u0263\u0265\5j\66\2\u0264")
        buf.write("\u0261\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0263\3\2\2\2")
        buf.write("\u0265[\3\2\2\2\u0266\u0269\5|?\2\u0267\u0269\5n8\2\u0268")
        buf.write("\u0266\3\2\2\2\u0268\u0267\3\2\2\2\u0269\u026b\3\2\2\2")
        buf.write("\u026a\u026c\5^\60\2\u026b\u026a\3\2\2\2\u026c\u026d\3")
        buf.write("\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e]")
        buf.write("\3\2\2\2\u026f\u0270\7\t\2\2\u0270\u0271\5N(\2\u0271\u0272")
        buf.write("\7\n\2\2\u0272_\3\2\2\2\u0273\u0274\5h\65\2\u0274\u0275")
        buf.write("\7\16\2\2\u0275\u0279\5f\64\2\u0276\u0278\5^\60\2\u0277")
        buf.write("\u0276\3\2\2\2\u0278\u027b\3\2\2\2\u0279\u0277\3\2\2\2")
        buf.write("\u0279\u027a\3\2\2\2\u027a\u028b\3\2\2\2\u027b\u0279\3")
        buf.write("\2\2\2\u027c\u027f\7\16\2\2\u027d\u0280\5f\64\2\u027e")
        buf.write("\u0280\5x=\2\u027f\u027d\3\2\2\2\u027f\u027e\3\2\2\2\u0280")
        buf.write("\u0282\3\2\2\2\u0281\u027c\3\2\2\2\u0282\u0283\3\2\2\2")
        buf.write("\u0283\u0281\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0288\3")
        buf.write("\2\2\2\u0285\u0287\5d\63\2\u0286\u0285\3\2\2\2\u0287\u028a")
        buf.write("\3\2\2\2\u0288\u0286\3\2\2\2\u0288\u0289\3\2\2\2\u0289")
        buf.write("\u028c\3\2\2\2\u028a\u0288\3\2\2\2\u028b\u0281\3\2\2\2")
        buf.write("\u028b\u028c\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028e\7")
        buf.write("\16\2\2\u028e\u0290\5b\62\2\u028f\u028d\3\2\2\2\u028f")
        buf.write("\u0290\3\2\2\2\u0290a\3\2\2\2\u0291\u0292\5\u0090I\2\u0292")
        buf.write("c\3\2\2\2\u0293\u0294\7\t\2\2\u0294\u0295\5N(\2\u0295")
        buf.write("\u0296\7\n\2\2\u0296e\3\2\2\2\u0297\u0298\5\u0090I\2\u0298")
        buf.write("g\3\2\2\2\u0299\u02a2\5\u0084C\2\u029a\u02a2\5\\/\2\u029b")
        buf.write("\u02a2\5\u008aF\2\u029c\u029d\7\5\2\2\u029d\u029e\5N(")
        buf.write("\2\u029e\u029f\7\6\2\2\u029f\u02a2\3\2\2\2\u02a0\u02a2")
        buf.write("\7\66\2\2\u02a1\u0299\3\2\2\2\u02a1\u029a\3\2\2\2\u02a1")
        buf.write("\u029b\3\2\2\2\u02a1\u029c\3\2\2\2\u02a1\u02a0\3\2\2\2")
        buf.write("\u02a2i\3\2\2\2\u02a3\u02a7\5`\61\2\u02a4\u02a7\5n8\2")
        buf.write("\u02a5\u02a7\5|?\2\u02a6\u02a3\3\2\2\2\u02a6\u02a4\3\2")
        buf.write("\2\2\u02a6\u02a5\3\2\2\2\u02a7k\3\2\2\2\u02a8\u02aa\5")
        buf.write("v<\2\u02a9\u02ab\5^\60\2\u02aa\u02a9\3\2\2\2\u02ab\u02ac")
        buf.write("\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad")
        buf.write("m\3\2\2\2\u02ae\u02af\5\u0090I\2\u02af\u02b1\7\5\2\2\u02b0")
        buf.write("\u02b2\5r:\2\u02b1\u02b0\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2")
        buf.write("\u02b3\3\2\2\2\u02b3\u02b4\7\6\2\2\u02b4o\3\2\2\2\u02b5")
        buf.write("\u02b6\5\u0090I\2\u02b6\u02b8\7\5\2\2\u02b7\u02b9\5r:")
        buf.write("\2\u02b8\u02b7\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02ba")
        buf.write("\3\2\2\2\u02ba\u02bb\7\6\2\2\u02bbq\3\2\2\2\u02bc\u02bd")
        buf.write("\5N(\2\u02bd\u02be\5t;\2\u02bes\3\2\2\2\u02bf\u02c0\7")
        buf.write("\13\2\2\u02c0\u02c1\5N(\2\u02c1\u02c2\5t;\2\u02c2\u02c5")
        buf.write("\3\2\2\2\u02c3\u02c5\3\2\2\2\u02c4\u02bf\3\2\2\2\u02c4")
        buf.write("\u02c3\3\2\2\2\u02c5u\3\2\2\2\u02c6\u02c7\5\u0084C\2\u02c7")
        buf.write("\u02cb\7\16\2\2\u02c8\u02c9\5x=\2\u02c9\u02ca\7\16\2\2")
        buf.write("\u02ca\u02cc\3\2\2\2\u02cb\u02c8\3\2\2\2\u02cc\u02cd\3")
        buf.write("\2\2\2\u02cd\u02cb\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u02cf")
        buf.write("\3\2\2\2\u02cf\u02d0\5x=\2\u02d0\u02da\3\2\2\2\u02d1\u02d5")
        buf.write("\5\u0084C\2\u02d2\u02d5\5`\61\2\u02d3\u02d5\5n8\2\u02d4")
        buf.write("\u02d1\3\2\2\2\u02d4\u02d2\3\2\2\2\u02d4\u02d3\3\2\2\2")
        buf.write("\u02d5\u02d6\3\2\2\2\u02d6\u02d7\7\16\2\2\u02d7\u02d8")
        buf.write("\5x=\2\u02d8\u02da\3\2\2\2\u02d9\u02c6\3\2\2\2\u02d9\u02d4")
        buf.write("\3\2\2\2\u02daw\3\2\2\2\u02db\u02dc\5\u0090I\2\u02dc\u02de")
        buf.write("\7\5\2\2\u02dd\u02df\5r:\2\u02de\u02dd\3\2\2\2\u02de\u02df")
        buf.write("\3\2\2\2\u02df\u02e0\3\2\2\2\u02e0\u02e1\7\6\2\2\u02e1")
        buf.write("y\3\2\2\2\u02e2\u02e6\5\u0084C\2\u02e3\u02e6\58\35\2\u02e4")
        buf.write("\u02e6\5`\61\2\u02e5\u02e2\3\2\2\2\u02e5\u02e3\3\2\2\2")
        buf.write("\u02e5\u02e4\3\2\2\2\u02e6\u02e7\3\2\2\2\u02e7\u02e8\7")
        buf.write("\16\2\2\u02e8\u02ea\5x=\2\u02e9\u02eb\7\f\2\2\u02ea\u02e9")
        buf.write("\3\2\2\2\u02ea\u02eb\3\2\2\2\u02eb{\3\2\2\2\u02ec\u02ed")
        buf.write("\7\5\2\2\u02ed\u02ee\5N(\2\u02ee\u02ef\7\6\2\2\u02ef\u02f3")
        buf.write("\3\2\2\2\u02f0\u02f3\5\u0082B\2\u02f1\u02f3\5~@\2\u02f2")
        buf.write("\u02ec\3\2\2\2\u02f2\u02f0\3\2\2\2\u02f2\u02f1\3\2\2\2")
        buf.write("\u02f3}\3\2\2\2\u02f4\u02f6\5\u0080A\2\u02f5\u02f7\5\u0086")
        buf.write("D\2\u02f6\u02f5\3\2\2\2\u02f6\u02f7\3\2\2\2\u02f7\177")
        buf.write("\3\2\2\2\u02f8\u02fa\5\24\13\2\u02f9\u02f8\3\2\2\2\u02fa")
        buf.write("\u02fb\3\2\2\2\u02fb\u02f9\3\2\2\2\u02fb\u02fc\3\2\2\2")
        buf.write("\u02fc\u02ff\3\2\2\2\u02fd\u0300\5\20\t\2\u02fe\u0300")
        buf.write("\5\u0084C\2\u02ff\u02fd\3\2\2\2\u02ff\u02fe\3\2\2\2\u0300")
        buf.write("\u0081\3\2\2\2\u0301\u030d\7:\2\2\u0302\u030d\7<\2\2\u0303")
        buf.write("\u030d\7>\2\2\u0304\u030d\7?\2\2\u0305\u030d\7=\2\2\u0306")
        buf.write("\u030d\7;\2\2\u0307\u030d\7\66\2\2\u0308\u030d\7@\2\2")
        buf.write("\u0309\u030d\5\u008aF\2\u030a\u030d\5\u0084C\2\u030b\u030d")
        buf.write("\7\65\2\2\u030c\u0301\3\2\2\2\u030c\u0302\3\2\2\2\u030c")
        buf.write("\u0303\3\2\2\2\u030c\u0304\3\2\2\2\u030c\u0305\3\2\2\2")
        buf.write("\u030c\u0306\3\2\2\2\u030c\u0307\3\2\2\2\u030c\u0308\3")
        buf.write("\2\2\2\u030c\u0309\3\2\2\2\u030c\u030a\3\2\2\2\u030c\u030b")
        buf.write("\3\2\2\2\u030d\u0083\3\2\2\2\u030e\u030f\79\2\2\u030f")
        buf.write("\u0085\3\2\2\2\u0310\u0313\7\7\2\2\u0311\u0314\5\u0082")
        buf.write("B\2\u0312\u0314\5\u0086D\2\u0313\u0311\3\2\2\2\u0313\u0312")
        buf.write("\3\2\2\2\u0314\u0315\3\2\2\2\u0315\u0316\5\u0088E\2\u0316")
        buf.write("\u0317\7\b\2\2\u0317\u0087\3\2\2\2\u0318\u031b\7\13\2")
        buf.write("\2\u0319\u031c\5\u0082B\2\u031a\u031c\5\u0086D\2\u031b")
        buf.write("\u0319\3\2\2\2\u031b\u031a\3\2\2\2\u031c\u031d\3\2\2\2")
        buf.write("\u031d\u031e\5\u0088E\2\u031e\u0321\3\2\2\2\u031f\u0321")
        buf.write("\3\2\2\2\u0320\u0318\3\2\2\2\u0320\u031f\3\2\2\2\u0321")
        buf.write("\u0089\3\2\2\2\u0322\u0323\5\u0090I\2\u0323\u0325\7\7")
        buf.write("\2\2\u0324\u0326\5\u008cG\2\u0325\u0324\3\2\2\2\u0325")
        buf.write("\u0326\3\2\2\2\u0326\u0327\3\2\2\2\u0327\u0328\7\b\2\2")
        buf.write("\u0328\u008b\3\2\2\2\u0329\u032a\5\u0090I\2\u032a\u032b")
        buf.write("\7\r\2\2\u032b\u032c\5N(\2\u032c\u032d\5\u008eH\2\u032d")
        buf.write("\u008d\3\2\2\2\u032e\u032f\7\13\2\2\u032f\u0330\5\u008c")
        buf.write("G\2\u0330\u0331\5\u008eH\2\u0331\u0334\3\2\2\2\u0332\u0334")
        buf.write("\3\2\2\2\u0333\u032e\3\2\2\2\u0333\u0332\3\2\2\2\u0334")
        buf.write("\u008f\3\2\2\2\u0335\u0336\79\2\2\u0336\u0091\3\2\2\2")
        buf.write("\u0337\u033c\7\4\2\2\u0338\u033c\7\f\2\2\u0339\u033a\7")
        buf.write("\f\2\2\u033a\u033c\7\4\2\2\u033b\u0337\3\2\2\2\u033b\u0338")
        buf.write("\3\2\2\2\u033b\u0339\3\2\2\2\u033c\u0093\3\2\2\2a\u0097")
        buf.write("\u009e\u00aa\u00af\u00b6\u00bc\u00cb\u00d1\u00d5\u00dc")
        buf.write("\u00e1\u00e6\u00ed\u00f3\u00fa\u0105\u010e\u0114\u0119")
        buf.write("\u0123\u0129\u012e\u0136\u013b\u0142\u0146\u014d\u0153")
        buf.write("\u015e\u0164\u0169\u0171\u0177\u017e\u0187\u018c\u0196")
        buf.write("\u019c\u01a2\u01a8\u01b3\u01ba\u01c0\u01c5\u01cc\u01d3")
        buf.write("\u01d9\u01e0\u01e3\u01e9\u01ef\u01f5\u01ff\u0203\u0216")
        buf.write("\u021e\u0228\u0233\u023e\u0249\u0254\u025a\u025f\u0264")
        buf.write("\u0268\u026d\u0279\u027f\u0283\u0288\u028b\u028f\u02a1")
        buf.write("\u02a6\u02ac\u02b1\u02b8\u02c4\u02cd\u02d4\u02d9\u02de")
        buf.write("\u02e5\u02ea\u02f2\u02f6\u02fb\u02ff\u030c\u0313\u031b")
        buf.write("\u0320\u0325\u0333\u033b")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "';'", "':'", "'.'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
                     "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "WS", "NL", "LB", "RB", "LC", "RC", "LP", 
                      "RP", "COMMA", "SEMICOLON", "COLON", "DOT", "ADD", 
                      "SUBTR", "MUL", "DIV", "MOD", "EQ", "UNEQ", "LESS", 
                      "LESSEQ", "GREATER", "GREATEREQ", "AND", "OR", "NOT", 
                      "INITOP", "ASSIGN", "ADDASS", "SUBASS", "MULASS", 
                      "DIVASS", "MODASS", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                      "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                      "RANGE", "NIL", "BOOLLIT", "TRUE", "FALSE", "ID", 
                      "INTLIT", "FLOATLIT", "DECIMAL", "HEXADECIMAL", "BINARY", 
                      "OCTAL", "STRINGLIT", "COMMENT", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

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
    RULE_prototype = 15
    RULE_parameters = 16
    RULE_paraTail = 17
    RULE_funcDeclare = 18
    RULE_method = 19
    RULE_paramDeclare = 20
    RULE_paraDeclTail = 21
    RULE_methodDeclare = 22
    RULE_stmt = 23
    RULE_statement = 24
    RULE_assignment = 25
    RULE_lhs = 26
    RULE_arrayCell = 27
    RULE_assignOp = 28
    RULE_ifstmt = 29
    RULE_elsestmt = 30
    RULE_forstmt = 31
    RULE_initFor = 32
    RULE_assignment_for = 33
    RULE_rangeFor = 34
    RULE_breakstmt = 35
    RULE_contstmt = 36
    RULE_returnstmt = 37
    RULE_expr = 38
    RULE_expr1 = 39
    RULE_expr2 = 40
    RULE_expr3 = 41
    RULE_expr4 = 42
    RULE_expr5 = 43
    RULE_expr6 = 44
    RULE_arrayElement = 45
    RULE_index = 46
    RULE_structField = 47
    RULE_lastFieldAccess = 48
    RULE_indexTail = 49
    RULE_fieldAccess = 50
    RULE_structReceiver = 51
    RULE_expr7 = 52
    RULE_funcArrayCell = 53
    RULE_funcCall = 54
    RULE_funcCallReceiver = 55
    RULE_arguments = 56
    RULE_argTail = 57
    RULE_methodCallExpr = 58
    RULE_funcCallMeth = 59
    RULE_methodCall = 60
    RULE_expr8 = 61
    RULE_arrayInit = 62
    RULE_arrayTypeInit = 63
    RULE_literal = 64
    RULE_identifierType = 65
    RULE_arrayLit = 66
    RULE_literalTail = 67
    RULE_structLit = 68
    RULE_structElement = 69
    RULE_elementTail = 70
    RULE_identifier = 71
    RULE_endStmt = 72

    ruleNames =  [ "program", "declarations", "declare", "declareTail", 
                   "constDeclare", "varDeclare", "modify", "varType", "arrayType", 
                   "dimensions", "init", "typeDeclare", "structDeclare", 
                   "field", "interfaceDeclare", "prototype", "parameters", 
                   "paraTail", "funcDeclare", "method", "paramDeclare", 
                   "paraDeclTail", "methodDeclare", "stmt", "statement", 
                   "assignment", "lhs", "arrayCell", "assignOp", "ifstmt", 
                   "elsestmt", "forstmt", "initFor", "assignment_for", "rangeFor", 
                   "breakstmt", "contstmt", "returnstmt", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "arrayElement", 
                   "index", "structField", "lastFieldAccess", "indexTail", 
                   "fieldAccess", "structReceiver", "expr7", "funcArrayCell", 
                   "funcCall", "funcCallReceiver", "arguments", "argTail", 
                   "methodCallExpr", "funcCallMeth", "methodCall", "expr8", 
                   "arrayInit", "arrayTypeInit", "literal", "identifierType", 
                   "arrayLit", "literalTail", "structLit", "structElement", 
                   "elementTail", "identifier", "endStmt" ]

    EOF = Token.EOF
    WS=1
    NL=2
    LB=3
    RB=4
    LC=5
    RC=6
    LP=7
    RP=8
    COMMA=9
    SEMICOLON=10
    COLON=11
    DOT=12
    ADD=13
    SUBTR=14
    MUL=15
    DIV=16
    MOD=17
    EQ=18
    UNEQ=19
    LESS=20
    LESSEQ=21
    GREATER=22
    GREATEREQ=23
    AND=24
    OR=25
    NOT=26
    INITOP=27
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
    BOOLLIT=52
    TRUE=53
    FALSE=54
    ID=55
    INTLIT=56
    FLOATLIT=57
    DECIMAL=58
    HEXADECIMAL=59
    BINARY=60
    OCTAL=61
    STRINGLIT=62
    COMMENT=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65
    ERROR_CHAR=66

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
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 146
                self.match(MiniGoParser.NL)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.declarations()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 153
                self.match(MiniGoParser.NL)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
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
            self.state = 161
            self.declare()
            self.state = 162
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
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.constDeclare()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.varDeclare()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.typeDeclare()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 170
                    self.match(MiniGoParser.NL)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 176
                self.declare()
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 177
                        self.match(MiniGoParser.NL) 
                    self.state = 182
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 183
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def endStmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndStmtContext,0)


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
            self.state = 188
            self.match(MiniGoParser.CONST)
            self.state = 189
            self.identifier()
            self.state = 190
            self.init()
            self.state = 191
            self.endStmt()
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def modify(self):
            return self.getTypedRuleContext(MiniGoParser.ModifyContext,0)


        def endStmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndStmtContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.VAR)
            self.state = 194
            self.identifier()
            self.state = 195
            self.modify()
            self.state = 196
            self.endStmt()
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


        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


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
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LP]:
                    self.state = 198
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 199
                    self.varType()
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 200
                    self.identifierType()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LP]:
                    self.state = 204
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 205
                    self.varType()
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 206
                    self.identifierType()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 209
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
            self.state = 213
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

        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


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
        self.enterRule(localctx, 16, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 215
                self.dimensions()
                self.state = 218 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LP):
                    break

            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 220
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 221
                self.match(MiniGoParser.STRUCT)
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 222
                self.identifierType()
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

        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MiniGoParser.LP)
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTLIT]:
                self.state = 226
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 227
                self.identifierType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 230
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
            self.state = 232
            self.match(MiniGoParser.INITOP)
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 233
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 234
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(MiniGoParser.TYPE)
            self.state = 238
            self.identifier()
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 239
                self.structDeclare()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 240
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

        def endStmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndStmtContext,0)


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
            self.state = 243
            self.match(MiniGoParser.STRUCT)
            self.state = 244
            self.match(MiniGoParser.LC)
            self.state = 246 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 245
                self.field()
                self.state = 248 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 250
            self.match(MiniGoParser.RC)
            self.state = 251
            self.endStmt()
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def endStmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndStmtContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def structDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclareContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def interfaceDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclareContext,0)


        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.identifier()
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 254
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 255
                self.structDeclare()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 256
                self.arrayType()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 257
                self.interfaceDeclare()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 258
                self.identifierType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 261
            self.endStmt()
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

        def endStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EndStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EndStmtContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def prototype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.PrototypeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.PrototypeContext,i)


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
            self.state = 263
            self.match(MiniGoParser.INTERFACE)
            self.state = 264
            self.match(MiniGoParser.LC)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 265
                self.match(MiniGoParser.NL)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 271
                self.prototype()
                self.state = 274 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 277 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 276
                self.endStmt()
                self.state = 279 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                    break

            self.state = 281
            self.match(MiniGoParser.RC)
            self.state = 282
            self.endStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def parameters(self):
            return self.getTypedRuleContext(MiniGoParser.ParametersContext,0)


        def paraTail(self):
            return self.getTypedRuleContext(MiniGoParser.ParaTailContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def endStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EndStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EndStmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_prototype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototype" ):
                return visitor.visitPrototype(self)
            else:
                return visitor.visitChildren(self)




    def prototype(self):

        localctx = MiniGoParser.PrototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_prototype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.identifier()
            self.state = 285
            self.match(MiniGoParser.LB)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 286
                self.parameters()
                self.state = 287
                self.paraTail()


            self.state = 291
            self.match(MiniGoParser.RB)
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 292
                self.varType()

            elif la_ == 2:
                self.state = 293
                self.arrayType()

            elif la_ == 3:
                self.state = 294
                self.identifierType()


            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 297
                    self.endStmt() 
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierContext,i)


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
            self.state = 303
            self.identifier()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 304
                self.match(MiniGoParser.COMMA)
                self.state = 305
                self.identifier()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 311
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 312
                self.arrayType()
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
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(MiniGoParser.COMMA)
                self.state = 316
                self.parameters()
                self.state = 317
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

        def endStmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndStmtContext,0)


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
            self.state = 322
            self.match(MiniGoParser.FUNC)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LB:
                self.state = 323
                self.methodDeclare()


            self.state = 326
            self.method()
            self.state = 327
            self.match(MiniGoParser.LC)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 328
                self.match(MiniGoParser.NL)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY) | (1 << MiniGoParser.OCTAL) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 334
                self.stmt()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 340
            self.match(MiniGoParser.RC)
            self.state = 341
            self.endStmt()
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierContext,i)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def paramDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.ParamDeclareContext,0)


        def paraDeclTail(self):
            return self.getTypedRuleContext(MiniGoParser.ParaDeclTailContext,0)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def endStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EndStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EndStmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.identifier()
            self.state = 344
            self.match(MiniGoParser.LB)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 345
                self.paramDeclare()
                self.state = 346
                self.paraDeclTail()


            self.state = 350
            self.match(MiniGoParser.RB)
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 351
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 352
                self.arrayType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 353
                self.identifier()
                pass
            elif token in [MiniGoParser.NL, MiniGoParser.LC, MiniGoParser.SEMICOLON]:
                pass
            else:
                pass
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON:
                self.state = 356
                self.endStmt()
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierContext,i)


        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_paramDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclare" ):
                return visitor.visitParamDeclare(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclare(self):

        localctx = MiniGoParser.ParamDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_paramDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.identifier()
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 363
                self.match(MiniGoParser.COMMA)
                self.state = 364
                self.identifier()
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 370
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 371
                self.arrayType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 372
                self.identifierType()
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


    class ParaDeclTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramDeclare(self):
            return self.getTypedRuleContext(MiniGoParser.ParamDeclareContext,0)


        def paraDeclTail(self):
            return self.getTypedRuleContext(MiniGoParser.ParaDeclTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paraDeclTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaDeclTail" ):
                return visitor.visitParaDeclTail(self)
            else:
                return visitor.visitChildren(self)




    def paraDeclTail(self):

        localctx = MiniGoParser.ParaDeclTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_paraDeclTail)
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(MiniGoParser.COMMA)
                self.state = 376
                self.paramDeclare()
                self.state = 377
                self.paraDeclTail()
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


    class MethodDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierContext,i)


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
        self.enterRule(localctx, 44, self.RULE_methodDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(MiniGoParser.LB)
            self.state = 383
            self.identifier()
            self.state = 384
            self.identifier()
            self.state = 385
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


        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def endStmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.VAR]:
                    self.state = 387
                    self.varDeclare()
                    pass
                elif token in [MiniGoParser.CONST]:
                    self.state = 388
                    self.constDeclare()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.LB, MiniGoParser.LP, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.statement()
                self.state = 392
                self.endStmt()
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 398
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 399
                self.breakstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 400
                self.contstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 401
                self.funcCall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 402
                self.methodCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 403
                self.returnstmt()
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
        self.enterRule(localctx, 50, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.lhs()
            self.state = 407
            self.assignOp()
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 408
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 409
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

        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def structField(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldContext,0)


        def methodCallExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.identifierType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.arrayElement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.structField()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.methodCallExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayCellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayCell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayCell" ):
                return visitor.visitArrayCell(self)
            else:
                return visitor.visitChildren(self)




    def arrayCell(self):

        localctx = MiniGoParser.ArrayCellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arrayCell)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.identifierType()
            self.state = 420 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 419
                self.index()
                self.state = 422 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LP):
                    break

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
        self.enterRule(localctx, 56, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
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
        self.enterRule(localctx, 58, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.IF)
            self.state = 427
            self.match(MiniGoParser.LB)
            self.state = 428
            self.expr(0)
            self.state = 429
            self.match(MiniGoParser.RB)
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY) | (1 << MiniGoParser.OCTAL) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 443
                self.stmt()
                self.state = 448
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 449
            self.match(MiniGoParser.RC)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 450
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
        self.enterRule(localctx, 60, self.RULE_elsestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(MiniGoParser.ELSE)
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF]:
                self.state = 454
                self.ifstmt()
                pass
            elif token in [MiniGoParser.NL, MiniGoParser.LC]:
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 455
                    self.match(MiniGoParser.NL)
                    self.state = 460
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 461
                self.match(MiniGoParser.LC)
                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 462
                    self.match(MiniGoParser.NL)
                    self.state = 467
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY) | (1 << MiniGoParser.OCTAL) | (1 << MiniGoParser.STRINGLIT))) != 0):
                    self.state = 468
                    self.stmt()
                    self.state = 473
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 474
                self.match(MiniGoParser.RC)
                self.state = 478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 475
                        self.match(MiniGoParser.NL) 
                    self.state = 480
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        self.enterRule(localctx, 62, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(MiniGoParser.FOR)
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 484
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 485
                self.initFor()
                pass

            elif la_ == 3:
                self.state = 486
                self.rangeFor()
                pass


            self.state = 489
            self.match(MiniGoParser.LC)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 490
                self.match(MiniGoParser.NL)
                self.state = 495
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY) | (1 << MiniGoParser.OCTAL) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 496
                self.stmt()
                self.state = 501
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 502
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

        def endStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EndStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EndStmtContext,i)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assignment_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_forContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_forContext,i)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
        self.enterRule(localctx, 64, self.RULE_initFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 504
                self.assignment_for()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 505
                self.match(MiniGoParser.VAR)
                self.state = 506
                self.identifier()
                self.state = 509
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 507
                    self.varType()
                    pass
                elif token in [MiniGoParser.LP]:
                    self.state = 508
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.INITOP]:
                    pass
                else:
                    pass
                self.state = 511
                self.init()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 515
            self.endStmt()
            self.state = 516
            self.expr(0)
            self.state = 517
            self.endStmt()
            self.state = 518
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

        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def assignOp(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_for" ):
                return visitor.visitAssignment_for(self)
            else:
                return visitor.visitChildren(self)




    def assignment_for(self):

        localctx = MiniGoParser.Assignment_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignment_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.identifierType()
            self.state = 521
            self.assignOp()
            self.state = 522
            self.expr(0)
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

        def identifierType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierTypeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,i)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


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
        self.enterRule(localctx, 68, self.RULE_rangeFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.identifierType()
            self.state = 525
            self.match(MiniGoParser.COMMA)
            self.state = 526
            self.identifierType()
            self.state = 527
            self.match(MiniGoParser.ASSIGN)
            self.state = 528
            self.match(MiniGoParser.RANGE)
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 529
                self.literal()
                pass

            elif la_ == 2:
                self.state = 530
                self.arrayInit()
                pass

            elif la_ == 3:
                self.state = 531
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
        self.enterRule(localctx, 70, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
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
        self.enterRule(localctx, 72, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
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
        self.enterRule(localctx, 74, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(MiniGoParser.RETURN)
            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY) | (1 << MiniGoParser.OCTAL) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 539
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 550
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 545
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 546
                    self.match(MiniGoParser.OR)
                    self.state = 547
                    self.expr1(0) 
                self.state = 552
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 561
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 556
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 557
                    self.match(MiniGoParser.AND)
                    self.state = 558
                    self.expr2(0) 
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 572
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 567
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 568
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.UNEQ) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESSEQ) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATEREQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 569
                    self.expr3(0) 
                self.state = 574
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 583
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 578
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 579
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUBTR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 580
                    self.expr4(0) 
                self.state = 585
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 594
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 589
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 590
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 591
                    self.expr5() 
                self.state = 596
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 605
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT:
                    self.state = 597
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 602
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 603
                self.expr6()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
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
        self.enterRule(localctx, 88, self.RULE_expr6)
        try:
            self.state = 610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.arrayElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                self.methodCallExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 609
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
        self.enterRule(localctx, 90, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 612
                self.expr8()
                pass

            elif la_ == 2:
                self.state = 613
                self.funcCall()
                pass


            self.state = 617 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 616
                    self.index()

                else:
                    raise NoViableAltException(self)
                self.state = 619 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

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
        self.enterRule(localctx, 92, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(MiniGoParser.LP)
            self.state = 622
            self.expr(0)
            self.state = 623
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

        def structReceiver(self):
            return self.getTypedRuleContext(MiniGoParser.StructReceiverContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def fieldAccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FieldAccessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FieldAccessContext,i)


        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def lastFieldAccess(self):
            return self.getTypedRuleContext(MiniGoParser.LastFieldAccessContext,0)


        def indexTail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexTailContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexTailContext,i)


        def funcCallMeth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncCallMethContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncCallMethContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructField" ):
                return visitor.visitStructField(self)
            else:
                return visitor.visitChildren(self)




    def structField(self):

        localctx = MiniGoParser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.structReceiver()
            self.state = 626
            self.match(MiniGoParser.DOT)
            self.state = 627
            self.fieldAccess()
            self.state = 631
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 628
                    self.index() 
                self.state = 633
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

            self.state = 649
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.state = 639 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 634
                        self.match(MiniGoParser.DOT)
                        self.state = 637
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                        if la_ == 1:
                            self.state = 635
                            self.fieldAccess()
                            pass

                        elif la_ == 2:
                            self.state = 636
                            self.funcCallMeth()
                            pass



                    else:
                        raise NoViableAltException(self)
                    self.state = 641 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

                self.state = 646
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 643
                        self.indexTail() 
                    self.state = 648
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,69,self._ctx)



            self.state = 653
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.state = 651
                self.match(MiniGoParser.DOT)
                self.state = 652
                self.lastFieldAccess()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LastFieldAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lastFieldAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLastFieldAccess" ):
                return visitor.visitLastFieldAccess(self)
            else:
                return visitor.visitChildren(self)




    def lastFieldAccess(self):

        localctx = MiniGoParser.LastFieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_lastFieldAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 655
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexTailContext(ParserRuleContext):
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
            return MiniGoParser.RULE_indexTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexTail" ):
                return visitor.visitIndexTail(self)
            else:
                return visitor.visitChildren(self)




    def indexTail(self):

        localctx = MiniGoParser.IndexTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_indexTail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self.match(MiniGoParser.LP)
            self.state = 658
            self.expr(0)
            self.state = 659
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAccess" ):
                return visitor.visitFieldAccess(self)
            else:
                return visitor.visitChildren(self)




    def fieldAccess(self):

        localctx = MiniGoParser.FieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_fieldAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structReceiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructReceiver" ):
                return visitor.visitStructReceiver(self)
            else:
                return visitor.visitChildren(self)




    def structReceiver(self):

        localctx = MiniGoParser.StructReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_structReceiver)
        try:
            self.state = 671
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.identifierType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 664
                self.arrayElement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 665
                self.structLit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 666
                self.match(MiniGoParser.LB)
                self.state = 667
                self.expr(0)
                self.state = 668
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 670
                self.match(MiniGoParser.BOOLLIT)
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
        self.enterRule(localctx, 104, self.RULE_expr7)
        try:
            self.state = 676
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                self.structField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 674
                self.funcCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 675
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncArrayCellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodCallExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallExprContext,0)


        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcArrayCell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncArrayCell" ):
                return visitor.visitFuncArrayCell(self)
            else:
                return visitor.visitChildren(self)




    def funcArrayCell(self):

        localctx = MiniGoParser.FuncArrayCellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_funcArrayCell)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.methodCallExpr()
            self.state = 680 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 679
                self.index()
                self.state = 682 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LP):
                    break

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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
        self.enterRule(localctx, 108, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.identifier()
            self.state = 685
            self.match(MiniGoParser.LB)
            self.state = 687
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY) | (1 << MiniGoParser.OCTAL) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 686
                self.arguments()


            self.state = 689
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcCallReceiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallReceiver" ):
                return visitor.visitFuncCallReceiver(self)
            else:
                return visitor.visitChildren(self)




    def funcCallReceiver(self):

        localctx = MiniGoParser.FuncCallReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_funcCallReceiver)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.identifier()
            self.state = 692
            self.match(MiniGoParser.LB)
            self.state = 694
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY) | (1 << MiniGoParser.OCTAL) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 693
                self.arguments()


            self.state = 696
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
        self.enterRule(localctx, 112, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.expr(0)
            self.state = 699
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
        self.enterRule(localctx, 114, self.RULE_argTail)
        try:
            self.state = 706
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 701
                self.match(MiniGoParser.COMMA)
                self.state = 702
                self.expr(0)
                self.state = 703
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

        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def funcCallMeth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncCallMethContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncCallMethContext,i)


        def structField(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCallExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallExpr" ):
                return visitor.visitMethodCallExpr(self)
            else:
                return visitor.visitChildren(self)




    def methodCallExpr(self):

        localctx = MiniGoParser.MethodCallExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_methodCallExpr)
        try:
            self.state = 727
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 708
                self.identifierType()
                self.state = 709
                self.match(MiniGoParser.DOT)
                self.state = 713 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 710
                        self.funcCallMeth()
                        self.state = 711
                        self.match(MiniGoParser.DOT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 715 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

                self.state = 717
                self.funcCallMeth()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 722
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                if la_ == 1:
                    self.state = 719
                    self.identifierType()
                    pass

                elif la_ == 2:
                    self.state = 720
                    self.structField()
                    pass

                elif la_ == 3:
                    self.state = 721
                    self.funcCall()
                    pass


                self.state = 724
                self.match(MiniGoParser.DOT)
                self.state = 725
                self.funcCallMeth()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallMethContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcCallMeth

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallMeth" ):
                return visitor.visitFuncCallMeth(self)
            else:
                return visitor.visitChildren(self)




    def funcCallMeth(self):

        localctx = MiniGoParser.FuncCallMethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_funcCallMeth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.identifier()
            self.state = 730
            self.match(MiniGoParser.LB)
            self.state = 732
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY) | (1 << MiniGoParser.OCTAL) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 731
                self.arguments()


            self.state = 734
            self.match(MiniGoParser.RB)
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

        def funcCallMeth(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallMethContext,0)


        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def arrayCell(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayCellContext,0)


        def structField(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = MiniGoParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.state = 736
                self.identifierType()
                pass

            elif la_ == 2:
                self.state = 737
                self.arrayCell()
                pass

            elif la_ == 3:
                self.state = 738
                self.structField()
                pass


            self.state = 741
            self.match(MiniGoParser.DOT)
            self.state = 742
            self.funcCallMeth()
            self.state = 744
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 743
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
        self.enterRule(localctx, 122, self.RULE_expr8)
        try:
            self.state = 752
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 746
                self.match(MiniGoParser.LB)
                self.state = 747
                self.expr(0)
                self.state = 748
                self.match(MiniGoParser.RB)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 750
                self.literal()
                pass
            elif token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 751
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

        def arrayTypeInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeInitContext,0)


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
        self.enterRule(localctx, 124, self.RULE_arrayInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 754
            self.arrayTypeInit()
            self.state = 756
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.state = 755
                self.arrayLit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


        def dimensions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DimensionsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DimensionsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayTypeInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayTypeInit" ):
                return visitor.visitArrayTypeInit(self)
            else:
                return visitor.visitChildren(self)




    def arrayTypeInit(self):

        localctx = MiniGoParser.ArrayTypeInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_arrayTypeInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 759 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 758
                self.dimensions()
                self.state = 761 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LP):
                    break

            self.state = 765
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 763
                self.varType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 764
                self.identifierType()
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


        def identifierType(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierTypeContext,0)


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
        self.enterRule(localctx, 128, self.RULE_literal)
        try:
            self.state = 778
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 767
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 768
                self.match(MiniGoParser.DECIMAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 769
                self.match(MiniGoParser.BINARY)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 770
                self.match(MiniGoParser.OCTAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 771
                self.match(MiniGoParser.HEXADECIMAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 772
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 773
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 774
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 775
                self.structLit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 776
                self.identifierType()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 777
                self.match(MiniGoParser.NIL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_identifierType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierType" ):
                return visitor.visitIdentifierType(self)
            else:
                return visitor.visitChildren(self)




    def identifierType(self):

        localctx = MiniGoParser.IdentifierTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_identifierType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 780
            self.match(MiniGoParser.ID)
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

        def literalTail(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralTailContext,0)


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
        self.enterRule(localctx, 132, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 782
            self.match(MiniGoParser.LC)
            self.state = 785
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                self.state = 783
                self.literal()
                pass
            elif token in [MiniGoParser.LC]:
                self.state = 784
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 787
            self.literalTail()
            self.state = 788
            self.match(MiniGoParser.RC)
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
        self.enterRule(localctx, 134, self.RULE_literalTail)
        try:
            self.state = 798
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 790
                self.match(MiniGoParser.COMMA)
                self.state = 793
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                    self.state = 791
                    self.literal()
                    pass
                elif token in [MiniGoParser.LC]:
                    self.state = 792
                    self.arrayLit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 795
                self.literalTail()
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


    class StructLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
        self.enterRule(localctx, 136, self.RULE_structLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 800
            self.identifier()
            self.state = 801
            self.match(MiniGoParser.LC)
            self.state = 803
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 802
                self.structElement()


            self.state = 805
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
        self.enterRule(localctx, 138, self.RULE_structElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 807
            self.identifier()
            self.state = 808
            self.match(MiniGoParser.COLON)
            self.state = 809
            self.expr(0)
            self.state = 810
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


        def elementTail(self):
            return self.getTypedRuleContext(MiniGoParser.ElementTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elementTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementTail" ):
                return visitor.visitElementTail(self)
            else:
                return visitor.visitChildren(self)




    def elementTail(self):

        localctx = MiniGoParser.ElementTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_elementTail)
        try:
            self.state = 817
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 812
                self.match(MiniGoParser.COMMA)
                self.state = 813
                self.structElement()
                self.state = 814
                self.elementTail()
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


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = MiniGoParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 819
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_endStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndStmt" ):
                return visitor.visitEndStmt(self)
            else:
                return visitor.visitChildren(self)




    def endStmt(self):

        localctx = MiniGoParser.EndStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_endStmt)
        try:
            self.state = 825
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 821
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 822
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 823
                self.match(MiniGoParser.SEMICOLON)
                self.state = 824
                self.match(MiniGoParser.NL)
                pass


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
        self._predicates[38] = self.expr_sempred
        self._predicates[39] = self.expr1_sempred
        self._predicates[40] = self.expr2_sempred
        self._predicates[41] = self.expr3_sempred
        self._predicates[42] = self.expr4_sempred
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
         




