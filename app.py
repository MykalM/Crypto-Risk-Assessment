from pathlib import Path
import questionary
import numpy as np
import fire
# import voila
#from Database.ipynb import x
from Database.py import ETH_variance
#from IPython.display import display


# Portfolio Distribution
low_risk_portfolio = { 'NEO' : .15, 'VERGE' : .15, 'TRON' : .20, 'ADA' : .25, 'XMR' : .25 }
med_risk_portfolio = { 'TRON' : .25, 'BNB' : .25, 'XRP' : .25, 'XMR' : .25 }
high_risk_portfolio = { 'BTT' : .20, 'TRON' : .40, 'BNB' : .40 }

# CLI for asking asking the user questions
def run_questions():
    user_name = questionary.text("What is your name?").ask()
    print(f"Hi {user_name}! Welcome to your personal crypto advisor! Lets get started with a few questions so I can make the best portfolio for you.")
    debt = questionary.text("What is your current amount of monthly debt?").ask()
    income = questionary.text("What is your total monthly income?").ask()
    investment_amount = questionary.text("What's your desired investment amount?").ask()
    # return(investment_amount)
    investment_length = questionary.select("How long do you plan on holding your investment for?",
    choices=["short: < 1 year", "medium: 1-3 years", "long: > 3 years"]).ask()
    risk_level = questionary.select("Please select the risk category that best describes your investment goals?", 
    choices=["Low: I am willing to accept lower returns to minimize the risk of losing money.", 
    "Medium: I want moderate returns but I don't want to be exposed to high levels of risk.", 
    "High: I want to maximize my returns and I am comfortable with the risks.\n"]).ask()
    if risk_level == "Low: I am willing to accept lower returns to minimize the risk of losing money.\n":
        for key in low_risk_portfolio:
            low_risk_portfolio [key] *=int(investment_amount)
            portfolio_risk = 'low'
        return low_risk_portfolio,portfolio_risk 
    elif risk_level == "Medium: I want moderate returns but I don't want to be exposed to high levels of risk.":
        for key in med_risk_portfolio:
            med_risk_portfolio [key] *=int(investment_amount)
            portfolio_risk = 'medium'
        return med_risk_portfolio,portfolio_risk 
    else:     
        for key in high_risk_portfolio:
            high_risk_portfolio [key] *=int(investment_amount)
            portfolio_risk = 'high'
        return high_risk_portfolio,portfolio_risk 
    print(run_questions)
 

if __name__=='__main__':
    fire.Fire(run_questions)
    
