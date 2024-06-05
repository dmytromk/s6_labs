package dmytromk.lexer.lexer.token.position;

public class PositionBuilder {
    private int line, column;

    public PositionBuilder(int line, int column) {
        this.line = line;
        this.column = column;
    }

    public PositionBuilder(PositionBuilder builder) {
        this.line = builder.line;
        this.column = builder.column;
    }

    public PositionBuilder(Position position) {
        this.line = position.line();
        this.column = position.column();
    }

    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }

    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }

    public Position build() {
        return new Position(this);
    }
}
