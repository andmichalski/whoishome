import sys


class WhoIs():

    def __init__(self):
        self.my_ip = None
        self.home_macs = self._get_home_macs()
        self.active_macs = self._open_active_macs()

    def _get_home_macs(self):
        home_macs = {}
        with open('home_macs.txt', 'r') as f:
            for line in f.read().splitlines():
                record = line.split(" ")
                MAC = record[1]
                IP = record[0]
                NAME = record[2]
                home_macs[MAC] = [IP, NAME, False]
        return home_macs

    def _open_active_macs(self):
        active_macs = {}
        with open('active_macs.txt', 'r') as f:
            for line in f.read().splitlines():
                record = line.split(" ")
                if ":" in record[1]:
                    MAC = record[1]
                    IP = record[0]
                    active_macs[MAC] = IP
                else:
                    self.my_ip = record[0]
        return active_macs

    def compare_macs(self):
        new_macs = []
        for active_mac in self.active_macs.keys():
            if active_mac in self.home_macs:
                self.home_macs[active_mac][2] = True
            else:
                new_macs.append((active_mac, self.active_macs[active_mac]))
        return new_macs

    def get_inmates_status(self):
        inmates = [(value[1], value[2]) for (_, value) in
                   self.home_macs.items()]
        return inmates

    def create_inmates_status_file(self):
        inmates = self.get_inmates_status()
        text = ""
        text += '{:^20s}|{:^20s}\n'.format("NAME", "IS_ACTIVE")
        text += 41 * "-" + "\n"
        for inmate in inmates:
            NAME = inmate[0]
            STATUS = inmate[1]
            text += '{:^20s}|{:^20s}\n'.format(NAME, str(STATUS))
        return text

    def write_log_file(self, text):
        with open("inmates_log.txt", "w+") as f:
            f.write(text)


if __name__ == "__main__":
    w = WhoIs()
    new_macs = w.compare_macs()
    text_log = w.create_inmates_status_file()
    print(text_log)
    # w.write_log_file(text_log)
    if new_macs != []:
        print("New macs: ", new_macs)
