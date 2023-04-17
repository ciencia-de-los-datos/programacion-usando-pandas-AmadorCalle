"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return len(tbl0)


def pregunta_02():
    return len(tbl0.columns)


def pregunta_03():
    return tbl0.groupby(["_c1"])._c1.count()


def pregunta_04():
    return tbl0.groupby(["_c1"])._c2.mean()


def pregunta_05():
    return tbl0.groupby(["_c1"])._c2.max()


def pregunta_06():
    return sorted(tbl1["_c4"].str.upper().unique().tolist())


def pregunta_07():
    return tbl0.groupby("_c1")._c2.sum()


def pregunta_08():
    tbl0["suma"] = tbl0[["_c0", "_c2"]].sum(axis = 1)
    return tbl0


def pregunta_09():
    tbl0["year"] = tbl0.apply(lambda fila: fila["_c3"][:4], axis = 1)
    return tbl0


def pregunta_10():
    parcial_0 = tbl0[["_c1","_c2"]].sort_values("_c2")
    parcial_0["_c2"] = parcial_0["_c2"].astype(str)
    resultado = parcial_0.groupby(["_c1"], as_index = False).aggregate({"_c2": ":".join})
    resultado.set_index("_c1", inplace = True)
    return resultado


def pregunta_11():
    resultado = tbl1.groupby("_c0")["_c4"].apply(lambda x: ",".join(sorted(x))).reset_index()
    resultado.columns = ["_c0", "_c4"]
    return resultado


def pregunta_12():
    tbl2['_c5'] = tbl2['_c5a'] + ':' + tbl2['_c5b'].astype(str)
    resultado = tbl2.groupby('_c0')['_c5'].apply(lambda x: ','.join(sorted(x))).reset_index()
    resultado['_c5'] = resultado['_c5'].astype(str)
    resultado.columns = ['_c0', '_c5']
    return resultado


def pregunta_13():
    union = pd.merge(tbl0, tbl2, on = "_c0")
    sumatoria = union.groupby("_c1")["_c5b"].sum()
    sumatoria.index.name = "_c1"
    sumatoria.name = "_c5b" 
    return sumatoria
