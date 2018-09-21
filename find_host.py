#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

hosts_config = """
server {
    listen 80;

    server_name {0};

    location / {
        root /wwwroot/{0}/_build/html;
    }
}

server {
    listen 80;
    server_name www.{0};

    location / {
        return 301 http://{0}$request_uri;
    }
}
"""

host_default = """
server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    server_name _;

    return 444;
}
"""


if __name__ == '__main__':
    root_dir = '/wwwroot'

    config_dir = '/wwwconfig'

    dirs = os.listdir(root_dir)
    host_pattern = r'^[a-zA-Z0-9\-\.]+\.(com|org|net|wiki|cc|cn|blog|xyz)$'
    writen_cnt = 0
    for k in dirs:
        if re.match(host_pattern,k):
            cfg_str = hosts_config.replace('{0}',k)
            with open(os.path.join(config_dir,k),'w') as fout:
                fout.write(cfg_str)
            writen_cnt += 1
    if writen_cnt > 0:
        # create a forbid default
        with open(os.path.join(config_dir,'forbid_default'),'w') as fout:
                fout.write(host_default)
    print('total write {} sites\n',writen_cnt)
