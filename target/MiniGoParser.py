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
        buf.write("\u02db\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\7\2|\n\2\f\2\16\2\177\13\2\3\2\3\2\7")
        buf.write("\2\u0083\n\2\f\2\16\2\u0086\13\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\5\4\u0091\n\4\3\5\7\5\u0094\n\5\f\5\16")
        buf.write("\5\u0097\13\5\3\5\3\5\7\5\u009b\n\5\f\5\16\5\u009e\13")
        buf.write("\5\3\5\3\5\3\5\5\5\u00a3\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\5\b\u00b2\n\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u00b8\n\b\3\b\3\b\5\b\u00bc\n\b\3\t\3\t\3\n\6\n")
        buf.write("\u00c1\n\n\r\n\16\n\u00c2\3\n\3\n\3\n\5\n\u00c8\n\n\3")
        buf.write("\13\3\13\3\13\5\13\u00cd\n\13\3\13\3\13\3\f\3\f\3\f\5")
        buf.write("\f\u00d4\n\f\3\r\3\r\3\r\3\r\5\r\u00da\n\r\3\16\3\16\3")
        buf.write("\16\6\16\u00df\n\16\r\16\16\16\u00e0\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\5\17\u00ec\n\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\7\20\u00f3\n\20\f\20\16\20\u00f6\13\20")
        buf.write("\3\20\6\20\u00f9\n\20\r\20\16\20\u00fa\3\20\6\20\u00fe")
        buf.write("\n\20\r\20\16\20\u00ff\3\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u010a\n\21\3\21\3\21\3\21\3\21\5\21\u0110")
        buf.write("\n\21\3\21\7\21\u0113\n\21\f\21\16\21\u0116\13\21\3\22")
        buf.write("\3\22\3\22\7\22\u011b\n\22\f\22\16\22\u011e\13\22\3\22")
        buf.write("\3\22\3\22\5\22\u0123\n\22\3\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u012a\n\23\3\24\3\24\5\24\u012e\n\24\3\24\3\24\3\24")
        buf.write("\7\24\u0133\n\24\f\24\16\24\u0136\13\24\3\24\7\24\u0139")
        buf.write("\n\24\f\24\16\24\u013c\13\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\5\26\u0148\n\26\3\26\3\26\3")
        buf.write("\26\5\26\u014d\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0157\n\27\3\30\3\30\6\30\u015b\n\30\r\30\16")
        buf.write("\30\u015c\3\30\3\30\5\30\u0161\n\30\3\31\3\31\7\31\u0165")
        buf.write("\n\31\f\31\16\31\u0168\13\31\3\31\3\31\3\31\6\31\u016d")
        buf.write("\n\31\r\31\16\31\u016e\5\31\u0171\n\31\3\31\3\31\3\31")
        buf.write("\7\31\u0176\n\31\f\31\16\31\u0179\13\31\6\31\u017b\n\31")
        buf.write("\r\31\16\31\u017c\5\31\u017f\n\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\7\33\u0188\n\33\f\33\16\33\u018b\13\33")
        buf.write("\3\33\3\33\7\33\u018f\n\33\f\33\16\33\u0192\13\33\3\33")
        buf.write("\7\33\u0195\n\33\f\33\16\33\u0198\13\33\3\33\3\33\5\33")
        buf.write("\u019c\n\33\3\34\3\34\3\34\7\34\u01a1\n\34\f\34\16\34")
        buf.write("\u01a4\13\34\3\34\3\34\7\34\u01a8\n\34\f\34\16\34\u01ab")
        buf.write("\13\34\3\34\7\34\u01ae\n\34\f\34\16\34\u01b1\13\34\3\34")
        buf.write("\3\34\7\34\u01b5\n\34\f\34\16\34\u01b8\13\34\5\34\u01ba")
        buf.write("\n\34\3\35\3\35\3\35\3\35\5\35\u01c0\n\35\3\35\3\35\7")
        buf.write("\35\u01c4\n\35\f\35\16\35\u01c7\13\35\3\35\7\35\u01ca")
        buf.write("\n\35\f\35\16\35\u01cd\13\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u01d6\n\36\3\36\3\36\5\36\u01da\n\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \5 \u01ed\n \3!\3!\3\"\3\"\3#\3#\5#\u01f5")
        buf.write("\n#\3$\3$\3$\3$\3$\3$\7$\u01fd\n$\f$\16$\u0200\13$\3%")
        buf.write("\3%\3%\3%\3%\3%\7%\u0208\n%\f%\16%\u020b\13%\3&\3&\3&")
        buf.write("\3&\3&\3&\7&\u0213\n&\f&\16&\u0216\13&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\7\'\u021e\n\'\f\'\16\'\u0221\13\'\3(\3(\3(\3")
        buf.write("(\3(\3(\7(\u0229\n(\f(\16(\u022c\13(\3)\7)\u022f\n)\f")
        buf.write(")\16)\u0232\13)\3)\3)\5)\u0236\n)\3*\3*\3*\5*\u023b\n")
        buf.write("*\3+\3+\5+\u023f\n+\3+\6+\u0242\n+\r+\16+\u0243\3,\3,")
        buf.write("\3,\3,\3-\3-\3-\5-\u024d\n-\3-\3-\3-\5-\u0252\n-\3-\7")
        buf.write("-\u0255\n-\f-\16-\u0258\13-\6-\u025a\n-\r-\16-\u025b\3")
        buf.write(".\3.\3.\5.\u0261\n.\3/\3/\3/\5/\u0266\n/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u0272\n\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u027c\n\62\3")
        buf.write("\62\3\62\3\62\3\62\7\62\u0282\n\62\f\62\16\62\u0285\13")
        buf.write("\62\3\62\5\62\u0288\n\62\3\63\3\63\7\63\u028c\n\63\f\63")
        buf.write("\16\63\u028f\13\63\3\63\3\63\3\63\5\63\u0294\n\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\5\64\u029c\n\64\3\65\3\65\5")
        buf.write("\65\u02a0\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u02ad\n\66\3\67\3\67\3\67\5\67\u02b2")
        buf.write("\n\67\3\67\3\67\3\67\3\67\38\38\38\58\u02bb\n8\38\38\3")
        buf.write("8\58\u02c0\n8\39\39\39\59\u02c5\n9\39\39\3:\3:\3:\3:\3")
        buf.write(":\3;\3;\3;\5;\u02d1\n;\3<\3<\3=\3=\3=\3=\5=\u02d9\n=\3")
        buf.write("=\2\7FHJLN>\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvx\2")
        buf.write("\13\3\2/\62\3\2!&\3\2\3\4\3\2\4\5\3\2\27\34\3\2\22\23")
        buf.write("\3\2\24\26\4\2\23\23\37\37\5\2\3\3\5\5<<\2\u031b\2}\3")
        buf.write("\2\2\2\4\u0089\3\2\2\2\6\u0090\3\2\2\2\b\u00a2\3\2\2\2")
        buf.write("\n\u00a4\3\2\2\2\f\u00a9\3\2\2\2\16\u00bb\3\2\2\2\20\u00bd")
        buf.write("\3\2\2\2\22\u00c0\3\2\2\2\24\u00c9\3\2\2\2\26\u00d0\3")
        buf.write("\2\2\2\30\u00d5\3\2\2\2\32\u00db\3\2\2\2\34\u00e5\3\2")
        buf.write("\2\2\36\u00ef\3\2\2\2 \u0104\3\2\2\2\"\u0117\3\2\2\2$")
        buf.write("\u0129\3\2\2\2&\u012b\3\2\2\2(\u0140\3\2\2\2*\u014c\3")
        buf.write("\2\2\2,\u0156\3\2\2\2.\u0158\3\2\2\2\60\u017e\3\2\2\2")
        buf.write("\62\u0180\3\2\2\2\64\u0182\3\2\2\2\66\u019d\3\2\2\28\u01bb")
        buf.write("\3\2\2\2:\u01d9\3\2\2\2<\u01e0\3\2\2\2>\u01e4\3\2\2\2")
        buf.write("@\u01ee\3\2\2\2B\u01f0\3\2\2\2D\u01f2\3\2\2\2F\u01f6\3")
        buf.write("\2\2\2H\u0201\3\2\2\2J\u020c\3\2\2\2L\u0217\3\2\2\2N\u0222")
        buf.write("\3\2\2\2P\u0235\3\2\2\2R\u023a\3\2\2\2T\u023e\3\2\2\2")
        buf.write("V\u0245\3\2\2\2X\u024c\3\2\2\2Z\u0260\3\2\2\2\\\u0262")
        buf.write("\3\2\2\2^\u0269\3\2\2\2`\u0271\3\2\2\2b\u027b\3\2\2\2")
        buf.write("d\u0289\3\2\2\2f\u029b\3\2\2\2h\u029d\3\2\2\2j\u02ac\3")
        buf.write("\2\2\2l\u02ae\3\2\2\2n\u02bf\3\2\2\2p\u02c1\3\2\2\2r\u02c8")
        buf.write("\3\2\2\2t\u02d0\3\2\2\2v\u02d2\3\2\2\2x\u02d8\3\2\2\2")
        buf.write("z|\7\7\2\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2")
        buf.write("~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0084\5\4\3\2\u0081")
        buf.write("\u0083\7\7\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2")
        buf.write("\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0087\3")
        buf.write("\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088\7\2\2\3\u0088\3")
        buf.write("\3\2\2\2\u0089\u008a\5\6\4\2\u008a\u008b\5\b\5\2\u008b")
        buf.write("\5\3\2\2\2\u008c\u0091\5\n\6\2\u008d\u0091\5\f\7\2\u008e")
        buf.write("\u0091\5\30\r\2\u008f\u0091\5&\24\2\u0090\u008c\3\2\2")
        buf.write("\2\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f")
        buf.write("\3\2\2\2\u0091\7\3\2\2\2\u0092\u0094\7\7\2\2\u0093\u0092")
        buf.write("\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0098\u009c\5\6\4\2\u0099\u009b\7\7\2\2\u009a\u0099\3")
        buf.write("\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009f")
        buf.write("\u00a0\5\b\5\2\u00a0\u00a3\3\2\2\2\u00a1\u00a3\3\2\2\2")
        buf.write("\u00a2\u0095\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\t\3\2\2")
        buf.write("\2\u00a4\u00a5\7\63\2\2\u00a5\u00a6\5v<\2\u00a6\u00a7")
        buf.write("\5\26\f\2\u00a7\u00a8\5x=\2\u00a8\13\3\2\2\2\u00a9\u00aa")
        buf.write("\7\64\2\2\u00aa\u00ab\5v<\2\u00ab\u00ac\5\16\b\2\u00ac")
        buf.write("\u00ad\5x=\2\u00ad\r\3\2\2\2\u00ae\u00b2\5\22\n\2\u00af")
        buf.write("\u00b2\5\20\t\2\u00b0\u00b2\5v<\2\u00b1\u00ae\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00bc\3")
        buf.write("\2\2\2\u00b3\u00bc\5\26\f\2\u00b4\u00b8\5\22\n\2\u00b5")
        buf.write("\u00b8\5\20\t\2\u00b6\u00b8\5v<\2\u00b7\u00b4\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00ba\5\26\f\2\u00ba\u00bc\3\2\2\2\u00bb")
        buf.write("\u00b1\3\2\2\2\u00bb\u00b3\3\2\2\2\u00bb\u00b7\3\2\2\2")
        buf.write("\u00bc\17\3\2\2\2\u00bd\u00be\t\2\2\2\u00be\21\3\2\2\2")
        buf.write("\u00bf\u00c1\5\24\13\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c7\3\2\2\2\u00c4\u00c8\5\20\t\2\u00c5\u00c8\7-\2\2")
        buf.write("\u00c6\u00c8\5v<\2\u00c7\u00c4\3\2\2\2\u00c7\u00c5\3\2")
        buf.write("\2\2\u00c7\u00c6\3\2\2\2\u00c8\23\3\2\2\2\u00c9\u00cc")
        buf.write("\7\f\2\2\u00ca\u00cd\7=\2\2\u00cb\u00cd\5v<\2\u00cc\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00cf\7\r\2\2\u00cf\25\3\2\2\2\u00d0\u00d3\7 \2\2\u00d1")
        buf.write("\u00d4\5F$\2\u00d2\u00d4\5h\65\2\u00d3\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d4\27\3\2\2\2\u00d5\u00d6\7,\2\2\u00d6")
        buf.write("\u00d9\5v<\2\u00d7\u00da\5\32\16\2\u00d8\u00da\5\36\20")
        buf.write("\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\31\3")
        buf.write("\2\2\2\u00db\u00dc\7-\2\2\u00dc\u00de\7\n\2\2\u00dd\u00df")
        buf.write("\5\34\17\2\u00de\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2")
        buf.write("\u00e2\u00e3\7\13\2\2\u00e3\u00e4\5x=\2\u00e4\33\3\2\2")
        buf.write("\2\u00e5\u00eb\5v<\2\u00e6\u00ec\5\20\t\2\u00e7\u00ec")
        buf.write("\5\32\16\2\u00e8\u00ec\5\22\n\2\u00e9\u00ec\5\36\20\2")
        buf.write("\u00ea\u00ec\5v<\2\u00eb\u00e6\3\2\2\2\u00eb\u00e7\3\2")
        buf.write("\2\2\u00eb\u00e8\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\5x=\2\u00ee\35")
        buf.write("\3\2\2\2\u00ef\u00f0\7.\2\2\u00f0\u00f4\7\n\2\2\u00f1")
        buf.write("\u00f3\7\7\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f8\3")
        buf.write("\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f9\5 \21\2\u00f8\u00f7")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb\u00fd\3\2\2\2\u00fc\u00fe\5x=\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u00fd\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\7")
        buf.write("\13\2\2\u0102\u0103\5x=\2\u0103\37\3\2\2\2\u0104\u0105")
        buf.write("\5v<\2\u0105\u0109\7\b\2\2\u0106\u0107\5\"\22\2\u0107")
        buf.write("\u0108\5$\23\2\u0108\u010a\3\2\2\2\u0109\u0106\3\2\2\2")
        buf.write("\u0109\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010f\7")
        buf.write("\t\2\2\u010c\u0110\5\20\t\2\u010d\u0110\5\22\n\2\u010e")
        buf.write("\u0110\5v<\2\u010f\u010c\3\2\2\2\u010f\u010d\3\2\2\2\u010f")
        buf.write("\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0114\3\2\2\2")
        buf.write("\u0111\u0113\5x=\2\u0112\u0111\3\2\2\2\u0113\u0116\3\2")
        buf.write("\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115!\3")
        buf.write("\2\2\2\u0116\u0114\3\2\2\2\u0117\u011c\5v<\2\u0118\u0119")
        buf.write("\7\16\2\2\u0119\u011b\5v<\2\u011a\u0118\3\2\2\2\u011b")
        buf.write("\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011d\u0122\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0123\5")
        buf.write("\20\t\2\u0120\u0123\5\22\n\2\u0121\u0123\5v<\2\u0122\u011f")
        buf.write("\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("#\3\2\2\2\u0124\u0125\7\16\2\2\u0125\u0126\5\"\22\2\u0126")
        buf.write("\u0127\5$\23\2\u0127\u012a\3\2\2\2\u0128\u012a\3\2\2\2")
        buf.write("\u0129\u0124\3\2\2\2\u0129\u0128\3\2\2\2\u012a%\3\2\2")
        buf.write("\2\u012b\u012d\7+\2\2\u012c\u012e\5(\25\2\u012d\u012c")
        buf.write("\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("\u0130\5 \21\2\u0130\u0134\7\n\2\2\u0131\u0133\7\7\2\2")
        buf.write("\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132\3")
        buf.write("\2\2\2\u0134\u0135\3\2\2\2\u0135\u013a\3\2\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0137\u0139\5*\26\2\u0138\u0137\3\2\2\2\u0139")
        buf.write("\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013d\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e\7")
        buf.write("\13\2\2\u013e\u013f\5x=\2\u013f\'\3\2\2\2\u0140\u0141")
        buf.write("\7\b\2\2\u0141\u0142\5v<\2\u0142\u0143\5v<\2\u0143\u0144")
        buf.write("\7\t\2\2\u0144)\3\2\2\2\u0145\u0148\5\f\7\2\u0146\u0148")
        buf.write("\5\n\6\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148")
        buf.write("\u014d\3\2\2\2\u0149\u014a\5,\27\2\u014a\u014b\5x=\2\u014b")
        buf.write("\u014d\3\2\2\2\u014c\u0147\3\2\2\2\u014c\u0149\3\2\2\2")
        buf.write("\u014d+\3\2\2\2\u014e\u0157\5.\30\2\u014f\u0157\5\64\33")
        buf.write("\2\u0150\u0157\58\35\2\u0151\u0157\5@!\2\u0152\u0157\5")
        buf.write("B\"\2\u0153\u0157\5\\/\2\u0154\u0157\5d\63\2\u0155\u0157")
        buf.write("\5D#\2\u0156\u014e\3\2\2\2\u0156\u014f\3\2\2\2\u0156\u0150")
        buf.write("\3\2\2\2\u0156\u0151\3\2\2\2\u0156\u0152\3\2\2\2\u0156")
        buf.write("\u0153\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2")
        buf.write("\u0157-\3\2\2\2\u0158\u015a\5\60\31\2\u0159\u015b\5\62")
        buf.write("\32\2\u015a\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u0160\3\2\2\2\u015e")
        buf.write("\u0161\5F$\2\u015f\u0161\5h\65\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u015f\3\2\2\2\u0161/\3\2\2\2\u0162\u0166\5v<\2\u0163")
        buf.write("\u0165\5V,\2\u0164\u0163\3\2\2\2\u0165\u0168\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u017f\3\2\2\2")
        buf.write("\u0168\u0166\3\2\2\2\u0169\u0171\5v<\2\u016a\u016c\5v")
        buf.write("<\2\u016b\u016d\5V,\2\u016c\u016b\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("\u0171\3\2\2\2\u0170\u0169\3\2\2\2\u0170\u016a\3\2\2\2")
        buf.write("\u0171\u017a\3\2\2\2\u0172\u0173\7\21\2\2\u0173\u0177")
        buf.write("\5v<\2\u0174\u0176\5V,\2\u0175\u0174\3\2\2\2\u0176\u0179")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u0172\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3")
        buf.write("\2\2\2\u017d\u017f\3\2\2\2\u017e\u0162\3\2\2\2\u017e\u0170")
        buf.write("\3\2\2\2\u017f\61\3\2\2\2\u0180\u0181\t\3\2\2\u0181\63")
        buf.write("\3\2\2\2\u0182\u0183\7\'\2\2\u0183\u0184\7\b\2\2\u0184")
        buf.write("\u0185\5F$\2\u0185\u0189\7\t\2\2\u0186\u0188\7\7\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0189\3")
        buf.write("\2\2\2\u018c\u0190\7\n\2\2\u018d\u018f\7\7\2\2\u018e\u018d")
        buf.write("\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0196\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0193\u0195\5*\26\2\u0194\u0193\3\2\2\2\u0195\u0198\3")
        buf.write("\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0199")
        buf.write("\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019b\7\13\2\2\u019a")
        buf.write("\u019c\5\66\34\2\u019b\u019a\3\2\2\2\u019b\u019c\3\2\2")
        buf.write("\2\u019c\65\3\2\2\2\u019d\u01b9\7(\2\2\u019e\u01ba\5\64")
        buf.write("\33\2\u019f\u01a1\7\7\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a5\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a9\7\n\2\2")
        buf.write("\u01a6\u01a8\7\7\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3")
        buf.write("\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01af")
        buf.write("\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae\5*\26\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01af\3")
        buf.write("\2\2\2\u01b2\u01b6\7\13\2\2\u01b3\u01b5\7\7\2\2\u01b4")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3")
        buf.write("\2\2\2\u01b9\u019e\3\2\2\2\u01b9\u01a2\3\2\2\2\u01ba\67")
        buf.write("\3\2\2\2\u01bb\u01bf\7)\2\2\u01bc\u01c0\5F$\2\u01bd\u01c0")
        buf.write("\5:\36\2\u01be\u01c0\5> \2\u01bf\u01bc\3\2\2\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("\u01c5\7\n\2\2\u01c2\u01c4\7\7\2\2\u01c3\u01c2\3\2\2\2")
        buf.write("\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3")
        buf.write("\2\2\2\u01c6\u01cb\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01ca")
        buf.write("\5*\26\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce\3\2\2\2")
        buf.write("\u01cd\u01cb\3\2\2\2\u01ce\u01cf\7\13\2\2\u01cf9\3\2\2")
        buf.write("\2\u01d0\u01da\5<\37\2\u01d1\u01d2\7\64\2\2\u01d2\u01d5")
        buf.write("\5v<\2\u01d3\u01d6\5\20\t\2\u01d4\u01d6\5\22\n\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d8\5\26\f\2\u01d8\u01da")
        buf.write("\3\2\2\2\u01d9\u01d0\3\2\2\2\u01d9\u01d1\3\2\2\2\u01da")
        buf.write("\u01db\3\2\2\2\u01db\u01dc\5x=\2\u01dc\u01dd\5F$\2\u01dd")
        buf.write("\u01de\5x=\2\u01de\u01df\5<\37\2\u01df;\3\2\2\2\u01e0")
        buf.write("\u01e1\7<\2\2\u01e1\u01e2\5\62\32\2\u01e2\u01e3\5j\66")
        buf.write("\2\u01e3=\3\2\2\2\u01e4\u01e5\t\4\2\2\u01e5\u01e6\7\16")
        buf.write("\2\2\u01e6\u01e7\t\5\2\2\u01e7\u01e8\7!\2\2\u01e8\u01ec")
        buf.write("\7\67\2\2\u01e9\u01ed\5v<\2\u01ea\u01ed\5j\66\2\u01eb")
        buf.write("\u01ed\5T+\2\u01ec\u01e9\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed?\3\2\2\2\u01ee\u01ef\7\66\2\2\u01ef")
        buf.write("A\3\2\2\2\u01f0\u01f1\7\65\2\2\u01f1C\3\2\2\2\u01f2\u01f4")
        buf.write("\7*\2\2\u01f3\u01f5\5F$\2\u01f4\u01f3\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5E\3\2\2\2\u01f6\u01f7\b$\1\2\u01f7\u01f8")
        buf.write("\5H%\2\u01f8\u01fe\3\2\2\2\u01f9\u01fa\f\4\2\2\u01fa\u01fb")
        buf.write("\7\36\2\2\u01fb\u01fd\5H%\2\u01fc\u01f9\3\2\2\2\u01fd")
        buf.write("\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2")
        buf.write("\u01ffG\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0202\b%\1\2")
        buf.write("\u0202\u0203\5J&\2\u0203\u0209\3\2\2\2\u0204\u0205\f\4")
        buf.write("\2\2\u0205\u0206\7\35\2\2\u0206\u0208\5J&\2\u0207\u0204")
        buf.write("\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2\u0209")
        buf.write("\u020a\3\2\2\2\u020aI\3\2\2\2\u020b\u0209\3\2\2\2\u020c")
        buf.write("\u020d\b&\1\2\u020d\u020e\5L\'\2\u020e\u0214\3\2\2\2\u020f")
        buf.write("\u0210\f\4\2\2\u0210\u0211\t\6\2\2\u0211\u0213\5L\'\2")
        buf.write("\u0212\u020f\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0212\3")
        buf.write("\2\2\2\u0214\u0215\3\2\2\2\u0215K\3\2\2\2\u0216\u0214")
        buf.write("\3\2\2\2\u0217\u0218\b\'\1\2\u0218\u0219\5N(\2\u0219\u021f")
        buf.write("\3\2\2\2\u021a\u021b\f\4\2\2\u021b\u021c\t\7\2\2\u021c")
        buf.write("\u021e\5N(\2\u021d\u021a\3\2\2\2\u021e\u0221\3\2\2\2\u021f")
        buf.write("\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220M\3\2\2\2\u0221")
        buf.write("\u021f\3\2\2\2\u0222\u0223\b(\1\2\u0223\u0224\5P)\2\u0224")
        buf.write("\u022a\3\2\2\2\u0225\u0226\f\4\2\2\u0226\u0227\t\b\2\2")
        buf.write("\u0227\u0229\5P)\2\u0228\u0225\3\2\2\2\u0229\u022c\3\2")
        buf.write("\2\2\u022a\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022bO\3")
        buf.write("\2\2\2\u022c\u022a\3\2\2\2\u022d\u022f\t\t\2\2\u022e\u022d")
        buf.write("\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2\u0230")
        buf.write("\u0231\3\2\2\2\u0231\u0233\3\2\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0233\u0236\5R*\2\u0234\u0236\5R*\2\u0235\u0230\3\2\2")
        buf.write("\2\u0235\u0234\3\2\2\2\u0236Q\3\2\2\2\u0237\u023b\5T+")
        buf.write("\2\u0238\u023b\5b\62\2\u0239\u023b\5Z.\2\u023a\u0237\3")
        buf.write("\2\2\2\u023a\u0238\3\2\2\2\u023a\u0239\3\2\2\2\u023bS")
        buf.write("\3\2\2\2\u023c\u023f\5f\64\2\u023d\u023f\5\\/\2\u023e")
        buf.write("\u023c\3\2\2\2\u023e\u023d\3\2\2\2\u023f\u0241\3\2\2\2")
        buf.write("\u0240\u0242\5V,\2\u0241\u0240\3\2\2\2\u0242\u0243\3\2")
        buf.write("\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244U\3")
        buf.write("\2\2\2\u0245\u0246\7\f\2\2\u0246\u0247\5F$\2\u0247\u0248")
        buf.write("\7\r\2\2\u0248W\3\2\2\2\u0249\u024d\5v<\2\u024a\u024d")
        buf.write("\5T+\2\u024b\u024d\5p9\2\u024c\u0249\3\2\2\2\u024c\u024a")
        buf.write("\3\2\2\2\u024c\u024b\3\2\2\2\u024d\u0259\3\2\2\2\u024e")
        buf.write("\u0251\7\21\2\2\u024f\u0252\5v<\2\u0250\u0252\5\\/\2\u0251")
        buf.write("\u024f\3\2\2\2\u0251\u0250\3\2\2\2\u0252\u0256\3\2\2\2")
        buf.write("\u0253\u0255\5V,\2\u0254\u0253\3\2\2\2\u0255\u0258\3\2")
        buf.write("\2\2\u0256\u0254\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u025a")
        buf.write("\3\2\2\2\u0258\u0256\3\2\2\2\u0259\u024e\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3\2\2\2")
        buf.write("\u025cY\3\2\2\2\u025d\u0261\5X-\2\u025e\u0261\5\\/\2\u025f")
        buf.write("\u0261\5f\64\2\u0260\u025d\3\2\2\2\u0260\u025e\3\2\2\2")
        buf.write("\u0260\u025f\3\2\2\2\u0261[\3\2\2\2\u0262\u0263\5v<\2")
        buf.write("\u0263\u0265\7\b\2\2\u0264\u0266\5^\60\2\u0265\u0264\3")
        buf.write("\2\2\2\u0265\u0266\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0268")
        buf.write("\7\t\2\2\u0268]\3\2\2\2\u0269\u026a\5F$\2\u026a\u026b")
        buf.write("\5`\61\2\u026b_\3\2\2\2\u026c\u026d\7\16\2\2\u026d\u026e")
        buf.write("\5F$\2\u026e\u026f\5`\61\2\u026f\u0272\3\2\2\2\u0270\u0272")
        buf.write("\3\2\2\2\u0271\u026c\3\2\2\2\u0271\u0270\3\2\2\2\u0272")
        buf.write("a\3\2\2\2\u0273\u027c\5\\/\2\u0274\u027c\5v<\2\u0275\u027c")
        buf.write("\5h\65\2\u0276\u027c\79\2\2\u0277\u0278\7\b\2\2\u0278")
        buf.write("\u0279\5F$\2\u0279\u027a\7\t\2\2\u027a\u027c\3\2\2\2\u027b")
        buf.write("\u0273\3\2\2\2\u027b\u0274\3\2\2\2\u027b\u0275\3\2\2\2")
        buf.write("\u027b\u0276\3\2\2\2\u027b\u0277\3\2\2\2\u027c\u027d\3")
        buf.write("\2\2\2\u027d\u0287\7\21\2\2\u027e\u0288\5\\/\2\u027f\u0283")
        buf.write("\5v<\2\u0280\u0282\5V,\2\u0281\u0280\3\2\2\2\u0282\u0285")
        buf.write("\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0284\3\2\2\2\u0284")
        buf.write("\u0288\3\2\2\2\u0285\u0283\3\2\2\2\u0286\u0288\5b\62\2")
        buf.write("\u0287\u027e\3\2\2\2\u0287\u027f\3\2\2\2\u0287\u0286\3")
        buf.write("\2\2\2\u0288c\3\2\2\2\u0289\u028d\5v<\2\u028a\u028c\5")
        buf.write("V,\2\u028b\u028a\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028b")
        buf.write("\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u0290\3\2\2\2\u028f")
        buf.write("\u028d\3\2\2\2\u0290\u0291\7\21\2\2\u0291\u0293\5F$\2")
        buf.write("\u0292\u0294\7\17\2\2\u0293\u0292\3\2\2\2\u0293\u0294")
        buf.write("\3\2\2\2\u0294e\3\2\2\2\u0295\u0296\7\b\2\2\u0296\u0297")
        buf.write("\5F$\2\u0297\u0298\7\t\2\2\u0298\u029c\3\2\2\2\u0299\u029c")
        buf.write("\5j\66\2\u029a\u029c\5h\65\2\u029b\u0295\3\2\2\2\u029b")
        buf.write("\u0299\3\2\2\2\u029b\u029a\3\2\2\2\u029cg\3\2\2\2\u029d")
        buf.write("\u029f\5\22\n\2\u029e\u02a0\5l\67\2\u029f\u029e\3\2\2")
        buf.write("\2\u029f\u02a0\3\2\2\2\u02a0i\3\2\2\2\u02a1\u02ad\7=\2")
        buf.write("\2\u02a2\u02ad\7?\2\2\u02a3\u02ad\7A\2\2\u02a4\u02ad\7")
        buf.write("B\2\2\u02a5\u02ad\7@\2\2\u02a6\u02ad\7>\2\2\u02a7\u02ad")
        buf.write("\79\2\2\u02a8\u02ad\7C\2\2\u02a9\u02ad\5p9\2\u02aa\u02ad")
        buf.write("\5v<\2\u02ab\u02ad\78\2\2\u02ac\u02a1\3\2\2\2\u02ac\u02a2")
        buf.write("\3\2\2\2\u02ac\u02a3\3\2\2\2\u02ac\u02a4\3\2\2\2\u02ac")
        buf.write("\u02a5\3\2\2\2\u02ac\u02a6\3\2\2\2\u02ac\u02a7\3\2\2\2")
        buf.write("\u02ac\u02a8\3\2\2\2\u02ac\u02a9\3\2\2\2\u02ac\u02aa\3")
        buf.write("\2\2\2\u02ac\u02ab\3\2\2\2\u02adk\3\2\2\2\u02ae\u02b1")
        buf.write("\7\n\2\2\u02af\u02b2\5j\66\2\u02b0\u02b2\5l\67\2\u02b1")
        buf.write("\u02af\3\2\2\2\u02b1\u02b0\3\2\2\2\u02b2\u02b3\3\2\2\2")
        buf.write("\u02b3\u02b4\5n8\2\u02b4\u02b5\7\13\2\2\u02b5\u02b6\5")
        buf.write("n8\2\u02b6m\3\2\2\2\u02b7\u02ba\7\16\2\2\u02b8\u02bb\5")
        buf.write("j\66\2\u02b9\u02bb\5l\67\2\u02ba\u02b8\3\2\2\2\u02ba\u02b9")
        buf.write("\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02bd\5n8\2\u02bd\u02c0")
        buf.write("\3\2\2\2\u02be\u02c0\3\2\2\2\u02bf\u02b7\3\2\2\2\u02bf")
        buf.write("\u02be\3\2\2\2\u02c0o\3\2\2\2\u02c1\u02c2\5v<\2\u02c2")
        buf.write("\u02c4\7\n\2\2\u02c3\u02c5\5r:\2\u02c4\u02c3\3\2\2\2\u02c4")
        buf.write("\u02c5\3\2\2\2\u02c5\u02c6\3\2\2\2\u02c6\u02c7\7\13\2")
        buf.write("\2\u02c7q\3\2\2\2\u02c8\u02c9\5v<\2\u02c9\u02ca\7\20\2")
        buf.write("\2\u02ca\u02cb\5F$\2\u02cb\u02cc\5t;\2\u02ccs\3\2\2\2")
        buf.write("\u02cd\u02ce\7\16\2\2\u02ce\u02d1\5r:\2\u02cf\u02d1\3")
        buf.write("\2\2\2\u02d0\u02cd\3\2\2\2\u02d0\u02cf\3\2\2\2\u02d1u")
        buf.write("\3\2\2\2\u02d2\u02d3\t\n\2\2\u02d3w\3\2\2\2\u02d4\u02d9")
        buf.write("\7\7\2\2\u02d5\u02d9\7\17\2\2\u02d6\u02d7\7\17\2\2\u02d7")
        buf.write("\u02d9\7\7\2\2\u02d8\u02d4\3\2\2\2\u02d8\u02d5\3\2\2\2")
        buf.write("\u02d8\u02d6\3\2\2\2\u02d9y\3\2\2\2X}\u0084\u0090\u0095")
        buf.write("\u009c\u00a2\u00b1\u00b7\u00bb\u00c2\u00c7\u00cc\u00d3")
        buf.write("\u00d9\u00e0\u00eb\u00f4\u00fa\u00ff\u0109\u010f\u0114")
        buf.write("\u011c\u0122\u0129\u012d\u0134\u013a\u0147\u014c\u0156")
        buf.write("\u015c\u0160\u0166\u016e\u0170\u0177\u017c\u017e\u0189")
        buf.write("\u0190\u0196\u019b\u01a2\u01a9\u01af\u01b6\u01b9\u01bf")
        buf.write("\u01c5\u01cb\u01d5\u01d9\u01ec\u01f4\u01fe\u0209\u0214")
        buf.write("\u021f\u022a\u0230\u0235\u023a\u023e\u0243\u024c\u0251")
        buf.write("\u0256\u025b\u0260\u0265\u0271\u027b\u0283\u0287\u028d")
        buf.write("\u0293\u029b\u029f\u02ac\u02b1\u02ba\u02bf\u02c4\u02d0")
        buf.write("\u02d8")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'index'", "'_'", "'value'", "<INVALID>", 
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
    RULE_statement = 21
    RULE_assignment = 22
    RULE_lhs = 23
    RULE_assignOp = 24
    RULE_ifstmt = 25
    RULE_elsestmt = 26
    RULE_forstmt = 27
    RULE_initFor = 28
    RULE_assignment_for = 29
    RULE_rangeFor = 30
    RULE_breakstmt = 31
    RULE_contstmt = 32
    RULE_returnstmt = 33
    RULE_expr = 34
    RULE_expr1 = 35
    RULE_expr2 = 36
    RULE_expr3 = 37
    RULE_expr4 = 38
    RULE_expr5 = 39
    RULE_expr6 = 40
    RULE_arrayElement = 41
    RULE_index = 42
    RULE_structField = 43
    RULE_expr7 = 44
    RULE_funcCall = 45
    RULE_arguments = 46
    RULE_argTail = 47
    RULE_methodCallExpr = 48
    RULE_methodCall = 49
    RULE_expr8 = 50
    RULE_arrayInit = 51
    RULE_literal = 52
    RULE_arrayLit = 53
    RULE_literalTail = 54
    RULE_structLit = 55
    RULE_structElement = 56
    RULE_elementTail = 57
    RULE_identifier = 58
    RULE_endStmt = 59

    ruleNames =  [ "program", "declarations", "declare", "declareTail", 
                   "constDeclare", "varDeclare", "modify", "varType", "arrayType", 
                   "dimensions", "init", "typeDeclare", "structDeclare", 
                   "field", "interfaceDeclare", "method", "parameters", 
                   "paraTail", "funcDeclare", "methodDeclare", "stmt", "statement", 
                   "assignment", "lhs", "assignOp", "ifstmt", "elsestmt", 
                   "forstmt", "initFor", "assignment_for", "rangeFor", "breakstmt", 
                   "contstmt", "returnstmt", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "arrayElement", "index", "structField", 
                   "expr7", "funcCall", "arguments", "argTail", "methodCallExpr", 
                   "methodCall", "expr8", "arrayInit", "literal", "arrayLit", 
                   "literalTail", "structLit", "structElement", "elementTail", 
                   "identifier", "endStmt" ]

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
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 120
                self.match(MiniGoParser.NL)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.declarations()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 127
                self.match(MiniGoParser.NL)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
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
            self.state = 135
            self.declare()
            self.state = 136
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
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.constDeclare()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.varDeclare()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.typeDeclare()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 141
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
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 144
                    self.match(MiniGoParser.NL)
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 150
                self.declare()
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 151
                        self.match(MiniGoParser.NL) 
                    self.state = 156
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 157
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
            self.state = 162
            self.match(MiniGoParser.CONST)
            self.state = 163
            self.identifier()
            self.state = 164
            self.init()
            self.state = 165
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
            self.state = 167
            self.match(MiniGoParser.VAR)
            self.state = 168
            self.identifier()
            self.state = 169
            self.modify()
            self.state = 170
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


        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LP]:
                    self.state = 172
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 173
                    self.varType()
                    pass
                elif token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.ID]:
                    self.state = 174
                    self.identifier()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LP]:
                    self.state = 178
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 179
                    self.varType()
                    pass
                elif token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.ID]:
                    self.state = 180
                    self.identifier()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 183
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
            self.state = 187
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
            self.state = 190 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 189
                self.dimensions()
                self.state = 192 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LP):
                    break

            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 194
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 195
                self.match(MiniGoParser.STRUCT)
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.ID]:
                self.state = 196
                self.identifier()
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
            self.state = 199
            self.match(MiniGoParser.LP)
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTLIT]:
                self.state = 200
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.ID]:
                self.state = 201
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 204
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
            self.state = 206
            self.match(MiniGoParser.INITOP)
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 207
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 208
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
            self.state = 211
            self.match(MiniGoParser.TYPE)
            self.state = 212
            self.identifier()
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 213
                self.structDeclare()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 214
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
            self.state = 217
            self.match(MiniGoParser.STRUCT)
            self.state = 218
            self.match(MiniGoParser.LC)
            self.state = 220 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 219
                self.field()
                self.state = 222 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 224
            self.match(MiniGoParser.RC)
            self.state = 225
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierContext,i)


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
            self.state = 227
            self.identifier()
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 228
                self.varType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 229
                self.structDeclare()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 230
                self.arrayType()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 231
                self.interfaceDeclare()
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.ID]:
                self.state = 232
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 235
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
            self.state = 237
            self.match(MiniGoParser.INTERFACE)
            self.state = 238
            self.match(MiniGoParser.LC)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 239
                self.match(MiniGoParser.NL)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 245
                self.method()
                self.state = 248 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 251 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 250
                self.endStmt()
                self.state = 253 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                    break

            self.state = 255
            self.match(MiniGoParser.RC)
            self.state = 256
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

        def parameters(self):
            return self.getTypedRuleContext(MiniGoParser.ParametersContext,0)


        def paraTail(self):
            return self.getTypedRuleContext(MiniGoParser.ParaTailContext,0)


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
        self.enterRule(localctx, 30, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.identifier()
            self.state = 259
            self.match(MiniGoParser.LB)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.ID))) != 0):
                self.state = 260
                self.parameters()
                self.state = 261
                self.paraTail()


            self.state = 265
            self.match(MiniGoParser.RB)
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 266
                self.varType()

            elif la_ == 2:
                self.state = 267
                self.arrayType()

            elif la_ == 3:
                self.state = 268
                self.identifier()


            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 271
                    self.endStmt() 
                self.state = 276
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
            self.state = 277
            self.identifier()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 278
                self.match(MiniGoParser.COMMA)
                self.state = 279
                self.identifier()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 285
                self.varType()
                pass
            elif token in [MiniGoParser.LP]:
                self.state = 286
                self.arrayType()
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.ID]:
                self.state = 287
                self.identifier()
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
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(MiniGoParser.COMMA)
                self.state = 291
                self.parameters()
                self.state = 292
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
            self.state = 297
            self.match(MiniGoParser.FUNC)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LB:
                self.state = 298
                self.methodDeclare()


            self.state = 301
            self.method()
            self.state = 302
            self.match(MiniGoParser.LC)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 303
                self.match(MiniGoParser.NL)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 309
                self.stmt()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 315
            self.match(MiniGoParser.RC)
            self.state = 316
            self.endStmt()
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
        self.enterRule(localctx, 38, self.RULE_methodDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(MiniGoParser.LB)
            self.state = 319
            self.identifier()
            self.state = 320
            self.identifier()
            self.state = 321
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
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.VAR]:
                    self.state = 323
                    self.varDeclare()
                    pass
                elif token in [MiniGoParser.CONST]:
                    self.state = 324
                    self.constDeclare()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.statement()
                self.state = 328
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
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 335
                self.breakstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 336
                self.contstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 337
                self.funcCall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 338
                self.methodCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 339
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
        self.enterRule(localctx, 44, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.lhs()
            self.state = 344 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 343
                self.assignOp()
                self.state = 346 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADDASS) | (1 << MiniGoParser.SUBASS) | (1 << MiniGoParser.MULASS) | (1 << MiniGoParser.DIVASS) | (1 << MiniGoParser.MODASS))) != 0)):
                    break

            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 348
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 349
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierContext,i)


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
        self.enterRule(localctx, 46, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.identifier()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.LP:
                    self.state = 353
                    self.index()
                    self.state = 358
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 359
                    self.identifier()
                    pass

                elif la_ == 2:
                    self.state = 360
                    self.identifier()
                    self.state = 362 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 361
                        self.index()
                        self.state = 364 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==MiniGoParser.LP):
                            break

                    pass


                self.state = 376 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 368
                    self.match(MiniGoParser.DOT)
                    self.state = 369
                    self.identifier()
                    self.state = 373
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MiniGoParser.LP:
                        self.state = 370
                        self.index()
                        self.state = 375
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 378 
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
        self.enterRule(localctx, 48, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
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
        self.enterRule(localctx, 50, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.IF)
            self.state = 385
            self.match(MiniGoParser.LB)
            self.state = 386
            self.expr(0)
            self.state = 387
            self.match(MiniGoParser.RB)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 388
                self.match(MiniGoParser.NL)
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 394
            self.match(MiniGoParser.LC)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 395
                self.match(MiniGoParser.NL)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 401
                self.stmt()
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 407
            self.match(MiniGoParser.RC)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 408
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
            self.state = 411
            self.match(MiniGoParser.ELSE)
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF]:
                self.state = 412
                self.ifstmt()
                pass
            elif token in [MiniGoParser.NL, MiniGoParser.LC]:
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 413
                    self.match(MiniGoParser.NL)
                    self.state = 418
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 419
                self.match(MiniGoParser.LC)
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NL:
                    self.state = 420
                    self.match(MiniGoParser.NL)
                    self.state = 425
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 426
                    self.stmt()
                    self.state = 431
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 432
                self.match(MiniGoParser.RC)
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 433
                        self.match(MiniGoParser.NL) 
                    self.state = 438
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
            self.state = 441
            self.match(MiniGoParser.FOR)
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 442
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 443
                self.initFor()
                pass

            elif la_ == 3:
                self.state = 444
                self.rangeFor()
                pass


            self.state = 447
            self.match(MiniGoParser.LC)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NL:
                self.state = 448
                self.match(MiniGoParser.NL)
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 454
                self.stmt()
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 460
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
        self.enterRule(localctx, 56, self.RULE_initFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 462
                self.assignment_for()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 463
                self.match(MiniGoParser.VAR)
                self.state = 464
                self.identifier()
                self.state = 467
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 465
                    self.varType()
                    pass
                elif token in [MiniGoParser.LP]:
                    self.state = 466
                    self.arrayType()
                    pass
                elif token in [MiniGoParser.INITOP]:
                    pass
                else:
                    pass
                self.state = 469
                self.init()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 473
            self.endStmt()
            self.state = 474
            self.expr(0)
            self.state = 475
            self.endStmt()
            self.state = 476
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
        self.enterRule(localctx, 58, self.RULE_assignment_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(MiniGoParser.ID)
            self.state = 479
            self.assignOp()
            self.state = 480
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


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
        self.enterRule(localctx, 60, self.RULE_rangeFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 483
            self.match(MiniGoParser.COMMA)
            self.state = 484
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__1 or _la==MiniGoParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 485
            self.match(MiniGoParser.ASSIGN)
            self.state = 486
            self.match(MiniGoParser.RANGE)
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 487
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 488
                self.literal()
                pass

            elif la_ == 3:
                self.state = 489
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
        self.enterRule(localctx, 62, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
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
        self.enterRule(localctx, 64, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
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
        self.enterRule(localctx, 66, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(MiniGoParser.RETURN)
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY))) != 0) or _la==MiniGoParser.OCTAL or _la==MiniGoParser.STRINGLIT:
                self.state = 497
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 508
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 503
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 504
                    self.match(MiniGoParser.OR)
                    self.state = 505
                    self.expr1(0) 
                self.state = 510
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 519
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 514
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 515
                    self.match(MiniGoParser.AND)
                    self.state = 516
                    self.expr2(0) 
                self.state = 521
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 530
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 525
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 526
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.UNEQ) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESSEQ) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATEREQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 527
                    self.expr3(0) 
                self.state = 532
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 541
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 536
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 537
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUBTR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 538
                    self.expr4(0) 
                self.state = 543
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 552
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 547
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 548
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 549
                    self.expr5() 
                self.state = 554
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT:
                    self.state = 555
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.SUBTR or _la==MiniGoParser.NOT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 560
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 561
                self.expr6()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
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
        self.enterRule(localctx, 80, self.RULE_expr6)
        try:
            self.state = 568
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.arrayElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.methodCallExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 567
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
        self.enterRule(localctx, 82, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 570
                self.expr8()
                pass

            elif la_ == 2:
                self.state = 571
                self.funcCall()
                pass


            self.state = 575 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 574
                    self.index()

                else:
                    raise NoViableAltException(self)
                self.state = 577 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(MiniGoParser.LP)
            self.state = 580
            self.expr(0)
            self.state = 581
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierContext,i)


        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def funcCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncCallContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncCallContext,i)


        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructField" ):
                return visitor.visitStructField(self)
            else:
                return visitor.visitChildren(self)




    def structField(self):

        localctx = MiniGoParser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 583
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 584
                self.arrayElement()
                pass

            elif la_ == 3:
                self.state = 585
                self.structLit()
                pass


            self.state = 599 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 588
                    self.match(MiniGoParser.DOT)
                    self.state = 591
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                    if la_ == 1:
                        self.state = 589
                        self.identifier()
                        pass

                    elif la_ == 2:
                        self.state = 590
                        self.funcCall()
                        pass


                    self.state = 596
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 593
                            self.index() 
                        self.state = 598
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,67,self._ctx)


                else:
                    raise NoViableAltException(self)
                self.state = 601 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_expr7)
        try:
            self.state = 606
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                self.structField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
                self.funcCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 605
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
        self.enterRule(localctx, 90, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.identifier()
            self.state = 609
            self.match(MiniGoParser.LB)
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SUBTR) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.DECIMAL) | (1 << MiniGoParser.HEXADECIMAL) | (1 << MiniGoParser.BINARY))) != 0) or _la==MiniGoParser.OCTAL or _la==MiniGoParser.STRINGLIT:
                self.state = 610
                self.arguments()


            self.state = 613
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
        self.enterRule(localctx, 92, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.expr(0)
            self.state = 616
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
        self.enterRule(localctx, 94, self.RULE_argTail)
        try:
            self.state = 623
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                self.match(MiniGoParser.COMMA)
                self.state = 619
                self.expr(0)
                self.state = 620
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


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IdentifierContext,i)


        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


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


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCallExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallExpr" ):
                return visitor.visitMethodCallExpr(self)
            else:
                return visitor.visitChildren(self)




    def methodCallExpr(self):

        localctx = MiniGoParser.MethodCallExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_methodCallExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.state = 625
                self.funcCall()
                pass

            elif la_ == 2:
                self.state = 626
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 627
                self.arrayInit()
                pass

            elif la_ == 4:
                self.state = 628
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 5:
                self.state = 629
                self.match(MiniGoParser.LB)
                self.state = 630
                self.expr(0)
                self.state = 631
                self.match(MiniGoParser.RB)
                pass


            self.state = 635
            self.match(MiniGoParser.DOT)
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.state = 636
                self.funcCall()
                pass

            elif la_ == 2:
                self.state = 637
                self.identifier()
                self.state = 641
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 638
                        self.index() 
                    self.state = 643
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

                pass

            elif la_ == 3:
                self.state = 644
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

        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


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
        self.enterRule(localctx, 98, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.identifier()
            self.state = 651
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LP:
                self.state = 648
                self.index()
                self.state = 653
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 654
            self.match(MiniGoParser.DOT)
            self.state = 655
            self.expr(0)
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 656
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
        self.enterRule(localctx, 100, self.RULE_expr8)
        try:
            self.state = 665
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self.match(MiniGoParser.LB)
                self.state = 660
                self.expr(0)
                self.state = 661
                self.match(MiniGoParser.RB)
                pass
            elif token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 663
                self.literal()
                pass
            elif token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 664
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
        self.enterRule(localctx, 102, self.RULE_arrayInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.arrayType()
            self.state = 669
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 668
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


        def identifier(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierContext,0)


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
        self.enterRule(localctx, 104, self.RULE_literal)
        try:
            self.state = 682
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 671
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 672
                self.match(MiniGoParser.DECIMAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 673
                self.match(MiniGoParser.BINARY)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 674
                self.match(MiniGoParser.OCTAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 675
                self.match(MiniGoParser.HEXADECIMAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 676
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 677
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 678
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 679
                self.structLit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 680
                self.identifier()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 681
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
        self.enterRule(localctx, 106, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.match(MiniGoParser.LC)
            self.state = 687
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                self.state = 685
                self.literal()
                pass
            elif token in [MiniGoParser.LC]:
                self.state = 686
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 689
            self.literalTail()
            self.state = 690
            self.match(MiniGoParser.RC)
            self.state = 691
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
        self.enterRule(localctx, 108, self.RULE_literalTail)
        try:
            self.state = 701
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 693
                self.match(MiniGoParser.COMMA)
                self.state = 696
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.T__0, MiniGoParser.T__2, MiniGoParser.NIL, MiniGoParser.BOOLLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.DECIMAL, MiniGoParser.HEXADECIMAL, MiniGoParser.BINARY, MiniGoParser.OCTAL, MiniGoParser.STRINGLIT]:
                    self.state = 694
                    self.literal()
                    pass
                elif token in [MiniGoParser.LC]:
                    self.state = 695
                    self.arrayLit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 698
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
        self.enterRule(localctx, 110, self.RULE_structLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 703
            self.identifier()
            self.state = 704
            self.match(MiniGoParser.LC)
            self.state = 706
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.ID))) != 0):
                self.state = 705
                self.structElement()


            self.state = 708
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
        self.enterRule(localctx, 112, self.RULE_structElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710
            self.identifier()
            self.state = 711
            self.match(MiniGoParser.COLON)
            self.state = 712
            self.expr(0)
            self.state = 713
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
        self.enterRule(localctx, 114, self.RULE_elementTail)
        try:
            self.state = 718
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 715
                self.match(MiniGoParser.COMMA)
                self.state = 716
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
        self.enterRule(localctx, 116, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.ID))) != 0)):
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
        self.enterRule(localctx, 118, self.RULE_endStmt)
        try:
            self.state = 726
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 722
                self.match(MiniGoParser.NL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 723
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 724
                self.match(MiniGoParser.SEMICOLON)
                self.state = 725
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
        self._predicates[34] = self.expr_sempred
        self._predicates[35] = self.expr1_sempred
        self._predicates[36] = self.expr2_sempred
        self._predicates[37] = self.expr3_sempred
        self._predicates[38] = self.expr4_sempred
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
         




