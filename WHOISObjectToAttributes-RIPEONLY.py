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
    It will retrieve the attributes of a RIPE Database object.
"""

import sys
import json
import urllib2
from MaltegoTransform import *

ripeobject = sys.argv[1]

try:
    url = "https://rest.db.ripe.net/search.json?flags=rB&query-string=" + ripeobject + "&resource-holder=true"
    response = json.loads(urllib2.urlopen(url).read())
    whoisObjects = response['objects']['object'][0]['attributes']['attribute']
except:
    m = MaltegoTransform()
    m.addUIMessage("There was an issue fetching the WHOIS data.","Inform")
    m.returnOutput()
    sys.exit(0)

me = MaltegoTransform()

for key in whoisObjects:
    if key['name'] == "country":
        orgObjValue = key['value']
        me.addEntity("maltego.Location", orgObjValue)
    elif key['name'] == "admin-c":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISHandle", orgObjValue)
    elif key['name'] == "nic-hdl":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISHandle", orgObjValue)
    elif key['name'] == "tech-c":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISHandle", orgObjValue)
    elif key['name'] == "abuse-c":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISHandle", orgObjValue)
    elif key['name'] == "notify":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['name'] == "upd-to":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['name'] == "mnt-nfy":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['name'] == "mnt-ref":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISMaintainer", orgObjValue)
    elif key['name'] == "mnt-by":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISMaintainer", orgObjValue)
    elif key['name'] == "mntner":
        orgObjValue = key['value']
        me.addEntity("RIPENCC.WHOISMaintainer", orgObjValue)
    elif key['name'] == "org":
        orgObjValue = key['value']
        me.addEntity("pt.whoisOrganization", orgObjValue)
    elif key['name'] == "sponsoring-org":
        orgObjValue = key['value']
        me.addEntity("pt.whoisOrganization", orgObjValue)
    elif key['name'] == "org-name":
        orgObjValue = key['value']
        me.addEntity("pt.whoisOrganization", orgObjValue)
    elif key['name'] == "as-name":
        orgObjValue = key['value']
        me.addEntity("maltego.Phrase", orgObjValue)
    elif key['name'] == "netname":
        orgObjValue = key['value']
        me.addEntity("maltego.Phrase", orgObjValue)
    elif key['name'] == "address":
        orgObjValue = key['value']
        me.addEntity("maltego.Location", orgObjValue)
    elif key['name'] == "phone":
        orgObjValue = key['value']
        me.addEntity("maltego.PhoneNumber", orgObjValue)
    elif key['name'] == "fax-no":
        orgObjValue = key['value']
        me.addEntity("maltego.PhoneNumber", orgObjValue)
    elif key['name'] == "e-mail":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['name'] == "abuse-mailbox":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['name'] == "ref-nfy":
        orgObjValue = key['value']
        me.addEntity("maltego.EmailAddress", orgObjValue)
    elif key['name'] == "person":
        orgObjValue = key['value']
        me.addEntity("maltego.Person", orgObjValue)
    else:
        orgObjValue = key['value']
        me.addEntity("maltego.Phrase", orgObjValue)
me.returnOutput()
