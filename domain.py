"""
Author : Florian DJERBI
Object : List NAS OVH
Creation Date : 04/26/2023
Modification Date : 04/26/2023
"""

import json
import sys
from login import api_ovh


def domain_list(login):
    list_all = []
    list_domain = login.get('/domain')
    for i in list_domain:
        list_all.append({"DOMAIN": i})
    return list_all


if __name__ == '__main__':
    # Test
    login_api = api_ovh("667c3c9f7779c7a6", "e276b5e0143ed04d2d52774c284afdeb", "6520e2d1d63c2c9c75854c2b2900c3c4")
    # Prod
    # login_api = api_ovh(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(domain_list(login_api)))
