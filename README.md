# Image Recovery with Histograms
Primeiro trabalho prático da disciplina de Visão Computacional, que consiste em achar as N imagens mais similares a imagem de busca, através de seus histogramas.

## Descrição:
O programa está estruturado de forma a receber imagens com nome completo da forma "{class}_{filename}.png" (e.g.: c001_001.png seria a imagem '001" da class "c001"), e com base nas classes retornadas, determinar a porcentagem de classes corretas.

## Como usar:
O programa pode ser utilizado de duas maneiras:
1. Através dos argumentos por linha de comando.

```bash
  python image_recovery.py path search_image n
```
Onde "path" é o caminho onde as imagens estão (incluindo a imagem de busca), "search_image" é o nome completo da imagem de busca e, n é quantidade de imagens mais semelhantes que devem ser retornadas.

2. Através do prompt que o programa irá fazer, pedindo as mesmas informações passadas por argumento no item anterior. Portanto, basta executar:

```bash
  python image_recovery.py
```
