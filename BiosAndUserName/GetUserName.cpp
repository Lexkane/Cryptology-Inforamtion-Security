char buffer[UNLEN+1];
DWORD size;
size=sizeof(buffer);
GetUserName(buffer,&size);