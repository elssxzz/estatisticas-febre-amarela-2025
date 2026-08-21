import json
import ijson

entrada_dados = "vacinacao_jan_2025.json"  
arquivo_saida = "vacinas_dados_reduzidos.json"
contador = 0

with open(entrada_dados, "rb") as f_entrada, open(arquivo_saida, "w", encoding="utf-8") as f_saida:
    
    f_saida.write("[\n")
    
    objetos = ijson.items(f_entrada, "item")
    
    for obj in objetos:
        if contador > 0:
            f_saida.write(",\n") 
        
        registro_filtrado = {
            "co_vacina": obj.get("co_vacina"),
            "sg_imunobiologico": obj.get("sg_imunobiologico"),
            "no_uf_paciente": obj.get("no_uf_paciente"),
            "no_uf_estabelecimento": obj.get("no_uf_estabelecimento")
        }
        
        json.dump(registro_filtrado, f_saida, ensure_ascii=False)
        contador += 1
        
        if contador % 100000 == 0:
            print(f"-> {contador} dados já processados")

    f_saida.write("\n]")

print("\n" + "="*40)
print(f"total de dados processados: {contador}")
print(f"salvo em: '{arquivo_saida}'")
print("="*40)
