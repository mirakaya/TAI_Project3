# TAI - Project 3
Automatic identificationof musics from a sample

## Para executar a aplicação principal

```bash
$ python3 src/main.py -t <test file> [flags]
```

Apenas o parâmetro com o test file é necessario.

### Flags disponíveis - aplicação principal:

-c -> Permite definir o tipo de compresssor. O valor default é 'gzip'.


## Para executar a avaliação

```bash
$ python3 src/evaluation.py [flags]
```

Nenhuma das flags é obrigatória.

### Flags disponíveis - pesquisa:

-l -> Permite selecionar o tamanho em segundos do ficheiro de teste(1, 3, 6, 10). O valor default é 10.

-c -> Permite definir o tipo de compresssor. O valor default é 'gzip'.

-n -> Permite definir se os testes são efetuados com ficheiros com(true) ou sem(false) presença de ruído. O valor default é false