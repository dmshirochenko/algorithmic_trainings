import math

with open("input.txt", "r") as reader:
    n, k = map(int, reader.readline().strip().split(" "))


class Device:
    def __init__(self, device_num, n, k):
        self.device_num = device_num
        self.total_devices = n
        self.total_packages_to_download = k
        self.downloaded_parts = set()
        self.devices_values = self.initial_devices_values_dct_creation()
        self.timeslot_counter = 0

    def is_all_packages_loaded(self):
        if len(self.downloaded_parts) == self.total_packages_to_download:
            return True

        return False

    def choose_package_to_request(self, package_dct):
        package_to_request = None
        min_num_dowloaded_package = math.inf
        if len(self.downloaded_parts) < self.total_packages_to_download:
            for package_num, package_info in package_dct.items():
                if package_info["num_times_downloaded"] < min_num_dowloaded_package:
                    if package_num not in self.downloaded_parts:
                        min_num_dowloaded_package = package_info["num_times_downloaded"]
                        package_to_request = package_num

        return package_to_request

    def initial_devices_values_dct_creation(self):
        device_values_to_return = dict()

        for i in range(self.total_devices):
            if i == self.device_num:
                continue
            device_values_to_return[i] = 0

        return device_values_to_return

    def choose_device_to_send_package(self, lst_of_device_and_packages):

        device_to_allow_to_download = None
        package_to_download = None
        max_priority = -math.inf

        for device, package in lst_of_device_and_packages:
            current_priority = self.devices_values[device.device_num]

            if (
                device_to_allow_to_download is None
                or (current_priority > max_priority)
                or (
                    current_priority == max_priority
                    and len(device.downloaded_parts) < len(device_to_allow_to_download.downloaded_parts)
                )
                or (
                    current_priority == max_priority
                    and len(device.downloaded_parts) == len(device_to_allow_to_download.downloaded_parts)
                    and device.device_num < device_to_allow_to_download.device_num
                )
            ):

                max_priority = current_priority
                device_to_allow_to_download = device
                package_to_download = package

        return device_to_allow_to_download, package_to_download

    def download_package(self, source_device, package):
        self.downloaded_parts.add(package)
        self.devices_values[source_device.device_num] += 1

    def __repr__(self):
        lst_to_show = []
        for part in self.downloaded_parts:
            lst_to_show.append(part + 1)
        return f"{self.device_num + 1} : {lst_to_show}"


class Network:
    def __init__(self, n, k):
        self.device_pool = self.device_pool_creation(n, k)
        self.total_device = n
        self.package_to_deliver = k
        self.total_package_to_deliver = (n - 1) * k
        self.package_num_times_dowloaded = self.initial_package_num_times_dowloaded_creation(k)
        self.request_pool = dict()
        self.fully_updated_devices = set()

    def device_pool_creation(self, n, k):
        device_pool_to_return = []
        # master device setting
        master_device = Device(0, n, k)
        master_device.timeslot_counter = k
        for i in range(k):
            master_device.downloaded_parts.add(i)

        device_pool_to_return.append(master_device)

        # slave device creation
        for i in range(1, n):
            device_pool_to_return.append(Device(i, n, k))

        return device_pool_to_return

    def initial_package_num_times_dowloaded_creation(self, k):
        initial_package_num_times_dowloaded = dict()
        for i in range(k):
            initial_package_num_times_dowloaded[i] = {"num_times_downloaded": 0, "on_devices": {self.device_pool[0]}}

        return initial_package_num_times_dowloaded

    def downloaded_package_network_update(self, package, device_recieved_package):
        self.package_num_times_dowloaded[package]["num_times_downloaded"] += 1
        self.package_num_times_dowloaded[package]["on_devices"].add(device_recieved_package)
        self.total_package_to_deliver -= 1

    def choose_device_to_ask_package(self, package_to_request, requested_device):
        device_to_return = None
        min_package_per_device = math.inf

        for device in self.package_num_times_dowloaded[package_to_request]["on_devices"]:
            if device == requested_device:
                continue
            if len(device.downloaded_parts) < min_package_per_device:
                min_package_per_device = len(device.downloaded_parts)
                device_to_return = device
            elif len(device.downloaded_parts) == min_package_per_device:
                if device_to_return.device_num > device.device_num:
                    device_to_return = device

        return device_to_return

    def add_to_request_pool(self, requester, destination, package):
        if destination not in self.request_pool:
            self.request_pool[destination] = [(requester, package)]
        else:
            self.request_pool[destination].append((requester, package))

    def clear_request_pool(self):
        if self.request_pool:
            self.request_pool = dict()


if __name__ == "__main__":
    network_instance = Network(n, k)
    network_instance.device_pool_creation(n, k)

    count_timeslots = 1
    while network_instance.total_package_to_deliver > 0:
        # first part - packages request
        # with open('logs.txt', 'a') as file:
        #    print('BEFORE: ', network_instance.device_pool,  file=file)
        for device in network_instance.device_pool[1:]:
            if device in network_instance.fully_updated_devices:
                continue
            package_to_request = device.choose_package_to_request(network_instance.package_num_times_dowloaded)
            if package_to_request is not None:
                device_to_ask = network_instance.choose_device_to_ask_package(package_to_request, device)
                # print('device', device, 'device_to_ask', device_to_ask, 'package_to_request', package_to_request)
                network_instance.add_to_request_pool(device, device_to_ask, package_to_request)

        # with open('logs.txt', 'a') as file:
        #    print('REQUESTS:', network_instance.request_pool, file=file)
        lst_of_updates = []
        # second part - device package select
        for destination_device, lst_of_device_and_packages in network_instance.request_pool.items():
            device_which_will_recieve_package, package = destination_device.choose_device_to_send_package(
                lst_of_device_and_packages
            )
            lst_of_updates.append((destination_device, device_which_will_recieve_package, package))

        for destination_device, device_which_will_recieve_package, package in lst_of_updates:
            device_which_will_recieve_package.download_package(destination_device, package)
            network_instance.downloaded_package_network_update(package, device_which_will_recieve_package)

        for device in network_instance.device_pool[1:]:
            if device not in network_instance.fully_updated_devices and device.is_all_packages_loaded():
                device.timeslot_counter = count_timeslots
                network_instance.fully_updated_devices.add(device)

        # with open('logs.txt', 'a') as file:
        #    print('AFTER: ', network_instance.device_pool, "\n", file=file)
        network_instance.clear_request_pool()
        count_timeslots += 1

    ans = ""
    for device in network_instance.device_pool[1:]:
        ans += str(device.timeslot_counter) + " "

    with open("output.txt", "w") as file:
        file.write(str(ans))
