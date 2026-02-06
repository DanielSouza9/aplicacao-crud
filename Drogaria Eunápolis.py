
import json
import os

DB = "data.json"


# -------- carregar / salvar --------
def carregar():
    if not os.path.exists(DB):
        return []
    with open(DB, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []


def salvar(lista):
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)


# -------- operações CRUD (lista + dicionários) --------
def listar(lista):
    if not lista:
        print("Nenhum registro.")
        return
    for item in lista:
        print(f"id={item['id']} | nome={item.get('nome')} | email={item.get('email')}")


def criar(lista, nome, email):
    novo_id = len(lista) + 1  # Forma 1: simples e didática
    item = {"id": novo_id, "nome": nome, "email": email}
    lista.append(item)
    salvar(lista)
    return item


def ler(lista, item_id):
    return next((i for i in lista if i["id"] == item_id), None)


def atualizar(lista, item_id, nome=None, email=None):
    for item in lista:
        if item["id"] == item_id:
            if nome:
                item["nome"] = nome
            if email:
                item["email"] = email
            salvar(lista)
            return item
    return None


def deletar(lista, item_id):
    for item in lista:
        if item["id"] == item_id:
            lista.remove(item)
            salvar(lista)
            return True
    return False


# ------------------ menu ------------------
def menu():
    lista = carregar()
    while True:
        print("\n=== CLIENTE PRIME DA DROGARIA EUNÁPOLIS ===")
        print("\n=== SEJA BEM-VINDO/A! ===")
        print("\n=== Com o cadastro Cliente Prime, você tem acesso a descontos exclusivos e concorre a Prêmios todos os meses! ===")
        print('\nO que você deseja?')
        print("1 - Listar Clientes")
        print("2 - Fazer Cadastro Prime")
        print("3 - Buscar Cliente por ID")
        print("4 - Atualizar Cadastro")
        print("5 - Excluir Cadastro")
        print("0 - Sair")
        op = input("> ").strip()

        if op == "1":
            listar(lista)

        elif op == "2":
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            while not nome or not email:
                print("Nome e email são obrigatórios.")
                nome = input("Nome: ").strip()
                email = input("Email: ").strip()
                continue
            criado = criar(lista, nome, email)
            print("Criado:", criado)

        elif op == "3":
            try:
                item_id = int(input("ID: ").strip())
            except ValueError:
                print("ID inválido. OBS.: Se não sabe o ID, reinicie e digite 1 para ver o ID.")
                continue
            except TypeError:
                print('Você não digitou um número inteiro.')
                continue
            print(ler(lista, item_id) or "ID não encontrado.")

        elif op == "4":
            try:
                item_id = int(input("ID: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            except TypeError:
                print('Você não digitou um número inteiro.')
                continue
            nome = input("Novo nome (Enter para manter): ").strip()
            email = input("Novo email (Enter para manter): ").strip()
            resultado = atualizar(lista, item_id, nome or None, email or None)
            print(resultado or "ID não encontrado.")

        elif op == "5":
            try:
                item_id = int(input("ID: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            print("Excluído." if deletar(lista, item_id) else "ID não encontrado.")

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
