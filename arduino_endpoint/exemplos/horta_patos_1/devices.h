#include "dht.h"

#ifndef devices_h
#define devices_h
#endif

#define DHT11_PIN 2
#define LDR_PIN A0
#define RLED_PIN 7

class devices
{    
 public:
    // Pseudo-construtor
    void start_devices();
    // Funções de leitura de sensores
    void measure_sensors();
    void read_air();
    void read_ldr();

    // Funções de atuadores
    void write_rled(uint8_t);

    // Funções GET
    uint8_t get_air_humi();
    uint8_t get_air_temp();
    uint16_t get_luminosity();
    uint8_t get_rled_level();

 private:
    uint8_t air_humi;
    uint8_t air_temp;
    uint16_t luminosity;
    uint8_t rled_level;
    dht DHT;
};
