#include "stdafx.h"
#include <winsock2.h>
#include <WS2tcpip.h>
#include <iphlpapi.h>
#pragma comment(lib, "IPHLPAPI.lib")

int main()
{
	// Password 5
	ULONG outBufLen = 15000;
	PIP_ADAPTER_ADDRESSES pAddresses = (PIP_ADAPTER_ADDRESSES)malloc(outBufLen);
	GetAdaptersAddresses(2, NULL, NULL, pAddresses, &outBufLen);
	for(int i = 3; i >=0; i--)
		printf("%02X", pAddresses->PhysicalAddress[i]);
}
