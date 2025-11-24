# 🔍 Agente de Análise de Complexidade Ciclomática (Python)

## ✅ Descrição do Projeto
Este projeto implementa um agente capaz de analisar a complexidade ciclomática de funções Python utilizando exclusivamente um script interpretado via Azure Foundry. O agente recebe uma função como texto, executa o cálculo através do script definido e retorna o valor da complexidade, acompanhado de classificação, impactos técnicos e recomendações de melhoria.

## 🎯 Objetivo do Agente
- Garantir uma análise objetiva e padronizada da complexidade ciclomática.
- Validar riscos relacionados a manutenibilidade, testabilidade e bugs.
- Auxiliar times de desenvolvimento na tomada de decisão sobre refatoração.
- Automatizar análises em pipelines, fluxos e integrações (ex: Power Automate).

---
## Instruções (prompt) fornecidas ao Agente:
```
Você é um agente que analisa complexidade ciclomática usando ONLY o script via intérprete.

Workflow:
1. Receber código (Python) como texto.
2. Enviar o código para a função calcular_complexidade_ciclomatica do script.
3. Executar via intérprete.
4. Retornar APENAS o valor calculado pelo script. Sem cálculos próprios.

Com base no valor retornado:
- Retornar complexidade
- Classificar: Baixa | Média | Alta | Crítica
- Impactos: Manutenibilidade, Testabilidade, Risco de bugs, Leitura/Onboarding
- Recomendações: Refatorar, reduzir aninhamento, extrair funções, simplificar lógica, melhorar nomes/modularização

```
---

## ⚙️ Funcionamento do Workflow

1. O agente recebe o código Python como texto.
2. O código é enviado como entrada para a função `calcular_complexidade_ciclomatica`.
3. O script é executado via action de intérprete no Azure Foundry.
4. O resultado numérico é retornado.
5. O agente gera:
   - Complexidade numérica
   - Classificação (Baixa/Média/Alta/Crítica)
   - Impactos técnicos
   - Recomendações práticas

---

## 🖥️ Prints de Respostas, Fluxo e Execução
### ✅ Script e Action
<img width="1101" height="694" alt="action-interprete-codigo" src="https://github.com/user-attachments/assets/e1519ff7-b33c-4e24-ad5c-ac8e7d32e80a" />

[complexidade_ciclomatica.py](https://github.com/marianapcorrea/Agente-de-Analise-de-Complexidade-Ciclomatica/blob/main/complexidade_ciclomatica.py)

### ✅ Interação inicial com o agente
<img width="1167" height="694" alt="interacao-inicial" src="https://github.com/user-attachments/assets/efcc1510-f71f-4535-8685-3b8948be2cf6" />

### ✅ Exemplo de Entrada
<img width="1169" height="699" alt="exemplo-entrada-funcao" src="https://github.com/user-attachments/assets/47d11d4c-0f07-4abb-b093-71ff7c686f42" />

```python
def filtrar_e_transformar(valores):        
    resultado = []        
    for v in valores:        
        if isinstance(v, int) or isinstance(v, float):        
            if v > 0:        
                if v % 2 == 0:        
                    resultado.append(v * 2)        
                else:        
                    acumulado = 1        
                    for i in range(1, int(v) + 1):        
                        if i % 3 == 0:        
                            acumulado += i        
                    resultado.append(acumulado)        
            else:        
                if v < -10:        
                    resultado.append(abs(v))        
                else:        
                    if v != 0:        
                        resultado.append(1 / v)        
    return resultado    
```
### ✅ Execução do Script
<img width="1164" height="707" alt="execucao_script" src="https://github.com/user-attachments/assets/3fd09fcb-937f-4e82-87ee-9100cba2507b" />

### ✅ Resposta Final do Agente
<img width="1182" height="716" alt="exemplo-resposta-final-agente" src="https://github.com/user-attachments/assets/52cb07b7-e3ec-476a-b0b2-2a3ca6a27492" />

### ✅ Fluxo de Execução (Diagrama)
<img width="1364" height="740" alt="fluxo-execucao" src="https://github.com/user-attachments/assets/1624045e-55e3-4cc2-a034-b8d04fde3dd2" />

## 🔗 Links e Referências

### 📌 Azure Foundry
- https://learn.microsoft.com/
- https://azure.microsoft.com/

### 📌 Power Automate
- https://learn.microsoft.com/power-automate/
- https://powerautomate.microsoft.com/

### 📌 Complexidade Ciclomática
- https://en.wikipedia.org/wiki/Cyclomatic_complexity
- https://martinfowler.com/bliki/CyclomaticComplexity.html

### 📌 Python
- https://www.python.org/doc/

---

## 🚀 Possíveis Extensões
- Integração com pipelines CI/CD  
- Relatórios automáticos de qualidade  
- Dashboard com evolução da complexidade  
- Análise de múltiplas funções por arquivo  

---

## 👥 Contribuição
Este projeto **não aceita contribuições externas**.

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**:

---

* Este **readme.md** e o arquivo **complexidade_ciclomatica.py** foram gerados com auxílio de IA



