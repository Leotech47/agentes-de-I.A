# Script PowerShell: Integração Local com Agente de IA (Exemplo de automação administrativa)
# Ação: Mover arquivos de relatórios para pasta "Finalizados" com base no mês informado pelo agente

param (
    [string]$mesReferencia
)

# Caminho da pasta base (ajuste conforme necessário)
$origem = "C:\Documentos\Relatorios\Pendentes"
$destino = "C:\Documentos\Relatorios\Finalizados\$mesReferencia"

# Cria a pasta de destino se não existir
if (-not (Test-Path -Path $destino)) {
    New-Item -ItemType Directory -Path $destino | Out-Null
}

# Move arquivos com nome contendo o mês informado
Get-ChildItem -Path $origem -Filter "*$mesReferencia*.pdf" | ForEach-Object {
    Move-Item $_.FullName -Destination $destino -Force
}

Write-Output "Arquivos de $mesReferencia foram movidos para a pasta Finalizados com sucesso."

# Possível integração:
# Este script pode ser chamado por um fluxo do Power Automate Desktop ou via comando do agente de IA Copilot usando HTTP request, PowerShell remoto ou via botão em Power Apps.
