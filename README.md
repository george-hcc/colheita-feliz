# Colheita Feliz

![colheita_feliz](https://user-images.githubusercontent.com/56853081/111224882-cb3cba80-85bd-11eb-9968-aff943de284c.png)

O intuíto deste projeto é criar um sistema de IoT com o objetivo de gerenciar hortas e jardins, sendo composto estruturalmente por:

- Endpoints com Arduinos acoplados com sensores (temperatura, humidade, luminosidade) e atuadores (lampadas, drenos, torneiras) com acesso a internet via ESP32/ESP8266;
- Servidor central com banco de dados responsável por receber as informações enviadas pelos Arduinos, armazena-las e executar lógica de controle para atuar de volta;
- Frontend web para clientes poderem acompanhar o estado dos dispositivos IoT com valores atuais e passados, além da possibilidade de controlar o processo remotamente.
