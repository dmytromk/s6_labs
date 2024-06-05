package dmytromk.lexer.lexer.handlers;

import java.util.List;

public class Helper {
    static private final List<Character> separators = List.of(' ', '\t', '\n', '\r');

    static public boolean isDigit(char ch) {
        return ch >= '0' && ch <= '9';
    }

    static public boolean isLetter(char ch) {
        return ( ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
    }

    static public boolean isSeparator(char ch) {
        return separators.contains(ch);
    }
}
