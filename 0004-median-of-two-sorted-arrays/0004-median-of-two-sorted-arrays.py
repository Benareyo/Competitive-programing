class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        
        while imin <= imax:
            partitionX = (imin + imax) // 2
            partitionY = half_len - partitionX
            
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == n else nums2[partitionY]
            
            if maxX <= minY and maxY <= minX:
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2.0
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                imax = partitionX - 1
            else:
                imin = partitionX + 1

        raise ValueError("Input arrays are not sorted properly.")

# Example usage:
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
