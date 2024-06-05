package dmytromk.lexer.lexer.token;

public enum TokenType {
    KEYWORD,
    OPERATOR,
    PUNCTUATION,

    IDENTIFIER,
    COMMENT,

    REAL_LIT,
    INTEGER_LIT,
    STRING_LIT,

    ERROR
}
