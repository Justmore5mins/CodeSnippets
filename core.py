import git
from error import *

class Git:
    def __init__(self,mode:str="clone") -> None:
        """
        this class makes git use easier, and there has two modes
        1. clone: clone the repo from the .git url
        2. commit: commit your code into your own repo
        """
        if mode is "clone" or mode is "commit":
            pass
        else:
            InputError("Didn't I said it can only be clone & commit? haiyaa")