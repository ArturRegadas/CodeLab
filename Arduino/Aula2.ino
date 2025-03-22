//classificacao de modo de porta, e definicao de estado da porta

void setup() {
  pinMode(13, OUTPUT);//definindo porta como saida e nao entrada


}

void loop() {
  digitalWrite(13, HIGH);//definindo estado da porta
  delay(1000); //pausa em ms
  digitalWrite(13, LOW);//definindo estado da porta
  delay(1000);

}
