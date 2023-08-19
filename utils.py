def dict_to_equation(node):
    if "children" in node:
        children = node["children"]
        left_child = dict_to_equation(children[0])
        
        if len(children) > 1:  # Check if there's a right child
            right_child = dict_to_equation(children[1])
        
        if node["type"] == "add":
            return f"{left_child} + {right_child}"
        elif node["type"] == "sub":
            return f"{left_child} - {right_child}"
        elif node["type"] == "mul":
            return f"{left_child} \\times {right_child}"
        elif node["type"] == "div":
            return f"{left_child} \\div {right_child}"
        elif node["type"] == "frac":
            return "\\frac{"+f"{left_child}" + "}{" f"{right_child}" +"}"
        elif node["type"] == "pow":
            return f"{left_child} ^ {right_child}"
        elif node["type"] == "endequals":
            return f"{left_child} ="
        elif node["type"] == "negative":
            return f"-{left_child}"
        elif node["type"] == "bracket":
            return f"({left_child})"
        elif node["type"] == "gt":
            return f"{left_child} > {right_child}" 
        elif node["type"] == "gte":
            return f"{left_child} \geq {right_child}"
        elif node["type"] == "lt":
            return f"{left_child} < {right_child}"
        elif node["type"] == "lte":
            return f"{left_child} \leq {right_child}"    
        elif node["type"] == "percentage":
            return f"{left_child}%"
        elif node["type"] == "muli":
            return f"{left_child} \\times {right_child}"        
        elif node["type"] == "mixedfrac":
            return f"{left_child}" + "\\frac{" + f"{dict_to_equation(children[1])}" + "}{" + f"{dict_to_equation(children[2])}" + "}"
        
        