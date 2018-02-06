
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        HostL = self.addHost( 'h1' )
        HostR = self.addHost( 'h2' )
        SwitchL = self.addSwitch( 's3' )
        SwitchR = self.addSwitch( 's4' )

        # Add links
        self.addLink( HostL, SwitchL )
        self.addLink( SwitchL, SwitchL )
        self.addLink( SwitchR, HostR )


topos = { 'mytopo': ( lambda: MyTopo() ) }
