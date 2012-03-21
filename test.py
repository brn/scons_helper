import os
import glob
import SCons
from sources import Sources
def TestRunner(root) :
    def CheckTest(env, source, target) :
        current = os.getcwd().replace('\\', '/')
        os.system(current + '/' + str(target[0]))
        os.remove(current + '/' + str(target[0]))
        for m in glob.glob(root + '/*.o') :
            os.remove(str(m))
            for m in glob.glob(root + '/*.obj') :
                os.remove(str(m))
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

    def Build(self, cpppath, root) :
        self.__targets.extend(self.__config["DEPENDS"])
        objs = []
        for target in self.__targets :
            objs.append(self.__env.Object(target))
        if self.__config.configlist().has_key("STATIC_LIBS") :
            objs.append(self.__config["STATIC_LIBS"])
        test = self.__env.Program(self.__config.target(), objs, CPPPATH=[cpppath])
        self.__env.AddPostAction(test, TestRunner(root))
        self.__env.AlwaysBuild(test)
