class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 1
        for elements in range(len(nums1)):
            if i <= n:
                nums1.pop(m)
            i = i+1
        print(nums1)
        for x in nums2:
            nums1.append(x)
        nums1.sort()
        print(nums1)