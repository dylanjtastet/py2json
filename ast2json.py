import ast
import json

#Convert python code string to json ast
def json_ast(s,fname="Unknown"):
    seen = {}

    # Recursive helper, converts one node
    def process_node(node):
        if node in seen:
            return {"ast2json_nodetype":"ast2json_reference", "ast2json_ref":seen[node]}
        out = {}
        h = hash(node)
        seen[node] = h
        out["ast2json_nodetype"] = type(node).__name__
        out["ast2json_id"] = h
        for f in ast.iter_fields(node):
            val = None
            if isinstance(f[1], ast.AST):
                val = process_node(f[1])
            elif isinstance(f[1], list):
                ol = []
                for item in f[1]:
                    ol.append(process_node(item) if isinstance(item, ast.AST) else item)
                val = ol
            elif isinstance(f[1], dict):
                od = {}
                for key in f[1]:
                    item = f[1][key]
                    od[key] = process_node(item) if isinstance(item, ast.AST) else item
                val = od
            else:
                val = f[1]

            out[f[0]] = val
        
        return out

    #Convert string to ast object and pass to helper
    tree = ast.parse(s, filename=fname)
    obj = process_node(tree)
    return json.dumps(obj)
