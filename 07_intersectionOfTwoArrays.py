def intersect(self, nums1, nums2):
    return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
