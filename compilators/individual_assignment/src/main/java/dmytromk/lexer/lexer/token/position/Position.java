package dmytromk.lexer.lexer.token.position;

public record Position(int line, int column) {
    public Position(PositionBuilder builder) {
        this(builder.getLine(), builder.getColumn());
    }

    @Override
    public String toString() {
        return line + ":" + column;
    }
}
