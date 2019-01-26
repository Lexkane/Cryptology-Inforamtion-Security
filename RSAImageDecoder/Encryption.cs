public string encrypt(string imageToEncrypt)
{
   string hex = imageToEncrypt;
   char[] ar = hex.ToCharArray();
   String c = "";
   progressBar1.Maximum = ar.Length;
   for (int i = 0; i < ar.Length; i++)
   {
      Application.DoEvents();
      progressBar1.Value = i;
      if (c == "")
         c = c + ImageCrypto.RSAalgorithm.BigMod(ar[i], RSA_E, n);
      else
         c = c + "-" + ImageCrypto.RSAalgorithm.BigMod(ar[i], RSA_E, n);
    }
    return c;
} 