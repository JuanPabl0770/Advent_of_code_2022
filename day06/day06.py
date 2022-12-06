class DeviceFixer:
    def get_start_of_packet(self, datastream, num_diff_chars):
        for i in range(len(datastream)):
            if i >= num_diff_chars and len({datastream[i] for i in range(i, i - num_diff_chars, -1)}) == num_diff_chars:
                return i + 1, {datastream[i] for i in range(i, i - num_diff_chars, -1)}
        return None


f = open('input.txt', 'r')
datastream = f.readline()
deviceFixer = DeviceFixer()
print(deviceFixer.get_start_of_packet(datastream.strip(), 4))
print(deviceFixer.get_start_of_packet(datastream.strip(), 14))
f.close()
