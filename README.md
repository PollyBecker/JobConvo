# Plataforma Job 
Inspirado em plataformas de emprego este app despojado foi desenvolvido utilizando Python, Django e os frameworks de front end Tailwind e Bootstrap além de SQLite. As principais funcionalidades estão presentes neste projeto incrivel! Quer conferir?

🚀 Tecnologias e ferramentas utilizadas

PYTHON DJANGO HTML TAILWIND BOOTSTRAP SQLITE

🖥️ Demonstração

Ao final do projeto apos criar um perfil o site tera disponivel : Um catalogo de vagas na home ordenados do mais recente ao mais antigo; Pode ver detalhes das vagas na pagina de detalhes, Pesquisar por vagas e empresas; Alterar seus dados e sua senha de forma intuitiva;
A empresa podera: Cadastrar vagas, ver, alterar, deletar suas vagas, ver as vagas mais acessadas, ver os usuarios que se candidataram para cada vaga;
o Usuario podera: Ver as vagas, se candidatar para as vagas, salvar vagas;
Atualmente ja foi implementado cerca de 65% das funcionalidades;
 
 Código
 
 O site gira em torno das vagas publicadas e para começar vamos ver o app Job que esta relacionado com as vagas. Quais vagas publicadas e a lista de candidatos que se inscreveram para cada vaga.
 O arquivo models.py contém duas classes.Primeiro definimos duas variáveis de Listas que consiste em dois tipos de llistas com escolhas que usemos em ambas classes. A primeira Classe Jobs recebe todos os parâmetros que cada objeto que no caso é uma vaga de emprego terá e a segunda Aplicados que guarda os dados dos candidatos se liga a primeira atraves de uma FK.

 Agora lidaremos com o arquivo views que contém todas as visualizações relacionadas à parte de Jobs. Aqui predominam as CBV(Classe Based Views) deixando o codigo muito mais legivel. Com apenas algumas linhas de codigo temos funçoes claras, de fácil manutenção que realizam simutaneamente o metodo Get,Post,Redirect e pequenas funcs para controle de contadores.
 
 As views mais simples como home, login e cadastro náo precisam de muitas explicações. A view de Detalhes do Candidato é a que exibirá o post dos detalhes de uma vaga selecionada na Homepage. Aqui eu sobrescrevi duas funçoes inerentes a view. A primeira sobrescrevi a func Get para contabilizar as views. A segunda sobreescrevi a func de validação do formulario para salvar automaticamente a a vaga que o usuario esta acessando como o nome da vaga para qual ele se aplicou e tambem aproveitei para dar update na variavel com oo numero de inscritos nas vagas.
 
 Ainda no app Job temos um arquivo gerenciador onde temos algumas funçoes auxiliares de manipulaçao de dados. Temos ali a função que organiza os jobs em ordem cronologica apartir do mais recente. Outras duas de funcionamento semelhante são a func que organiza por mais visualizados e outra com maior numero de candidatos.
 
 Por ultimo vale citar o arquivo de testes unitarios.Teste Unitárioé a forma de se testar unidades individuais de código fonte sem precisar efetivamente executar a aplicaçao e com menor taxa de falhas.foram executados ate o momento testes para validação das Urls atraves do reverse e dos Templates.
 
 Agora temos o app Sujeito. Sujeito concerne ao que diz respeito aos usuarios. Ali temos a classe Empresa que contém todas as informações sobre a Empresa. Alem dos dados do Usuario do Django temos ali data de cadastro, numero de vagas criadas e numero do cnpj. Temos por fim a classe candidato.
 
 As views aqui são em sua maioria FormViews para exibir e manipular formulários. A unica que os estatísticos diriam que "sai da curva" é a view Dashboard que é uma Detailview onde eu manipulei a func de contexto para filtrar as vagas de acordo com o user que esta acessando para que ele possa ter acesso a tela de vagas com número de visualizações, numero de candidatos e um link para uma pagina com a lista de detelhes de todos os candidatos inscritos.
 
 Por ultimo ainda podemos citar o arquivo de Formularios onde temos todos os Forms usados.
 
Ao fim, concluímos todo o back-end relacionado ao aplicativo Candidatos.
Esperançosamente, você gostou! Se você leu até aqui tenho certeza que você ficou com o mouse coçando para marcar com estrela, bifurcar e testá-lo por conta própria.
