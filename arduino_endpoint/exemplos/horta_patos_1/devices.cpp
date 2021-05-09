#include "devices.h"
#define TRUE 1
#define FALSE 0

#define DEBUG TRUE

void devices::start_devices()
{
#if DEBUG
    Serial.println("Inicializando dispositivos.");
#endif
    measure_sensors();
    pinMode(RLED_PIN, OUTPUT);
    write_rled(0);
}

void devices::measure_sensors()
{
    read_air();
    read_ldr();
}

void devices::read_air()
{
    int dht_check = DHT.read11(DHT11_PIN);
    air_humi = DHT.humidity;
    air_temp = DHT.temperature;

#if DEBUG
    if (dht_check != DHTLIB_OK){
        Serial.println("Failed to read from DHT");
    }
    else{
        Serial.print("Umidade: ");
        Serial.print(air_humi);
        Serial.print(" \t");
        Serial.print("Temperatura: ");
        Serial.print(air_temp);
        Serial.println(" *C");
    }
#endif

}

void devices::read_ldr()
{
    luminosity = analogRead(LDR_PIN);
#if DEBUG
    Serial.print("Luminosidade: ");
    Serial.println(luminosity);
#endif
}

void devices::write_rled(uint8_t value)
{
    if(value)
        rled_level = HIGH;
    else
        rled_level = LOW;
    digitalWrite(RLED_PIN, rled_level);
#if DEBUG
    Serial.print("RLed Atualizado: ");
    Serial.println(rled_level);
#endif

}

uint8_t devices::get_air_humi()
{
    return air_humi;
}

uint8_t devices::get_air_temp()
{
    return air_temp;
}

uint16_t devices::get_luminosity()
{
    return luminosity;
}

uint8_t devices::get_rled_level()
{
    return rled_level;
}
