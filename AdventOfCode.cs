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

        /************************
         * 
         * 
         *      DAY 2
         *      
         * 
         * **********************/

        public void Day2A()
        {
            string[] input = ReadProblemInput("Problem2AInput");

            int forward = 0;
            int down = 0;

            string[] tempStrings = new string[2];

            for (int i = 0; i < input.Length; i++)
            {
                tempStrings = input[i].Split(' ');

                if (tempStrings[0].CompareTo("forward") == 0)
                    forward += int.Parse(tempStrings[1]);
                else if (tempStrings[0].CompareTo("down") == 0)
                    down += int.Parse(tempStrings[1]);
                else if (tempStrings[0].CompareTo("up") == 0)
                    down -= int.Parse(tempStrings[1]);
            }

            Debug.WriteLine(forward * down);
            
        }//Day2A

        public void Day2B()
        {
            string[] input = ReadProblemInput("Problem2AInput");

            int forward = 0;
            int down = 0;
            int aim = 0;
            string[] tempStrings = new string[2];

            for (int i = 0; i < input.Length; i++)
            {
                tempStrings = input[i].Split(' ');

                if (tempStrings[0].CompareTo("forward") == 0)
                {
                    forward += int.Parse(tempStrings[1]);
                    down += (int.Parse(tempStrings[1]) * aim);
                }
                else if (tempStrings[0].CompareTo("down") == 0)
                    aim += int.Parse(tempStrings[1]);
                else if (tempStrings[0].CompareTo("up") == 0)
                    aim -= int.Parse(tempStrings[1]);
            }

            Debug.WriteLine(forward * down);
        }//Day2B

        /************************
         * 
         * 
         *      DAY 2
         *      
         * 
         * **********************/

        /************************
         * 
         * 
         *      DAY 3
         *      
         * 
         * **********************/

        public void Day3A()
        {
            string[] input = ReadProblemInput("Problem3AInput");

            int bitLength = input[0].Length;
            int[] counts = new int[bitLength];
            char[] bits = new char[bitLength];

            string bitString = "";
            for (int i = 0; i < input.Length; i++)
            {
                bits = input[i].ToCharArray();

                for (int j = 0; j < bitLength; j++)
                {
                    counts[j] += int.Parse(bits[j].ToString());
                }
            }

            for (int i = 0; i < counts.Length; i++)
            {
                if (counts[i] > (input.Length / 2))
                    bits[i] = '1';
                else
                    bits[i] = '0';
            }

            bitString = new string(bits);


            Debug.WriteLine(Convert.ToInt32(bitString, 2) * (Convert.ToInt32(bitString, 2) ^ 0b111111111111));
        }//Day3A

        public void Day3B()
        {
            List<string> oneList = new List<string>();
            List<string> zeroList = new List<string>();
            List<string> tempList = new List<string>();
            List<List<string>> o2Master = new List<List<string>>();
            List<List<string>> co2Master = new List<List<string>>();

            string[] input = ReadProblemInput("Problem3AInput");
            tempList = input.ToList<string>();

            int bitLength = input[0].Length;

            string bitString = "";

            for (int i = 0; i < bitLength; i++)
            {
                foreach (string str in tempList)
                {
                    if (str[0].CompareTo('1') >= 0)
                        oneList.Add(str);
                    else
                        zeroList.Add(str);
                }

                
                if (oneList.Count > zeroList.Count)
                {
                    foreach (string str in oneList)
                        tempList.Remove(str);
                }
                else
                {
                    foreach (string str in zeroList)
                        tempList.Remove(str);
                }

            }

            foreach (string str in tempList)
                Debug.WriteLine(str);
        }

        /************************
         * 
         * 
         *      DAY 3
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
