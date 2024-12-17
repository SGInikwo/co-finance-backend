import datetime
from datetime import datetime, timedelta

def date_transform(date, type):
  if type == "Revolut":
    excel_start_date = datetime(1899, 12, 30)
    delta = timedelta(days=date)
    full_date = excel_start_date + delta

    parsed_date = datetime.strptime(str(full_date), "%Y-%m-%d %H:%M:%S")
    date = parsed_date.strftime("%Y-%m-%d")
    return date
  
  if type == "Ing":
    date_input = date

    parsed_date = datetime.strptime(str(date_input), "%Y%m%d")

    date = parsed_date.strftime("%Y-%m-%d")
    return date

def amount_transform(amount_plus, min_credit, type):
  if type == "Shinha":
    if amount_plus == 0 or amount_plus == None:
      amount = f"-{min_credit}"
      return amount
    else:
      return f"{amount_plus}"
  
  if type == "Ing":
    if min_credit == "credit":
      amount = f"-{min_credit}"
      return amount
    else:
      return f"{amount_plus}"
  

def is_valid_date(date_string: str) -> bool:
    try:
        # Attempt to parse the date string with the specified format
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        # If parsing fails, the format is incorrect
        return False
    
def get_currency(data):
  currency = {"Euros": 1, "Won": 2, "KES": 3, "GBP":4}

  return currency[data]