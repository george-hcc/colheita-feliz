#include "devices.h"
devices DVC;

const uint32_t loop_delay = 2000;

void setup()
{
  Serial.begin(9600);
  DVC.start_devices();
}

void loop()
{
  DVC.measure_sensors();
  DVC.write_rled(!DVC.get_rled_level());
  delay(loop_delay);

  DVC.measure_sensors();
  DVC.write_rled(!DVC.get_rled_level());
  delay(loop_delay);
}
  
