import os
import ConfigParser

def get_config(option):
    env = os.environ['VIRTUAL_ENV']
    env_name, env_path = (os.path.basename(env), os.path.dirname(env))

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
        pass
