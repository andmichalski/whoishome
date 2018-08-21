#! venv/bin/python
from collections import namedtuple
import nmap


class WifiScanner():

    def __init__(self):
        self.host = namedtuple("Host", "ip mac name")
        self.active_host = namedtuple('AHost', 'ip mac')
        self.nm = nmap.PortScanner()
        file = 'home_macs.txt'
        self.home_hosts = self._create_mac_list(file)
        self.home_macs = {host['mac']: host['name'] for host in self.home_hosts}
        self.active_hosts = []

    def _create_mac_list(self, file):
        mac_list = []
        with open("home_macs.txt", "r") as f:
            for line in f:
                record = line.split(" ")
                host = self.host(record[0], record[1], record[2])
                mac_list.append(host)
        return mac_list

# TODO work about correct output from nm scan - need mac adress
    def scan(self):
        report = []
        self.nm.scan(hosts='192.168.1.1/24', arguments='-n -sP')
        # self.nm.scan(hosts='192.168.1.1/24', arguments='-O')
        active_hosts = self.nm.all_hosts()
        # return active_hosts
        for host in active_hosts:
            result = self.nm.scan(host, arguments="-O")
            report.append(result)
        return report

    def check_home_host_is_on(self):
        active_macs = [active_host['mac'] for active_host in active_hosts]
        for active_mac in active_macs:
            if active_mac in self.home_macs:
                pass
            else:
                print("In home is new user!!!!!")




if __name__ == "__main__":
    wf = WifiScanner()
    active_hosts = wf.scan()
    print(active_hosts)
    # print(wf.home_macs)
