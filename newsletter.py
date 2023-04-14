import os
from datetime import date
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import yfinance as yf


def stockPrices():
  stocks = ['aapl','sbux','amzn','aos','cost','dhi','googl','iyt','low','panw','snps','uber','voo']
  results = []
  for stock in stocks:
    price = yf.Ticker(f"{stock}").info
    results.append(f"{stock.upper()} closed at {price['previousClose']} after opening at {price['open']}")

  return results

# generate todays date for the email subject line
today = date.today()
todays_date = today.strftime("%B %d, %Y")
stockprices = []

message = Mail(
    from_email = 'jovan@jovannewland.net',
    to_emails= 'jovannewland@gmail.com',
    subject = f"Daily Digest for {todays_date}",
    html_content=f"<strong>Good Afternoon Jovan. Here's what's going on today</strong> \
    <p>Here's how some of your favorite stocks opened the day:<br> \
    {stockPrices()[0]}<br> {stockPrices()[1]}<br> {stockPrices()[2]}<br> {stockPrices()[3]}<br> {stockPrices()[4]}<br> {stockPrices()[5]}<br> \
    {stockPrices()[6]}<br> {stockPrices()[7]}<br> {stockPrices()[8]}<br> {stockPrices()[9]}<br> {stockPrices()[10]}<br> {stockPrices()[11]}<br> {stockPrices()[12]}</p>"
)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)