package dmytromk.lexer.lexer.textbuffer;

import dmytromk.lexer.lexer.token.position.Position;

import java.util.NoSuchElementException;

public class TextBuffer {
    private final String text;
    private TextBufferPosition currentPosition;
    private TextBufferPosition rememberedPosition;

    public TextBuffer(String text) {
        this.text = text;
        this.currentPosition = new TextBufferPosition();
        this.rememberedPosition = new TextBufferPosition();
    }

    private void updateOnCurrent() {
        if (hasChar()) {
            char ch = getChar();
            if (ch == '\n') {
                currentPosition.nextLine();
            } else {
                currentPosition.nextColumn();
            }
        }
    }

    public boolean hasChar() {
        return currentPosition.getIndex() < text.length();
    }

    public Character getChar() {
        return text.charAt(currentPosition.getIndex());
    }

    public void next() {
        if (hasChar()) {
            updateOnCurrent();
            currentPosition.nextIndex();
        } else {
            throw new NoSuchElementException();
        }
    }

    public void jump(int chars) {
        for (int i = 0; i < chars; i++) {
            next();
        }
    }

    public void rememberPosition() {
        rememberedPosition = new TextBufferPosition(currentPosition);
    }

    public void restorePosition() {
        currentPosition = new TextBufferPosition(rememberedPosition);
    }

    public Position currentPosition() {
        return currentPosition.getPosition();
    }

    public Position rememberedPosition() {
        return rememberedPosition.getPosition();
    }
}