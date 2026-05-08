import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(caminho_arquivo):
    """
    Le o arquivo CSV e retorna um DataFrame.
    """
    df = pd.read_csv(
        caminho_arquivo,
        na_values=[" ", ""]
    )

    return df

def tratar_dados(df):
    """
    Realiza tratamento e organização dos dados.
    """

    # Converter coluna de data
    df["data"] = pd.to_datetime(df["data"])

    # Interpolação dos valores ausentes
    df["nivel_rio_m"] = df["nivel_rio_m"].interpolate()
    df["ndvi"] = df["ndvi"].interpolate()

    return df


def calcular_estatisticas(df):
    """
    Calcula e exibe estatisticas básicas.
    """

    print("\nMédias:")

    print(
        f"Temperatura média: "
        f"{df['temperatura_c'].mean():.2f} °C"
    )

    print(
        f"Nível médio do rio: "
        f"{df['nivel_rio_m'].mean():.2f} m"
    )

    print(
        f"NDVI médio: "
        f"{df['ndvi'].mean():.3f}"
    )


def gerar_grafico_temperatura(df):
    """
    Gera grafico de temperatura ao longo do tempo.
    """

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        df["data"],
        df["temperatura_c"],
        marker="o"
    )

    ax.set_title("Temperatura ao longo do tempo")
    ax.set_xlabel("Data")
    ax.set_ylabel("Temperatura (°C)")

    ax.grid(True)

    plt.xticks(rotation=45)

    fig.tight_layout()

    fig.savefig("grafico_temperatura.png")
    plt.show()


def gerar_grafico_ambiental(df):
    """
    Gera grafico com eixo duplo para:
    - nível do rio
    - NDVI
    """

    fig, ax1 = plt.subplots(figsize=(10, 5))

    linha1 = ax1.plot(
        df["data"],
        df["nivel_rio_m"],
        marker="o",
        color="blue",
        label="Nível do Rio"
    )

    ax1.set_xlabel("Data")
    ax1.set_ylabel("Nível do Rio (m)")

    ax1.grid(True)

    ax2 = ax1.twinx()

    linha2 = ax2.plot(
        df["data"],
        df["ndvi"],
        marker="o",
        linestyle="--",
        color="green",
        label="NDVI"
    )

    ax2.set_ylabel("NDVI")

    plt.title("Nível do Rio e NDVI ao longo do tempo")

    plt.xticks(rotation=45)

    linhas = linha1 + linha2
    labels = [linha.get_label() for linha in linhas]

    ax1.legend(linhas, labels, loc="upper left")

    fig.tight_layout()

    fig.savefig("grafico_ambiental.png")
    plt.show()


def main():

    # Carregar dados
    df = carregar_dados("dados_pantanal.csv")

    # Tratar dados
    df = tratar_dados(df)

    # Mostrar dados tratados
    print("\nDados tratados:")
    print(df)

    # Estatísticas
    calcular_estatisticas(df)

    # Gráficos
    gerar_grafico_temperatura(df)
    gerar_grafico_ambiental(df)


if __name__ == "__main__":
    main()