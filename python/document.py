# Documentation about vim lib:
#http://vimdoc.sourceforge.net/htmldoc/if_pyth.html

# We will only be able to import Vim if this script is executed inside
# vim
import vim


# -------------------------------- CONSTANTS -------------------------------- #
MAX_LINE_SIZE = 80

# ------------------------------ document_func ------------------------------ #
#
#   DESCRIPTION:
#     This function automatically generates a documentation header for a
#     python functions using this exact format.
#
#   PARAMETERS:
#     func_name - (IN) The name of the function
#     iden_lvl  - (IN) An integer defining the identation level
#     params    - (IN) A comma separated string with all parameters, if no
#                      parameter is required, we should use "None"
#
#   RAISES:
#     N/A
#
#   NOTES:
#     This script is intended to be executed from Vim, thus, we write
#     the output to the vim buffer (the file opened in vim for which we are
#     currently working)
#
#     This script assumes a line size limit of 80 characters
#
#     Each identation level equals 2 spaces
#     We do not define default values in this function as we have not found
#     a way to pass None values from Vim to Python
#
def document_func(func_name, iden_lvl, params):
    assert func_name is not None

    # Get current line in vim
    row, col = vim.current.window.cursor
    row = int(row)

    iden_lvl = int(iden_lvl)

    # Variable to keep track of the output string
    output = ""

    # Header size determines the number of "-" to use to build the header
    # Add +1 to iden_lvl so that the base level is 1, This is to prevent
    # (2 * 0) when calculating the header size
    # 80 character is the total size limit for any line
    # 2 is the identation level (+1, see above)
    # 2 spaces before and after (#)
    # 2 spaces before and after function name
    header_size = MAX_LINE_SIZE - (2 * ((iden_lvl + 1))) - len(func_name) - 4

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

    # RETURNS
    output += f"{ident}#   RETURNS:\n"
    output += f"{ident}#     <your descr>\n"
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

    # Add the function signature
    definition_string = f"{ident}def {func_name}("

    # Add the parameters to the function signature
    if not real_params:
        # If control reached this point we have no params for this function,
        definition_string += "):"

    for idx, param in enumerate(real_params):
        last_param = idx == len(real_params) - 1

        # Check if we should add this argument to the current line
        # take in consideration the lenght of the param + 2 characters.
        #
        # If this is not the last parameter, the 2 characters are for
        # ". " in order to separate arguments
        #
        # If this is the last parameter, the 2 characters are for "):"
        if (len(definition_string) + len(param) + 2) > MAX_LINE_SIZE:
            # The argument + 2 is too big for this file, add a new line
            definition_string += "\n"
            output += definition_string
            # Reset defintion_string, add the number of spaces
            # equivalent to:
            # def <function_name>(
            definition_string = f"{ident}"
            # 4 characters for "def "
            # 1 character for ("
            definition_string += " " * (4 + len(func_name) + 1)

        definition_string += f"{param}"

        if last_param:
            # If control reached this point this is the last param
            definition_string += "):"
        else:
            definition_string += ", "

    # Add the function signature to the output
    output += definition_string

    # Iterate over all new lines, we cannot add strings with "\n" to the
    # vim buffer, however, we can simulate breaklines by appending
    # into the buffer
    for line in output.split("\n"):
        if line.strip():
            # Add line bellow the row in which we are
            vim.current.buffer.append(line, row)
            row += 1

