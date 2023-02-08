from struct import *


class TriggerSettings():
    state = ["STOP", "Ready", "AUTO", "Trigd", "Scan",  "Astop",  "Armed"]
    type = ["Edge", "Video", "Pulse", "Slope", "O.T.", "ALT"]
    source = ["CH1", "CH2", "Ext", "Ext/5", "AC50"]

    def __init__(self, TRIG_STATE, TRIG_TYPE, TRIG_SRC, TRIG_MODE, TRIG_COUP, TRIG_VPOS, TRIG_FREQUENCY, TRIG_HOLDTIME_MIN, TRIG_HOLDTIME_MAX, TRIG_HOLDTIME, TRIG_EDGE_SLOPE, TRIG_VIDEO_NEG, TRIG_VIDEO_PAL, TRIG_VIDEO_SYN, TRIG_VIDEO_LINE, TRIG_PULSE_NEG, TRIG_PULSE_WHEN, TRIG_PULSE_TIME, TRIG_SLOPE_SET, TRIG_SLOPE_WIN, TRIG_SLOPE_WHEN, TRIG_SLOPE_V1, TRIG_SLOPE_V2, TRIG_SLOPE_TIME, TRIG_SWAP_CH1_TYPE, TRIG_SWAP_CH1_MODE, TRIG_SWAP_CH1_COUP, TRIG_SWAP_CH1_EDGE_SLOPE, TRIG_SWAP_CH1_VIDEO_NEG, TRIG_SWAP_CH1_VIDEO_PAL, TRIG_SWAP_CH1_VIDEO_SYN, TRIG_SWAP_CH1_VIDEO_LINE, TRIG_SWAP_CH1_PULSE_NEG, TRIG_SWAP_CH1_PULSE_WHEN, TRIG_SWAP_CH1_PULSE_TIME, TRIG_SWAP_CH1_SLOPE_SET, TRIG_SWAP_CH1_SLOPE_WIN, TRIG_SWAP_CH1_SLOPE_WHEN, TRIG_SWAP_CH1_SLOPE_V1, TRIG_SWAP_CH1_SLOPE_V2, TRIG_SWAP_CH1_SLOPE_TIME, TRIG_SWAP_CH2_TYPE, TRIG_SWAP_CH2_MODE, TRIG_SWAP_CH2_COUP, TRIG_SWAP_CH2_EDGE_SLOPE, TRIG_SWAP_CH2_VIDEO_NEG, TRIG_SWAP_CH2_VIDEO_PAL, TRIG_SWAP_CH2_VIDEO_SYN, TRIG_SWAP_CH2_VIDEO_LINE, TRIG_SWAP_CH2_PULSE_NEG, TRIG_SWAP_CH2_PULSE_WHEN, TRIG_SWAP_CH2_PULSE_TIME, TRIG_SWAP_CH2_SLOPE_SET, TRIG_SWAP_CH2_SLOPE_WIN, TRIG_SWAP_CH2_SLOPE_WHEN, TRIG_SWAP_CH2_SLOPE_V1, TRIG_SWAP_CH2_SLOPE_V2, TRIG_SWAP_CH2_SLOPE_TIME, TRIG_OVERTIME_NEG, TRIG_OVERTIME_TIME):
        self.TRIG_STATE = TRIG_STATE
        self.TRIG_TYPE = TRIG_TYPE
        self.TRIG_SRC = TRIG_SRC
        self.TRIG_MODE = TRIG_MODE
        self.TRIG_COUP = TRIG_COUP
        self.TRIG_VPOS = TRIG_VPOS
        self.TRIG_FREQUENCY = TRIG_FREQUENCY
        self.TRIG_HOLDTIME_MIN = TRIG_HOLDTIME_MIN
        self.TRIG_HOLDTIME_MAX = TRIG_HOLDTIME_MAX
        self.TRIG_HOLDTIME = TRIG_HOLDTIME
        self.TRIG_EDGE_SLOPE = TRIG_EDGE_SLOPE
        self.TRIG_VIDEO_NEG = TRIG_VIDEO_NEG
        self.TRIG_VIDEO_PAL = TRIG_VIDEO_PAL
        self.TRIG_VIDEO_SYN = TRIG_VIDEO_SYN
        self.TRIG_VIDEO_LINE = TRIG_VIDEO_LINE
        self.TRIG_PULSE_NEG = TRIG_PULSE_NEG
        self.TRIG_PULSE_WHEN = TRIG_PULSE_WHEN
        self.TRIG_PULSE_TIME = TRIG_PULSE_TIME
        self.TRIG_SLOPE_SET = TRIG_SLOPE_SET
        self.TRIG_SLOPE_WIN = TRIG_SLOPE_WIN
        self.TRIG_SLOPE_WHEN = TRIG_SLOPE_WHEN
        self.TRIG_SLOPE_V1 = TRIG_SLOPE_V1
        self.TRIG_SLOPE_V2 = TRIG_SLOPE_V2
        self.TRIG_SLOPE_TIME = TRIG_SLOPE_TIME
        self.TRIG_SWAP_CH1_TYPE = TRIG_SWAP_CH1_TYPE
        self.TRIG_SWAP_CH1_MODE = TRIG_SWAP_CH1_MODE
        self.TRIG_SWAP_CH1_COUP = TRIG_SWAP_CH1_COUP
        self.TRIG_SWAP_CH1_EDGE_SLOPE = TRIG_SWAP_CH1_EDGE_SLOPE
        self.TRIG_SWAP_CH1_VIDEO_NEG = TRIG_SWAP_CH1_VIDEO_NEG
        self.TRIG_SWAP_CH1_VIDEO_PAL = TRIG_SWAP_CH1_VIDEO_PAL
        self.TRIG_SWAP_CH1_VIDEO_SYN = TRIG_SWAP_CH1_VIDEO_SYN
        self.TRIG_SWAP_CH1_VIDEO_LINE = TRIG_SWAP_CH1_VIDEO_LINE
        self.TRIG_SWAP_CH1_PULSE_NEG = TRIG_SWAP_CH1_PULSE_NEG
        self.TRIG_SWAP_CH1_PULSE_WHEN = TRIG_SWAP_CH1_PULSE_WHEN
        self.TRIG_SWAP_CH1_PULSE_TIME = TRIG_SWAP_CH1_PULSE_TIME
        self.TRIG_SWAP_CH1_SLOPE_SET = TRIG_SWAP_CH1_SLOPE_SET
        self.TRIG_SWAP_CH1_SLOPE_WIN = TRIG_SWAP_CH1_SLOPE_WIN
        self.TRIG_SWAP_CH1_SLOPE_WHEN = TRIG_SWAP_CH1_SLOPE_WHEN
        self.TRIG_SWAP_CH1_SLOPE_V1 = TRIG_SWAP_CH1_SLOPE_V1
        self.TRIG_SWAP_CH1_SLOPE_V2 = TRIG_SWAP_CH1_SLOPE_V2
        self.TRIG_SWAP_CH1_SLOPE_TIME = TRIG_SWAP_CH1_SLOPE_TIME
        self.TRIG_SWAP_CH2_MODE = TRIG_SWAP_CH2_MODE
        self.TRIG_SWAP_CH2_COUP = TRIG_SWAP_CH2_COUP
        self.TRIG_SWAP_CH2_EDGE_SLOPE = TRIG_SWAP_CH2_EDGE_SLOPE
        self.TRIG_SWAP_CH2_VIDEO_NEG = TRIG_SWAP_CH2_VIDEO_NEG
        self.TRIG_SWAP_CH2_VIDEO_PAL = TRIG_SWAP_CH2_VIDEO_PAL
        self.TRIG_SWAP_CH2_VIDEO_SYN = TRIG_SWAP_CH2_VIDEO_SYN
        self.TRIG_SWAP_CH2_VIDEO_LINE = TRIG_SWAP_CH2_VIDEO_LINE
        self.TRIG_SWAP_CH2_PULSE_NEG = TRIG_SWAP_CH2_PULSE_NEG
        self.TRIG_SWAP_CH2_PULSE_WHEN = TRIG_SWAP_CH2_PULSE_WHEN
        self.TRIG_SWAP_CH2_PULSE_TIME = TRIG_SWAP_CH2_PULSE_TIME
        self.TRIG_SWAP_CH2_SLOPE_SET = TRIG_SWAP_CH2_SLOPE_SET
        self.TRIG_SWAP_CH2_SLOPE_WIN = TRIG_SWAP_CH2_SLOPE_WIN
        self.TRIG_SWAP_CH2_SLOPE_WHEN = TRIG_SWAP_CH2_SLOPE_WHEN
        self.TRIG_SWAP_CH2_SLOPE_V1 = TRIG_SWAP_CH2_SLOPE_V1
        self.TRIG_SWAP_CH2_SLOPE_V2 = TRIG_SWAP_CH2_SLOPE_V2
        self.TRIG_SWAP_CH2_SLOPE_TIME = TRIG_SWAP_CH2_SLOPE_TIME
        self.TRIG_OVERTIME_NEG = TRIG_OVERTIME_NEG
        self.TRIG_OVERTIME_TIME = TRIG_OVERTIME_TIME
        self.TRIG_SWAP_CH2_TYPE = TRIG_SWAP_CH2_TYPE
    #status,type,src,mode,coupling_mode_idx,vert_pos,freq,hold_time_min,hold_time_max,hold_time,edge_slope_idx,video_polarity_idx,video_system_idx,video_sync_idx,video_trigger_line,pulse_polarity_idx,pulse_condition_idx,pulse_width,slope_set,slope_win,slope_cond,slope_v1_value,slope_v2_value,slope_time,alt_ch1_type_idx,ch1_mode,ch1_coupling_idx,ch1_video_polarity,)

