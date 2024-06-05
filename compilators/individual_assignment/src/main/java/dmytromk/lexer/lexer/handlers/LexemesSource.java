package dmytromk.lexer.lexer.handlers;

import java.util.List;

public class LexemesSource {
    public static final List<String> KEYWORDS = List.of(
            "array", "begin", "case", "const", "do", "downto", "else", "end", "file", "for", "function",
            "goto", "if", "label", "nil", "of", "packed", "procedure", "program", "record", "repeat",
            "set", "then", "to", "type", "until", "var", "while", "with", "abs", "arctan", "boolean",
            "char", "chr", "cos", "dispose", "eof", "eoln", "exp", "false", "get", "input", "integer",
            "ln", "maxint", "new", "odd", "ord", "output", "pack", "page", "pred", "put", "read",
            "readln", "real", "reset", "rewrite", "round", "sin", "sqr", "sqrt", "succ", "text", "true",
            "trunc", "unpack", "write", "writeln");

    public static final List<String> OPERATORS = List.of(
            "+", "-", "*", "/", "div", "mod", "=", "<", ">", "<>", "<=", ">=", "in", "and", "or", "not");

    public static final List<String> PUNCTUATION = List.of(
            "[", "]", ".", ",", ":", ";", "(", ")", "..", "^", ":=");

    public static final List<String> LEFT_COMMENTS = List.of(
            "{", "(*");

    public static final List<String> RIGHT_COMMENTS = List.of(
            "}", "*)");
}
