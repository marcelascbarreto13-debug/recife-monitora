from pathlib import Path
import pandas as pd


def obter_base(pasta_dados=None):
    """
    Carrega as cinco bases brutas utilizadas no projeto Recife Monitora.

    Parameters
    ----------
    pasta_dados : str ou Path, opcional
        Caminho para a pasta que contém os arquivos CSV.
        Caso não seja informado, utiliza a pasta 'dados'
        localizada na raiz do projeto.

    Returns
    -------
    dict
        Dicionário contendo os DataFrames carregados.
    """

    if pasta_dados is None:
        pasta_dados = Path(__file__).resolve().parent.parent / "dados"
    else:
        pasta_dados = Path(pasta_dados)

    arquivos = {
        "equipes": "equipes.csv",
        "resultados": "resultados_ciclos.csv",
        "eixo3": "eixo3_indicadores.csv",
        "nps": "nps_atributos.csv",
        "planos": "planos_acao.csv"
    }

    bases = {}

    for nome, arquivo in arquivos.items():
        caminho = pasta_dados / arquivo

        if not caminho.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {caminho}"
            )

        # Identificadores são carregados como texto,
        # pois representam códigos e não valores numéricos.
        dtype = {"codigo_ine": "string"}

        if nome == "equipes":
            dtype["codigo_cnes"] = "string"

        bases[nome] = pd.read_csv(
            caminho,
            dtype=dtype
        )

    return bases


if __name__ == "__main__":
    bases = obter_base()

    for nome, df in bases.items():
        print(f"{nome}: {df.shape}")