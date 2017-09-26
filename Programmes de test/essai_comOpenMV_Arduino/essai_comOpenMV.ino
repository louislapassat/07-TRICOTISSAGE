//Created August 15 2006
//Heather Dewey-Hagborg
//http://www.arduino.cc

#include <ctype.h> //inclusion du fichier pour avoir accès à la fonction toupper()

#define bit9600Delay 84  
#define halfBit9600Delay 42
#define bit4800Delay 188 
#define halfBit4800Delay 94 

byte rx = 19;  // set receiving pin
//byte tx = 18;  // set transmit pin
byte SWval;

void setup() {
  pinMode(rx,INPUT);
  //pinMode(tx,OUTPUT);
  //digitalWrite(tx,HIGH);
  //digitalWrite(13,HIGH); //turn on debugging LED
  SWprint('h');  //debugging hello ; SWprint prend des nombres ou des caractères individuels
  SWprint('i');
  SWprint(10); //carriage return
}

void SWprint(int data)
{
  /*byte mask;
  startbit
  digitalWrite(tx,LOW);
  delayMicroseconds(bit9600Delay);
  for (mask = 0x01; mask>0; mask <<= 1) {
    if (data & mask){ // choose bit
     digitalWrite(tx,HIGH); // send 1
    }
    else{
     digitalWrite(tx,LOW); // send 0
    }
    delayMicroseconds(bit9600Delay);
  }
  //stop bit
  digitalWrite(tx, HIGH);
  delayMicroseconds(bit9600Delay);*/
}

int SWread()
{
  byte val = 0;
  while (digitalRead(rx));
  //wait for start bit
  if (digitalRead(rx) == LOW) {
    delayMicroseconds(halfBit9600Delay); // attendre pour vérifier que l'on reçoit bien un bit et non pas du bruit
    for (int offset = 0; offset < 8; offset++) {
     delayMicroseconds(bit9600Delay);
     val |= digitalRead(rx) << offset;
    }
    //wait for stop bit + extra
    delayMicroseconds(bit9600Delay); 
    delayMicroseconds(bit9600Delay);
    return val;
  }
}

void loop()
{
    SWval = SWread(); 
    //SWprint(toupper(SWval));
    Serial.print(SWval);
}
