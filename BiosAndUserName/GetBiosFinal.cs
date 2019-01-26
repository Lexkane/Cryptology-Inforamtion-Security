using System;
using System.Text;
using System.Management;
using System.IO;

namespace Program
{
    class Program
    {
        static void Main(string[] args)
        {
            string user = "\u0031\u0031\u0031\u002d\u041f\u041a\u005c\u0031\u0031\u0031";
            string userName = System.Security.Principal.WindowsIdentity.GetCurrent().Name;

            using (ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS"))

              
            using (System.Management.ManagementObjectCollection moc = mos.Get())

            {

                StringBuilder sb = new StringBuilder();

                foreach (ManagementObject mo in moc)

                {

                    string[] BIOSVersions = (string[])mo["BIOSVersion"];

                    foreach (string version in BIOSVersions)

                    {

                        sb.Append(string.Format(version));

                    }

                }

                string data = "ACRSYS - 6040000Ver 1.00PARTTBL";
                string biosdata = sb.ToString();

                if (user.Equals(userName) && data.Equals(biosdata))
                {
                    Console.WriteLine("Program is running !!!");
                }
                 else
                {
                    Console.WriteLine("Your Bios and username doesn't support this program");
                }

                Console.ReadLine();
                                
            }

        }
    }
}
