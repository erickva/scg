import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# Configuração da figura
plt.figure(figsize=(12, 10))
plt.title('Cronograma de Implementação - Website Camila Golin', fontsize=16, pad=20)

# Definir data de início do projeto
start_date = datetime.now()

# Definir as fases e tarefas
phases = {
    'Fase 1: Melhorias de Alto Impacto (1-2 meses)': {
        'Calculadora de frete': {'start': 0, 'duration': 14, 'priority': 'Alta'},
        'Informações de prazo de entrega': {'start': 7, 'duration': 7, 'priority': 'Alta'},
        'Disponibilidade de estoque': {'start': 14, 'duration': 14, 'priority': 'Alta'},
        'Métodos de pagamento aceitos': {'start': 0, 'duration': 7, 'priority': 'Alta'},
        'Otimização de meta tags': {'start': 0, 'duration': 7, 'priority': 'Alta'},
        'Implementação do Google Analytics': {'start': 7, 'duration': 7, 'priority': 'Alta'},
        'Depoimentos de clientes': {'start': 21, 'duration': 14, 'priority': 'Alta'},
        'Selos de segurança': {'start': 28, 'duration': 7, 'priority': 'Alta'},
        'Política de privacidade LGPD': {'start': 35, 'duration': 14, 'priority': 'Alta'},
        'FAQ - Perguntas frequentes': {'start': 42, 'duration': 14, 'priority': 'Média'}
    },
    'Fase 2: Melhorias de Médio Impacto (3-4 meses)': {
        'Campo de busca': {'start': 60, 'duration': 21, 'priority': 'Alta'},
        'Filtros de produtos': {'start': 81, 'duration': 21, 'priority': 'Alta'},
        'CTAs mais persuasivos': {'start': 60, 'duration': 14, 'priority': 'Alta'},
        'Pop-up de captura de e-mail': {'start': 74, 'duration': 14, 'priority': 'Alta'},
        'Textos persuasivos para produtos': {'start': 88, 'duration': 21, 'priority': 'Alta'},
        'Formulário de contato na página inicial': {'start': 102, 'duration': 7, 'priority': 'Média'},
        'Cross-selling de produtos': {'start': 109, 'duration': 14, 'priority': 'Média'},
        'Conteúdo sobre processo de criação': {'start': 123, 'duration': 14, 'priority': 'Média'}
    },
    'Fase 3: Melhorias Avançadas (5-6 meses)': {
        'Visualização 360° dos produtos': {'start': 150, 'duration': 30, 'priority': 'Alta'},
        'Sistema de recomendação': {'start': 180, 'duration': 30, 'priority': 'Alta'},
        'Chat online': {'start': 150, 'duration': 21, 'priority': 'Alta'},
        'Feed do Instagram no site': {'start': 171, 'duration': 14, 'priority': 'Média'},
        'Teste e otimização mobile': {'start': 185, 'duration': 21, 'priority': 'Alta'},
        'Programa de fidelidade': {'start': 206, 'duration': 30, 'priority': 'Média'},
        'Recursos de acessibilidade': {'start': 206, 'duration': 21, 'priority': 'Média'},
        'Testes A/B': {'start': 227, 'duration': 30, 'priority': 'Média'}
    }
}

# Definir cores por prioridade
colors = {
    'Alta': '#FF5733',  # Vermelho
    'Média': '#33A8FF',  # Azul
    'Baixa': '#33FF57'   # Verde
}

# Preparar dados para o gráfico
y_labels = []
y_positions = []
starts = []
durations = []
colors_list = []
phase_separators = []

current_y = 0
for phase, tasks in phases.items():
    phase_start_y = current_y
    for task, details in tasks.items():
        y_labels.append(task)
        y_positions.append(current_y)
        starts.append(start_date + timedelta(days=details['start']))
        durations.append(timedelta(days=details['duration']))
        colors_list.append(colors[details['priority']])
        current_y += 1
    phase_separators.append((phase, phase_start_y, current_y - 0.5))
    current_y += 1  # Espaço entre fases

# Criar o gráfico de Gantt
ax = plt.gca()
for i, (start, duration) in enumerate(zip(starts, durations)):
    ax.barh(y_positions[i], duration, left=start, height=0.5, 
            color=colors_list[i], alpha=0.8, edgecolor='black', linewidth=0.5)
    # Adicionar texto de duração
    days_text = f"{duration.days} dias"
    text_x = start + duration / 2
    ax.text(text_x, y_positions[i], days_text, ha='center', va='center', color='black', fontsize=8)

# Configurar eixos
ax.set_yticks(y_positions)
ax.set_yticklabels(y_labels)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
plt.xticks(rotation=45)

# Adicionar linhas e rótulos de fase
for phase_info in phase_separators:
    phase_name, start_y, end_y = phase_info
    mid_y = (start_y + end_y) / 2
    ax.axhline(y=end_y + 0.25, color='gray', linestyle='-', alpha=0.3)
    ax.text(start_date - timedelta(days=5), mid_y, phase_name, ha='right', va='center', 
            fontsize=10, fontweight='bold')

# Adicionar legenda de prioridade
priority_patches = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors.values()]
plt.legend(priority_patches, colors.keys(), title="Prioridade", loc='upper right')

# Configurar limites e grade
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.subplots_adjust(left=0.3)

# Salvar o gráfico
plt.savefig('/home/ubuntu/roadmap_implementation/gantt_chart.png', dpi=300, bbox_inches='tight')
plt.close()

print("Gráfico de Gantt criado com sucesso em /home/ubuntu/roadmap_implementation/gantt_chart.png")
