package dmytromk.lexer.lexer.handlers;

import dmytromk.lexer.lexer.token.Token;
import dmytromk.lexer.lexer.token.TokenType;

public class PunctuationHandler extends SequenceHandler {
    public PunctuationHandler() {
        super(LexemesSource.PUNCTUATION, ' ');
    }

    @Override
    protected Token getTokenQuery() {
        return new Token(TokenType.PUNCTUATION, accumulatorString().substring(0, numCharsConsumed()));
    }
}
