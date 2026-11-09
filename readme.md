## Projeto 1 - Simulando um malware de captura de dados em Python

### Sobre o projeto

Projeto para validação de aprendizado no Bootcamp de Cybersegurança da DIO - criando um script para criptografar arquivos.

### Requisitos necessários
Para esse projeto, não foi necessário subir uma VM com outro SO. Como o código rodou só em uma pasta isolada, criada dentro de um diretório específico para o projeto, é possível rodar na máquina sem complicações. Caso o estudante quisesse tentar criptografar muito mais que o visto aqui, aí sim seria ideal rodar em uma máquina virtual, pela facilidade de reverter tudo caso algo desse errado. Seria possível criar um snapshot de uma imagem já com arquivos adicionados para validação. Se algo desse errado, com um simples click seria possível carregar a VM antes de os arquivos terem sido criptografados. 

Editor de código e capacidade de rodar scripts Python. Eu já tinha o Python 3 na minha máquina e utilizei o VSCodium.

### Configuração do ambiente de teste
Criação de um projeto no editor de texto, com estrutura de pastas:
- readme.md
- malware
- test_files

De saída, criar um arquivo de texto dentro do test_files com uma senha. Nesse projeto chamado de senhas.txt e utilizado só para validar a criptografia.

Criar mais um arquivo (aqui no caso o dados_confidencias.txt) com qualquer informação. Eu adicionei um lorem ipsum, que é só um texto em latim, muito utilizado para preencher espaços de texto em ferramentas de design.

Após isso, na pasta raiz do projeto criar um arquivo ransomware.py, com a lógica para executar o ransonware. O código é bem simples de entender, e possui as seguintes etapas:
- carrega duas bibliotecas do python. O cryptography (que é uma biblioteca externa e deve ser instalada com o Pip) e o OS, que é uma biblioteca nativa do Python. 
- sequência de funções para criar e utilizar uma chave de criptografia
- função para criptografar arquivo
- função para encontrar arquivos (um loop que gera uma lista de strings)
- função para exibir mensagem de resgate para a vítima
- definição do método main (necessário para o script Python ser executado) chamando as funções criadas anteriormente na ordem correta para criar chave, localizar e finalmente criptografar os arquivos. 

Antes de rodar o script (e não mencionando em lugar algum do vídeo) é necessário instalar a biblioteca cryptography. Para python 3, é possível instalar com o comando

  ```bash
  pip3 install cryptography
  ```

Após isso, é possível executar o script. No meu caso eu precisei abrir o terminal, navegar para a pasta malware e então executar o script com:

  ```bash
  python3 ransonware.py
  ```

Os arquivos foram criptografados, e uma chave necessária para descriptografar os arquivos foi gerada na pasta. Num cenário realista, essa chave não seria salva na pasta que contém o script, já que é a chave que os atacantes "vendem" para a vítima. 

### Descriptografando os arquivos 
Para validar o funcionamento, foi criado um novo script chamado descriptografar.py, que tem as seguintes funções:

- carregar a chave (script duplicado)
- descriptografar os arquivos
- encontrar os arquivos criptografados (script duplicado. Poderia ser feito um terceiro script, para ter uma única cópia desse código compartilhado entre os outros dois scripts. Como é um projeto muito simples, ainda não é um problema, mas são boas práticas de desenvolvimento de código).
- função main para executar as funções. Bem parecida com a lógica do script de criptografar aquivos. Também poderia ser movido para um arquivo shared, mas nesse caso seriam necessárias alterações no código para rodar a lógica certa via atributos passados no momento de chamar o método. 

O script também não tem nenhuma configuração extra, e pode ser rodado com:

  ```bash
  python3 descriptografar.py
  ```

Se a chave não estiver correta, o script python vai dar erro (sem nenhum tipo de tratamento de erros). Se a chave estiver correta, os arquivos serão descriptografados normalmente e a vítima passa a possuir seus arquivos em formato legível de volta. 

<br>

## Projeto 2 - Keylogger

### Sobre o projeto

Projeto para validação de aprendizado no Bootcamp de Cybersegurança da DIO - criando um keylogger com Python.

