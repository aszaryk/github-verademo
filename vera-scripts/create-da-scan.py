#!/usr/bin/env python3
import os
import json  
import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py.dynamic import Analyses, Scans, ScanCapacitySummary, ScanOccurrences, ScannerVariables, DynUtils, Occurrences

#name of Dynamic Analysis will be the same as the name of the Github repository:
analysis_name = "Project: " + os.environ.get("JOB_NAME") + " - Workflow Number: " + os.environ.get("JOB_ID")

def main():

    #Payload for creating and scheduling new DA job

    url = DynUtils().setup_url('http://my.verademo.site','DIRECTORY_AND_SUBDIRECTORY',False)

    allowed_hosts = [url]

    auth = DynUtils().setup_auth('AUTO','admin','smithy')

    auth_config = DynUtils().setup_auth_config(auth)

    crawl_config = DynUtils().setup_crawl_configuration([],False)

    scan_setting = DynUtils().setup_scan_setting(blocklist_configs=[],custom_hosts=[],user_agent=None)

    scan_config_request = DynUtils().setup_scan_config_request(url, allowed_hosts,auth_config, crawl_config, scan_setting)

    scan = DynUtils().setup_scan(scan_config_request)

    start_scan = DynUtils().start_scan(12, "HOUR")

    print("TargetURL Scan Settings: ")
    print(scan)

    #Send configuration to Veracode and initiate Scan

    analysis = Analyses().create(analysis_name,scans=[scan],owner='Andrzej',email='andrzej@example.com', start_scan=start_scan)


if __name__ == "__main__":
    main()