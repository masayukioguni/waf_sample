APPNAME = 'test-project'
VERSION = '1.0.0'

srcdir = '.'
blddir = 'build'

def set_options(opt):
    print "set_options"
    opt.tool_options('compiler_cc')
    

    

def configure(conf):
    print "configure"
    conf.check_tool('compiler_cc')
    # libmの存在確認
    #conf.check_cxx(lib = 'm')
    # ディレクトリを指定して確認
    # conf.check_cxx(lib = 'superlib', libpath = '/var/super/lib')
    # time.hの存在確認
    #conf.check_cxx(header_name = 'time.h')
    #conf.check_cxx(function_name = 'printf', 
    #              header_name   = 'stdio.h',
    #              mandatory     = True)

def build(bld):
    print "build"
    # .so   
    bld(features = 'cc cshlib',
        source = 'main.c',
        target = 'main',
        includes = '.')
    # .a
    bld(features = 'cc cstaticlib',
        source = 'main.c',
        target = 'main',
        includes = '.')

    bld(features = 'cc cprogram',
    source = 'main.c',
    target = 'main',
    includes = '.',
    uselib_local = 'main')

def shutdown(ctx):
    print "shutdown"
