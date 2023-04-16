import os
from datetime import date
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content
import yfinance as yf
from jinja2 import Template


def stockPrices():
  stocks = ['aapl','sbux','amzn','aos','cost','dhi','googl','iyt','low','panw','snps','uber','voo']
  results = []
  for stock in stocks:
    price = yf.Ticker(f"{stock}").info
    results.append(f"{stock.upper()} closed at {price['previousClose']} after opening at {price['open']}")

  return results
def sendEmail():
  # generate todays date for the email subject line
  today = date.today()
  todays_date = today.strftime("%B %d, %Y")
  prices = stockPrices()
  template = Template("""
      <font color="black"><strong>Good Afternoon Jovan. Here's what's going on today</strong> \
      <p>Here's how some of your favorite stocks opened the day:<br><ul>
      {% for price in prices %}
        <li>{{ price }}</li>
      {% endfor %}
      </ul></p></font>
  """)

  html_content = template.render(prices=prices)
  content = Content("text/html", html_content)
  message = Mail(
      from_email = 'jovan@jovannewland.net',
      to_emails= 'jovannewland@gmail.com',
      subject = f"Daily Digest for {todays_date}",
      html_content = content
  )

  # for stock_update in prices:
  #   message.add_content(str(f"<li>{stock_update}</li><br>"), mime_type='text/html')



  try:
      sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except Exception as e:
      print(e.message)

sendEmail()