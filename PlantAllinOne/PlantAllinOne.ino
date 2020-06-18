#include "DHT.h"
#include "ph_grav.h"                           

Gravity_pH pH = Gravity_pH(A1);                        

#define DHTPIN 2

#define DHTTYPE DHT11

#define SensorPin 0          //light meter Analog output to Arduino Analog Input 0
unsigned long int avgValue;  //Store the average value of the sensor feedback
float b;
int buf[10],temp;


DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);

  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  for(int i=0;i<10;i++)       //Get 10 sample value from the sensor for smooth the value
    { 
      buf[i]=analogRead(SensorPin);
      delay(10);
    }
    for(int i=0;i<9;i++)        //sort the analog from small to large
    {
      for(int j=i+1;j<10;j++)
      {
        if(buf[i]>buf[j])
        {
          temp=buf[i];
          buf[i]=buf[j];
          buf[j]=temp;
        }
      }
    }
    avgValue=0;
    for(int i=2;i<8;i++)                      //take the average value of 6 center sample
      avgValue+=buf[i];
  int lightVal=avgValue;                     //convert the millivolt into pH value

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

//  Serial.print(F("Lux:"));  
  Serial.print(lightVal);
  Serial.print(" ");
//  Serial.print(F("  Humidity: "));
  Serial.print(h);
//  Serial.print(F("%  Temperature: "));
  Serial.print(" ");
  Serial.print(f);
  Serial.print(" ");
  Serial.println(pH.read_ph());
  digitalWrite(13, HIGH);       
  delay(800);
  digitalWrite(13, LOW);
}
