import os
import logging
import logging.config
import json
import sys
import argparse
import timeit

from mongoengine import connect
from pycoshark.mongomodels import Project
from pycoshark.utils import create_mongodb_uri_string
from pycoshark.utils import get_base_argparser


def setup_logging(default_path=os.path.dirname(os.path.realpath(__file__))+"/loggerConfiguration.json",
                  default_level=logging.INFO):
        """
        Setup logging configuration

        :param default_path: path to the logger configuration
        :param default_level: defines the default logging level if configuration file is not found(default:logging.INFO)
        """
        path = default_path
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)


def start():
    start = timeit.default_timer()
    setup_logging()
    logger = logging.getLogger("main")
    logger.info("Starting pymweSHARK...")

    parser = get_base_argparser('', '0.0.1')
    parser.add_argument('--output', help='Output Folder', required='true')

    parser.add_argument('--debug', help='Sets the debug level.', default='DEBUG',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
						
	print("Hello World")

    args = parser.parse_args()
    uri = create_mongodb_uri_string(args.db_user, args.db_password, args.db_hostname, args.db_port, args.db_authentication, args.ssl)


if __name__ == "__main__":
    start()
