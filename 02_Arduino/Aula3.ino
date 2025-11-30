//criacao de variaveis
int porta=2;//[variavel global]qual porta foi usada

void setup() {
  pinMode(porta, OUTPUT);

}


void loop() {
  digitalWrite(porta, HIGH);
  delay(100);
  digitalWrite(porta, LOW);
  delay(100);
  

}
