#!/usr/bin/env python3
import os
#import time
#import hmac
#import codecs
import json  
import sys                                                              
#from hashlib import sha256
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py.dynamic import Analyses, Scans, ScanCapacitySummary, ScanOccurrences, ScannerVariables, DynUtils, Occurrences

#from requests.adapters import HTTPAdapter
#from urllib.parse import urlparse


def main():

    #Payload for creating and scheduling new DA job

    url = DynUtils().setup_url('http://my.verademo.site','DIRECTORY_AND_SUBDIRECTORY',False)

    allowed_hosts = [url]

    auth = DynUtils().setup_auth('AUTO','admin','smithy')

    auth_config = DynUtils().setup_auth_config(auth)

    crawl_config = DynUtils().setup_crawl_configuration([],False)

    scan_setting = DynUtils().setup_scan_setting(blocklist_configs=[],custom_hosts=[],user_agent=None)

    scan_config_request = DynUtils().setup_scan_config_request(url, allowed_hosts,auth_config, crawl_config, scan_setting)

    scan_contact_info = DynUtils().setup_scan_contact_info('andrzej@example.com','Alan Smithee','800-555-1212')

    scan = DynUtils().setup_scan(scan_config_request,scan_contact_info)

    print(scan)

    #Send configuration to Veracode and initiate Scan

    analysis = Analyses().create('My API Analysis 4',scans=[scan],owner='Andrzej',email='andrzej@example.com')

    print(analysis)

if __name__ == "__main__":
    main()