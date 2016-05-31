# Stack AWS Cloudformation: Start/Stop de Instâncias Amazon EC2 via AWS Lambda
###### Funcionamento
* Cada diretório neste repositório representa **UMA** Região AWS. Assim, os templates podem ser lançados em **QUALQUER** Região que tenha o AWS Lambda disponível;
* Cada diretório contém um template, 2 scripts (start_all.py e stop_all.py) e um script zip_all.sh;
* Para cada edição feita nos scripts, você deve executar o zip_all.sh daquele diretório;
* O template do AWS Cloudformation cria, automaticamente, a role e a policy para execução dos das funções no AWS Lambda;

###### Uso
* Acesse a console de sua conta AWS e vá até a console de gerenciamento do [Amazon S3](https://console.aws.amazon.com/s3/);
* Crie um Bucket e clique para acessá-lo;
* Faça o upload dos arquivos **ec2-startstop.template** e **ec2-startstop.zip** da Região de sua escolha para seu Bucket Amazon S3 criado no item anterior;
* Clique no arquivo **ec2-startstop.template**, e clique em **Properties**;
* Copie o link do arquivo, ex: https://s3.amazonaws.com/SEU_BUCKET/ec2-startstop.template
* Agora, vá até a console de gerenciamento do [AWS Cloudformation](https://console.aws.amazon.com/cloudformation/);
* Clique em **Create Stack**;
* No campo **Specify an Amazon S3 template URL**, cole/insira o link que você copiou do template, e clique em next;
* Preencha os campos necessários: em nome do Bucket Amazon S3, coloque o nome do Bucket criado nos passos anteriores. Em tópico SNS, insira um nome para o tópico do AWS Push Notification Service, que será utilizado para receber alertas em caso de erro na execução dos scripts;
* Vá passando pelas opções até lançar o Stack;
* Assim que lançado, os recursos serão criados automaticamente;
* Após terminado o processo, vá até a console de gerenciamento do AWS SNS e se inscreva no tópico criado, para receber os alertas;
* Repita estes passos para outras funções de Regiões diferentes;
* Para agendamento da função no horário que quiser, após lançar os Stacks desejados, coloque um Event Source em cada Função AWS Lambda, conforme abaixo:
* Acesse a console de gerenciamento do [AWS Lambda](https://console.aws.amazon.com/lambda);
* Clique na função desejada;
* Clique na aba **Event sources**;
* Clique em **Add event source**;
* Nesta tela, preencha:
    * Event source type: **Cloudwatch Events - Schedule**;
    * Rule name: um nome para a regra, que você possa lembrar;
    * Rule description: uma descrição para regra;
    * Schedule expression: siga os exemplos de  expressão abaixo.
    * Clique em **Submit** e pronto, está agendado;
    * Repita estes passos para as outras funções;

Assim que finalizar, insira a Tag **AutoStartStop**, com o valor **TRUE** nas instâncias Amazon EC2 que vão participar do Stop/Start. Caso a instância Amazon EC2 não tenham esta Tag, ou não tenha a Tag com o valor em **TRUE**, ela não entra na execução.

###### Exemplos de Expressões para agendamento
As expressões são do cron (Linux), e seguem a hora UTC (+3BRT). Abaixo seguem alguns exemplos:

* Executado às 17:00 (BRT) de segunda à sexta:
```
cron(0 20 ? * MON-FRI * )
```
* Executado às 08:00 (BRT) de segunda à sexta:
```
cron(0 11 ? * MON-FRI * )
```  

###### Funções
**start_all.py**: Executa o START todas as Instâncias Amazon EC2 com a Tag Name AutoStartStop, e Valor TRUE (CASE-SENSITIVE);  
**stop_all.py**: Executa o STOP todas as Instâncias Amazon EC2 com a Tag Name AutoStartStop, e Valor TRUE (CASE-SENSITIVE);
###### Arquivos
```
ec2-serverless-startstop
├── California
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Frankfurt
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Ireland
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Oregon
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── README.md
├── SaoPaulo
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Seoul
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Singapore
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Sydney
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Tokyo
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
└── Virginia
    ├── ec2-startstop.template
    ├── ec2-startstop.zip
    ├── start_all.py
    ├── stop_all.py
    └── zip_all.sh
```
