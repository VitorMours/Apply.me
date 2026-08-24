# Notes.md 


### 04/08/2026

Vai ser preciso rodar a LLM dentro do docker com a internet interna dentro do sistema, vou verificar isso e colocar dentro do sistema.



#### 01/08/2026

Relacionado ao comportamento de chat dentro do frontend, vale ser necessário que o comportamento e os dados sejam adminitrados pelo backend responsável pelo mesmo, sendo assim, o microsserviço de LLM. Ele vai ter que gerir os dados presentes dentro do sistema, e dentro dele vamos ter a possibilidade de que dentro do mongodb, vamos ter as informações de histórico dentro do chat, isso vai ser utilizado por ser a maneira com menos possibilidade de problemas. Como vamos ter um tamanho limitado, para traçar o perfil do usuário, podesmos usar dentro do mongodb, sendo um documento o perfil completo do usuario. Posteriormente, podemos ter que algumas informações de como o perfil dele se comporta no mercado de trabalho, e quais tecnologias seriam interessantes, ficam dentro do posgres que usa o pgvector

Toda vez que o llm for ativado, vai ter que ser criado um chat de forma que a administração do mesmo é do LLM.  Não vai ser usado rag pois as informações vao ser providas pelo usuário, sem necessidade de buscas



