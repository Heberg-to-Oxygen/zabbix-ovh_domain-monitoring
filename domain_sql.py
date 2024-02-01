"""
Author : Florian DJERBI
Object : List NAS OVH
Creation Date : 04/27/2023
Modification Date : 04/28/2023
"""

import sys
import domain_info
from login import api_ovh, sql_connexion


def domain_list(login):
    list_domain = login.get('/domain')
    return list_domain


def domain_sql(login):
    for info_domain in domain_list(login):
        try:
            info = domain_info.domain_info(login, info_domain)
            request = "INSERT `ovh-domain` (domain, expiration_date, expiration_day, admin, billing, tech)" \
                      "VALUES (%s, %s, %s, %s, %s, %s)" \
                      "ON DUPLICATE KEY UPDATE expiration_date= %s, expiration_day=%s, admin=%s, billing=%s, tech=%s"
            val = (info[0], info[1], info[2], info[3], info[4], info[5], info[1], info[2], info[3], info[4], info[5])
            my_cursor = sql_connexion.cursor()
            my_cursor.execute(request, val)
            sql_connexion.commit()
        except:
            pass


if __name__ == '__main__':
    # Test
    login_api = api_ovh("667c3c9f7779c7a6", "e276b5e0143ed04d2d52774c284afdeb", "6520e2d1d63c2c9c75854c2b2900c3c4")
    sql_connexion = sql_connexion(host="infra.vigicorp.lan", user="adm_fdjerbi", password="NbCqE97RZpvAtJwVzxrQh6ev6lP5", database="ovh-domain")
    # Prod
    # login_api = api_ovh(sys.argv[1], sys.argv[2], sys.argv[3])
    # sql_connexion = sql_connexion(host=sys.argv[4], user=sys.argv[5], password=sys.argv[6], database=sys.argv[7])
    domain_sql(login_api)
