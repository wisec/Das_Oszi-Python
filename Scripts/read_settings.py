import sys

sys.path +=['..']

from das_oszi.das_oszi import DasOszi
from das_oszi.das_oszi import Settings
import array
import IPython

if(False):
 pack = array.array('B',[1, 12, 0, 0, 0, 1, 0, 0, 10, 0, 0, 6, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 134, 1, 0, 0, 0, 0, 0, 0, 160, 114, 78, 24, 9, 0, 0, 32, 161, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 32, 161, 7, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 206, 255, 32, 161, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 32, 161, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 161, 7, 0, 0, 0, 0, 0, 17, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 8, 15, 0, 5, 15, 0, 2, 0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 6, 0, 7, 0, 10, 0, 8, 0, 17, 0])
 s=(Settings(pack).ch1)
 
#readline.parse_and_bind('tab: complete')
#readline.parse_and_bind('set editing-mode vi')
else:
 dso = DasOszi(  0x049f, 0x505a,debug=False)
 r=dso.ReadSettings()
 IPython.embed()
 print(r.horiz.__dict__)