#!/usr/bin/env python3
#import os
#import time
#import hmac
#import codecs
import json  
import sys                                                              
#from hashlib import sha256
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py import VeracodeAPI as vapi

#from requests.adapters import HTTPAdapter
#from urllib.parse import urlparse


def main():
#Setup variables according to environment

#GitHub:
api_id = '${{ secrets.VERACODE_API_ID }}'
api_secret = '${{ secrets.VERACODE_API_KEY }}'
dynamic_job =  'GitHub Test Scan'    #'${{ github.repository }}' #Dynamic Job name will be same as GitHub project name

#Payload for creating and scheduling new DA job
data =   {
  "name": dynamic_job,
  "scans": [
    {
      "scan_config_request": {
        "target_url": {
          "url": "http://my.verademo.site"
        }
      }
    }
  ],
  "schedule": {
    "now": True,
    "duration": {
      "length": 1,
      "unit": "DAY"
    }
  }
}

analyses = vapi.get_analyses()
print(analyses)

if __name__ == "__main__":
    main()