
import nltk
import string
import heapq


nltk.download("punkt")
nltk.download("stopwords")


def preprocessamento(texto):
    stopwords = nltk.corpus.stopwords.words("portuguese")
    # deixando o texto em minusculo
    texto_formatado = texto.lower()
    tokens = []

    # tokenizando o texto
    for token in nltk.word_tokenize(texto_formatado):
        tokens.append(token)
    # removendo as stopwords
    tokens = [palavra for palavra in tokens if palavra not in stopwords]

    # removendo a pontuação
    tokens = [
        palavra for palavra in tokens
        if palavra not in string.punctuation
    ]

    # formatando a lista em string
    texto_formatado = " ".join([str(elemento) for elemento in tokens
                                if not elemento.isdigit()])

    return texto_formatado


def sumarizar(texto, top_n_palavra, distancia, quantidade_sentencas):
    """
        Funçao para fazer a sumarização dos textos
    Args:
        texto (string): Texto para ser sumarizado
        top_n_palavra (int): quantidade que palavras top
        distancia (int): Distancia entre aas palavras
        quantidade_sentencas (int): Quantidade de sentencas

    Returns:
        sentencas_originais (lista): Lista com as sentencas originais
        melhores_sentencas (lista): As melhores sentencas
        notas_sentencas (lista): Notas das sentencas
    """
    sentencas_originais = [sentenca for sentenca in nltk.sent_tokenize(texto)]
    sentencas_formatadas = [
        preprocessamento(sentenca) for sentenca in sentencas_originais]

    palavra = [
        palavra for sentenca in sentencas_formatadas
        for palavra in nltk.word_tokenize(sentenca)]
    frequencia = nltk.FreqDist(palavra)

    top_palavras = [
        palavra[0] for palavra in frequencia.most_common(top_n_palavra)]
    notas_sentencas = calcular_nota_sentenca(
        sentencas_formatadas, top_palavras, distancia)

    melhores_sentencas = heapq.nlargest(quantidade_sentencas, notas_sentencas)
    melhores_sentencas = [
        sentencas_originais[i] for (nota, i) in melhores_sentencas]

    return sentencas_originais, melhores_sentencas, notas_sentencas


def calcular_nota_sentenca(sentencas, palavras_importantes, distancia):
    """
        Algoritmo de LUHN,
        Função para fazer o calculo das notas das sentencas
    Args:
        sentencas ([lista]): lista contendo as sentencas
        palavras_importantes ([lista]): lista contendos as palavras importantes
        distancia ([int]): [description]

    Returns:
        [lista]: Lista contendo as notas
    """
    notas = []
    indice_sentenca = 0

    for sentenca in [
        nltk.word_tokenize(sentenca.lower())
            for sentenca in sentencas]:

        indice_palavra = []
        for palavras in palavras_importantes:
            try:
                indice_palavra. append(sentenca.index(palavras))
            except ValueError:
                pass
        indice_palavra.sort()
        if len(indice_palavra) == 0:
            continue
        lista_grupos = []
        grupo = [indice_palavra[0]]
        i = 1
        while i < len(indice_palavra):
            if indice_palavra[i] - indice_palavra[i - 1] < distancia:
                grupo.append(indice_palavra[i])
            else:
                lista_grupos.append(grupo[:])
                grupo = [indice_palavra[i]]

            i += 1
            lista_grupos.append(grupo)
            nota_maxima_grupo = 0

            for g in lista_grupos:
                palavras_import_grupo = len(g)
                total_palavras_grupo = g[-1] - g[0] + 1
                nota = 1.0 * palavras_import_grupo ** 2 / total_palavras_grupo

                if nota > nota_maxima_grupo:
                    nota_maxima_grupo = nota
            notas.append((nota_maxima_grupo, indice_sentenca))
            indice_sentenca += 1

    return notas