### Requisitos necessários
Para esse projeto, não foi necessário subir uma VM com outro SO. Como o código rodou só em uma pasta isolada, criada dentro de um diretório específico para o projeto, é possível rodar na máquina sem complicações. Caso o estudante quisesse tentar criptografar muito mais que o visto aqui, aí sim seria ideal rodar em uma máquina virtual, pela facilidade de reverter tudo caso algo desse errado. Seria possível criar um snapshot de uma imagem já com arquivos adicionados para validação. Se algo desse errado, com um simples click seria possível carregar a VM antes de os arquivos terem sido criptografados. 

Editor de código e capacidade de rodar scripts Python. Eu já tinha o Python 3 na minha máquina e utilizei o VSCodium.

### Configuração do ambiente de teste
Criação de uma nova pasta (no caso chamada de keylogger).

Instalação de uma biblioteca externa, chamada pynput. Instalada usando Pip com o comando:

  ```bash
  pip3 install pynput
  ```

Com a instalação copncluída, foi criado um arquivo keylogger.py, com o código do script. No arquivo estão incluídos:

- comando para importar a dependência instalada anteriormente
- lista de teclas a serem ignoradas pelo keylogger. A ideia é deixar o arquivo com as capturas mais limpo.
- função para habilitar a captura em si, com inclusão de condições para melhorar o visual da captura.

Após a finalização de escrito do script, só navegar para a pasta e executar o mesmo:

  ```bash
  python3 keylogger.py
  ```

Com isso, enquanto o programa estiver rodando, ele vai capturar tudo que o usuário digitar, independente do programa que o usuário estiver utilizando.

### Escondendo o keylogger para dificultar detecção pela vítima

Para evitar de exibir uma janela de terminal aberta (o que pode deixar a identificação do keylogger muito fácil) é possível alterar a extensão do arquivo para pyw. Pyw é uma extensão que o Window roda nativamente, e não precisa de terminal aberto ou qualquer outro tipo de alerta visual para o usuário de que algo está rodando. Para converter o arquivo é só usar o comando:

  ```bash
  ren .\keylogger.py .\keylogger.pyw
  ```

Como no meu caso estou utilizando uma máquina linux, o comando é:

  ```bash
  mv keylogger.py keylogger.pyw
  ```

Também é possível renomear o arquivo manualmente, no próprio editor de texto. Após isso, é possível executar o script da mesma maneira de antes (tudo permanece inalterado - só não existe uma indicação visual de que o script está rodando na máquina da vítima)
  

### Enviando os dados capturados por e-mail 
Para enviar os dados capturados, uma opção é envio por e-mail. Pode se usar qualquer e-mail, mas pensando em segurança o ideal é criar um e-mail só pra isso. Após criar o e-mail, algumas configurações são necessárias (no treinamento foi utilizado um e-mail do Google).

Logado na conta é necessário adicionar um configuração para o login em 2 etapas (necessário para o funcionamento do e-mail via scripts).

Depois, outra configuração. Agora acessando a url

  ```bash
  https://myaccount.google.com/apppasswords
  ```

vai ser necessário cadastrar uma chave para o aplicativo python. A chave é diferente da sua senha de acesso a conta de e-mail. 

Após as configurações do e-mail, precisamos instalar mais uma biblioteca externa, com o comando:

  ```bash
  pip install secure-smtplib
  ```
O código para configurar o keylogger mais o controle de envio dos e-mails vai ser adicionado em um novo script (chamado aqui de keylogger_email.py).

Nesse novo arquivo existem:
- imports de todos os recursos necessários
- configurações da conta de e-mail
- script básico de envio de e-mail
- criação de um timer para enviar e-mail a cada 60 segundos
- regras para registrar input e enviar. Uma versão mais simples da configuração do primeiro script. 
- chamada para capturar as teclas e começar o envio de e-mails

Da mesma forma como o primeiro exemplo, o arquivo também pode ser renomeado para pyw para dificultar a detecção pelo usuário. Para rodar o código, mesmo comando de antes:

  ```bash
  python3 keylogger_email.py
  ```

agora tudo que a vítima digitar será registrado e enviado para o e-mail cadastrado! 