#include "defines.h"
#include "devices.h"

void devices::start_devices()
{
#if DEBUG
    Serial.println("Inicializando dispositivos.");
#endif
    measure_sensors();
    pinMode(RLED_PIN, OUTPUT);
    write_rled(0);
    delay_ms = STARTING_DELAY;
}

void devices::measurement_loop()
{
    measure_sensors();
    write_rled(!rled_level);
    delay(delay_ms);
}

void devices::measure_sensors()
{
    read_air();
    read_ldr();
#if !DEBUG
    send_json();
#endif
}

void devices::send_json()
{
    String payload;
    payload += "{\"endpoint_id\": ";
    payload += ENDPOINT_ID;
    payload += ", \"name_reference\": false, \"samples\": {";
    // Luminosidade
    payload += "\"";
    payload += LUMI_ID;
    payload += "\": ";
    payload += luminosity;
    payload += ", ";
    // Umidade e Temperatura
    if (dht_status == DHTLIB_OK){
        payload += "\"";
        payload += UMID_ID;
        payload += "\": ";
        payload += air_humi;
        payload += ", ";
        payload += "\"";
        payload += TEMP_ID;
        payload += "\": ";
        payload += air_temp;
        payload += ", ";
    }
    // RLed
    payload += "\"";
    payload += RLED_ID;
    payload += "\": ";
    if(rled_level)
        payload += "true";
    else
        payload += "false";
    payload += "}}";
    // Finalização e envio
    Serial.println(payload);

}

void devices::read_air()
{
    dht_status = DHT.read11(DHT11_PIN);
    air_humi = DHT.humidity;
    air_temp = DHT.temperature;

#if DEBUG
    if (dht_status != DHTLIB_OK){
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

void devices::write_delay_ms(uint32_t value)
{
    delay_ms = value;
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

uint32_t devices::get_delay_ms()
{
    return delay_ms;
}
