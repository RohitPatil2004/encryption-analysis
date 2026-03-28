from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI
 
 
class TwoHopTopo(Topo):
    def build(self, bw=100, delay="5ms", loss=0):
        h1 = self.addHost("h1", ip="10.0.0.1/24")
        h2 = self.addHost("h2", ip="10.0.0.2/24")
        h3 = self.addHost("h3", ip="10.0.0.3/24")
        link_opts = dict(bw=bw, delay=delay, loss=loss, use_htb=True)
        self.addLink(h1, h2, **link_opts)
        self.addLink(h2, h3, **link_opts)
 
 
def run(bw=100, delay="5ms", loss=0):
    setLogLevel("info")
    topo = TwoHopTopo(bw=bw, delay=delay, loss=loss)
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    print("\n=== 2-Hop Topology Started ===")
    net.pingAll()
    CLI(net)
    net.stop()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--bw",    type=int,   default=100)
    parser.add_argument("--delay", type=str,   default="5ms")
    parser.add_argument("--loss",  type=float, default=0)
    args = parser.parse_args()
    run(bw=args.bw, delay=args.delay, loss=args.loss)