class MathSettings():
    def __init__(self,MATH_DISP, MATH_MODE, MATH_FFT_SRC, MATH_FFT_WIN, MATH_FFT_FACTOR, MATH_FFT_DB):
        self.MATH_MODE = MATH_MODE
        self.MATH_FFT_SRC = MATH_FFT_SRC
        self.MATH_FFT_WIN = MATH_FFT_WIN
        self.MATH_FFT_FACTOR = MATH_FFT_FACTOR
        self.MATH_FFT_DB = MATH_FFT_DB
        self.MATH_DISP = MATH_DISP

class HorizSettings():
    sec_divs_float = [i*1e-9 for i in [2,4,8]]+ \
                    [i*1e-8 for i in [2,4,8]]+ \
                    [i*1e-7 for i in [2,4,8]]+ \
                    [i*1e-6 for i in [2,4,8]]+ \
                    [i*1e-5 for i in [2,4,8]]+\
                    [i*1e-4 for i in [2,4,8]]+\
                    [i*1e-3 for i in [2,4,8]]+\
                    [i*1e-2 for i in [2,4,8]]+\
                    [i*1e-1 for i in [2,4,8]]+\
                    [i for i in [2,4,8]]+\
                    [i*1e1 for i in [2,4,8]]
    sec_divs_str = [ "2ns", "4ns", "8ns","20ns", "40ns", "80ns", "200ns", "400ns", "800ns","2us", "4us", "8us",
                     "20us", "40us", "80us", "200us", "400us", "800us","2ms", "4ms", "8ms",
                     "20ms", "40ms", "80ms", "200ms", "400ms", "800ms","2s", "4s", "8s","20s", "40s"
                    ]
    def __init__(self, HORIZ_TB, HORIZ_WIN_TB, HORIZ_WIN_STATE, HORIZ_TRIGTIME):
        self.HORIZ_TB = HORIZ_TB
        self.HORIZ_WIN_TB = HORIZ_WIN_TB
        self.HORIZ_WIN_STATE = HORIZ_WIN_STATE
        self.HORIZ_TRIGTIME = HORIZ_TRIGTIME

    def get_win_tb_str(self):
        return self.sec_divs_str[self.HORIZ_WIN_TB]
    
    def get_tb_str(self):
        return self.sec_divs_str[self.HORIZ_TB]
   
    def get_win_tb(self):
        return self.sec_divs_float[self.HORIZ_WIN_TB]
    
    def get_tb(self):
        return self.sec_divs_float[self.HORIZ_TB]
    
