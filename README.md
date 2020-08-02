# todo-app

Pequeno repositório para exemplo no KT de Roteiro de Testes

## Front

O código do front-end foi baseado [neste post](https://medium.com/@hugo.bjarred/learn-vuejs-by-building-a-simple-todo-app-44e2e7dfccae). Para executar, considerando que os pacotes já tenham sido instalados de acordo com a seção Project setup, basta executar `npm run serve`, e o projeto estará disponível localmente na porta 8080.

Para obter a primeira versão, sem a feature de completar, basta realizar um checkout na tag `0.1.2`: `git checkout tags/0.1.2`. Para inserir a feature de completar basta realizar a mesma operação, porém desta vez referenciando a tag `0.1.3`.

## Back

O código do backend é um exemplo básico de [Flask](https://flask.palletsprojects.com/en/1.1.x/). Para executar, contando que os pacotes já tenham sido instalados (`pip install -r requirements.txt`, preferencialmente num [ambiente virtual](https://docs.python.org/3/library/venv.html)), basta inserir o comando `flask run`. Uma coleção de requests do [Insomnia](https://insomnia.rest/) contém os itens destinados à apresentação.

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
