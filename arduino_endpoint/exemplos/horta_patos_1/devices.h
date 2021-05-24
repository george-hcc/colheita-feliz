#include "dht.h"

#ifndef devices_h
#define devices_h
#endif

#define DHT11_PIN 8
#define LDR_PIN A0
#define RLED_PIN 9

#define ENDPOINT_ID 5
#define LUMI_ID 6
#define UMID_ID 7
#define TEMP_ID 8
#define RLED_ID 9
#define DELAY_ID 10

class devices
{
 public:
    // Pseudo-construtor
    void start_devices();
    // Funções de leitura de sensores
    void measurement_loop();
    void measure_sensors();
    void send_json();
    void read_air();
    void read_ldr();

    // Funções de atuadores
    void write_rled(uint8_t);
    void write_delay_ms(uint32_t);

    // Funções GET
    uint8_t get_air_humi();
    uint8_t get_air_temp();
    uint16_t get_luminosity();
    uint8_t get_rled_level();
    uint32_t get_delay_ms();

 private:
    uint8_t dht_status;
    uint8_t air_humi;
    uint8_t air_temp;
    uint16_t luminosity;
    uint8_t rled_level;
    uint32_t delay_ms;

    dht DHT;
};
