# 📡 RSS Feed - João Paulo Charleaux (Carta Capital)

Feed RSS automático dos artigos de **João Paulo Charleaux** publicados na **Carta Capital**.

## 🎯 O que é?

Este repositório gera automaticamente um feed RSS com os artigos mais recentes do colunista João Paulo Charleaux da Carta Capital. O feed é atualizado **diariamente** via GitHub Actions.

## 🔗 Link do RSS

Copie este link para adicionar ao seu leitor de RSS:

```
https://raw.githubusercontent.com/alefernandesrs-debug/carta-capital-rss-feed/main/feed.xml
```

## 📲 Como usar?

### Opção 1: No seu leitor RSS favorito
1. Abra seu aplicativo leitor de RSS (Feedly, Inoreader, etc.)
2. Clique em "Adicionar feed"
3. Cole o link acima
4. Pronto! Você receberá atualizações diárias

### Opção 2: No navegador
- Visite: [feed.xml](https://github.com/alefernandesrs-debug/carta-capital-rss-feed/blob/main/feed.xml)

## ⚙️ Como funciona?

- **Python Script** (`generate_rss.py`) - Faz web scraping da página do autor
- **GitHub Actions** - Executa o script automaticamente todos os dias às 8:00 AM (UTC)
- **feed.xml** - Arquivo RSS gerado com os artigos mais recentes

## 📅 Agendamento

O feed é atualizado **automaticamente** todos os dias às **8:00 AM (UTC)** (5:00 AM no horário de Brasília).

Para atualizar manualmente:
1. Vá para a aba **Actions** do repositório
2. Clique em **Gerar RSS Feed**
3. Clique em **Run workflow**

## 🛠️ Desenvolvimento Local

Se quiser executar o script localmente:

```bash
# Clone o repositório
git clone https://github.com/alefernandesrs-debug/carta-capital-rss-feed.git
cd carta-capital-rss-feed

# Instale as dependências
pip install -r requirements.txt

# Execute o script
python generate_rss.py
```

## 📝 Tecnologias

- **Python 3** - Linguagem de programação
- **BeautifulSoup** - Web scraping
- **Requests** - Cliente HTTP
- **GitHub Actions** - Automação

## ⚠️ Notas

- Este projeto usa web scraping, que depende da estrutura HTML do site
- Se a Carta Capital alterar o layout, o script pode precisar ser atualizado
- O feed inclui os 10 artigos mais recentes
- Atualizações podem levar alguns minutos para refletir

## 📧 Contato

Para dúvidas ou problemas, abra uma **Issue** no repositório.

---

**Última atualização:** Verifique o arquivo `feed.xml` para ver quando foi gerado pela última vez.
