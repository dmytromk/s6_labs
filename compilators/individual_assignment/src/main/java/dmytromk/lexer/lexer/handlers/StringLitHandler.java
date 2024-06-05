package dmytromk.lexer.lexer.handlers;

import dmytromk.lexer.lexer.exceptions.LexicalException;
import dmytromk.lexer.lexer.token.Token;
import dmytromk.lexer.lexer.token.TokenType;

public class StringLitHandler extends Handler {
    private boolean inString = false;

    @Override
    protected HandlingStatus appendCharQuery(char ch) throws LexicalException {
        if (ch == '\'') {
            if (!inString) {
                inString = true;
                return HandlingStatus.WAITING;
            }
            return HandlingStatus.ACCEPTED;
        }
        if (inString) {
            if (ch == '\n') {
                throw new LexicalException("Unclosed string literal.");
            }
            return HandlingStatus.WAITING;
        }
        return HandlingStatus.REJECTED;
    }

    @Override
    protected HandlingStatus appendEOFQuery() throws LexicalException {
        return appendCharQuery('\n');
    }

    @Override
    protected int numCharsConsumedQuery() {
        return accumulatorString().length();
    }

    @Override
    protected Token getTokenQuery() {
        return new Token(TokenType.STRING_LIT, accumulatorString());
    }

    @Override
    protected void resetQuery() {
        inString = false;
    }
}
