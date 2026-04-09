#type:ignore
from mark import parser,runner
import ctypes
import sys

if sys.platform == "win32":
    libc = ctypes.cdll.msvcrt
else:
    libc = ctypes.cdll.LoadLibrary("libc.so.6")

libc.printf.argtypes = [ctypes.c_char_p]
libc.printf.restype = ctypes.c_int

def c_printf(text):
    if isinstance(text, str):
        text = text.encode("utf-8")
    libc.printf(text)

class lang(runner):
    def __init__(self):
        pass
    def prinst(self,itens):
        if itens[0].type == "str":
            c_printf(f"{itens[0]}\n")
        else:
            self.error("Expected a string")

psr = parser("lexer.mark",lang)
code = """
print("1")
print("2")
"""
psr.run(code)
#resultado:
#1
#2