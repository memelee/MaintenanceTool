NET = {
    'PROXY': {
        'ENABLE': True,
        'URL': '10.144.1.10:8080'
    }
}

LOG = {
    'ENABLE': False,
    'FILE': '/root/app/tool/maintenance.log',
    'SIZE': 1024 * 1024,
    'COUNT': 10
}

DB = {
    'URL': '10.69.120.34:3306',
    'NAME': 'maintenance',
    'USER': 'query',
    'PASS': '!@mY0urF@th3r'
}

TABLE = {
    'NUM': 20
}
