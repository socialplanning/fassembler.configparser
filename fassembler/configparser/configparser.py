import os
import sys
import ConfigParser

def asbool(obj):
    """XXX cargo culted from paste.deploy.converters"""
    if isinstance(obj, (str, unicode)):
        obj = obj.strip().lower()
        if obj in ['true', 'yes', 'on', 'y', 't', '1']:
            return True
        elif obj in ['false', 'no', 'off', 'n', 'f', '0']:
            return False
        else:
            raise ValueError(
                "String is not true/false: %r" % obj)
    return bool(obj)

def get_config(option, default=None, ini_paths=None):

    if default is None:
        default = ''

    # Figure out what VIRTUAL_ENV we're in.
    # In a fassembler build, this tells you what "application" we're in.
    env = os.path.normpath(sys.prefix)
    env_name, env_path = (os.path.basename(env), os.path.dirname(env))

    if ini_paths is None:
        # order is important here: if default-build.ini and build.ini define the
        # same setting, the one in build.ini will win because it comes after.
        ini_paths = [os.sep.join([env_path, 'requirements', 'default-build.ini']),
                     os.sep.join([env_path, 'etc', 'build.ini'])]

    parser = ConfigParser.SafeConfigParser()

    parser.read(ini_paths)

    real_option = '_'.join([env_name, option])
    try:
        return parser.get('applications', real_option)
    except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
        try:
            return parser.get('applications', option)
        except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
            pass
    try:
        return parser.get('general', option)
    except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
        pass
    try:
        return parser.get('google_maps_keys', option)
    except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
        return default

class FCParser(object):
    def get(self, option, default=None):
        return get_config(option, default)
