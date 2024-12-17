from pydantic import BaseModel, Field
from typing import Optional, Union, List
from models.receive.transactions import Transactions_ing, Transactions_revolut, Transactions_shinha
import secrets

from models.send.helper_functions.transaction_data import amount_transform, date_transform, get_currency, is_valid_date

def get_insert_data(requests: Union[List[Transactions_ing], List[Transactions_revolut], List[Transactions_shinha]], user_data):
  data = []
  for request in requests:
    request_dict = dict(request)

    if isinstance(request, Transactions_ing):
        # print(request_dict)
        request_data = {
           "id": secrets.token_hex(8),
           "user_id": user_data[0],
           "date": date_transform(request_dict["date"], "Ing"),
           "recipient": request_dict["name"],
           "currency": int(user_data[1]),
           "amount": amount_transform(request_dict["amount"], request_dict["debit_credit"], "Ing"),
           "transaction_type": request_dict["transaction_type"],
           "transaction_details": request_dict["notification"],
           "icon": 0,
           "user_currency": int(user_data[1]),
           "balance": str(request_dict["balance"])
        }
        data.append(request_data)
        # print("Using Transactions_ing")
    elif isinstance(request, Transactions_revolut):
        # print(request_dict)
        request_data = {
           "id": secrets.token_hex(8),
           "user_id": user_data[0],
           "date": date_transform(request_dict["start_date"], "Revolut"),
           "recipient": request_dict["description"],
           "currency": get_currency(request_dict["currency"]),
           "amount": str(request_dict["amount"]),
           "transaction_type": request_dict["type"],
           "transaction_details": request_dict["description"],
           "icon": 0,
           "user_currency": int(user_data[1]),
           "balance": str(request_dict["balance"])
        }
        data.append(request_data)
        # print("Using Transactions_revolut")
    elif isinstance(request, Transactions_shinha):
        # print(request_dict)
        if is_valid_date(request_dict["date"]):
          request_data = {
            "id": secrets.token_hex(8),
            "user_id": user_data[0],
            "date": request_dict["date"],
            "recipient": request_dict["recipient"],
            "currency": int(user_data[1]),
            "amount": amount_transform(request_dict["withdrawal"], request_dict["deposit"], "Shinha"),
            "transaction_type": request_dict["transaction_place"],
            "transaction_details": request_dict["description"],
            "icon": 0,
            "user_currency": int(user_data[1]),
            "balance": str(request_dict["balance"])
          }
          data.append(request_data)
        # print("Using Transactions_shinha")
    else:
        print("Unknown type")

  return data

class Transactions(BaseModel):
  id: str
  user_id: str
  date: str
  recipient: str
  currency: int
  amount: str
  transaction_type: str
  transaction_details: str
  icon: int
  user_currency: int
  balance: str

class TransactionResponse(BaseModel):
  transactionList: list[Transactions]