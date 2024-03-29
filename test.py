import os
import glob
import SCons
from sources import Sources
def TestRunner(root, current, is_remove) :
    def CheckTest(env, source, target) :
        os.system(current + '/' + str(target[0]))
        if not is_remove :
            os.remove(current + '/' + str(target[0]))
            for m in source :
                if m.rstr().endswith('.o') or m.rstr().endswith('.obj') :
                    os.remove(current + '/' + m.rstr())
    return CheckTest

class TestBuilder :
    def __init__(self, mode, targets, env, config) :
        self.__config = config
        self.__sources = Sources(self.__config)
        flags = self.__sources.GetFlags(mode)
        self.__targets = targets
        self.__env = env
        self.__env.Replace(CCFLAGS=flags[0],
                           LIBS=flags[1],
                           LINKFLAGS=flags[2])

    def Build(self, cpppath, root, current, *args) :
        self.__targets.extend(self.__config["DEPENDS"])
        if self.__config.configlist().has_key("STATIC_LIBS") :
            self.__targets.extend(self.__config["STATIC_LIBS"])
        test = self.__env.Program(self.__config.target(), self.__targets, CPPPATH=[cpppath])
        self.__env.AlwaysBuild(test)
        if len(args) > 0 :
            self.__env.AddPostAction(test, TestRunner(root, current, args[0]))
        else :
            self.__env.AddPostAction(test, TestRunner(root, current, None))
        
