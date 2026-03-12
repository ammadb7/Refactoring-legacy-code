class ComputeStatistics:
    @staticmethod
    def compute_stats(file_path):
        total = 0
        total_sum = 0
        min_val = 0
        max_val = 0

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                if not lines:
                    return

                # Read the first line to initialize min and max
                first_line = int(lines[0].strip())
                min_val = first_line
                max_val = first_line

                # Process all lines
                for line in lines:
                    clean_line = line.strip()
                    if clean_line:
                        num = int(clean_line)
                        total += 1
                        total_sum += num

                        if min_val > num:
                            min_val = num
                        if max_val < num:
                            max_val = num

            # Print the final statistics
            print("total = " + str(total))
            print("summation = " + str(total_sum))
            print("average = " + str(round(total_sum / total)))
            print("Minimum = " + str(min_val))
            print("Maximum = " + str(max_val))

        except IOError as e:
            print(f"Error reading file: {e}")


if __name__ == "__main__":
    ComputeStatistics.compute_stats("random_nums.txt")