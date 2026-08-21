import json
import ijson

entrada_dados = "vacinas_dados_reduzidos.json"  
arquivo_saida = "vacinas_vfa_filtradas.json"

CO_VACINA_ALVO = "14"
SG_IMUNOBIOLOGICO_ALVO = "VFA"

contador_vfa = 0

with open(entrada_dados, "rb") as f_entrada, open(arquivo_saida, "w", encoding="utf-8") as f_saida:
    
    f_saida.write("[\n")
    
    objetos = ijson.items(f_entrada, "item")
    
    for obj in objetos:
        if str(obj.get("co_vacina")) == CO_VACINA_ALVO and obj.get("sg_imunobiologico") == SG_IMUNOBIOLOGICO_ALVO:
            
            if contador_vfa > 0:
                f_saida.write(",\n") 

            registro_final = {
                "co_vacina": obj.get("co_vacina"),
                "sg_imunobiologico": obj.get("sg_imunobiologico"),
                "no_uf_paciente": obj.get("no_uf_paciente"),
                "no_uf_estabelecimento": obj.get("no_uf_estabelecimento")
            }
            
            json.dump(registro_final, f_saida, ensure_ascii=False)
            contador_vfa += 1

    f_saida.write("\n]")

print("\n" + "="*40)
print(f"total de dados encontrados: {contador_vfa}")
print(f"salvos em: '{arquivo_saida}'")
print("="*40)
