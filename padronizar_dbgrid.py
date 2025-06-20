import os
import re


# Opções padrão que queremos aplicar aos TDBGrid
OPTIONS_PADRAO = 'Options = [dgTitles, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgRowSelect, dgAlwaysShowSelection, dgConfirmDelete, dgCancelOnExit]'


def padronizar_dbgrid_em_dfm(pasta):
    arquivos_modificados = 0
    grids_modificados = 0

    for arquivo in os.listdir(pasta):
        if not arquivo.lower().endswith(".dfm"):
            continue

        caminho = os.path.join(pasta, arquivo)
        with open(caminho, "r", encoding="latin-1") as f:
            linhas = f.readlines()

        nova_linha = []
        dentro_grid = False
        modificou_este = False
        options_setado = False

        for linha in linhas:
            linha_strip = linha.strip()

            # Detecta início do TDBGrid
            if linha_strip.startswith("object") and ": TDBGrid" in linha_strip:
                dentro_grid = True
                options_setado = False
                nova_linha.append(linha)
                continue

            if dentro_grid:
                # Verifica se encontrou uma linha Options e substitui
                if linha_strip.startswith("Options ="):
                    nova_linha.append(f"  {OPTIONS_PADRAO}\n")
                    options_setado = True
                    modificou_este = True
                    grids_modificados += 1
                    continue

                # Detecta fim do TDBGrid
                if linha_strip == "end":
                    # Se não tinha a linha Options, adiciona antes do 'end'
                    if not options_setado:
                        nova_linha.append(f"  {OPTIONS_PADRAO}\n")
                        modificou_este = True
                        grids_modificados += 1

                    nova_linha.append(linha)
                    dentro_grid = False
                    continue

            nova_linha.append(linha)

        # Se modificou, sobrescreve o arquivo
        if modificou_este:
            with open(caminho, "w", encoding="latin-1") as f:
                f.writelines(nova_linha)

            print(f"[✓] Atualizado: {caminho}")
            arquivos_modificados += 1

    print("\nResumo:")
    print(f"- Arquivos modificados: {arquivos_modificados}")
    print(f"- TDBGrids padronizados: {grids_modificados}")
    print("✅ Finalizado com sucesso.")


if __name__ == "__main__":
    padronizar_dbgrid_em_dfm(r"C:\Fontes\nomedoprojeto")