class DisplaySettings():
    def __init__(self,DISPLAY_MODE, DISPLAY_PERSIST, DISPLAY_FORMAT, DISPLAY_CONTRAST, DISPLAY_MAXCONTRAST, DISPLAY_GRID_KIND, DISPLAY_GRID_BRIGHT, DISPLAY_MAXGRID_BRIGHT):
        self.DISPLAY_MODE = DISPLAY_MODE
        self.DISPLAY_PERSIST = DISPLAY_PERSIST
        self.DISPLAY_FORMAT = DISPLAY_FORMAT
        self.DISPLAY_CONTRAST = DISPLAY_CONTRAST
        self.DISPLAY_MAXCONTRAST = DISPLAY_MAXCONTRAST
        self.DISPLAY_GRID_KIND = DISPLAY_GRID_KIND
        self.DISPLAY_GRID_BRIGHT = DISPLAY_GRID_BRIGHT
        self.DISPLAY_MAXGRID_BRIGHT = DISPLAY_MAXGRID_BRIGHT

class AcquireSettings():
    def __init__(self, ACQURIE_MODE, ACQURIE_AVG_CNT, ACQURIE_TYPE, ACQURIE_STORE_DEPTH):
        self.ACQURIE_MODE = ACQURIE_MODE
        self.ACQURIE_AVG_CNT = ACQURIE_AVG_CNT
        self.ACQURIE_TYPE = ACQURIE_TYPE
        self.ACQURIE_STORE_DEPTH = ACQURIE_STORE_DEPTH

