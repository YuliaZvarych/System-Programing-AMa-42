using System;
using System.Collections.Generic;
using System.Text;

namespace SystemProgramming
{
    class JumpSearch
    {
        public static int jump_Search(int[] arr, int Element)
        {
            int numberofElements = arr.Length;
            int step = (int)Math.Sqrt(numberofElements);
            while (true)
            {
                int i = 0;
                while (i < numberofElements)
                {
                    
                    if (arr[i] == Element)
                        return i;
                    if (arr[i] > Element)
                    {
                        numberofElements = i;
                        i = i - step;
                        step = (int)Math.Sqrt(step);
                        
                        /*for(int j = i-step;j < i;j++)
                        {
                            if (arr[j] == Element)
                            {
                                return j;
                            }
                        }*/
                    }
                    i = i + step;
                    if (i + step > numberofElements)
                        i = numberofElements - 1;
                }
            }
        }
    }
}
