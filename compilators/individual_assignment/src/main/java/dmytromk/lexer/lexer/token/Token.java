package dmytromk.lexer.lexer.token;

public class Token {
    protected final TokenType type;
    protected final String value;

    public Token(TokenType type, String value) {
        this.type = type;
        this.value = value;
    }

    public Token(Token token) {
        this.type = token.getType();
        this.value = token.getValue();
    }

    public TokenType getType() {
        return type;
    }

    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return type + ": " + value;
    }
}
