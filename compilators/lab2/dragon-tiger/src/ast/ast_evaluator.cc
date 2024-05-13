#include "ast_evaluator.hh"
#include "../utils/errors.hh"

namespace ast {

int ASTEvaluator::visit(const IntegerLiteral &literal) {
  return literal.value;
}

int ASTEvaluator::visit(const StringLiteral &literal) {
  utils::error("String cannot be evaluated");
}

int ASTEvaluator::visit(const BinaryOperator &binop) {
  int left_part = binop.get_left().accept(*this);
  int right_part = binop.get_right().accept(*this);

  switch (binop.op) {
    case o_plus:
        return left_part + right_part;
    case o_minus:
        return left_part - right_part;
    case o_times:
        return left_part * right_part;
    case o_divide:
        return left_part / right_part;
    case o_eq:
        return left_part == right_part;
    case o_neq:
        return left_part != right_part;
    case o_gt:
        return left_part > right_part;
    case o_ge:
        return left_part >= right_part;
    case o_lt:
        return left_part < right_part;
    case o_le:
        return left_part <= right_part;
    default:
        utils::error("Binary operator cannot be recognized");
  }
}

int ASTEvaluator::visit(const Sequence &seqExpr) {
    int result;
    const auto exprs = seqExpr.get_exprs();

    if (exprs.cbegin() == exprs.cend()) {
        utils::error("Empty sequence cannot be evaluated");
    }

    for (auto expr = exprs.cbegin(); expr < exprs.cend(); expr++) {
        result = (*expr)->accept(*this);
    }
    
    return result;
}

int ASTEvaluator::visit(const Let &let) {
  utils::error("Let operators are not implemented");
}

int ASTEvaluator::visit(const Identifier &id) {
  utils::error("Identifiers are not implemented");
}

int ASTEvaluator::visit(const IfThenElse &ite) {
    if (ite.get_condition().accept(*this)) {
        return ite.get_then_part().accept(*this);
    }
    else {
        return ite.get_else_part().accept(*this);
    }
}

int ASTEvaluator::visit(const VarDecl &decl) {
  utils::error("Variable declarations are not implemented");
}

int ASTEvaluator::visit(const FunDecl &decl) {
  utils::error("Function declarations are not implemented");
}

int ASTEvaluator::visit(const FunCall &call) {
  utils::error("Function calls are not implemented");
}

int ASTEvaluator::visit(const WhileLoop &loop) {
  utils::error("While loops are not implemented");
}

int ASTEvaluator::visit(const ForLoop &loop) {
  utils::error("For loops are not implemented");
}

int ASTEvaluator::visit(const Break &brk) {
  utils::error("Break is not implemented");
}

int ASTEvaluator::visit(const Assign &assign) {
  utils::error("Assignment operator is not implemented");
}

} // namespace ast
