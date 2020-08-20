# Descrição

Precisei converter um JSON escrito em um arquivo .csv (!).
No .csv (antigo JSON) havia uma coluna com chaves de strings i18n. Suas respectivas traduções estavam em uma coluna logo ao lado.
A ideia era extrair o valor traduzido na coluna B e inflar no seu respectivo valor na coluna A.

## Ilustração:
```
| COLUNA A (JSON)                                 |  COLUNA B(Tradução) |
|-------------------------------------------------|---------------------|
| {                                               |                     |
|   "LOGIN": {                                    |                     |
|     "EMAIL": "Email"                            | Email               |
|     "PASSWORD": "Senha"                         | Password            |
|     "CONFIRM": "Entrar"                         | Log in              |
|     "FORGOT": "Esqueci minha senha"             | I forgot my password|
|     "TITLE": "Título"                           | Title               |
|     "TYPE_EMAIL": "Digite seu email"            | Type your email     |
|     "SEND": "Enviar"                            | Send                |
|   },                                            |                     |  
|   "NAVBAR":{                                    |                     |
|     "HOME": "Home"                              | Home                |
|     "IMPORT_DATA": "Importar Dados"             | Import Data         |
|     "LOGOUT": "Sair"                            | Logout              |
|   }                                             |                     |
| }                                               |                     |
```

## Execução: 
Antes de executar o parser, realizei o seguinte tratamento nos dados:
```
{	
    "LOGIN": {	
        "EMAIL": "Email",	email
        "PASSWORD": "Senha",	Password
        "CONFIRM": "Entrar",	Log in
        "FORGOT": "Esqueci minha senha",	I forgot my password 
        "FORGOT_QUESTION": "Esqueceu sua senha?",	Did you forget your password?
        "TYPE_EMAIL": "Digite seu email",	Type your email
        "SEND": "Enviar"	Send
    },	
    "NAVBAR":{	
        "HOME": "Home",	Home
        "IMPORT_DATA": "Importar Dados",	Import Data
        "LOGOUT": "Sair"	Logout
    }
}	
```

Ou seja, concatenei as colunas A e B.
Os dados tratados foram salvos em um arquivo de texto.

O parser solicita dois arquivos: (i) o arquivo original, tratado acima e (ii) um arquivo de destino, onde o  resultado será escrito.

Segue trecho do código fonte responsável por apontar para esses dois arquivos:

```
originalPathTarget = r'.\file-en.json'
parsedPathTarget = r'.\file-en-parsed.json'
```

O resultado do parser foi:
```
{		
"LOGIN": {	
"EMAIL": "email",
"PASSWORD": "Password",
"CONFIRM": "Log in",
"FORGOT": "I forgot my password", 
"FORGOT_QUESTION": "Did you forget your password?", 
"TYPE_EMAIL": "Type your email",
"SEND": "Send"
},	
"NAVBAR":{	
"HOME": "Home",
"IMPORT_DATA": "Import Data",
"LOGOUT": "Logout"
}
}	
```	
