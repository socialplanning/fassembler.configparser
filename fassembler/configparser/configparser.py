import os
import sys
import ConfigParser

class FCParser(object):

    def get(self, option, default=None):
        return get_config(option, default)

def get_config(option, default=None, ini_paths=None):

    if default is None:
        default = ''

    # Figure out what VIRTUAL_ENV we're in.
    # In a fassembler build, this tells you what "application" we're in.
    env = os.path.normpath(sys.prefix)
    env_name, env_path = (os.path.basename(env), os.path.dirname(env))

    if ini_paths is None:
        ini_paths = [os.sep.join([env_path, 'requirements', 'default-build.ini']),
                     os.sep.join([env_path, 'etc', 'build.ini'])]

    parser = ConfigParser.SafeConfigParser()

    parser.read(ini_paths)

    real_option = '_'.join([env_name, option])
    try:
        return parser.get('applications', real_option)
    except ConfigParser.NoOptionError:
        try:
            return parser.get('applications', option)
        except ConfigParser.NoOptionError:
            pass
    try:
        return parser.get('general', option)
    except ConfigParser.NoOptionError:
        pass
    try:
        return parser.get('google_maps_keys', option)
    except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
        return default
