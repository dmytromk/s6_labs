package dmytromk.lexer.lexer.exceptions;

import dmytromk.lexer.lexer.token.Token;
import dmytromk.lexer.lexer.token.TokenType;

public class LexicalException extends Exception {
    public LexicalException(String message) {
        super(message);
    }

    public Token getToken() {
        return new Token(TokenType.ERROR, getMessage());
    }
}
