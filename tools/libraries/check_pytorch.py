import torch

def check_versions(): 
    # Verifica se há uma GPU disponível
    gpu_disponivel = torch.cuda.is_available()

    # Imprime a versão do PyTorch
    versao_pytorch = torch.__version__

    print(f"Versão do PyTorch: {versao_pytorch}")
    print("GPU disponível:" if gpu_disponivel else "GPU não disponível.")

    if gpu_disponivel:
        # Informações sobre a GPU
        gpu_nome = torch.cuda.get_device_name(0)
        print(f"Nome da GPU: {gpu_nome}")
        print(f"Quantidade de GPUs disponíveis: {torch.cuda.device_count()}")

def teste_is_compiling():
    if torch.compiler.is_compiling():
        print("Estamos em modo de compilação.")
    else:
        print("Estamos em modo de execução normal.")


if __name__ == "__main__":
    # Verificando a versão do PyTorch e se há GPU disponível
    check_versions()

    # Verificando se estamos em modo de compilação
    # Chamando a função diretamente
    teste_is_compiling()

    # Compilando a função com torch.compile
    func_compilada = torch.compile(teste_is_compiling)
    func_compilada()
