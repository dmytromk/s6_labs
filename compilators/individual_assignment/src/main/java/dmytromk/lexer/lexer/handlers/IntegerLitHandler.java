package dmytromk.lexer.lexer.handlers;

import dmytromk.lexer.lexer.token.Token;
import dmytromk.lexer.lexer.token.TokenType;

public class IntegerLitHandler extends Handler {
    @Override
    protected boolean includeLastChar() {
        return false;
    }

    @Override
    protected HandlingStatus appendCharQuery(char ch) {
        if (Helper.isLetter(ch)) {
            return HandlingStatus.REJECTED;
        }
        if (!Helper.isDigit(ch)) {
            return HandlingStatus.ACCEPTED;
        }
        return HandlingStatus.WAITING;
    }

    @Override
    protected HandlingStatus appendEOFQuery() {
        return appendCharQuery(' ');
    }

    @Override
    protected int numCharsConsumedQuery() {
        return accumulatorString().length();
    }

    @Override
    protected Token getTokenQuery() {
        return new Token(TokenType.INTEGER_LIT, accumulatorString());
    }

    @Override
    protected void resetQuery() {
    }
}
