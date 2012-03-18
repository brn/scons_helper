##
 #@author Taketoshi Aono
 #@fileOverview
 #@license
 #Copyright (c) 2011 Taketoshi Aono
 #Licensed under the BSD.
 #
 #Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
 #associated doc umentation files (the "Software"), to deal in the Software without restriction,
 #including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
 #and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
 #subject to the following conditions:
 #
 #The above copyright notice and this permission notice shall be included in all copies or
 #substantial portions ofthe Software.
 #
 #THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
 #TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 #THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
 #CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 #DEALINGS IN THE SOFTWARE.
 ##

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
                    
        
