using System;
using System.Collections.Generic;
using System.Text;

namespace SystemProgramming
{
    class Friend_Pairs
    {
        public static int friends_Pairs(int number)
        {
            if (number == 0 || number == 1)
                return 1;
            else
            return friends_Pairs(number - 1) + (number - 1) * friends_Pairs(number - 2);
        }
    }
}
