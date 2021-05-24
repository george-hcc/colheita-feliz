#include "devices.h"
#include "defines.h"
devices DVC;

void setup()
{
  Serial.begin(9600);
  DVC.start_devices();
}

void loop()
{
  DVC.measurement_loop();
}
  
