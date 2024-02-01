"""
Author : Florian DJERBI
Object : List NAS OVH
Creation Date : 04/26/2023
Modification Date : 04/27/2023
"""

import json
import sys
from login import api_ovh
from datetime import datetime


def domain_info(login, zone_name):
    all_info = login.get(f'/domain/zone/{zone_name}/serviceInfos')
    expiration = all_info['expiration']
    admin = all_info['contactAdmin']
    tech = all_info['contactTech']
    billing = all_info['contactBilling']

    d1 = datetime.strptime(expiration, "%Y-%m-%d")
    d2 = datetime.today()
    delta = d1 - d2
    return zone_name, expiration, delta.days, admin, billing, tech, expiration, delta.days, admin, billing, tech


def domain_zabbix(login, zone_name):
    try:
        info = domain_info(login, zone_name)
        result = {"Domain": zone_name, "Expiration_Date": info[1], "Admin": info[3], "Billing": info[4], "Tech": info[5],
                  "Expiration_Day": info[2]}
        return result
    except:
        pass


if __name__ == '__main__':
    # Test
    login_api = api_ovh("667c3c9f7779c7a6", "e276b5e0143ed04d2d52774c284afdeb", "6520e2d1d63c2c9c75854c2b2900c3c4")
    print(json.dumps(domain_zabbix(login_api, "compta-bettr.fr")))
    # Prod
    # login_api = api_ovh(sys.argv[1], sys.argv[2], sys.argv[3])
    # print(json.dumps(domain_info(sys.argv[4])))
