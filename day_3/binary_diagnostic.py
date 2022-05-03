class BinaryDiagnostic:
    def __init__(self, input_binary_report):
        self.binary_report = input_binary_report

    def nth_bits(self, bits, n):
        """
        Finds the nth bits of the binary report
        :return: A string of 1s and 0s
        """
        nth_bits = ""
        for entry in bits:
            nth_bit = entry[n]
            nth_bits += nth_bit
        return nth_bits

    def most_common_bit(self, input_binary_string):
        return input_binary_string.count("1") >= input_binary_string.count("0")


    def get_rate_binary(self):
        binary_number = ""
        for index in range(len(self.binary_report[0])):
            bits = self.nth_bits(self.binary_report, index)
            binary_number += "1" if self.most_common_bit(bits) else "0"
        return binary_number


    @property
    def gamma_rate(self):
        return int(self.get_rate_binary(), 2)

    @property
    def epsilon_rate(self):
        inverted = int(self.get_rate_binary(), 2) ^ 0b11111
        return inverted

    @property
    def power_consumption(self):
        return self.gamma_rate * self.epsilon_rate

    @property
    def oxygen_generator_rating(self):
        cache = self.binary_report.copy()
        for index in range(len(self.binary_report[0])):
            bits = self.nth_bits(cache, index)
            most_common_bit = self.most_common_bit(bits)
            filtered = [entry for entry in cache if int(entry[index]) == most_common_bit]
            cache = filtered
            if len(cache) == 1:
                break
        return int(cache[0], 2)

    @property
    def co2_scrubber_rating(self):
        cache = self.binary_report.copy()
        for index in range(len(self.binary_report[0])):
            bits = self.nth_bits(cache, index)
            most_common_bit = self.most_common_bit(bits)
            filtered = [entry for entry in cache if int(entry[index]) != most_common_bit]
            cache = filtered
            if len(cache) == 1:
                break
        return int(cache[0], 2)

    @property
    def life_support_rating(self):
        return self.oxygen_generator_rating * self.co2_scrubber_rating



def get_input(path):
    with open(path, "r") as input_file:
        data = input_file.readlines()
    return [entry.strip("\n") for entry in data]


def main():
    diagnostic = BinaryDiagnostic(get_input("input.txt"))
    print(f"Power Consumption:{diagnostic.power_consumption}")
    print(f"Life Support:{diagnostic.life_support_rating}")


if __name__ == "__main__":
    main()
