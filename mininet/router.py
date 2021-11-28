from mininet.topo import Topo 
#classe cria rede com 2 switches, e 3 hosts
#para executar no mininet, escreva: sudo mn --custom ./router.py --topo router
class Router_Topo(Topo): 
    def __init__(self): 
        "Create P2P topology." 
 
        # Initialize topology 
        Topo.__init__(self) 
 
        # Add hosts and switches  
        H1 = self.addHost('h1') 
        H2 = self.addHost('h2') 
        H3 = self.addHost('h3') 
        S1 = self.addSwitch('s1') 
        S2 = self.addSwitch('s2') 
 
        # Add links 
        self.addLink(H1, S1) 
        self.addLink(H2, S1) 
        self.addLink(H2, S2) 
        self.addLink(H3, S2) 
 
topos = { 
        'router': (lambda: Router_Topo()) 
} 
