import json
from ncclient import manager

if __name__ == "__main__":

    with manager.connect(host='192.168.10.80', port=830, username='admin', password='cisco',
                         hostkey_verify=False, device_params={'name': 'csr'},
                         allow_agent=False, look_for_keys=False) as device:

payload={
	"route": {
		"ip-route-interface-forwarding-list": {
			"prefix": "216.48.1.0",
			"mask": "255.255.255.0",
			"fwd-list": {
				"fwd": "10.1.1.1"
			}
		}
	}
}

        # UNCOMMENT THE NEXT TWO LINES FOR THE LAB AFTER YOU
        # GET THE NEW SECONDARY IP WORKING
        # nc_get_reply = device.get(('subtree', get_filter))
        # print etree.tostring(nc_get_reply.data_ele, pretty_print=True)

