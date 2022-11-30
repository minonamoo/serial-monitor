void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("HELLO WORLD");
}

int cnt = 0;

void loop() {
  // put your main code here, to run repeatedly
  delay(500);
  Serial.print("CNT: ");
  Serial.println(cnt);
  cnt++;
}
