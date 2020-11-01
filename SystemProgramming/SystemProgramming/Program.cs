using System;
using System.Collections.Generic;

namespace SystemProgramming
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array = new int[] { 43, 17, 87, 92, 31, 6, 96, 13, 66, 62, 4 };
            List<int> sorted = Bucket_Sort.Bucket_sort(array);
            foreach (var item in sorted)
            {
                Console.WriteLine(item);
            }

            int[] arr = new int[] { 0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 77, 89, 101, 201, 256, 780 };
            Console.WriteLine("index of item 2 = " + JumpSearch.jump_Search(arr, 2));

            Console.WriteLine("friends pair of 4 = " + Friend_Pairs.friends_Pairs(4));

            Console.ReadLine();

        }
    }
}
