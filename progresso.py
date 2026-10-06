import time
import sys

# --- CONFIGURAÇÕES ---
valor_final = 100    # O limite da barra (100%)
largura_visual = 30  # Quantos blocos a barra terá no total (deixa ela maior e mais bonita)

print("\n🚀 Preparando download do sistema...")
time.sleep(1) # Pequena pausa para dar efeito dramático

# O loop que faz a barra "encher"
for i in range(0, valor_final + 1, 2): # Pula de 2 em 2 para a animação ser mais suave

    # 1. LÓGICA PARA ENCHER A BARRA:
    # Calculamos quantos blocos devem estar preenchidos agora
    # (Largura total * porcentagem atual / porcentagem final)
    preenchido = int(largura_visual * i / valor_final)

    # Criamos a barra: blocos cheios '█' + blocos vazios '░'
    barra = "█" * preenchido + "░" * (largura_visual - preenchido)

    # 2. A MÁGICA DA ATUALIZAÇÃO:
    # \r faz o cursor voltar ao início da linha
    # f-string monta o texto com a barra e a porcentagem
    sys.stdout.write(f"\rCarregando: |{barra}| {i}%")

    # Força o terminal a mostrar o texto agora
    sys.stdout.flush()

    # Controla a velocidade da animação (quanto menor, mais rápido)
    time.sleep(0.05)

print("\n\n✅ Download concluído com sucesso! O sistema está pronto.")
