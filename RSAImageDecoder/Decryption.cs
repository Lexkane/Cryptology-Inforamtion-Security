public string decrypt(String imageToDecrypt)
{
    char[] ar = imageToDecrypt.ToCharArray();
    int i = 0, j = 0;
    string c = "", dc = "";
    progressBar2.Maximum = ar.Length;
    try
    {
       for (; i < ar.Length; i++)
       {
          Application.DoEvents();
          c = "";
          progressBar2.Value = i;
          for (j = i; ar[j] != '-'; j++)
                 c = c + ar[j];
          i = j;
          int xx = Convert.ToInt16(c);
          dc = dc + ((char)ImageCrypto.RSAalgorithm.BigMod(xx, d, n)).ToString();
       }
    }
    catch (Exception ex) { }
    return dc;
} 