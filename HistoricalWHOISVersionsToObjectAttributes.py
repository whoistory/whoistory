"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses
    
    ---
    
    This is a local transform for Maltego.
    It will retrieve a limited set of WHOIS objects related to Historical records from the RIPE Database.
    This is only Proof of Concept code and should not be used in Production environments.
    """

import sys
import json
import urllib2
from MaltegoTransform import *

argument = sys.argv[1]
argumentList = argument.split(',')
ipaddress = argumentList[0]
versionNumber = argumentList[1]

me = MaltegoTransform()

try:
    urlHist = "https://stat.ripe.net/data/historical-whois/data.json?resource=" + ipaddress + "&version=" + versionNumber
    responseHist = json.loads(urllib2.urlopen(urlHist).read())
    historicalWhois = responseHist['data']['objects'][0]['attributes']
    fromTime = responseHist['data']['objects'][0]['from_time']
    me.addEntity("RIPENCC.Timestamp", fromTime)
except:
    m = MaltegoTransform()
    m.addUIMessage("There was an issue fetching the WHOIS data.","Inform")
    m.returnOutput()
    sys.exit(0)

for key in historicalWhois:
    if key['attribute'] == "country":
        orgObjValue = key['value']
        me.addEntity("maltego.Location", orgObjValue)
    elif key['attribute'] == "admin-c":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISHandle", orgObjValue)
    elif key['attribute'] == "tech-c":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISHandle", orgObjValue)
    elif key['attribute'] == "abuse-c":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISHandle", orgObjValue)
    elif key['attribute'] == "notify":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISHandle", orgObjValue)
    elif key['attribute'] == "upd-to":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['attribute'] == "mnt-nfy":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['attribute'] == "mnt-ref":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISMaintainer", orgObjValue)
    elif key['attribute'] == "mnt-by":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISMaintainer", orgObjValue)
    elif key['attribute'] == "org":
        orgObjValue = key['value']
        me.addEntity("pt.whoisOrganization", orgObjValue)
    elif key['attribute'] == "sponsoring-org":
        orgObjValue = key['value']
        me.addEntity("pt.whoisOrganization", orgObjValue)
    elif key['attribute'] == "org-name":
        orgObjValue = key['value']
        me.addEntity("pt.whoisOrganization", orgObjValue)
    elif key['attribute'] == "as-name":
        orgObjValue = key['value']
        me.addEntity("maltego.Phrase", orgObjValue)
    elif key['attribute'] == "netname":
        orgObjValue = key['value']
        me.addEntity("maltego.Phrase", orgObjValue)
    elif key['attribute'] == "address":
        orgObjValue = key['value']
        me.addEntity("maltego.Location", orgObjValue)
    elif key['attribute'] == "phone":
        orgObjValue = key['value']
        me.addEntity("maltego.PhoneNumber", orgObjValue)
    elif key['attribute'] == "fax-no":
        orgObjValue = key['value']
        me.addEntity("maltego.PhoneNumber", orgObjValue)
    elif key['attribute'] == "e-mail":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['attribute'] == "abuse-mailbox":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['attribute'] == "ref-nfy":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
me.returnOutput()
