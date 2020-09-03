#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: TEXT TXRX
# Author: zuks
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import pam  # embedded python module
import pmt

from gnuradio import qtgui

class text_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "TEXT TXRX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("TEXT TXRX")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "text_simulation")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.tail_len = tail_len = 5
        self.sps = sps = 10
        self.ptype = ptype = 'rect'
        self.bps = bps = 1
        self.alpha = alpha = 0.2
        self.tag = tag = gr.tag_utils.python_to_tag((0, pmt.intern("Z"), pmt.intern("0x5a"), pmt.intern("Vsrc")))
        self.samp_rate = samp_rate = 320e3
        self.pttaps2 = pttaps2 = pam.pamhRt(sps,ptype,[tail_len,alpha])
        self.pttaps = pttaps = pam.pamampt(sps,ptype,[tail_len,alpha])
        self.polarity = polarity = 1
        self.noise = noise = 0
        self.gain = gain = 1
        self.delay = delay = 0
        self.b_eds = b_eds = 0
        self.M = M = 2**bps
        self.FB = FB = 32000

        ##################################################
        # Blocks
        ##################################################
        # Create the options list
        self._polarity_options = (0, 1, )
        # Create the labels list
        self._polarity_labels = ('unipolar', 'polar', )
        # Create the combo box
        # Create the radio buttons
        self._polarity_group_box = Qt.QGroupBox('polarity' + ": ")
        self._polarity_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._polarity_button_group = variable_chooser_button_group()
        self._polarity_group_box.setLayout(self._polarity_box)
        for i, _label in enumerate(self._polarity_labels):
            radio_button = Qt.QRadioButton(_label)
            self._polarity_box.addWidget(radio_button)
            self._polarity_button_group.addButton(radio_button, i)
        self._polarity_callback = lambda i: Qt.QMetaObject.invokeMethod(self._polarity_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._polarity_options.index(i)))
        self._polarity_callback(self.polarity)
        self._polarity_button_group.buttonClicked[int].connect(
            lambda i: self.set_polarity(self._polarity_options[i]))
        self.top_grid_layout.addWidget(self._polarity_group_box)
        self._noise_range = Range(0, 2, 0.01, 0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'noise', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "RX_TD", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "TX_TD", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0_0_0_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "RX_FD", #name
            1
        )
        self.qtgui_freq_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "TX_FD", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        # Create the options list
        self._ptype_options = ('rect', 'tri', 'sinc', 'rcf', 'rrcf', )
        # Create the labels list
        self._ptype_labels = ('rect', 'tri', 'sinc', 'rcf', 'rrcf', )
        # Create the combo box
        # Create the radio buttons
        self._ptype_group_box = Qt.QGroupBox('ptype' + ": ")
        self._ptype_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._ptype_button_group = variable_chooser_button_group()
        self._ptype_group_box.setLayout(self._ptype_box)
        for i, _label in enumerate(self._ptype_labels):
            radio_button = Qt.QRadioButton(_label)
            self._ptype_box.addWidget(radio_button)
            self._ptype_button_group.addButton(radio_button, i)
        self._ptype_callback = lambda i: Qt.QMetaObject.invokeMethod(self._ptype_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._ptype_options.index(i)))
        self._ptype_callback(self.ptype)
        self._ptype_button_group.buttonClicked[int].connect(
            lambda i: self.set_ptype(self._ptype_options[i]))
        self.top_grid_layout.addWidget(self._ptype_group_box)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(sps, pttaps)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_1 = filter.fir_filter_fff(sps, [1])
        self.fir_filter_xxx_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(1, pttaps2)
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.blocks_vector_source_x_0 = blocks.vector_source_b(list(ord(i) for i in "Zombie"), True, 1, [tag])
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(bps, b_eds)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(bps, b_eds)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(gain)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, polarity*0.5+(1-polarity)*1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/dev/pts/0', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/dev/pts/1', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_char*1, delay)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, polarity*0.5+(1-polarity)*1)
        self.blocks_and_const_xx_0_0 = blocks.and_const_bb(255)
        self.blocks_and_const_xx_0 = blocks.and_const_bb(255)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(polarity*(M-1)+(1-polarity)*0)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(-polarity*(M-1)+(1-polarity)*0)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_f(analog.GR_GAUSSIAN, noise, 0, 8192)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_and_const_xx_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_and_const_xx_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_and_const_xx_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.fir_filter_xxx_1, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_and_const_xx_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_and_const_xx_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.fir_filter_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.fir_filter_xxx_1, 0), (self.qtgui_freq_sink_x_0_0_0_0, 0))
        self.connect((self.fir_filter_xxx_1, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "text_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tail_len(self):
        return self.tail_len

    def set_tail_len(self, tail_len):
        self.tail_len = tail_len
        self.set_pttaps(pam.pamampt(self.sps,self.ptype,[self.tail_len,self.alpha]))
        self.set_pttaps2(pam.pamhRt(self.sps,self.ptype,[self.tail_len,self.alpha]))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_pttaps(pam.pamampt(self.sps,self.ptype,[self.tail_len,self.alpha]))
        self.set_pttaps2(pam.pamhRt(self.sps,self.ptype,[self.tail_len,self.alpha]))

    def get_ptype(self):
        return self.ptype

    def set_ptype(self, ptype):
        self.ptype = ptype
        self.set_pttaps(pam.pamampt(self.sps,self.ptype,[self.tail_len,self.alpha]))
        self.set_pttaps2(pam.pamhRt(self.sps,self.ptype,[self.tail_len,self.alpha]))
        self._ptype_callback(self.ptype)

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.set_M(2**self.bps)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_pttaps(pam.pamampt(self.sps,self.ptype,[self.tail_len,self.alpha]))
        self.set_pttaps2(pam.pamhRt(self.sps,self.ptype,[self.tail_len,self.alpha]))

    def get_tag(self):
        return self.tag

    def set_tag(self, tag):
        self.tag = tag
        self.blocks_vector_source_x_0.set_data(list(ord(i) for i in "Zombie"), [self.tag])

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)

    def get_pttaps2(self):
        return self.pttaps2

    def set_pttaps2(self, pttaps2):
        self.pttaps2 = pttaps2
        self.fir_filter_xxx_0_0.set_taps(self.pttaps2)

    def get_pttaps(self):
        return self.pttaps

    def set_pttaps(self, pttaps):
        self.pttaps = pttaps
        self.interp_fir_filter_xxx_0.set_taps(self.pttaps)

    def get_polarity(self):
        return self.polarity

    def set_polarity(self, polarity):
        self.polarity = polarity
        self._polarity_callback(self.polarity)
        self.blocks_add_const_vxx_0.set_k(-self.polarity*(self.M-1)+(1-self.polarity)*0)
        self.blocks_add_const_vxx_0_0.set_k(self.polarity*(self.M-1)+(1-self.polarity)*0)
        self.blocks_char_to_float_0.set_scale(self.polarity*0.5+(1-self.polarity)*1)
        self.blocks_float_to_char_0.set_scale(self.polarity*0.5+(1-self.polarity)*1)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_fastnoise_source_x_0.set_amplitude(self.noise)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.blocks_multiply_const_vxx_0.set_k(self.gain)

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0_0.set_dly(self.delay)
        self.blocks_delay_0_1.set_dly(self.delay)

    def get_b_eds(self):
        return self.b_eds

    def set_b_eds(self, b_eds):
        self.b_eds = b_eds

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.blocks_add_const_vxx_0.set_k(-self.polarity*(self.M-1)+(1-self.polarity)*0)
        self.blocks_add_const_vxx_0_0.set_k(self.polarity*(self.M-1)+(1-self.polarity)*0)

    def get_FB(self):
        return self.FB

    def set_FB(self, FB):
        self.FB = FB





def main(top_block_cls=text_simulation, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
