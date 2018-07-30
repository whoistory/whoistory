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
    It will retrieve historical WHOIS records from the the RIPE Database for the following object:
    INETNUM (IPv4), INET6NUM (IPv6), AS (AS number), ORGANISATION, MNTNER (Maintainer).
    This is only Proof of Concept code and should not be used in Production environments.
"""

import sys
import json
import urllib2
from MaltegoTransform import *

if 'ip-address' in sys.argv:
    argument = sys.argv[1]
    argumentList = argument.split('#')
    ipaddress = argumentList[0].split('=')
    internetresource = argumentList[0]
else:
    if (sys.argv[1] == "AS") and ('as' not in sys.argv[2].lower()):
        internetresource = ''.join((sys.argv[1],sys.argv[2]))
    elif 'as' in sys.argv[2].lower():
        internetresource = sys.argv[2]
    elif sys.argv[1] == "ORG":
        internetresource = ''.join(("organisation:",sys.argv[2]))
    elif sys.argv[1] == "MNT":
        internetresource = ''.join(("mntner:",sys.argv[2]))
    else:
        argument = sys.argv[1]
        argumentList = argument.split('#')
        ipaddress = argumentList[0].split('=')
        internetresource = argumentList[0]

try:
    url = "https://stat.ripe.net/data/historical-whois/data.json?resource=" + internetresource
    response = json.loads(urllib2.urlopen(url).read())
except:
    m = MaltegoTransform()
    m.addUIMessage("There was an issue fetching the WHOIS data:" + internetresource,"Inform")
    m.returnOutput()
    sys.exit(0)

try:
    amountVersions = response['data']['num_versions']
    startVersion = response['data']['versions'][0]['version']-response['data']['num_versions']+1
except:
    m = MaltegoTransform()
    m.addUIMessage("There was an issue with the WHOIS response. Likely the authoritative resource information is not held in the RIPE Database.","Inform")
    m.returnOutput()
    sys.exit(0)

if amountVersions == 1:
	me = MaltegoTransform()
	orgObjValue = "No historical information available for this INETNUM object"
	thisent = me.addEntity("maltego.Phrase", orgObjValue)
	thisent.setType("maltego.Phrase")
	thisent.setValue(orgObjValue)
	me.returnOutput()
else:
	me = MaltegoTransform()
	for versionNumber in range(startVersion, amountVersions + startVersion):
            orgObjValue = internetresource + "," + str(versionNumber)
            thisent = me.addEntity("ripe.HistoricalWhoisRecord", orgObjValue)
            thisent.setType("ripe.HistoricalWhoisRecord")
            thisent.addAdditionalFields("Notes", "Notes", "Notes", "Source: " + url)
            thisent.setValue(orgObjValue)
        me.returnOutput()
