#include <Servo.h>

Servo middle, left, right, claw ; // creates 4 servo
int a=0;
// for down-forward 2-180 3-120 max
// for up-forward 2-140 3-180 max

void setup(){
  Serial.begin(9600);
  middle.attach(5); //360
  
  left.attach(4);//60-150
  
  right.attach(3);//90-150
  claw.attach(2);//90-105



  }
void loop() {
  int  offset;
  Serial.println(middle.read());
  String a=Serial.readString();
    
  offset = a.toInt();
  Serial.println(offset);
  if(offset>0)
  {middle.write(offset);
  delay(1000);}
  
  
  
 // Serial.println(right.read());
 // Serial.println(left.read());
 // Serial.println(claw.read());
 // int inputMessage = Serial.parseInt();
 // Serial.println(inputMessage);
  
 // if(inputMessage == 1){
 //   Serial.println('1');
 //   inputMessage = Serial.parseInt();
    
 //   while (inputMessage==0){
 //     inputMessage = Serial.parseInt();
 //   }
    
 //   middle.write(inputMessage); 
 //   Serial.println(inputMessage);
 //  }
    
 //  else if(inputMessage == 2){
 //   Serial.println('2');
 //   inputMessage = Serial.parseInt();
 //   while (inputMessage==0){
 //     inputMessage = Serial.parseInt();
 //   }
 //   right.write(inputMessage); 
 //   Serial.println(inputMessage);
 //  }
    
 //  else  if(inputMessage == 3){
 //   Serial.println('3');
 //   inputMessage = Serial.parseInt();
 //   while (inputMessage==0){
 //     inputMessage = Serial.parseInt();
 //   }    
 //   left.write(inputMessage); 
 //   Serial.println(inputMessage);
 //  }
    
 //  else  if(inputMessage == 4){
 //   Serial.println('4');
 //   inputMessage = Serial.parseInt();
 //   while (inputMessage==0){
 //     inputMessage = Serial.parseInt();
 //   }    
 //   claw.write(inputMessage); 
 //   Serial.println(inputMessage);
 //  }

  

}
