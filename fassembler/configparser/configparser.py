import os
import ConfigParser

def get_config(option, default=None, ini_path=None):

    if default is None:
        default = ''

    env = os.environ['VIRTUAL_ENV']
    env_name, env_path = (os.path.basename(env), os.path.dirname(env))

    if ini_path is None:
        ini_path = os.sep.join([env_path, 'etc', 'build.ini'])

    parser = ConfigParser.SafeConfigParser()

    parser.read(ini_path)

    real_option = ' '.join([env_name, option])
    try:
        return parser.get('applications', real_option)
    except ConfigParser.NoOptionError:
        pass
    try:
        return parser.get('general', option)
    except ConfigParser.NoOptionError:
        return default
