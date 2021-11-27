from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_5
from ryu.app.simple_switch_15 import SimpleSwitch15


class BeHub(SimpleSwitch15):
    #OFP_VERSIONS = [ofproto_v1_5.OFP_VERSION]
    def __init__(self, *args,**kwargs):
        super(BeHub, self).__init__(*args, **kwargs)


    @set_ev_cls(ofp_event.EventOFPPacketIn,MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser


        actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
        out = ofp_parser.OFPPacketOut(datapath = dp, buffer_id = msg.buffer_id, in_port = msg.in_port, actions = actions)
        dp.send_msg(out)