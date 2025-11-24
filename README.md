# 🔍 Agente de Análise de Complexidade Ciclomática (Python)

## ✅ Descrição do Projeto
Este projeto implementa um agente capaz de analisar a complexidade ciclomática de funções Python utilizando exclusivamente um script interpretado via Azure Foundry. O agente recebe uma função como texto, executa o cálculo através do script definido e retorna o valor da complexidade, acompanhado de classificação, impactos técnicos e recomendações de melhoria.

## 🎯 Objetivo do Agente
- Garantir uma análise objetiva e padronizada da complexidade ciclomática.
- Validar riscos relacionados a manutenibilidade, testabilidade e bugs.
- Auxiliar times de desenvolvimento na tomada de decisão sobre refatoração.
- Automatizar análises em pipelines, fluxos e integrações (ex: Power Automate).

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
### ✅ Interação inicial com o agente

### ✅ Exemplo de Entrada
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

### ✅ Resposta Final do Agente
### ✅ Fluxo de Execução (Diagrama)


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


