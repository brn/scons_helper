import os

class Sources :
    def __init__(self, config) :
        self.__config = config
        self.__targets = []

    def GetFlags(self, mode) :
        return (self.__config[mode.upper()],
                self.__config["LIBS"],
                self.__config["LD_FLAGS"])

    def CreateSourceList(self) :
        self.__CollectSources()
        return self.__targets
    
    def __CollectSources(self) : 
        self.__IterateDir(self.__config.base());
        self.__SetStaticLibs();

    def __SetStaticLibs(self) :
        configlist = self.__config.configlist()
        if configlist.has_key("STATIC_LIBS") :
            for lib in configlist["STATIC_LIBS"]:
                self.__targets.append(lib)

    def __IterateDir(self, dirname) :
        exdir_list = self.__config.exclude_dir_list()
        exfile_list = self.__config.exclude_file_list()
        for file_or_dir in os.listdir(dirname) :
            name = dirname + '/' + file_or_dir
            if os.path.isdir(name) and not exdir_list.has_key(file_or_dir) :
                self.__IterateDir(name)
            elif os.path.isfile(name) :
                if not exfile_list.has_key(file_or_dir) and file_or_dir.endswith('.cc'):
                    self.__targets.append(name)
                    
        
