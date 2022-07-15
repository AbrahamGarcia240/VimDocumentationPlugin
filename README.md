# Vim Documentation Plugin
This is a Vim plugin coded in Python 3 which adds templates for Python documentation

For functions, such template looks like:
```
# --------------------------- <your_function_name> --------------------------- #
#
#   DESCRIPTION:
#     <your descr>
#
#   PARAMETERS:
#     arg1
#     arg2
#
#   RETURNS
#     <your descr>
#
#   RAISES:
#     <your descr>
#
#   NOTES:
#     <your descr>
#
#
def <your_function_name>(arg1, arg2):
```
Created by Abraham Garcia with the help of Kimsa :3

## Quick demo :D
![](https://github.com/AbrahamGarcia240/VimDocumentationPlugin/blob/master/Screen_Recording_2022-07-10_at_16_50_57.gif)



## Usage

You can use it by accessing Vim in command mode (i.e by pressing `esc` and typing the usage)

The usage for documenting functions is:
`:Document <function number> <identation level> <args>|None`
Keep in mind that no spaces should be in between args

Example:
`:Document sum_2_nums 0 num1,num2`

```
# -------------------------------- sum_2_nums -------------------------------- #
#
#   DESCRIPTION:
#     <your descr>
#
#   PARAMETERS:
#     num1
#     num2
#
#   RETURNS
#     <your descr>
#
#   RAISES:
#     <your descr>
#
#   NOTES:
#     <your descr>
#
#
def sum_2_nums(num1, num2):
```
Example with no arguments:
`:Document connect 0 None`

```
# --------------------------------- connect --------------------------------- #
#
#   DESCRIPTION:
#     <your descr>
#
#   PARAMETERS:
#     None
#
#   RETURNS
#     <your descr>
#
#   RAISES:
#     <your descr>
#
#   NOTES:
#     <your descr>
#
#
def connect():
```
Example with an identation level of 2
`:Document sum_2_nums 2 num1,num2`

```
    # ------------------------------ sum_2_nums ------------------------------ #
    #
    #   DESCRIPTION:
    #     <your descr>
    #
    #   PARAMETERS:
    #     num1
    #     num2
    #
    #   RETURNS
    #     <your descr>
    #
    #   RAISES:
    #     <your descr>
    #
    #   NOTES:
    #     <your descr>
    #
    #
    def sum_2_nums(num1, num2):
```
You can also add sections to your code, e.g.
`:CONSTANTS`
```
# --------------------------------------------------------------------------- #
#                                  CONSTANTS                                  #
# --------------------------------------------------------------------------- #
```
By default sections are in identation level 0
This plugin supports:
`:CONSTANTS`
`:GLOBALS`
`:FUNCTIONS`
`:CLASSES`

If needed, you can also add headers and specify an identation level, e.g.
`:HEADER example 0`

```
# --------------------------------- example --------------------------------- # 
```
`:HEADER example_with_ident 2`

```
   # -------------------------- example_with_ident -------------------------- #
```

## Install
Ensure your Vim has python3:
```
-bash-4.4$ vim --version | grep python3
+conceal           +linebreak         +python3/dyn       +wildignore
```

Create the following directory
`~/.vim/pack/my-plugins/start/document`
Inside such directory, clone this repository
```
-bash-4.4$ pwd
~/.vim/pack/my-plugins/start/document
-bash-4.4$ tree .
.
├── doc
├── plugin
│   └── document.vim
└── python
    └── document.py
```

Open vim, try the command :D
