#include <stdio.h>
//ifdef başındaki # ön işlemci kontrolünü sağlar
#ifdef _WIN32 // İşletim sistemi kontolü
    #include <windows.h>  //_WIN32 = Windows
    #define EXPORT __declspec(dllexport) //Dışa aktarma for WIN
#else 
    #include <unistd.h>
    #define EXPORT // Dışa aktarma for diğer işletim sistemleri
#endif

EXPORT void bekle_3_saat() {
    int saniye = 10800; // 3 saat = 10800 saniye
    #ifdef _WIN32
        Sleep(saniye * 1000);
        
    #else
        sleep(saniye);
        
    #endif
}
