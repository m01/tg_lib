Purpose
=======
Make it easy for you to write Python scripts that interact with the
telnet interface of Thomson/Technicolor routers.

For more information on the telnet interface, see: http://npr.me.uk/telnet.html

Caveats
=======
Currently there is very limited error handling.

Example script
==============
```python
import tg_lib
import re
c = tg_lib.Connection('192.168.1.254', 'Administrator', 'yourpassword')
# see how many devices are on the wireless network
output = c.run('wireless stations list')
print(output)
# extract nr of associated stations : X
m=re.search(r"Total number of associated stations : ([0-9]+)", output)
print("number of devices: " + m.groups()[0])

# get DSL stats
print(c.run('xdsl info')) # add ' expand=enabled' for more data
```

Sample output
=============
<pre>
wireless stations list
flags: station is [A]associated (on 802.11 level)
       station is auth[O]rized (WPA handshake is ok)
       station is in [P]ower save mode
       station is [W]ME (QOS) capable
Station Name          Hardware Address   bss                             Flags      Time (assoc/idle)   
unknown               00:12:34:56:ef:de  myssid                                AO-W  167/0
unknown               db:08:12:34:56:ab  myssid                                AOPW  236/0
unknown               00:ab:cd:ef:12:34  myssid                                AOPW  2834/0

Total number of associated stations : 3

number of devices: 3
xdsl info
Modem state:                  		 up
Up time (Days hh:mm:ss):      		 6 days, 16:17:26
xDSL Type:                    		 ADSL2+
Bandwidth (Down/Up - kbit/s): 		 19793/1337
</pre>
