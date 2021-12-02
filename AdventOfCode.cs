using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class AdventOfCode
    {
        public AdventOfCode()
        {

        }

        /************************
         * 
         * 
         *      DAY 1
         *      
         * 
         * **********************/
        public void Day1A()
        {
            string[] input = ReadProblemInput("Problem1AInput");

            int tempNum = 0;
            int count = 0;

            tempNum = Int32.Parse(input[0]);

            for (int i = 1; i < input.Length; i++)
            {
                if (tempNum < Int32.Parse(input[i]))
                {
                    count++;
                }

                tempNum = Int32.Parse(input[i]);
            }

            Debug.Write(count);
        }//Day1A

        public void Day1B()
        {
            string[] input = ReadProblemInput("Problem1AInput");

            int tempNum = 0;
            int tempNum2 = 0;
            int count = 0;

            for (int i = 0; i < 3; i++)
                tempNum += Int32.Parse(input[i]);

            for (int i = 1; i < input.Length - 2; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    tempNum2 += Int32.Parse(input[i + j]);
                }

                if (tempNum < tempNum2)
                {
                    count++;
                }

                tempNum = tempNum2;
                tempNum2 = 0;
            }

            Debug.WriteLine(count);
        } //Day1B
        /************************
         * 
         * 
         *      DAY 1
         *      
         * 
         * **********************/

        private string[] ReadProblemInput(string txtFileName)
        {
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\movil\source\repos\LeetCode\LeetCode\AOCInput\" + txtFileName + ".txt");

            if (lines != null)
                return lines;

            Console.WriteLine("didn't read file");

            return null;
        }
    }
}
