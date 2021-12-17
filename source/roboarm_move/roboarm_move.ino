#include <Servo.h>

Servo middle, left, right, claw ; // creates 4 "servo objects"
int a=0;

void setup(){
  Serial.begin(9600);
  middle.attach(2); // attaches the servo on pin 11 to the middle object
  left.attach(4);
  right.attach(3);
  claw.attach(5);
  }
void loop() {
  int inputMessage = Serial.parseInt();
  Serial.println(inputMessage);
  
  if(inputMessage == 1){
    Serial.println('1');
    inputMessage = Serial.parseInt();
    
    while (inputMessage==0){
      inputMessage = Serial.parseInt();
    }
    
    middle.write(inputMessage); 
    Serial.println(inputMessage);
   }
    
   else if(inputMessage == 2){
    Serial.println('2');
    inputMessage = Serial.parseInt();
    while (inputMessage==0){
      inputMessage = Serial.parseInt();
    }
    right.write(inputMessage); 
    Serial.println(inputMessage);
   }
    
   else  if(inputMessage == 3){
    Serial.println('3');
    inputMessage = Serial.parseInt();
    while (inputMessage==0){
      inputMessage = Serial.parseInt();
    }    
    left.write(inputMessage); 
    Serial.println(inputMessage);
   }
    
   else  if(inputMessage == 4){
    Serial.println('4');
    inputMessage = Serial.parseInt();
    while (inputMessage==0){
      inputMessage = Serial.parseInt();
    }    
    claw.write(inputMessage); 
    Serial.println(inputMessage);
   }

  

}
