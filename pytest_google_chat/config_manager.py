import os
import configparser

class ConfigManager(object):
    def __init__(self, cfg_file_path, config):
        """
        Handles retrieving configuration values.
        Config options set in flags are given preferance over options set in the config file.
        :param cfg_file_path: Path to the config file containing information about google chat options.
        :type cfg_file_path: str or None
        :param config: Config object containing commandline flag options.
        :type config: _pytest.config.Config
        """
        self.cfg_file = None
        if os.path.isfile(cfg_file_path) or os.path.islink(cfg_file_path):
            self.cfg_file = configparser.ConfigParser(interpolation=None)
            self.cfg_file.read(cfg_file_path)

        self.config = config

    def getoption(self, flag, cfg_name, section=None, is_bool=False, default=None):
        # priority: cli > config file > default

        # 1. return cli option (if set)
        value = self.config.getoption(f'--{flag}')
        if value is not None:
            return value

        # 2. return default if no config file path is specified
        if section is None or self.cfg_file is None:
            return os.getenv(cfg_name.upper(), default)

        if self.cfg_file.has_option(section, cfg_name):
            # 3. return config file value
            return self.cfg_file.getboolean(section, cfg_name) if is_bool else self.cfg_file.get(section, cfg_name)
        else:
            # 4. if entry not found in config file
            return os.getenv(cfg_name.upper(), default)