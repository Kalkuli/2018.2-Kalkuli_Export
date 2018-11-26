# Serviço de Exportação de Relatórios    

<div style="text-align: center"> 

<a href="https://travis-ci.com/Kalkuli/2018.2-Kalkuli_Export"><img src="https://travis-ci.com/Kalkuli/2018.2-Kalkuli_Export.svg?branch=master"/></a>
<a href="https://codeclimate.com/github/Kalkuli/2018.2-Kalkuli_Export/maintainability"><img src="https://api.codeclimate.com/v1/badges/b1f0c20fae43ac3f8c59/maintainability" /></a>
<a href="https://codeclimate.com/github/Kalkuli/2018.2-Kalkuli_Export/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b1f0c20fae43ac3f8c59/test_coverage" /></a>
<a href="https://opensource.org/licenses/GPL-3.0"><img src="https://img.shields.io/badge/license-GPL-%235DA8C1.svg"/></a>

</div> 

# Configurando o ambiente
Para instruções de como instalar o _Docker_ e o _Docker-compose_ clique [aqui](https://github.com/Kalkuli/2018.2-Kalkuli_Front-End/blob/master/README.md). 



## Colocando no ar
Com o Docker e Docker-Compose instalados, basta apenas utilizar os comandos:

```docker-compose -f docker-compose-dev.yml build```

e

```docker-compose -f docker-compose-dev.yml up```


As rotas estarão disponíveis através de [localhost:5007](http://localhost:5007/).


Agora você já pode começar a contribuir!


## Testando

```
docker-compose -f docker-compose-dev.yml run base python manage.py test
```   

E para saber a cobertura dos testes utilize:

```
docker-compose -f docker-compose-dev.yml run base python manage.py cov
```

# Ambientes

## Produção
Para acessar o ambiente de produção, utilize o link a seguir:
```https://kalkuli-export.herokuapp.com/```
<!-- ## Homologação
Para acessar o ambiente de homologação, utilize o link a seguir:```https://b4iplfd1yj.execute-api.sa-east-1.amazonaws.com/hom```

https://b4iplfd1yj.execute-api.sa-east-1.amazonaws.com/hom -->