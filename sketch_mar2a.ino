#include <dummy.h>

#include <WiFi.h>

const char* SSID = "ESP32-CAM Access Point";
const char* PASSWORD = "123";

void init_wifi(){
  WiFi.softAP(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
}

void setup() {
  // wait till a device is connected
  init_wifi();

  // set up the
}

void loop() {
  // put your main code here, to run repeatedly:

}
