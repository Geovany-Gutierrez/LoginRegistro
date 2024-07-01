## Projeto Django: Login e Cadastro

Este projeto demonstra a implementação básica de um sistema de login e cadastro utilizando o framework Django em Python. Ele oferece funcionalidades simples para permitir que os usuários se registrem, façam login e logout no sistema.

### Tecnologias Utilizadas
- **Python 3.12**: Linguagem de programação principal.
- **Django 3.x**: Framework web utilizado para desenvolvimento backend.
- **Bootstrap 4**: Biblioteca de front-end para estilização e componentes responsivos.

### Estrutura do Projeto
```
LoginRegistro/
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── home.html
│   │       ├── signIn.html
│   │       └── signUp.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── caseLoginRegistro/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
└── manage.py
```

### Funcionalidades Principais
**Página Inicial (`home`)**:
- Exibe uma mensagem de boas-vindas e oferece links para cadastro e login.
- Mostra o nome de usuário autenticado se estiver logado.

**Cadastro (`signup`)**:
- Permite aos usuários se registrarem fornecendo um nome de usuário, email e senha.
- Validação de formulários é feita com `UserCreationForm` do Django.

**Login (`login`)**:
- Usuários podem fazer login usando seu nome de usuário e senha.
- Implementado com `AuthenticationForm` do Django para autenticação.

**Logout (`logout`)**:
- Permite aos usuários saírem do sistema.

### Como Executar o Projeto Localmente
Para executar este projeto localmente, siga estas etapas:

1. Clone o repositório do GitHub:
   ```sh
   git clone -b master https://github.com/Geovany-Gutierrez/LoginRegistro.git
   ```

2. Aplique as migrações do Django para configurar o banco de dados SQLite:
   ```sh
   python manage.py migrate
   ```

3. Inicie o servidor de desenvolvimento:
   ```sh
   python manage.py runserver
   ```

4. Acesse o projeto em seu navegador web:
   ```sh
   http://localhost:8000/
   ```
