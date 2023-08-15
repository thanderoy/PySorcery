# 🐍🔮 PyScorcery

> Part of the build-your-own-x.

PySorcery is a Python interpreter written in Python. (gcc is also a C compiler written in C 🌚)
It's slow & not optimized. The goal here is more of learnig about the workings of an interpreter.

## 👉 Note

The PySorcery Interpreter is a *virtual machine* (softwre that emulates a physical computer). This in particualer is a stack machine (uses a last-in, first-out stack to hold short-lived temporary values).

The PySorcery Interpreter is a *byte-code interpreter* (input instruction sets are called bytecodes). The interpreter operates on the byte-code generated by the *lexer, parser & compiler*
> Bytecode to Python is like Assembly to C
