#include <Servo.h>
#include <LiquidCrystal.h>

const int buttonPin = 2;
const int servoPin = 3;
Servo servo;
LiquidCrystal lcd(9, 8, 7, 6, 5, 4);


//Variaveis para loop independente
float ultimoTempo = 0;
const int intervalo = 5000;

// Configurações que virão da plataforma em Python
// Elas guiaram o paciente e posterior o RTC e buzzer
int proximoHorario = 17;
int intervaloMedicacao = 8;
int medicamentosDisponiveis = 3;

//
int usoNormal = 0;
int tentativasDeUso = 0;

void setup() {
  
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  servo.attach(servoPin);
  servo.write(0); 
  lcd.begin(16, 2);

  // Inicia o lcd com a mensagem da próximo medicação 
  lcd.clear();
  lcd.print("Proxima dose");
  lcd.setCursor(0, 1);
  lcd.print("as ");
  lcd.print(proximoHorario);
  lcd.print(":00");
}

void loop() {
  
  
  // Loop independente para mostrar os uso e bloqueios do sistema
  if (millis() - ultimoTempo >= intervalo) {
    ultimoTempo = millis();
    
	Serial.print("Uso normal: ");
  	Serial.println(usoNormal);
  
  	Serial.print("Uso bloqueado: ");
  	Serial.println(tentativasDeUso);
  }
  
  // Variavel rastreia o estado do servo do motor(a tampa do slot)
  // O estado static evita o que incongruencia software/hardware ocorram entre loops
  static bool isOpen = false;
  
  // Verificação do clique do botão dupla com debounce evitando os possíveis ruídos elétricos, erros e falsas leituras
  // Como as boas práticas indicam
  if (digitalRead(buttonPin) == HIGH) {
    delay(75); 
    if (digitalRead(buttonPin) == HIGH) {
      
      // Verificação se o sistema está aberto ou fechado
      if (isOpen) {
        // Caso do sistema aberto
        
        // Fechar a tampa do slot
        servo.write(0); 
        isOpen = false;

        // Verificação se há medicamentos disponíveis para o próximo horário
        if (medicamentosDisponiveis > 0) {
          
          // Atualiza o horário para a próxima medicação
          proximoHorario = (proximoHorario + intervaloMedicacao) % 24;

          // Atualiza mensagem no LCD
          lcd.clear();
          lcd.print("Proxima dose");
          lcd.setCursor(0, 1);
          lcd.print("as ");
          lcd.print(proximoHorario);
          lcd.print(":00");
          
        } else {
          
          // Exibe mensagem no LCD se não houver medicamentos disponíveis
          lcd.clear();
          lcd.print("Sem comprimidos!");
          lcd.setCursor(0, 1);
          lcd.print("Consulte medico2.");
          
          
        }
      } else {
        // Caso do sistema fechado
        
        // Verificação se há medicamentos disponíveis
        if (medicamentosDisponiveis > 0) {
          
          // Abertura da tampa, atualização dos medicamentos, e estado da tampa
          servo.write(90);
          isOpen = true;
          medicamentosDisponiveis--;

          // Exibição mensagem no LCD de disponibilidade de compridos
          lcd.clear();
          lcd.print("Remedio tomado!");
          lcd.setCursor(0, 1);
          lcd.print("Disponiveis: ");
          lcd.print(medicamentosDisponiveis);
          usoNormal++;
          
        } else {
          
          // Exibição mensagem no LCD de falta de remédios
          lcd.clear();
          lcd.print("Sem comprimidos!");
          lcd.setCursor(0, 1);
          lcd.print("Consulte medico.");
          tentativasDeUso++;
        }
      }
      delay(75); // Debounce
    }
  }
}
