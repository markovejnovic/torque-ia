volatile int count;

void isr() {
  count++;
}

void setup() {
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), isr, FALLING);
  Serial.begin(9600);
}

void loop() {
  Serial.println(count);
}
