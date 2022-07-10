# Vim Documentation Plugin
This is a Vim plugin coded in Python 3 that creates the command **Document** which adds in the current Vim line a documentation header like:

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
#   RAISES:
#     <your descr>
#
#   NOTES:
#     <your descr>
#
#
def <your_function_name>(arg1, arg2):
```
![](https://github.com/AbrahamGarcia240/VimDocumentationPlugin/blob/master/Screen%20Recording%202022-07-10%20at%2016.50.57.gif)



## Usage

You can use it by accessing Vim in command mode (i.e by pressing `esc` and typing the usage)

The usage is:
`:Document <function number> <identation level> <args>|None`

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
    #   RAISES:
    #     <your descr>
    #
    #   NOTES:
    #     <your descr>
    #
    #
    def sum_2_nums(num1, num2):
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
