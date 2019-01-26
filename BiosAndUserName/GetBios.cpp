 LPSTR GetSystemBiosVersion() {
HKEY hKey; LONG Res1, Res2; DWORD cData=255; TCHAR SystemBiosVersion[255]={'\0'}; Res1=RegOpenKeyEx(HKEY_LOCAL_MACHINE,"HARDWARE\\DESCRIPTION\\System",NULL, KEY_QUERY_VALUE, &hKey);
if(Res1==ERROR_SUCCESS)
{
Res2=RegQueryValueEx(hKey,"SystemBiosVersion",NULL,NULL,...
(LPBYTE)SystemBiosVersion,&cData);
if(Res2==ERROR_SUCCESS)
{
for (const char* p = SystemBiosVersion; *p; p += strlen(p)+1)
{
printf("%s\n", p); }
return SystemBiosVersion; } else
{
MessageBox(NULL,"RegQueryValueEx: SystemBiosVesion","ERROR",MB_OK); return NULL; } } else
{
MessageBox(NULL,"RegOpenKeyEx: SystemBiosVersion","ERROR",MB_OK); return NULL; } RegCloseKey(hKey); } 
