function mergeArrays(nums1, m, nums2, n) {
  while (m > 0 || n > 0) {
    if (m === 0) {
      nums1[m + n - 1] = num2[n - 1];
      n--;
    } else if (n === 0) {
      nums1[m + n - 1] = nums1[m - 1];
      m--;
    } else if (nums2[n - 1] > nums1[m - 1]) {
      nums1[m + n - 1] = num2[n - 1];
      n--;
    } else {
      nums1[m + n - 1] = nums1[m - 1];
      m--;
    }
  }
  return nums1;
}
