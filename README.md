# FileCheck

File status check for cloud BTS environment VNF OAM part development

## Purpose
    At the CBTS OAM part development, we can change the javascript code directly at real environment.
    but if we share use the  environment, maybe we can't make sure the current package is the origin code.
    the tool will create one hash index for all js file at firstly(need user execute the tool at the environment create)
    and next time use the environment, user could run the tool again, and there can check and compare which files changed.
## usage

    python fileCheck.py  [path]
    * the [path] argument is optional, if not carry the argument, the default [path] is current path.
## author
    Jacob Duan, zhuangzhuang.1.duan@nokia-sbell.com


## history
    2018-3-26: 0.0.1 version for the draft.
