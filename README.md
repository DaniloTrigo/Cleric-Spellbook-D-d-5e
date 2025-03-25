# Cleric Spellbook 📖✨  

Cleric Spellbook é um projeto Python que utiliza a API **D&D 5e** para obter e exibir todas as magias disponíveis para a classe **Clérigo** no sistema de RPG *Dungeons & Dragons 5ª Edição*.  

## 🎯 Motivação  

Sempre que eu jogava de Clérigo, acabava perdendo tempo procurando as descrições das magias no *Livro do Jogador*, usando **Ctrl + F** no PDF, o que às vezes resultava em muitas ocorrências e tornava a busca cansativa. Isso atrapalhava o ritmo da sessão, tanto para mim quanto para o mestre e os outros jogadores.  

Por isso, decidi criar este programa para **agilizar minhas consultas durante as sessões**, trazendo todas as informações das magias de forma prática e organizada. Agora, não tenho mais desculpa para esquecer os efeitos das magias ou demorar para encontrá-los!  

## 🔮 Sobre o Projeto  

Este programa acessa diretamente a API [D&D 5e](https://www.dnd5eapi.co/) para recuperar informações detalhadas sobre todas as magias do Clérigo, incluindo:  
- Nome da magia  
- Nível  
- Tempo de conjuração  
- Alcance  
- Componentes necessários (verbais, somáticos e materiais)  
- Duração  
- Se exige concentração  
- Efeitos adicionais ao conjurar em níveis superiores  

Os usuários podem visualizar a lista completa de magias ou buscar uma magia específica pelo nome.  

## ⚙️ Como Usar  

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/DaniloTrigo/cleric-spellbook.git  
   cd cleric-spellbook
   ```  
2. **Instale as dependências**  
   O projeto utiliza apenas a biblioteca `requests`, que pode ser instalada com:  
   ```bash
   pip install requests
   ```  
3. **Execute o programa**  
   ```bash
   python cleric_spellbook.py
   ```  
4. **Escolha uma opção no menu interativo**  
   - 📜 Listar todas as magias de Clérigo  
   - 🔎 Buscar uma magia pelo nome  
   - ❌ Sair do programa  

## 🔗 API Utilizada  
Este projeto consome dados da [D&D 5e API](https://www.dnd5eapi.co/), uma API pública que fornece informações sobre o sistema de regras da 5ª edição de *Dungeons & Dragons*.  

## 📌 Futuras Implementações  
- Melhorar a exibição das descrições das magias  
- Permitir filtros por nível de magia  
- Criar uma interface gráfica para facilitar a navegação  

