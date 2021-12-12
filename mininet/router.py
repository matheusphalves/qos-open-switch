# -- coding: utf-8 --
from mininet.topo import Topo 
#classe cria rede com 2 switches, e 4 hosts
#para executar no mininet, escreva: sudo mn --custom ./router.py --topo router
class Minimal_Topo(Topo): 
    def __init__(self): 
        "Create topology." 
 
        # Initialize topology 
        Topo.__init__(self) 
 
        # Add hosts and switches  
        H1 = self.addHost('h1') 
        H2 = self.addHost('h2') 
        H3 = self.addHost('h3') 
        H4 = self.addHost('h4') 
        S1 = self.addSwitch('s1') 
        S2 = self.addSwitch('s2') 
 
        # Add links 
        self.addLink(H1, S1) 
        self.addLink(H2, S1) 
        self.addLink(H3, S2) 
        self.addLink(H4, S2) 
        self.addLink(S1, S2)
 
topos = { 
        'router': (lambda: Minimal_Topo()) 
} 