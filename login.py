"""
Author : Florian DJERBI
Object : Login OVH API
Creation Date : 04/26/2023
Modification Date : 04/27/2023
"""

import ovh
import mysql.connector


def api_ovh(application_key, application_secret, consumer_key):
    endpoint = "ovh-eu"
    client = ovh.Client(
        endpoint=endpoint,
        application_key=application_key,
        application_secret=application_secret,
        consumer_key=consumer_key,
    )
    return client


def sql_connexion(host, user, password, database):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return mydb