class MeasureSettings():
    def __init__(self, MEASURE_ITEM1_SRC, MEASURE_ITEM1, MEASURE_ITEM2_SRC, MEASURE_ITEM2, MEASURE_ITEM3_SRC, MEASURE_ITEM3, MEASURE_ITEM4_SRC, MEASURE_ITEM4, MEASURE_ITEM5_SRC, MEASURE_ITEM5, MEASURE_ITEM6_SRC, MEASURE_ITEM6, MEASURE_ITEM7_SRC, MEASURE_ITEM7, MEASURE_ITEM8_SRC, MEASURE_ITEM8):
        self.MEASURE_ITEM1_SRC = MEASURE_ITEM1_SRC
        self.MEASURE_ITEM1 = MEASURE_ITEM1
        self.MEASURE_ITEM2_SRC = MEASURE_ITEM2_SRC
        self.MEASURE_ITEM2 = MEASURE_ITEM2
        self.MEASURE_ITEM3_SRC = MEASURE_ITEM3_SRC
        self.MEASURE_ITEM3 = MEASURE_ITEM3
        self.MEASURE_ITEM4_SRC = MEASURE_ITEM4_SRC
        self.MEASURE_ITEM4 = MEASURE_ITEM4
        self.MEASURE_ITEM5_SRC = MEASURE_ITEM5_SRC
        self.MEASURE_ITEM5 = MEASURE_ITEM5
        self.MEASURE_ITEM6_SRC = MEASURE_ITEM6_SRC
        self.MEASURE_ITEM6 = MEASURE_ITEM6
        self.MEASURE_ITEM7_SRC = MEASURE_ITEM7_SRC
        self.MEASURE_ITEM7 = MEASURE_ITEM7
        self.MEASURE_ITEM8_SRC = MEASURE_ITEM8_SRC
        self.MEASURE_ITEM8 = MEASURE_ITEM8

class ControlSettings():
    def __init__(self,CONTROL_TYPE, CONTROL_MENUID, CONTROL_DISP_MENU):
        self.CONTROL_TYPE = CONTROL_TYPE
        self.CONTROL_MENUID = CONTROL_MENUID
        self.CONTROL_DISP_MENU = CONTROL_DISP_MENU

# 1, 8, 0, 1, 0, 1, 0, 0, 0, 0,  #CH1 0:9
# 0, 6, 0, 0, 0, 1, 0, 0, 0, 0,  #CH2 10:19
# 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 134, 1, 0, 0, 0, 0, 0, 0, 160, 114, 78, 24, 9, 0, 0, 160, 134, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 32, 161, 7, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 206, 255, 32, 161, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 32, 161, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 161, 7, 0, 0, 0, 0, 0, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 8, 15, 0, 5, 15, 0, 2, 0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 6, 0, 7, 0, 10, 0, 8, 0, 42, 0])
class ChannelSettings():
    volt_div_arr_str = [ "10mV", "20mV","50mV", "100mV","200mV","500mV", "1V", "2V", "5V", "10V","20V","50V", "100V"]
    volt_div_arr_float = [ 0.010, 0.020, 0.050, 0.1, 0.2, 0.5, 1., 2., 5., 10., 20., 50., 100. ]
    volt_div_tuning_type_str = ["coarse","fine"]
    coupling = ['DC', 'AC','GND']
    probe = [1,10,100,1000]   ## probe type 1x, 10x etc
    phase = ['normal','inverted'] ## Phase 

    def __init__(self,is_on,volt_div_idx,coupling_idx,filter_20Mh_On,volt_div_tuning_type,probe_type_idx,phase_idx,volt_div_fine,pos) -> None:
        self.is_on = is_on # 0x00 off, 0x01 on

        self.volt_div_idx = volt_div_idx #  see volt_div_arr_str and volt_div_arr_float vars

        self.coupling_idx = coupling_idx #see coupling var
        self.filter_20MHz_On = filter_20Mh_On
        self.volt_div_tuning_type = volt_div_tuning_type
        self.probe_type_idx = probe_type_idx
        self.phase_idx = phase_idx #normal, inverted

        ###0x00 to 0x31 : when between "factor 2x" level
        ###0x01 to 0x4A : when between "factor 2.5x" levels 
        self.volt_div_fine = volt_div_fine #CNT_FINE

        # Position refer to center line of the LCD
        # Mid of screen i 0x00, above center line bytes are 
        # positive , below center line bytes are negative
        self.pos = pos
    
    def get_volt_div_str(self):
       return self.volt_div_arr_str[self.volt_div_idx]
    
    
    def get_volt_div_float(self):
       return self.volt_div_arr_float[self.volt_div_idx]
    
    def get_coupling(self):
       return self.coupling[self.coupling_idx]
        
    def get_filter_20MHz(self):
       return self.filter_20MHz_On

    def get_volt_div_tuning_type(self):
       return self.volt_div_tuning_type

    def get_probe_type(self):
       return self.probe[self.probe_type_idx]

    def get_phase_type(self):
       return self.phase[self.phase_idx]

    def get_volt_div_fine(self):
       return self.volt_div_fine

    def get_pos(self):
       return self.pos

    def get_settings(self)-> str:
        return self.__str__();

    def __str__(self) -> str:
       return (f'is_on {self.is_on}\n\
        volts_div {self.get_volt_div_str()} {self.volt_div_idx}\n\
        coupling {self.get_coupling()}\n\
        filter_20MHz {self.get_filter_20MHz()}\n\
        Tuning type {self.get_volt_div_tuning_type()}\n\
        Probe type: {self.get_probe_type()}\n\
        Phase {self.get_phase_type()}\n\
        Volt Div {self.get_volt_div_fine()}\n\
        Position {self.get_pos()}')
        

