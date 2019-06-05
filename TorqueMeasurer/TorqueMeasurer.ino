volatile int count;
int theta;

void isr() {
  count++;
}

void setup() {
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), isr, FALLING);
  Serial.begin(9600);
}

void printAllValues() {
  long t = millis();
  theta = analogRead(A0);

  Serial.print(t);
  Serial.print(",");
  Serial.print(count);
  Serial.print(",");
  Serial.println(theta);
}

void loop() {
  printAllValues();
}
