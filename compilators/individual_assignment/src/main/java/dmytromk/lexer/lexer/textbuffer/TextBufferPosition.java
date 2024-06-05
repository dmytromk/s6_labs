package dmytromk.lexer.lexer.textbuffer;

import dmytromk.lexer.lexer.token.position.Position;
import dmytromk.lexer.lexer.token.position.PositionBuilder;

public class TextBufferPosition {
    private int index;
    private final PositionBuilder position;

    public TextBufferPosition() {
        this.index = 0;
        this.position = new PositionBuilder(1, 1);
    }

    public TextBufferPosition(TextBufferPosition textBufferPosition) {
        this.index = textBufferPosition.getIndex();
        this.position = new PositionBuilder(textBufferPosition.getPosition());
    }

    public int getIndex() {
        return index;
    }

    public Position getPosition() {
        return position.build();
    }

    public void nextIndex() {
        index++;
    }

    public void nextColumn() {
        position.setColumn(position.getColumn() + 1);
    }

    public void nextLine() {
        position.setLine(position.getLine() + 1);
        position.setColumn(1);
    }
}
