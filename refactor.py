class ComputeStatistics:
    def __init__(self, file_path):
        """Constructor to take the file path."""
        self.file = file_path

    def read_int(self):
        """Reads integer values from the file and creates a list."""
        data = []
        try:
            with open(self.file, 'r') as f:
                for line in f:
                    clean_line = line.strip()
                    if clean_line:
                        data.append(int(clean_line))
        except IOError as e:
            print(f"Error reading file: {e}")
        return data

    def count(self):
        """Calculates the count of integers in the list."""
        data = self.read_int()
        return len(data)

    def summation(self):
        """Calculates the sum of all integers."""
        data = self.read_int()
        return sum(data)

    def average(self):
        """Calculates the average of the data."""
        data = self.read_int()
        total_sum = self.summation()
        count_val = self.count()
        if count_val == 0:
            return 0.0
        return total_sum / count_val

    def minimum(self):
        """Finds the minimum value."""
        data = self.read_int()
        return min(data) if data else 0

    def maximum(self):
        """Finds the maximum value."""
        data = self.read_int()
        return max(data) if data else 0


if __name__ == "__main__":
    file_name = "random_nums.txt"
    cs = ComputeStatistics(file_name)

    print("The values are:", cs.read_int())
    print("Total values in file are:", cs.count())
    print("Summation of data is:", cs.summation())
    print("Average of data is:", cs.average())
    print("Minimum value from data is:", cs.minimum())
    print("Maximum value from data is:", cs.maximum())