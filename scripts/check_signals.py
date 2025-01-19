import ast
import sys


class SignalCheckVisitor(ast.NodeVisitor):
    def __init__(self):
        self.unused_signals = []

    def visit_ClassDef(self, node):
        for stmt in node.body:
            if isinstance(stmt, ast.Assign) and any(
                isinstance(value, ast.Call) and value.func.id == "Signal"
                for value in stmt.value.args
            ):
                signal_name = stmt.targets[0].id
                if signal_name not in ast.dump(node):
                    self.unused_signals.append(signal_name)

        self.generic_visit(node)


def main():
    for filename in sys.argv[1:]:
        with open(filename) as file:
            tree = ast.parse(file.read(), filename=filename)
            visitor = SignalCheckVisitor()
            visitor.visit(tree)

        if visitor.unused_signals:
            print(f"Unused signals in {filename}: {visitor.unused_signals}")
            sys.exit(1)


if __name__ == "__main__":
    main()
