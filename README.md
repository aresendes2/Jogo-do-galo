# 🐓 Jogo do Galo - Documentação Completa

## 📋 Índice
1. [Descrição do Projeto](#descrição-do-projeto)
2. [Funcionalidades Implementadas](#funcionalidades-implementadas)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Requisitos](#requisitos)
5. [Como Executar](#como-executar)
6. [Alterações Realizadas](#alterações-realizadas)
7. [Detalhes Técnicos](#detalhes-técnicos)

---

## 📝 Descrição do Projeto

Este é um **Jogo do Galo (Tic-Tac-Toe)** completo desenvolvido em Python usando Tkinter, com interface gráfica temática e dois modos de jogo: **Singleplayer** (contra IA) e **Multiplayer** (2 jogadores).

O jogo utiliza imagens personalizadas (ovo e galinha) em vez dos tradicionais X e O, e inclui ecrãs de vitória/derrota inspirados no estilo GTA.

---

## ✨ Funcionalidades Implementadas

### 🎮 Modos de Jogo

1. **Singleplayer (vs IA)**
   - Jogador controla o **Ovo** (X)
   - IA controla a **Galinha** (O)
   - IA inteligente que tenta ganhar e bloqueia jogadas do jogador
   - Ecrãs de vitória ("Mission Passed!") e derrota ("WASTED") após 3 segundos

2. **Multiplayer (2 Jogadores)**
   - Um jogador controla o **Ovo** (X)
   - Outro jogador controla a **Galinha** (O)
   - Alternância automática de turnos
   - Mensagens de vitória personalizadas

### 🎨 Interface Gráfica

- **Menu Principal**: Ecrã inicial com opções de modo de jogo
- **Tabuleiro**: 9 botões clicáveis com fundo preto
- **Imagens Personalizadas**:
  - Ovo (`jogo (1).png`) representa X
  - Galinha (`jogo.png`) representa O
- **Status do Jogo**: Mostra "Vez do Ovo" ou "Vez da Galinha"
- **Ecrãs de Resultado**:
  - Vitória: `5.png` (Mission Passed!)
  - Derrota: `4.png` (WASTED)
  - Empate: Apenas mensagem de texto (sem imagem)

### 🎯 Funcionalidades Adicionais

- **Botão RESTART**: Reinicia o jogo mantendo o mesmo modo
- **Botão Menu Principal**: Volta ao menu inicial
- **Deteção Automática**: Vitória, derrota e empate
- **Bloqueio de Jogadas**: Impede cliques após o jogo terminar
- **Delay Visual**: 3 segundos antes de mostrar ecrã de vitória/derrota

---

## 📁 Estrutura do Projeto

```
jogo do galo/
├── main.py              # Ficheiro principal (menu inicial)
├── main2.py            # Versão alternativa do menu
├── game2.py            # Lógica do jogo e interface
├── run_game.py         # Script de lançamento automático
├── run.sh              # Script shell alternativo
├── README.md           # Este documento
├── COMO_EXECUTAR.txt   # Instruções rápidas
├── INSTRUÇÕES.txt     # Instruções originais
└── assets/             # Pasta de recursos
    ├── 1.png          # Background adicional
    ├── 2.png          # Background do menu principal
    ├── 3.png          # Background do tabuleiro
    ├── 4.png          # Ecrã de derrota (WASTED)
    ├── 5.png          # Ecrã de vitória (Mission Passed!)
    ├── jogo (1).png   # Imagem do ovo (X)
    ├── jogo.png       # Imagem da galinha (O)
    ├── single.png     # Botão singleplayer
    └── two.png        # Botão multiplayer
```

---

## 🔧 Requisitos

### Software Necessário

- **Python 3.x** (testado com Python 3.14.2)
- **Tkinter** (geralmente incluído com Python)
- **Pillow (PIL)** - Para processamento de imagens

### Instalação de Dependências

```bash
pip3 install Pillow
```

**Nota**: No macOS, pode ser necessário usar `/usr/local/bin/python3` em vez do Python do sistema.

---

## 🚀 Como Executar

### Método 1: Script Automático (Recomendado)

```bash
python3 run_game.py
```

ou

```bash
./run_game.py
```

### Método 2: Script Shell

```bash
./run.sh
```

### Método 3: Execução Direta

```bash
/usr/local/bin/python3 main.py
```

ou

```bash
python3 main.py
```

**⚠️ Importante**: Se usar `/usr/bin/python3` e der erro, use `/usr/local/bin/python3` que tem Tkinter funcional.

---

## 🔄 Alterações Realizadas

### 1. Correção de Paths
- ✅ Removidos paths absolutos do Windows (`C:/Users/...`)
- ✅ Implementados paths relativos compatíveis com macOS/Linux
- ✅ Função `asset_path()` para gestão centralizada de recursos

### 2. Implementação da Lógica do Jogo
- ✅ Sistema de tabuleiro com 9 casas
- ✅ Alternância de turnos (X/O)
- ✅ Deteção de vitória (8 combinações possíveis)
- ✅ Deteção de empate
- ✅ Bloqueio de jogadas após fim do jogo

### 3. Sistema de IA (Singleplayer)
- ✅ Algoritmo inteligente com prioridades:
  1. Tentar ganhar se possível
  2. Bloquear vitória do jogador
  3. Jogar no centro
  4. Jogar nos cantos
  5. Jogar nos lados
- ✅ Delay de 250ms para parecer mais "humano"

### 4. Interface Gráfica
- ✅ Menu principal com 2 modos de jogo
- ✅ Tabuleiro com 9 botões clicáveis
- ✅ Botões com fundo preto
- ✅ Status do jogo ("Vez do Ovo" / "Vez da Galinha")
- ✅ Fundo preto no status no modo multiplayer

### 5. Imagens Personalizadas
- ✅ Ovo (`jogo (1).png`) para X
- ✅ Galinha (`jogo.png`) para O
- ✅ Redimensionamento automático para 50x50 pixels
- ✅ Ecrãs de vitória/derrota (600x450 pixels)

### 6. Ecrãs de Resultado
- ✅ Vitória: Mostra `5.png` após 3 segundos
- ✅ Derrota: Mostra `4.png` após 3 segundos
- ✅ Empate: Apenas mensagem (sem imagem)
- ✅ Delay configurável (atualmente 3 segundos)

### 7. Navegação
- ✅ Botão RESTART funcional em todos os modos
- ✅ Botão Menu Principal para voltar ao menu
- ✅ Botões sempre visíveis (mesmo sobre imagens de resultado)
- ✅ Fechar janela também volta ao menu

### 8. Textos Personalizados
- ✅ "Vez do X" → "Vez do Ovo"
- ✅ "Vez do O" → "Vez da Galinha"
- ✅ Mensagens de vitória personalizadas

### 9. Correções Técnicas
- ✅ Resolução de problemas com Tkinter no macOS
- ✅ Script de lançamento que detecta Python correto
- ✅ Gestão de memória para imagens (guardadas no objeto game)

---

## 🔍 Detalhes Técnicos

### Estrutura do Código

#### `main.py`
- Cria a janela principal (menu)
- Carrega background e botões de modo
- Chama `open_game()` quando um modo é selecionado

#### `game2.py`
- **Função `open_game()`**: Cria janela de jogo e inicializa tudo
- **Função `_winner()`**: Verifica se há vencedor
- **Função `_best_ai_move()`**: Calcula melhor jogada da IA
- **Função `update_button()`**: Atualiza visual dos botões
- **Função `check_end()`**: Verifica fim do jogo
- **Função `restart()`**: Reinicia o jogo
- **Função `back_to_menu()`**: Volta ao menu principal

### Combinações de Vitória

O jogo verifica 8 combinações possíveis:
- 3 horizontais: (0,1,2), (3,4,5), (6,7,8)
- 3 verticais: (0,3,6), (1,4,7), (2,5,8)
- 2 diagonais: (0,4,8), (2,4,6)

### Sistema de Coordenadas

Os botões estão posicionados em:
```
(170, 90)  (280, 90)  (390, 90)
(170, 200) (280, 200) (390, 200)
(170, 310) (280, 310) (390, 310)
```

### Gestão de Estado

- `board`: Lista de 9 elementos representando o tabuleiro
- `current`: Jogador atual ("X" ou "O")
- `finished`: Flag indicando se o jogo terminou
- `mode`: Modo de jogo ("single" ou "two")

---

## 🐛 Resolução de Problemas

### Erro: "ModuleNotFoundError: No module named 'PIL'"
**Solução**: Instalar Pillow:
```bash
pip3 install Pillow
```

### Erro: "macOS 26 (2601) or later required"
**Solução**: Usar `/usr/local/bin/python3` em vez de `/usr/bin/python3`

### Botões não aparecem ou não são clicáveis
**Solução**: Verificar se as imagens estão na pasta `assets/` e se os paths estão corretos

### Imagens muito grandes ou pequenas
**Solução**: O código redimensiona automaticamente, mas pode ajustar os valores em `game2.py`:
- Botões: linha ~84-89 (50x50)
- Ecrãs: linha ~92-97 (600x450)

---

## 📝 Notas de Desenvolvimento

- O código foi desenvolvido para ser compatível com macOS, mas funciona em Windows e Linux
- As imagens são redimensionadas automaticamente usando Pillow
- O sistema de IA usa um algoritmo minimax simplificado
- Todos os textos estão em português
- O jogo mantém compatibilidade com Python 3.9+

---

## 👨‍💻 Autor

Resendes.

---

## 📄 Licença

Este projeto é fornecido "como está" para fins educacionais e de entretenimento.

---

**Última atualização**: Janeiro 2026
