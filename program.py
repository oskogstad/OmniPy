import sys
from email_client import send_email
from config import Config

title = False
body = False

argv_len = len(sys.argv)

if argv_len < 2:  # 1. argument is program title
    print('Needs at least one argument. \n1. argument will be used as title\n2. argument will be used as body\n\n'
          'Use -d to delete config')
    sys.exit()

for arg in sys.argv[1:]:
    if arg == '--help' or arg == '-h':
        print('OmniPy\n\n'
              '--help, -h           Display this help message and exit\n'
              '--delete-config, -d  Delete configuration and exit\n')
        sys.exit()

    if arg == '--delete-config' or arg == '-d':
        Config.delete_config()
        print('Settings deleted.')
        sys.exit()

conf = Config()
title = sys.argv[1]

if argv_len > 3:
    body = sys.argv[2]
else:
    body = ''

# Check all params
if conf.ait():
    send_email(
        conf.omni_email,
        conf.from_email,
        conf.password,
        title,
        body,
        conf.smtp_adr,
        conf.smtp_port)
else:
    print('Bad config, try editing it,\nor start over by deleting by running with \'-d\' flag')
