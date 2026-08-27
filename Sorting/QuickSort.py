class Solution:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quickSortHelper(self, arr, low, high):
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSortHelper(arr, low, pIndex - 1)
            self.quickSortHelper(arr, pIndex + 1, high)

    def quickSort(self, nums):
        n = len(nums)
        self.quickSortHelper(nums, 0, n - 1)
        return nums