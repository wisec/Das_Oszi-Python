# -*- coding: utf-8 -*-
#
# Thanks to:
#   https://elinux.org/Das_Oszi_Protocol (protocolo)
#   https://randomprojects.org/wiki/Voltcraft_DSO-3062C (uso de usb)
#
# My DSO5102P has idVendor=0x049f and idProduct=0x505a, EndpointAddress=0x81 and wMaxPacketSize=0x200
#
#--

import usb
import time
import array
import numpy as np 

from .settings import Settings

## MAX ATTEMPTS to retry USB
MAX_ATTEMPTS = 3 

class DasOszi():
    def __init__( self, idVendor, idProduct, debug=False ):
        self.debug = debug
        self.dev = usb.core.find( idVendor=idVendor, idProduct=idProduct )
        if( self.dev is None ):
            print( 'DSO Not Found' )
            exit()
        #print(self.dev)
        # unload de 'cdc_subset'
        for config in self.dev:
            for i in range(config.bNumInterfaces):
                if( self.dev.is_kernel_driver_active( i ) is True):
                    self.dev.detach_kernel_driver(i)
                    usb.util.claim_interface(self.dev, i)
                    self._dump(f"Claiming {i}")
                    #c+=1
                    self._dump("Claim ing usb.util.dispose_resources(my_device)but we need to detach kernel driver")
                #self.dev.detach_kernel_driver( 0 )

        # # limpia buffers
        # while( True ):
        #     try:
        #         r = self.dev.read( 0x81, 512, 1000 )
        #         self._dump( 'FLUSH', r )
        #     except usb.core.USBError as e:
        #         print( 'FLUSH:', e )
        #         break
    
    def __del__(self):
        if( self.debug ):
            print("DETACHED")
        if self.dev:
            usb.util.dispose_resources(self.dev)
            self.dev.attach_kernel_driver(0)

    def _dump( self, origin, data=None, prefix="" ):
        if( self.debug ):
            print(prefix) if prefix is not "" else ''
            if data is not None:
             print( origin, ':',  [ '0x%02X' % h for h in data ] )
            print(f"END {prefix}") if prefix is not "" else ''
            

    
    def _SendCommand( self, origin, cmd, data, isDebug=False ):
        assert isinstance( data, array.array ), '\'data\' must be array.array(\'B\')'

        time.sleep( 0.1 )
        action = 0x43 if isDebug else 0x53
        packetLen = 1 + len( data ) + 1
        packet = array.array( 'B', [ action, packetLen & 0xFF, ( packetLen >> 8 ) & 0xFF, cmd ] ) + data
        packet = packet + array.array( 'B', [ sum( packet ) & 0xFF ] )

        self._dump( origin.upper(), packet, prefix="SENDING: " )
        self.dev.write( 0x02, packet, 1000 )
        return packet

    def _ReadAnswer( self, origin, rcode ):
        r = None
        attempt = 1
        while( True ):
            try:
                if attempt > MAX_ATTEMPTS:
                    return
                r = self.dev.read( 0x81, 1024*1024, 1000 )
                attempt=0
                chksum = sum( r[:-1] ) & 0xFF
                if( chksum != r[-1] ):
                    self._dump( 'BADCHKSUM', r[:5] )
                if( r[3] == rcode ):
                    break
                else:
                    self._dump( 'BADANSWER', r[:5] )
            except Exception as ex:
                attempt+=1
                print(ex)
                

        
        self._dump( origin, r[:5], prefix="RECEIVED: " )
        return r

    def get_packet_len(self, packet):
        length = packet[1]
        length += packet[2] * 256
        #print(f"PCK Len: {length}")
        return length

    #---- USB functionalities

    def Echo( self, data ):
        data = array.array( 'B', data )
        self._SendCommand( 'Echo', 0x00, data )
        r = self._ReadAnswer( 'Echo', 0x80 )
        return list( r[4:-1] )
       
    def ReadSettings( self ):
        self._SendCommand( 'ReadSettings', 0x01, array.array( 'B' ) )
        r = self._ReadAnswer( 'ReadSettings', 0x81 )
        self.settings = Settings(r[4:-1])
        return self.settings

    def WriteSettings( self):

       # return array.array('B',self.settings.get_packed_config())
        self._SendCommand( 'WriteSettings', 0x11, array.array('B',self.settings.get_packed_config()) )
        r = self._ReadAnswer( 'WriteSettings', 0x91 )

        return r[4:-1]

    
    def lock(self):
        return self.LockControlPanel( )

    def unlock(self):
        return self.UnLockControlPanel( )

    # Locks control panel
    def LockControlPanel( self ):
        self._SendCommand( 'LockControlPanel', 0x12, array.array( 'B', [ 0x01, 0x01 ] ) )
        return self._ReadAnswer( 'LockControlPanel', 0x92 )

    # Unlocks control panel
    def UnLockControlPanel( self ):
        self._SendCommand( 'UnLockControlPanel', 0x12, array.array( 'B', [ 0x01, 0x00 ] ) )
        return self._ReadAnswer( 'UnLockControlPanel', 0x92 )

    def run(self):
        return self.StartAcquisition()
    
    def stop(self):
        return self.StopAcquisition()
    
    # run 
    def StartAcquisition( self ):
        self._SendCommand( 'StartAcquisition', 0x12, array.array( 'B', [ 0x00, 0x00 ] ) )
        return self._ReadAnswer( 'StartAcquisition', 0x92 )

    # stop
    def StopAcquisition( self ):
        self._SendCommand( 'StopAcquisition', 0x12, array.array( 'B', [ 0x00, 0x01 ] ) )
        return self._ReadAnswer( 'StopAcquisition', 0x92 )


    def ReadSampleData( self, channel ):
        self._SendCommand( 'ReadSampleData', 0x02, array.array( 'B', [ 0x01, channel   ] ) ) ## NB: why channel & 0x1?
        r = array.array( 'B' )
        raw_data_float = array.array( 'f' )
        sdlen = 0
        while( True ):
            d = self._ReadAnswer( 'ReadSampleData', 0x82 )
            if d is None:
                return []
            self.get_packet_len(d)
            command = d[3]
            #print(f"Command {'0x%02X' % command}")
            subcommand = d[4]
            if( subcommand == 0x00 ): # Total length of data sample
                sdlen = d[5] + (d[6]<<8) + (d[7]<<16) 
                print(f"Total Len { sdlen}")
            elif( subcommand == 0x01 ):
                channel = d[5]
                print(f"channel: {channel}")
                r = r + d[6:-1]
                
            elif( subcommand == 0x02 ):
                channel = d[5]
                print(f"End Transmission for channel: {channel}")
                raw_data_float = [(b / 127.0) if b < 128 else ((b - 256) / 128.0) for b in r]
                # d[6] == channel
                break;
            else:
                channel = d[5]
                print(f"[EE] Error received with code: {subcommand} for channel {channel}")
                # some error
                # d[6] == channel
                break;
        #print( sdlen, len( r ) )
        return raw_data_float

    # OK
    def ReadFile( self, fname ):
        p = self._SendCommand( 'ReadFile', 0x10, array.array( 'B', bytearray( '\x00' + fname, 'utf8' ) ) )
        r = array.array( 'B' )
        while( True ):
            d = self._ReadAnswer( 'ReadFile', 0x90 )
            if( d[4] == 0x01 ):
                r = r + d[5:-1]
            else:
                # checksum???
                break;
        r = ''.join( [ chr( c ) for c in r ] )
        return r

    # NOT TESTED 0x53 0x04 0x00 0x13
    def KeyTrigger( self, b1, b2 ):
        self._SendCommand( 'KeyTrigger', 0x13, array.array( 'B', [ b1, b2 ] ) )
        return self._ReadAnswer( 'KeyTrigger', 0x93 )

    # NOT TESTED
    def Screenshot( self ):
        self._SendCommand( 'Screenshot', 0x20, array.array( 'B' ) )
        bmp = array.array( 'B' )
        while( True ):
            d = self._ReadAnswer( 'Screenshot', 0xA0 )
            if( d[4] == 0x01 ):
                bmp = bmp + d[5:-1]
            else:
                # checksum???
                break;
        img = np.frombuffer( bytearray( bmp ), dtype=np.uint16 ).reshape( 480, 800 )
        img = img.astype( np.uint8 )
        return img

    # OK
    def ReadSystemTime( self ):
        self._SendCommand( 'ReadSystemTime', 0x21, array.array( 'B' ) )
        r = self._ReadAnswer( 'ReadSystemTime', 0xA1 )
        r = '%04d-%02d-%02d %02d:%02d:%02d' % ( r[5]*0xFF + r[4] + 7, r[6], r[7], r[8], r[9], r[10] )
        return r

    # OK
    def RemoteShell( self, cmdline ):
        self._SendCommand( 'RemoteShell', 0x11, array.array( 'B', bytearray( cmdline, 'utf8' ) ), True )
        r = self._ReadAnswer( 'RemoteShell', 0x91 )
        r = ''.join( [ chr( c ) for c in r ] )
        return r


##### Helper functions

    def compute_voltage(self,r, scale):
        return [i*scale for i in r]

    def compute_time(self,r, scale):
        return [i*scale for i in r]

