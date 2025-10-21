
# BankAccount
class BankAccount:
    def __init__(self, balance=0, username="", password=""):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Action impossible : compte non authentifié")
        if amount <= 0:
            raise ValueError("Le dépôt doit être un montant positif")
        self.balance += amount
        print(f"{amount} a été déposé. Nouveau solde : {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Action impossible : compte non authentifié")
        if amount <= 0:
            raise ValueError("Le retrait doit être un montant positif")
        self.balance -= amount
        print(f"{amount} a été retiré. Nouveau solde : {self.balance}")

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"{self.username} est maintenant authentifié")
        else:
            print("Nom d'utilisateur ou mot de passe incorrect")


# Partie II : MinimumBalanceAccount
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, username="", password="", minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Action impossible : compte non authentifié")
        if amount <= 0:
            raise ValueError("Le retrait doit être un montant positif")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Solde insuffisant pour respecter le solde minimum")
        self.balance -= amount
        print(f"{amount} a été retiré. Nouveau solde : {self.balance}")





# Partie IV : ATM
class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(acc, BankAccount) for acc in account_list):
            raise ValueError("account_list doit contenir uniquement des instances de BankAccount ou MinimumBalanceAccount")
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("try_limit invalide, définition sur 2")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- Menu principal ---")
            print("1. Connexion")
            print("2. Sortie")
            choice = input("Choisissez une option: ")
            if choice == "1":
                username = input("Nom d'utilisateur: ")
                password = input("Mot de passe: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Au revoir !")
                break
            else:
                print("Option invalide")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.username == username and account.password == password:
                account.authenticate(username, password)
                self.show_account_menu(account)
                return
        self.current_tries += 1
        print(f"Échec de l'authentification ({self.current_tries}/{self.try_limit})")
        if self.current_tries >= self.try_limit:
            print("Nombre maximal d'essais atteint. Arrêt du programme.")
            exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Menu du compte {account.username} ---")
            print("1. Déposer")
            print("2. Retirer")
            print("3. Voir solde")
            print("4. Sortie")
            choice = input("Choisissez une option: ")
            try:
                if choice == "1":
                    amount = float(input("Montant à déposer: "))
                    account.deposit(amount)
                elif choice == "2":
                    amount = float(input("Montant à retirer: "))
                    account.withdraw(amount)
                elif choice == "3":
                    print(f"Solde actuel : {account.balance}")
                elif choice == "4":
                    print("Retour au menu principal")
                    break
                else:
                    print("Option invalide")
            except Exception as e:
                print("Erreur:", e)
