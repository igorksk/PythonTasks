from random import seed, randint

seed()

count1, count2 = 5, 10;

nums1, nums2 = set(), set()

while len(nums1) < count1:
    nums1.add(randint(1, 10))

while len(nums2) < count2:
    nums2.add(randint(11, 30))

nums3 = nums1 | nums2;

print(nums3)

