from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Hostone = self.addHost( 'h1' )
        Hosttwo = self.addHost( 'h2' )
        Hostthree = self.addHost( 'h3' )
        Hostfour = self.addHost( 'h4' )
        Hostfive = self.addHost( 'h5' )
        Hostsix = self.addHost( 'h6' )
        Hostseven = self.addHost( 'h7' )
        Hosteight = self.addHost( 'h8' )

        Switchone = self.addSwitch( 's1' )
        Switchtwo = self.addSwitch( 's2' )
        Switchthree = self.addSwitch( 's3' )
        Switchfour = self.addSwitch( 's4' )
        Switchfive = self.addSwitch( 's5' )
        Switchsix = self.addSwitch( 's6' )
        Switchseven = self.addSwitch( 's7' )

        # Add links
        self.addLink( Hostone, Switchfour )
        self.addLink( Hosttwo, Switchfour )
        self.addLink( Hostthree, Switchfive )
        self.addLink( Hostfour, Switchfive )
        self.addLink( Hostfive, Switchsix )
        self.addLink( Hostsix, Switchsix )
        self.addLink( Hostseven, Switchseven )
        self.addLink( Hosteight, Switchseven )
        self.addLink( Switchtwo, Switchone )
        self.addLink( Switchthree, Switchone )
        self.addLink( Switchfour, Switchtwo )
        self.addLink( Switchfive, Switchtwo )
        self.addLink( Switchsix, Switchthree )
        self.addLink( Switchseven, Switchthree )



topos = { 'mytopo': ( lambda: MyTopo() ) }
