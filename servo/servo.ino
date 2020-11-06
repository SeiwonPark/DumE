#include<Servo.h>

Servo servoVer; //Vertical Servo
Servo servoHor; //Horizontal Servo

int x;
int y;

int prevX;
int prevY;

void setup()
{
  Serial.begin(9600);
  servoVer.attach(5); 
  servoHor.attach(6); 
  servoVer.write(20);
  servoHor.write(90);
}

void Pos()
{
  if(prevX != x || prevY != y)
  {
    //tune this range to generate map
    int servoX = map(x, 640, 0, 20, 160);
    //tune this range to generate map
    int servoY = map(y, 480, 0, 120, 10); 

    servoX = min(servoX, 160);
    servoX = max(servoX, 20);
    servoY = min(servoY, 120);
    servoY = max(servoY, 10);
    
    servoHor.write(servoX);
    servoVer.write(servoY);
  }
}

void loop()
{
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'X')
    {
      x = Serial.parseInt();
      if(Serial.read() == 'Y')
      {
        y = Serial.parseInt();
       Pos();
      }
    }
    while(Serial.available() > 0)
    {
      Serial.read();
    }
  }
}
