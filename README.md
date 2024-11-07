<!--<p align="center"><a href="#"><img src="src/icon.jpeg" width="350"></a></p>-->

# Sistema de Ponto Manual de Funcionários Avulsos

Repositório dedicado ao estudo do funcionamento do streamlit para desenvolvimento web integrado com sqlite3.

## Sobre o projeto

<p>
  O intuito desse projeto é realizar insights de planejamento de produção e demanda de funcionários avulsos para determinados períodos.
  Ele deve abranger toda a criação de banco, inserção de departamentos e funcionarios, além de regularização do sistema de ponto dos mesmos. A partir disso verificar com base na produção a quantidade de funcionários que vai ser alocada por período e realizar associações entre produtividade e base de funcionários presentes nesse período! 
</p>

## Tecnologia Utilizada
<p align="center"><a href="https://docs.streamlit.io/" target="_blank"><img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-lighttext.png" width="400"></a></p>

## About Streamlit
O Streamlit é uma biblioteca Python de código aberto que permite criar aplicativos web de forma rápida e intuitiva, especialmente para visualização de dados e aplicações de machine learning.
<br>

Streamlit facilita a implementação de tarefas comuns em projetos web, como:

- [Desenvolvimento de chats;](https://docs.streamlit.io/develop/tutorials/llms).
- [Multipáginas;](https://docs.streamlit.io/develop/tutorials/multipage).
- [Conexões à diferentes fontes de dados;](https://docs.streamlit.io/develop/tutorials/databases).
- [Execução de scripts.](https://docs.streamlit.io/develop/tutorials/execution-flow).

Streamlit é acessível, oferecendo ferramentas necessárias para a construção de pequenas aplicações web.

## Learning Streamlit

O [Streamlit](https://docs.streamlit.io/) possui uma documentação crescente com cada vez mais funcionalidades sendo criadas, facilitando o aprendizado para desenvolvedores de nível básico. Além da documentação oficial, há uma grande variedade de tutoriais e guias disponíveis para ajudar a dominar o framework.

## Construção do App

A [API](https://static.loongship.com/dataApi/api.html#_3-1-%E8%88%B9%E8%88%B6%E6%90%9C%E7%B4%A2) utilizada para a construção do projeto foi a do site [SHIPDT](https://www.shipdt.com/), a qual os usuários tinham mais familiaridade com a disposição dos dados que vinham nos resultados. Ela tem diversas opções de retorno de dados como temperatura da água, condições climáticas, entre outras, mas procurei focar na parte solicitada. 
<br>
O app foi construido com base em um menu lateral feito com o componente ```st.navigation``` contendo todas as solicitações feitas anteriormente na descrição do projeto, separadas por blocos utilizando o ```st.Page```. Ao abrir o "site" hospedado localmente o usuário se depara com a página inicial: <br>

## Desafios e Melhorias

Acredito que para uma versão inicial o app está bem coeso e funcional mas acrescentaria como pontos a serem melhorados: 
- Otimização do código;
- Velocidade de processamento dos dados colhidos;
- Documentação;
- Melhoria visual (tanto do mapa quanto da página).

Algumas coisas tentei implementar como a parte de carregamento assíncrono, algo que nunca tinha visto anteriormente, que me serviu de aprendizado, porém devo levar em consideração os pontos acima para próximas versões. 
