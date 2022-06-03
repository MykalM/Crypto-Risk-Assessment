from pathlib import Path
import questionary
import fire
from  import 

def run_questions():
    user_name = questionary.text("What is your name?").ask()
    print(f"Hi {user_name}! Welcome to your personal crypto advisor! Lets get started with a few questions so I can make the best portfolio for you.")
    debt = questionary.text("What is your current amount of monthly debt?").ask()
    income = questionary.text("What is your total monthly income?").ask()
    investment_amount = questionary.text("What's your desired investment amount?").ask()
    investment_length = questionary.select("How long do you plan on holding your investment for?",
    choices=["short: < 1 year", "medium: 1-3 years", "long: > 3 years"]).ask()
    risk_level = questionary.select("Please select the risk category that best describes your investment goals?", 
    choices=["Low: I am willing to accept lower returns to minimize the risk of losing money.", 
    "Medium: I want moderate returns but I don't want to be exposed to high levels of risk.", 
    "High: I want to maximize my returns and I am comfortable with the risks."]).ask()
    if risk_level == "Low: I am willing to accept lower returns to minimize the risk of losing money.":
        print(risk_level)
    elif risk_level == "Medium: I want moderate returns but I don't want to be exposed to high levels of risk.":
        print(risk_level)
    else:     
        print(risk_level)

    # return user_name, debt, income, investment_amount, investment_length, risk_level

    

    
    
# def get_user_info():
#     """Prompt dialog to get the user's information.
#     Returns:
#         Returns the user's information.
#     """
#     user_name = str(user_name) 
#     debt = float(debt)
#     income = float(income)
#     investment_amount = float(investment_amount)
#     investment_length = str(investment_length)
#     risk_level = str(risk_level)

#     return user_name, debt, income, investment_amount, investment_length, risk_level
# get_user_info()

# def find_investment_portfolio(debt, income, investment_amount, investment_length, risk_level):
#     """Determine which portfolio is best for the user.
#     Portfolio criteria is based on:
#         - Risk Level
#         - Investment Length
#         - Investment Amount
#         - Debt to Income ratio (calculated)
#         - Cryptocurrencies Sharpe ratio & Standard deviation (calculated)
#     Args:
#         crypto_list (list): A list of crypto data.
#         credit_score (int): The user's current credit score.
#         debt (float): The user's total monthly debt payments.
#         income (float): The user's total monthly income.
#         investment_amount (float): The total amount invested.
#         investment_length (float): The estimated time holding the investment.
#         risk_level (str): The level of risk the user is willing to accept.
#     Returns:
#         Porfolio tailored to the users risk allocation. """




# def risk_selector():
#     risk_list = ["Low", "Medium", "High"]

#     return .choice(risk_list)

if __name__=='__main__':
    fire.Fire(run_questions)


''' 
user_low_risk_portfolio = investment_amount / low_risk_portfolio ()
medium_risk_portfolio = investment_amount /
high_risk_portfolio = investment_amount /
'''
