# LLM Service

<p  align="center">
  <a href="https://go-skill-icons.vercel.app/">
    <img
      src="https://go-skill-icons.vercel.app/api/icons?i=python,fastapi,celery,pydantic,sqlalchemy,pytest,langchain,ollama,docker,githubactions,qdrant,grafana,opentelemetry&theme=dark"
    />
  </a>
</p>

O serviço de LLM existe com o intuito, de se comunicar por uma interface de texto mais amigável ao usuário, e ao mesmo tempo o mesmo poder se comunicar a inteligência artificial, buscando guiar ela sobre as necessidades do usuário, e a mesma interagir dando insights valorosos e importantes para o usuário. Com isso, temos que a estrutura do mesmo, é feita de forma que podemos ter observabilidade do mesmo tanto de maneira singular, como de maneira integrada aos outros sistemas os quais estamos desenvolvendo. 

## Estrutura do Projeto
Temos que a estrutura do projeto pode ser estudada de diversas formas, principalmente pela forma  como cada uma dessas partes produz um determinado resultado, e possui uma determinada responsabilidade que da mesma forma que independente do resto, funciona em conjunto.

### Base
Temos que por base, estamos usando o funcionamento mais comum de todos quando falamos de IA, utilizando ferramentas como **python** e **fastapi** para desenvolver nossa aplicação, e podemos disponibilizar o acesso dela à internet, por meio de uma API de comunicação nos padrões REST. Com isso, temos que a grande quantidade de complexidade que podemos ter dentro dos nossos sistemas, faz com que o estudo de sistemas distribuídos, e sistemas assíncrono se faz presente. A partir disso temos que a estrutura core se centraliza em:

- **Python:** Linguagem de desenvolvimento intepretada
- **FastAPI:** Framework de desenvolvimento web assíncrono
- **Pydantic:** Validação e Schema dos dados que vão ser usados e transferidos
- **SQLAlchemy:** Conexão com o banco de dados relacional
- **QDrant:** Banco de dados vetorial, com o foco em elementos de IA
- **PostgreSQL:** Banco de dados relacional

A partir disso, temos que o foco é que esse microsserviço tenha a capacidade de manejar todas as interações com o usuário de forma que os dados dessas interações vão ser armanzenados e administrados por esse serviço em específico, sem depender de outros serviços satélites a eles.

### Comunicação
A ideia da comunicação, é que esse sistema vai ter como foco, autenticar e autorizar a interação dos usuários dentro do chat, por meio do sistema de autenticação, via tokes JWT, facilitando assim o entendimento do funcionamento do sistema, e possibilitando também que o usuário transite entre diversos serviços, sem precisar ficar se autenticando várias vezes.

### Observabilidade
### Infraestrutura





## Rodando o Código