#################################
# #CH1 0:9
# #CH2 10:19
# #TRIG 20:159
# #HORIZ 160:170
# #MATH  171:176
# #DISPLAY 177:184
# #ACQURIE 185:188
# #MEASURE 189:204
# #CONTROL 205:207
class Settings():
    ch1 = None
    ch2 = None
    def __init__(self,ar_bytes) -> None:
        from_ = 0
        to = 10
        self.ch1 = self.read_ch_settings(ar_bytes[from_:to])

        from_=to
        to=from_+10
        self.ch2 = self.read_ch_settings(ar_bytes[from_:to])

        from_=to 
        to = from_+140
        #print(ar_bytes,ar_bytes[from_:to])
        
        self.trigger =self.read_trig_settings(ar_bytes[from_:to])

        from_=to 
        to = from_+11
        self.horiz =self.read_horiz_settings(ar_bytes[from_:to])
        
        from_=to 
        to = from_+6
        self.math =self.read_math_settings(ar_bytes[from_:to])

        from_=to 
        to = from_+8
        self.display =self.read_display_settings(ar_bytes[from_:to])

        from_=to 
        to = from_+4
        self.acquire =self.read_acquire_settings(ar_bytes[from_:to])

        from_=to 
        to = from_+16
        self.measure =self.read_measure_settings(ar_bytes[from_:to])

        from_=to 
        to = from_+3
        self.control =self.read_control_settings(ar_bytes[from_:to])

    def get_channel1(self):
        return self.ch1

    def get_channel2(self):
        return self.ch2

    def get_trigger(self):
        return self.trigger

    def get_horiz(self):
        return self.horiz

    def get_math(self):
        return self.math

    def get_display(self):
        return self.display

    def get_acquire(self):
        return self.acquire

    def get_measure(self):
        return self.measure

    def get_control(self):
        return self.measure
    
    
    ###########################################
    def read_ch_settings(self, ar_bytes ):
        settings = unpack(f'<{"B"*8}h', ar_bytes)
        return ChannelSettings(*settings)
    
    def read_trig_settings(self, ar_bytes ):
        settings = unpack(
            f'<{"B"*5}h{"Q"*4}{"B"*4}hBBQBBBhhQ{"B"*7}h{"B"*6}hhQ{"B"*7}hBBQBBBhhQBQ', ar_bytes)
        return TriggerSettings(*settings)
    
    #k
    def read_horiz_settings(self, ar_bytes ):
        settings = unpack('<BBBq', ar_bytes)
        return HorizSettings(*settings)
    
    #k
    def read_math_settings(self, ar_bytes ):
        settings = unpack(f'<{"B"*6}', ar_bytes)
        return MathSettings(*settings)
    
    #k
    def read_display_settings(self, ar_bytes ):
        settings = unpack(f'<{"B"*8}', ar_bytes)
        return DisplaySettings(*settings)
    
    #k
    def read_acquire_settings(self, ar_bytes ):
        settings = unpack(f'<{"B"*4}', ar_bytes)
        return AcquireSettings(*settings)

    #k
    def read_measure_settings(self, ar_bytes ):
        settings = unpack(f'<{"B"*16}', ar_bytes)
        return MeasureSettings(*settings)
    
    #k
    def read_control_settings(self, ar_bytes ):
        settings = unpack(f'<{"B"*3}', ar_bytes)
        return ControlSettings(*settings)
