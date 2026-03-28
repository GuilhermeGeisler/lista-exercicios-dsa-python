# 🧮 Fundamentos de Python com NumPy - Lista 3 de Exercícios (DSA)

## 🌟 Sobre o Projeto  
Lista de exercícios do curso **"Fundamentos de Linguagem Python - Do Básico a Aplicações de IA"** da **Data Science Academy**, focada na biblioteca NumPy. Os exercícios abordam desde operações básicas com arrays até conceitos avançados como inversão de matrizes e resolução de sistemas lineares, com níveis de dificuldade progressivos (de “Nível Baby” a “Nível Ninja Pro Master das Galáxias Plus”).

- 🎯 10 exercícios com NumPy para manipulação de arrays, indexação, slicing, operações matriciais, normalização, substituição condicional e álgebra linear.
- 📊 Uso prático de funções como `reshape`, `arange`, `dot`, `linalg.inv`, `linalg.solve` e indexação booleana.
- 🚀 Exercícios organizados por níveis de dificuldade, ideais para fixar conceitos de álgebra linear aplicada.

---

## 🚀 Funcionalidades  

| **Exercício** | **Nível**                     | **Descrição**                                                                 | **Conceitos NumPy**                              |
|---------------|-------------------------------|-------------------------------------------------------------------------------|--------------------------------------------------|
| 1️⃣            | Baby                          | Selecionar a terceira coluna de uma matriz 4x4                               | Indexação `[:, 2]`                               |
| 2️⃣            | Aprendiz                      | Extrair o bloco central 2x2 de uma matriz 4x4                                | Slicing `[1:3, 1:3]`                             |
| 3️⃣            | Iniciante                     | Calcular o produto matricial entre duas matrizes                             | `@`, `np.dot`, `np.matmul`                       |
| 4️⃣            | Iniciante Plus                | Selecionar linhas pares e colunas ímpares de uma matriz 9x9                  | Indexação com `::2` e `1::2`                     |
| 5️⃣            | Pro                           | Adicionar valor 5 ao bloco central 2x2 de uma matriz 4x4 de zeros            | Atribuição em fatia (`[1:3, 1:3] += 5`)          |
| 6️⃣            | Master                        | Normalizar matriz (Z‑score)                                                  | Operações vetoriais, `np.min`, `np.max`          |
| 7️⃣            | Ninja                         | Substituir valores > 8 por -1 (cópia)                                        | Indexação booleana (`dados > 8`)                 |
| 8️⃣            | Ninja Pro Master              | Calcular a inversa de uma matriz 2x2 e verificar com a identidade            | `np.linalg.det`, `np.linalg.inv`                 |
| 9️⃣            | Ninja Pro Master das Galáxias | Resolver sistema linear 2x2                                                   | `np.linalg.solve`                                |
| 🔟            | Ninja Pro Master das Galáxias Plus | Extrair a borda de uma matriz 5x5 em sentido horário                        | Combinação de fatias e concatenação (`np.concatenate`) |

---

## 🛠️ Tecnologias Utilizadas  
<div align="center">  
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">  
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">  
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">  
</div>  

---

## 🔥 Destaques Técnicos

- **Indexação e Slicing Avançados:** Uso de `matriz[::2, 1::2]` para selecionar linhas pares e colunas ímpares; extração de borda combinando fatias.
- **Operações Matriciais:** Demonstração de três formas de multiplicação (`@`, `np.dot`, `np.matmul`) e suas diferenças.
- **Álgebra Linear com NumPy:** Cálculo de determinante, inversa e resolução de sistemas lineares (`np.linalg.solve`).
- **Indexação Booleana:** Substituição condicional em arrays sem necessidade de loops (`dados[dados > 8] = -1`).
- **Normalização Manual:** Aplicação da fórmula (X - min) / (max - min) para normalização min‑max (embora o enunciado peça Z‑score, a solução apresentada usa min‑max; importante notar a diferença).
- **Criação de Arrays:** Uso de `np.arange` e `reshape` para gerar matrizes de teste rapidamente.
- **Extração de Borda:** Técnica que combina fatias da primeira linha, última coluna, última linha invertida e primeira coluna invertida, concatenadas em um array 1D.

---

## 🧑‍💻 Desenvolvedor  
<img src="https://avatars.githubusercontent.com/u/53203780?s=400&u=9a85ac6d2d3c55a872ab0bafd1d38d8bd0da5cc4&v=4" width="100px;" alt="Foto do Guilherme Geisler"/><br> <sub><b>Guilherme Geisler</b></sub>

---

## 📧 Contato

Se tiver alguma dúvida, sugestão ou quiser entrar em contato, fique à vontade:  

- **LinkedIn**: [Guilherme Geisler](https://www.linkedin.com/in/guilhermegeisler/)  
- **Email**: [guilherme.sgeisler@gmail.com](mailto:guilherme.sgeisler@gmail.com)  

---

Feito com ❤️ por [Guilherme Geisler](https://www.linkedin.com/in/guilhermegeisler/) durante o curso da **Data Science Academy** 🐍
