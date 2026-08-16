import pandas as pd


def load_data(file_path):
    """
    Carrega o dataset validado.

    Parameters
    ----------
    file_path : str ou Path
        Caminho para o arquivo CSV.

    Returns
    -------
    pd.DataFrame
        Dataset carregado.
    """

    return pd.read_csv(file_path)


def clean_data(df):
    """
    Realiza a limpeza inicial dos dados para modelagem.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset original.

    Returns
    -------
    pd.DataFrame
        Dataset limpo.
    """

    df = df.copy()

    # Converter TotalCharges para numérico
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Remover identificador do cliente
    df = df.drop(
        columns=["customerID"],
        errors="ignore"
    )

    return df