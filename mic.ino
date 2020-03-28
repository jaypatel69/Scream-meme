const int microphonePin= 0;
const int ledPin=13;

int sample;

const int threshold= 500;

void setup() {
pinMode (ledPin, OUTPUT);
Serial.begin(9600);
}

void loop(){
sample= analogRead(microphonePin);
Serial.println("FALSE");
if(sample > threshold)
{
digitalWrite (ledPin, HIGH);
Serial.println("TRUE");
}
else{ 
digitalWrite(ledPin, LOW); 
}

}
