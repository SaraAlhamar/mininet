#!/usr/bin/python

"Create a 64-node tree network, and test connectivity using ping."

from mininet.log import setLogLevel
from mininet.net import init, Mininet
from mininet.node import KernelSwitch, UserSwitch, OVSKernelSwitch
from mininet.topolib import TreeTopo



def treePing64():
    "Run ping test on 64-node tree networks."

    results = {}
    switches = { 'reference kernel': KernelSwitch,
        'reference user': UserSwitch,
        'Open vSwitch kernel': OVSKernelSwitch }

    for name in switches.keys():
        print "*** Testing", name, "datapath"
        switch = switches[ name ]
        network = TreeNet( depth=2, fanout=8, switch=switch )
        result = network.run( network.pingAll )
        results[ name ] = result

    print
    print "*** Tree network ping results:"
    for name in switches.keys():
        print "%s: %d%% packet loss" % ( name, results[ name ] )
    print

if __name__ == '__main__':
    setLogLevel( 'info' )
    init()
    treePing64()