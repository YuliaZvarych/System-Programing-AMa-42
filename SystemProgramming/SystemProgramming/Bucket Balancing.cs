using System;
using System.Collections.Generic;
using System.Numerics;
using System.Text;

namespace SystemProgramming
{
    class Bucket_Balancing
    {
        public static void Swap(ref int a,ref int b)
        {
            int c = a;
            a = b;
            b = c;
        }
        public static int SwapCount(string s)
        {
            List<int> pos = new List<int>();
            for (int i = 0; i < s.Length; ++i)
                if (s[i] == '[')
                    pos.Add(i);

            int count = 0; 
            int p = 0;  
            int sum = 0; 

            for (int i = 0; i < s.Length; ++i)
            {
                if (s[i] == '[')
                {
                    ++count;
                    ++p;
                }
                else if (s[i] == ']')
                    --count;

                if (count < 0)
                {
                    sum += pos[p] - i;
                    char[] array = s.ToCharArray();
                    char temp = array[i];
                    array[i] = array[pos[p]];
                    array[pos[p]] = temp;
                    s = new string(array);
                    ++p;

                    count = 1;
                }
            }
            return sum;
        }
    }
}
