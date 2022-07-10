# We will only be able to impor Vim if this script is executed inside
# vim
try:
    import vim
except ImportError:
    pass


def document_func(func_name, iden_lvl, params):
    assert func_name is not None

    iden_lvl = int(iden_lvl)

    # Variable to keep track of the output string
    output = ""
    
    
    # Add +1 to iden_lvl so that the base level is 1,
    # this is to prevent (2 * 0) when calculating
    # the header size
    # 80 total size limit
    # 2 is the identation level
    # 2 spaces before and after (#)
    # 2 spaces before and after function name
    header_size = 80 - (2 * ((iden_lvl + 1))) - len(func_name) - 4

    # String to keep identation
    ident = " " * (iden_lvl * 2)

    # If the params is None, do not add params
    real_params = []
    if params != "None":
        for param in params.split(","):
            real_params.append(param.strip())

    

    # Begin appending content to the output
    # HEADER
    output += f"{ident}# "
    output += "-" * (header_size//2)
    output += f" {func_name} "
    output += "-" * (header_size//2)
    output += " #\n"

    output += f"{ident}#\n"
    
    
    # DESCRIPTION
    output += f"{ident}#   DESCRIPTION:\n"
    output += f"{ident}#     <your descr>\n"
    output += f"{ident}#\n"

    # PARAMETERS
    output += f"{ident}#   PARAMETERS:\n"
    # Add parameters if any
    if real_params:
        for param in real_params:
            output += f"{ident}#     {param}\n"
    else:
        output += f"{ident}#     None\n" 
    output += f"{ident}#\n"

    # RAISES
    output += f"{ident}#   RAISES:\n"
    output += f"{ident}#     <your descr>\n"
    output += f"{ident}#\n"

    # NOTES
    output += f"{ident}#   NOTES:\n"
    output += f"{ident}#     <your descr>\n"
    output += f"{ident}#\n"

    output += f"{ident}#\n"

    # Add the function description
    definition_string = f"{ident}def {func_name}(" 

    for idx, param in enumerate(real_params):
        last_param = idx == len(real_params) - 1 

        # 2 is for comma and space or "):" if last param
        # Case in which the current lenght is > 80
        if (len(definition_string) + len(param) + 2) > 80:
            definition_string += "\n"
            output += definition_string
            # Reset defintion_string, add the number of spaces
            # equivalent to:
            # def <function_name>(
            definition_string = f"{ident}"
            definition_string += " " * (4 + len(func_name) + 1)

        definition_string += f"{param}"

        if last_param:
            # If control reached this point this is the last param
            definition_string += "):"
        else:
            definition_string += ", "

    output += definition_string

    for line in output.split("\n"):
        vim.current.buffer.append(line)
