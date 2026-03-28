from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI
 
 
class FourHopTopo(Topo):
    def build(self, bw=100, delay="5ms", loss=0):
        hosts = [self.addHost(f"h{i}", ip=f"10.0.0.{i}/24") for i in range(1, 6)]
        link_opts = dict(bw=bw, delay=delay, loss=loss, use_htb=True)
        for i in range(len(hosts) - 1):
            self.addLink(hosts[i], hosts[i + 1], **link_opts)
 
 
def run(bw=100, delay="5ms", loss=0):
    setLogLevel("info")
    topo = FourHopTopo(bw=bw, delay=delay, loss=loss)
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    print("\n=== 4-Hop Topology Started ===")
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
