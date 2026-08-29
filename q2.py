class sort:
    def sort1(self, array):
        n = len(array)
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                if array[j] < array[min]:
                    min = j
            array[i], array[min] = array[min], array[i]
        return array


array = ["Q1", "Delta", "Alpha", "Omega", "Beta"]
print("original array:", array)
print("sorted array:", sort().sort1(array))