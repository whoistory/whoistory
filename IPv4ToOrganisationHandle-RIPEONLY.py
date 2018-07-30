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
    It will retrieve the unique handle for the responsible Organisation.
    This handle can subsequently be used to retrieve the attributes for the responsible organisation.
    This is only Proof of Concept code and should not be used in Production environments.
"""

import sys
import json
import urllib2
from MaltegoTransform import *

ipv4address = sys.argv[1]

try:
    url = "https://rest.db.ripe.net/search.json?flags=rB&query-string=" + ipv4address + "&resource-holder=true"
    response = json.loads(urllib2.urlopen(url).read())
    nichandle = response['objects']['object'][0]['resource-holder']['key']
except:
    m = MaltegoTransform()
    m.addUIMessage("There was an issue fetching the WHOIS data.","Inform")
    m.returnOutput()
    sys.exit(0)

me = MaltegoTransform()
thisent = me.addEntity("pt.WhoisOrganization", nichandle)

thisent.setType("pt.WhoisOrganization")
thisent.setValue(nichandle)

me.returnOutput()
