//Uso de funcoes e Uso do define
//criacao de um semaforo
#define p1 7
#define p2 5
#define p3 3


int portas[3]={p1, p2, p3};
void semaforo(int time, int portasd[3], int porta){
  for(int i=0; i<3; i++){
    if (portasd[i]==porta){
      digitalWrite(portasd[i], HIGH);
    }
    else{
      digitalWrite(portasd[i], LOW);
    }
    
  }
  delay(time);
};
void setup() {
  pinMode(portas[0], OUTPUT);
  pinMode(portas[1], OUTPUT);
  pinMode(portas[2], OUTPUT);
  
}

void loop() {
  semaforo(7000, portas, portas[0]);
  semaforo(3000,portas, portas[1]);
  semaforo(9000,portas, portas[2]);
  
}
