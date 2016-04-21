# -*- coding: utf-8 -*-


ACCOUNT_TYPE = {
    1: 'TYPE_CHECKING',
    2: 'TYPE_SAVINGS',
    3: 'TYPE_DEPOSIT',
    4: 'TYPE_MARKET',
    5: 'TYPE_LIFE_INSURANCE',
    6: 'TYPE_LIFE_INSURANCE',
    8: 'TYPE_LOAN',
    9: 'TYPE_LOAN',
}

TRANSACTION_TYPE = {
    1:  'TYPE_CHECK', # Chèque émis
    2:  'TYPE_CHECK', # Chèque reçu
    3:  'TYPE_CASH_DEPOSIT', # Versement espèces
    4:  'TYPE_ORDER', # Virements reçus
    5:  'TYPE_ORDER', # Virements émis
    6:  'TYPE_LOAN_PAYMENT', # Prélèvements / amortissements prêts
    7:  'TYPE_CARD', # Paiements carte,
    8:  'TYPE_CARD', # Carte / Formule BNP Net,
    9:  'TYPE_UNKNOWN',  # Opérations Titres
    10: 'TYPE_UNKNOWN',  # Effets de Commerce
    11: 'TYPE_WITHDRAWAL', # Retraits d'espèces carte
    12: 'TYPE_UNKNOWN', # Opérations avec l'étranger
    13: 'TYPE_CARD', # Remises Carte
    14: 'TYPE_WITHDRAWAL', # Retraits guichets
    15: 'TYPE_BANK', # Intérêts/frais et commissions
    16: 'TYPE_UNKNOWN', # Tercéo
    30: 'TYPE_UNKNOWN', # Divers
}

COMING_TYPE = {
    2: 'TYPE_ORDER', # Prélèvement
    3: 'TYPE_CHECK', # Chèque
    4: 'TYPE_CARD', # Opération carte
}


def set_account_type(number):
	return ACCOUNT_TYPE[number]

def set_transaction_type(number):
	return TRANSACTION_TYPE[number]

def set_coming_type(number):
	return COMING_TYPE[number]