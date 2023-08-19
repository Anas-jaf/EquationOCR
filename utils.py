def dict_to_equation(node):
    if "children" in node:
        children = node["children"]
        left_child = dict_to_equation(children[0])
        
        if len(children) > 1:  # Check if there's a right child
            right_child = dict_to_equation(children[1])
            if len(children) > 2:
                last_child = dict_to_equation(children[2])
            # children = [dict_to_equation(child) for child in node["children"]] 
        
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
            return f"{left_child} \\cdot {right_child}"        
        elif node["type"] == "mixedfrac":
            return f"{left_child}" + "\\frac{" + f"{dict_to_equation(children[1])}" + "}{" + f"{dict_to_equation(children[2])}" + "}"
        elif node["type"] == "abs":
            return f"\\left|{left_child}\\right|"
        elif node["type"] == "exp":
            return f"\\exp({left_child})"
        elif node["type"] == "function":
            if len(children) > 2 : 
                return f"\\mathrm{{{left_child}}}(\\mathrm{{{right_child}}} , \\mathrm{{{last_child}}})"
            else :
                return f"\\mathrm{{{left_child}}}(\\mathrm{{{right_child}}})"
        elif node["type"] == "equals":
            return f"{left_child} = {right_child}"
        elif node["type"] == "log":
            return f"\\log_{{{left_child}}} ({{{right_child}}})"
        elif node["type"] == "ln":
            return f"\\ln({left_child})"        
        elif node["type"] == "conj":
            return f"\\overline{{{left_child}}}"        
        elif node["type"] == "sign":
            return f"\\text{{sign}}({left_child})"            
        elif node["type"] == "mixedfrac":
            whole = dict_to_equation(node["children"][0])
            numerator = dict_to_equation(node["children"][1])
            denominator = dict_to_equation(node["children"][2])
            return f"{whole} \\frac{{{numerator}}}{{{denominator}}}"
        elif node["type"] == "factorial":
            return f"{left_child}!"  
        elif node["type"] == "radian":
            return f"{left_child} \\, \\text{{rad}}"
        elif node["type"] == "deg":
            return f"{left_child} \\degree"
        elif node["type"] == "degmin":
            deg_child = dict_to_equation(node["children"][0])
            min_child = dict_to_equation(node["children"][1])
            return f"{deg_child}° {min_child}'"
        elif node["type"] == "degminsecond":
            deg_child = dict_to_equation(node["children"][0])
            min_child = dict_to_equation(node["children"][1])
            sec_child = dict_to_equation(node["children"][2])
            return f"{deg_child}° {min_child}' {sec_child}''"
        elif node["type"] == "sin":
            return f"\\sin({left_child})"
        elif node["type"] == "asin":
            return f"\\arcsin({left_child})"
        elif node["type"] == "sinh":
            return f"\\sinh({left_child})"  
        elif node["type"] == "asinh":
            return f"\\\\arsinh({left_child})"
        
        elif node["type"] == "cos":
            return f"\\cos({left_child})"
        elif node["type"] == "acos":
            return f"\\arccos({left_child})"
        elif node["type"] == "cosh":
            return f"\\cosh({left_child})"  
        elif node["type"] == "acosh":
            return f"\\\\arcosh({left_child})"

        elif node["type"] == "cos":
            return f"\\cos({left_child})"
        elif node["type"] == "acos":
            return f"\\arccos({left_child})"
        elif node["type"] == "cosh":
            return f"\\cosh({left_child})"  
        elif node["type"] == "acosh":
            return f"\\\\arcosh({left_child})"
        
        elif node["type"] == "tan":
            return f"\\tan({left_child})"
        elif node["type"] == "atan":
            return f"\\arctan({left_child})"
        elif node["type"] == "tanh":
            return f"\\tanh({left_child})"  
        elif node["type"] == "atanh":
            return f"\\\\artanh({left_child})"        
                        
        elif node["type"] == "cot":
            return f"\\cot({left_child})"
        elif node["type"] == "acot":
            return f"\\arccot({left_child})"
        elif node["type"] == "coth":
            return f"\\coth({left_child})"  
        elif node["type"] == "acoth":
            return f"\\\\arcoth({left_child})"                           

        elif node["type"] == "sec":
            return f"\\sec({left_child})"
        elif node["type"] == "asec":
            return f"\\arcsec({left_child})"
        elif node["type"] == "sech":
            return f"\\sech({left_child})"  
        elif node["type"] == "asech":
            return f"\\\\arsech({left_child})" 

        elif node["type"] == "csc":
            return f"\\csc({left_child})"
        elif node["type"] == "acsc":
            return f"\\arccsc({left_child})"
        elif node["type"] == "csch":
            return f"\\csch({left_child})"  
        elif node["type"] == "acsch":
            return f"\\\\arcsch({left_child})" 

        elif node["type"] == "lim":
            var_child = dict_to_equation(node["children"][0])
            lower_child = dict_to_equation(node["children"][1])
            function_child = dict_to_equation(node["children"][2])
            return f"\\lim_{{ {var_child} \\to {lower_child}}} ({function_child})"

        elif node["type"] == "lim_right":
            var_child = dict_to_equation(node["children"][0])
            lower_child = dict_to_equation(node["children"][1])
            function_child = dict_to_equation(node["children"][2])
            return f"\\lim_{{ {var_child} \\to {lower_child}^+}} ({function_child})"
        
        elif node["type"] == "lim_left":
            var_child = dict_to_equation(node["children"][0])
            lower_child = dict_to_equation(node["children"][1])
            function_child = dict_to_equation(node["children"][2])
            return f"\\lim_{{ {var_child} \\to {lower_child}^-}} ({function_child})"
                
                        
    elif node["type"] == "const":
        return str(node["value"])
    elif node["type"] == "var":
        if node["value"] == 'π':
          return '\pi'
        elif node["value"] == 'e':
          return '\mathrm{e}' 
        elif node["value"] == '∞':
            return '\infty'
        # elif '_' in node['value']:
        #   return node['value']
        
        return node["value"]
    elif node["type"] == "ellipsis":
        return "..."
