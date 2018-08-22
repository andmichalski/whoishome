class WhoIs():

    def __init__(self):
        self.my_ip = None
        self.home_macs = self._get_home_macs()
        self.active_macs = self._open_active_macs()

    def _get_home_macs(self):
        home_macs = {}
        with open('home_macs.txt', 'r') as f:
            for line in f:
                record = line.split(" ")
                MAC = record[1]
                IP = record[0]
                NAME = record[2]
                home_macs[MAC] = [IP, NAME, False]
        return home_macs

    def _open_active_macs(self):
        active_macs = {}
        with open('active_macs.txt', 'r') as f:
            for line in f:
                record = line.split(" ")
                if len(record) == 2:
                    MAC = record[1]
                    IP = record[0]
                    active_macs[MAC] = IP
                else:
                    self.my_ip = record[0]
                    del active_macs[record[0]]
        return active_macs

    def compare_macs(self):
        new_macs = []
        for active_mac in self.active_macs:
            if active_mac in self.home_macs:
                self.home_macs[active_mac][2] = True
            else:
                new_macs.append((active_mac, self.active_macs[active_mac]))
        return new_macs

    def get_inmates_status(self):
        inmates = [(value[1], value[2]) for (_, value) in self.home_macs.items()]
        return inmates

    def print_inmates_status(self):
        inmates = self.get_inmates_status()
        print("NAME | IS_ACTIVE")
        for inmate in inmates:
            NAME = inmate[0]
            STATUS = inmate[1]
            print(NAME + ': ' + str(STATUS))


if __name__ == "__main__":
    w = WhoIs()
    print(w.compare_macs())
    w.print_inmates_status()
    #TODO remove files