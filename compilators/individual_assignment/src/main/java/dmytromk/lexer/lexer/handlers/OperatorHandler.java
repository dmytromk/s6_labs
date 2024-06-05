package dmytromk.lexer.lexer.handlers;

import dmytromk.lexer.lexer.token.Token;
import dmytromk.lexer.lexer.token.TokenType;

public class OperatorHandler extends SequenceHandler {
    public OperatorHandler() {
        super(LexemesSource.OPERATORS, ' ');
    }

    @Override
    protected Token getTokenQuery() {
        return new Token(TokenType.OPERATOR, accumulatorString().substring(0, numCharsConsumed()));
    }
}
