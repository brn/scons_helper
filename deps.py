import SCons
from SCons import Conftest, Environment, SConf
from SCons.SConf import CheckContext, SConfBase
def CheckHeaders(environment, filename, lang, truncate, headers) :
    sconf = SConfBase(env = environment, config_h = filename)
    context = CheckContext(sconf);
    for header in headers :
        SConf.CheckHeader(context, header = header, language = lang)
    sconf.config_h_text = context.config_h
    sconf.Finish()
    return context.havedict


