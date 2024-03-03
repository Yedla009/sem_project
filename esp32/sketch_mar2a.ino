#include <WiFi.h>

const char* SSID = "ESP32-CAM Access Point";

void init_wifi(){
  Serial.print("WiFi turned on with SSID: ");
  Serial.println(SSID);

  WiFi.softAP(SSID);

  Serial.println("Waiting: for client");

  while (!(WiFi.softAPgetStationNum())){
    delay(500); 
    Serial.print(".");
  }
  
  Serial.println(".")
  Serial.println("Client Connected");
}

void setup() {
  // setting up ESP32 baud rate
  Serial.begin(115200);

  // wait till a device is connected
  init_wifi();
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
