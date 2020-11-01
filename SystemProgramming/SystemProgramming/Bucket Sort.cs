using System;
using System.Collections.Generic;
using System.Text;

namespace SystemProgramming
{
    class Bucket_Sort
    {
        public static List<int> Bucket_sort(int[] arr)
        {
            int n = 10;
            List<int> sorted = new List<int>();
            List<int>[] listofBuckets = new List<int>[n];
            for (int i = 0; i < n; i++)
            {
                listofBuckets[i] = new List<int>();
            }
            for (int i = 0; i < arr.Length; i++)
            {
                int bucketsIndex = arr[i] / n;
                listofBuckets[bucketsIndex].Add(arr[i]);
            }
            for (int i = 0; i < n; i++)
            {
                listofBuckets[i].Sort();
                sorted.AddRange(listofBuckets[i]);
            }
            return sorted;
        }
    }
}
