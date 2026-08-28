#!/usr/bin/env python3
"""
Script para gerar RSS feed dos artigos de João Paulo Charleaux
da Carta Capital
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

# URL do autor na Carta Capital
AUTHOR_URL = "https://www.cartacapital.com.br/author/joao-paulo-charleaux/"

def fetch_articles():
    """Busca os artigos do autor na página"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(AUTHOR_URL, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []
        
        # Procura pelos artigos na página
        article_elements = soup.find_all('article')
        
        if not article_elements:
            # Tenta alternativa: procurar por div com classe específica
            article_elements = soup.find_all('div', class_='post')
        
        for article in article_elements[:10]:  # Limita a 10 artigos
            try:
                # Extrai informações
                title_elem = article.find(['h2', 'h3', 'a'])
                link_elem = article.find('a', href=True)
                date_elem = article.find(['time', 'span'], class_=['date', 'published'])
                description_elem = article.find(['p', 'div'], class_=['excerpt', 'summary'])
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    link = link_elem['href']
                    
                    # Garante URL absoluta
                    if not link.startswith('http'):
                        link = 'https://www.cartacapital.com.br' + link
                    
                    # Extrai data
                    pub_date = date_elem.get_text(strip=True) if date_elem else datetime.now().strftime('%a, %d %b %Y %H:%M:%S -0000')
                    
                    # Extrai descrição
                    description = description_elem.get_text(strip=True) if description_elem else "Leia o artigo completo"
                    
                    articles.append({
                        'title': title,
                        'link': link,
                        'pub_date': pub_date,
                        'description': description
                    })
            except Exception as e:
                print(f"Erro ao processar artigo: {e}")
                continue
        
        return articles
    
    except Exception as e:
        print(f"Erro ao buscar artigos: {e}")
        return []

def generate_rss(articles):
    """Gera o arquivo RSS"""
    
    rss = ET.Element('rss')
    rss.set('version', '2.0')
    rss.set('xmlns:content', 'http://purl.org/rss/1.0/modules/content/')
    
    channel = ET.SubElement(rss, 'channel')
    
    # Informações do canal
    ET.SubElement(channel, 'title').text = 'Artigos de João Paulo Charleaux - Carta Capital'
    ET.SubElement(channel, 'link').text = AUTHOR_URL
    ET.SubElement(channel, 'description').text = 'Feed RSS dos artigos do colunista João Paulo Charleaux na Carta Capital'
    ET.SubElement(channel, 'language').text = 'pt-br'
    ET.SubElement(channel, 'lastBuildDate').text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S -0000')
    
    # Adiciona os artigos
    for article in articles:
        item = ET.SubElement(channel, 'item')
        ET.SubElement(item, 'title').text = article['title']
        ET.SubElement(item, 'link').text = article['link']
        ET.SubElement(item, 'pubDate').text = article['pub_date']
        ET.SubElement(item, 'author').text = 'João Paulo Charleaux'
        ET.SubElement(item, 'description').text = article['description']
    
    # Formata o XML com indentação
    xml_str = minidom.parseString(ET.tostring(rss)).toprettyxml(indent='  ')
    
    # Remove linhas vazias
    xml_str = '\n'.join([line for line in xml_str.split('\n') if line.strip()])
    
    # Remove a primeira linha de declaração XML duplicada
    lines = xml_str.split('\n')
    if lines[0].startswith('<?xml'):
        xml_str = '\n'.join(lines[:1] + lines[2:])
    
    return xml_str

def main():
    """Função principal"""
    print("📡 Gerando RSS feed...")
    
    print("🔍 Buscando artigos de João Paulo Charleaux...")
    articles = fetch_articles()
    
    if articles:
        print(f"✅ Encontrados {len(articles)} artigos")
        
        rss_content = generate_rss(articles)
        
        # Salva o arquivo RSS
        with open('feed.xml', 'w', encoding='utf-8') as f:
            f.write(rss_content)
        
        print("✅ RSS feed gerado com sucesso: feed.xml")
    else:
        print("⚠️  Nenhum artigo encontrado. Verificando estrutura do site...")
        print("💡 O site pode ter mudado sua estrutura HTML.")

if __name__ == '__main__':
    main()
