# easySale_System
 this is a project of an online sales system, organized in the MVC architecture, in view of the WEB Programming discipline
 
 Este projeto faz parte da avaliação final da disciplina de "Programação Web - DCT1109" do curso de Sistemas de Informação da UFRN.
 Projeto está sendo desenvolvido com o framework Django para o back-end,e para o front-end está sendo o utilizado o Bootstrap CSS
 Junto com Jquery.
 As linguagens utilizadas neste projeto são:<br/>
 <ul>
  <li>CSS (junto com Bootstrap);</li>
  <li>HTML;</li>
  <li> Python (com Django) ;</li>
  <li>SLQLite (integrado com o Django)</li>
  <li>Javascript ( com Jquery);</li>
    </ul>
<br/>
# Django
O django utiza a estrutra MVC(MVT), os models abstraem todo a informação que o sistema deve conter, as views fazem o trabalho árduo de comunição entre o cliente e o servidor, fazendo toda a lógica do sistema, os templates rederizam e mostram os resultados obtidos nas views e as URLs interligam as VIEWs com os templates.
Como o django por padrão já é integrado com o banco de dados, não é nescessário realizar uma consulta SQL no banco de dados de forma direta ( claro, se houver a necessidade, isto pode ser feito), tudo pode ser feito atráves de <code>manager's</code> 
<br>

# REQUERIDO
Essas bibliotecas foram utilizadas para o gerenciamento
<ul>
    <li>VENV (opcional)</li>
    <li>Django (obrigatório)</li>
    <li>Biblioteca Pillow (obrigatório)</li>
</ul>
</br>
Para instalar todos esses pacotes, rode no seu terminal > <code> $ pip install -r requirements.txt </code> 

<br/>

# Funcionalidades
<ul>
    <li>Cadastro de usuários: Funcionando</li>
    <li>Cadastro de produtos: Funcionando</li>
    <li>Edição de produtos: Funcionando</li>
    <li>Edição de conta: Funcionando</li>
    <li>Listagem de produtos: Funcionando</li>
    <li>Login e logout de usuários: Funcionando</li>
    <li>Comentário em produto: a fazer</li>
    <li>Compra de produtos: a fazer</li>
</ul>

# Antes de começar, inicialize o banco de dados!
Antes de começar a utilizar, siga esses passos na pasta onde o projeto foi clonado:
<ol>
    <li><code> $ python manage.py makemigrations</code></li>
    <li><code> $ python manage.py migrate</code></li>
</ol>
Este código cria e prepara o banco de dados. o <i>makemigrations</i> captura toda as alterações no feitas nos models, gerando um arquivo de migrações, o <i>migrate</i> captura as migrações feitas e gera tabelas a nível de banco de dados deixando-as prontas para realizar inserções, consultas e excluções.

# Rodando o projeto
Na pasta do do projeto rode em seu terminal: <code> $ python manage.py runserver</code> logo após vá até o seu navegador de preferência e coloque na barra de endereço <code>localhost:8000</code>, agora você tem acesso ao site.

# Criando um administrador do sistema
Caso tenha interesse em criar um administrador, na pasta raiz, rode <code> $ python manage.py createsuperuser</code>, logo após forneça todos os dados, e depois de criar um administador vá a sua barra de pesquisa e coloque <code>localhost:8000/admin</code>, faça o login com os dados criados anteriormente, agora você tem acesso a todas as informações do sistema, podem realizar qualquer alteração! (<strong>cuidado</strong> alterações no admnistrador, afetam os usuários normais)
