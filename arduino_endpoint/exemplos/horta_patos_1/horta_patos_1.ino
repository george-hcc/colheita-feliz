#include "dht.h"

#define TRUE 1
#define FALSE 0

#define DEBUG TRUE

#define DHT11_PIN 2
dht DHT;

const uint32_t loop_delay = 1000;
uint8_t air_humi;
uint8_t air_temp;

void read_air()
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

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  #if DEBUG
    Serial.println("DHT11 test!");;
  #endif
}

void loop()
{
  read_air();
  digitalWrite(13, HIGH);
  delay(loop_delay);
  digitalWrite(13, LOW);
  delay(loop_delay);
}
  
