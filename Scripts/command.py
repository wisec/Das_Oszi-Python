import sys

sys.path +=['..']

import readline
from das_oszi.das_oszi import DasOszi

#readline.parse_and_bind('tab: complete')
#readline.parse_and_bind('set editing-mode vi')

dso = DasOszi(  0x049f, 0x505a )

while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print(line)
    r = dso.RemoteShell( line )
    print( r )


