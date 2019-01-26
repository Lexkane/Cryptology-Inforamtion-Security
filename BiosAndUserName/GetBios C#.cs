string userName = System.Security.Principal.WindowsIdentity.GetCurrent().Name;


System.Management.SelectQuery query = new System.Management.SelectQuery(@"Select * from Win32_ComputerSystem");

 //initialize the searcher with the query it is supposed to execute
 using (System.Management.ManagementObjectSearcher searcher = new System.Management.ManagementObjectSearcher(query))
 {
     //execute the query
     foreach (System.Management.ManagementObject process in searcher.Get())
     {
         //print system info
         process.Get();
         Console.WriteLine("/*********Operating System Information ***************/");
         Console.WriteLine("{0}{1}", "System Manufacturer:", process["Manufacturer"]);
         Console.WriteLine("{0}{1}", " System Model:", process["Model"]);


     }
 }

 System.Management.ManagementObjectSearcher searcher1 = new System.Management.ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
 System.Management.ManagementObjectCollection collection = searcher1.Get();


foreach (ManagementObject obj in collection)
{
    if ( ((string[])obj["BIOSVersion"]).Length > 1)
        Console.WriteLine("BIOS VERSION: " + ((string[])obj["BIOSVersion"])[0] + " - " + ((string[])obj["BIOSVersion"])[1]);
    else
        Console.WriteLine("BIOS VERSION: " + ((string[])obj["BIOSVersion"])[0]);
}

//----------------------------------------------------------------------------------------------------------------------------//
using System.Management

 using (ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS"))

              
            using (System.Management.ManagementObjectCollection moc = mos.Get())

            {

                StringBuilder sb = new StringBuilder();

                foreach (ManagementObject mo in moc)

                {

                    string[] BIOSVersions = (string[])mo["BIOSVersion"];

                    foreach (string version in BIOSVersions)

                    {

                        sb.AppendLine(string.Format("BIOSVersion: {0}", version));

                    }

                    sb.AppendLine(string.Format("BuildNumber: {0}", (string)mo["BuildNumber"]));

                    sb.AppendLine(string.Format("Caption: {0}", (string)mo["Caption"]));

                    sb.AppendLine(string.Format("CodeSet: {0}", (string)mo["CodeSet"]));

                    sb.AppendLine(string.Format("CurrentLanguage: {0}", (string)mo["CurrentLanguage"]));

                    sb.AppendLine(string.Format("Description: {0}", (string)mo["Description"]));

                    sb.AppendLine(string.Format("IdentificationCode: {0}", (string)mo["IdentificationCode"]));

                    sb.AppendLine(string.Format("InstallableLanguages: {0}", Convert.ToUInt16(mo["InstallableLanguages"]).ToString()));

                    sb.AppendLine(string.Format("InstallDate: {0}", Convert.ToDateTime(mo["InstallDate"]).ToString()));

                    sb.AppendLine(string.Format("LanguageEdition: {0}", (string)mo["LanguageEdition"]));

                    sb.AppendLine(string.Format("Manufacturer : {0}", (string)mo["Manufacturer"]));

                }