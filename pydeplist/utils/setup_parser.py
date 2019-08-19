import ast

def get_func_call(tree):
    for node in tree.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            func_call = node.value
            if  isinstance(func_call.func, ast.Name) and func_call.func.id == 'setup':
                return func_call
    return None


def get_func_param(func_call):
    for keyword in func_call.keywords:
        if keyword.arg == 'install_requires':
            return keyword.value.id
    return None


def get_install_requires(file_path='setup.py'):
    print(file_path)
    with open(file_path, "r") as source:
        tree = ast.parse(source.read())
    
    func_call = get_func_call(tree)
    if func_call == None:
        for node in tree.body:
            print(ast.dump(node))
            if (isinstance(node, ast.If) 
                and (isinstance(node.test.left, ast.Name))
                and (node.test.left.id=='__name__')):
                func_call = get_func_call(node)

    requires_def_name = get_func_param(func_call)

    for node in tree.body:
        if isinstance(node, ast.Assign) and node.targets[0].id == requires_def_name:
            return [ ele.s for ele in node.value.elts ]

    return None

# install_requires = get_install_requires()
# print(install_requires)