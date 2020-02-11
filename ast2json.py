import ast
import sys
from os import path
import ntpath

def process_node(node):
    

def conv_ast(s,fname):
    tree = ast.parse(s, filename=fname)


if len(sys.argv) > 1:
    path = sys.argv[1]
    with open(path) as f:
        conv_ast(f.read(), path.basename(path))
else:
    print("Needs source filepath as argument")