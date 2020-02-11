import sys
from os import path
from ast2json import json_ast

if __name__ == "__main__":
    if len(sys.argv) > 1:
        spath = sys.argv[1]
        with open(spath) as f:
            print(json_ast(f.read(), path.basename(spath)))
    else:
        print("Needs source filepath as argument")