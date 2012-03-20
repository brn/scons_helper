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

import platform
from copy import deepcopy
_id = platform.system()
_name = "";
if _id == 'Linux':
    _name = 'linux'
elif _id == 'Darwin':
    _name = 'macos'
elif _id.find('CYGWIN') >= 0:
    _name = 'cygwin'
elif _id == 'Windows' or id == 'Microsoft':
    _name ='win32'
elif _id == 'FreeBSD':
    _name = 'freebsd'
elif _id == 'OpenBSD':
    _name = 'openbsd'
elif _id == 'SunOS':
    _name = 'solaris'
elif _id == 'NetBSD':
    _name = 'netbsd'
else:
    _name = "NA"

platform = _name

_exfiles_key = "EXCLUDE_FILES"
_exdirs_key = "EXCLUDE_DIRS"
_target_key = "TARGET"

class Config :
    def __init__(self, basepath, configlist) :
        self.__base = basepath
        self.__all_config = configlist
        self.__configlist = configlist[_name]
        self.__target = self.__configlist[_target_key]
        self.__exclude_files = {}
        self.__exclude_dirs = {}
        if self.__configlist.has_key(_exfiles_key) :
            self.AddExcludeFile(self.__configlist[_exfiles_key])
        if self.__configlist.has_key(_exdirs_key) :
            self.AddExcludeDir(self._configlist[_exdirs_key])

    def __getitem__(self, name) :
        return self.__configlist[name]

    def Copy(self) :
        base = self.__base
        configlist = deepcopy(self.__all_config)
        return Config(base, configlist)

    def Extend(self, configlist) :
        configs =  configlist[_name]
        for key in configs :
            if isinstance(configs[key], list) :
                if not self.__configlist.has_key(key) :
                    self.__configlist[key] = []
                self.__configlist[key].extend(configs[key])
                
            elif isinstance(configs[key], str) :
                if not self.__configlist.has_key(key) :
                    self.__configlist[key] = ""
                self.__configlist[key] += ' ' + configs[key]

    def AddExcludeFile(self, exclude_list) :
        for key in exclude_list :
            self.__exclude_files[key] = True

    def RemoveExcludeFile(self, name) :
        if self.__exclude_files.has_key(name) :
            del(self.__exclude_files[name])

    def AddExcludeDir(self, exclude_list) :
        for key in exclude_list :
            self.__exclude_dirs[key] = True
            
    def RemoveExcludeDir(self, name) :
        if self.__exclude_dirs.has_key(name) :
            del(self.__exclude_dirs[name])

    def exclude_file_list(self) :
        return self.__exclude_files

    def exclude_dir_list(self) :
        return self.__exclude_dirs

    def target(self) :
        return self.__target

    def configlist(self) :
        return self.__configlist
    
    def set_base(self, base) :
        self.__base = base
    
    def base(self) :
        return self.__base


