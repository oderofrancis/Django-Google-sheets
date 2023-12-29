import os
import gspread
from typing import List
from django.conf import settings
from decouple import config


def initialize_gspread() -> gspread.Client:
    """
    Initialize gspread client
    """
    gc = gspread.service_account_from_dict(get_credentials())

    return gc

def get_credentials() -> dict:
    """
    Get credentials from environment variables
    """
    # print(config("PRIVATE_KEY").replace("\\n", "\n"))
    return {
        "type": config("TYPE"),
        "project_id": config("PROJECT_ID"),
        "private_key_id": config("PRIVATE_KEY_ID"),
        "private_key": config("PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": config("CLIENT_EMAIL"),
        "client_id": config("CLIENT_ID"),
        "auth_uri": config("AUTH_URI"),
        "token_uri": config("TOKEN_URI"),
        "auth_provider_x509_cert_url": config("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": config("CLIENT_X509_CERT_URL"),
        }

def get_all_rows(doc_name: str, sheet_name: str = None) -> List[dict]:
  """
  Fetches all rows from a given Google Sheet worksheet.
  """
  sh = settings.GSPREAD_CLIENT.open(doc_name)
  worksheet = sh.worksheet[sheet_name] if sheet_name else sh.get_worksheet(0)
  return worksheet.get_all_records()
