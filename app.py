from flask import Flask,render_template,redirect,url_for,request
import stripe

app=Flask(__name__)
public_key='pk_test_6pRNASCoBOKtIshFeQd4XMUh'
stripe.api_key="sk_test_BQokikJOvBiI2HlWgH4olfQ2"

@app.route('/')

def index():
	return render_template('index.html',public_key=public_key)


@app.route('/thankyou')

def thankyou():
	return render_template('thankyou.html')

@app.route('/payment',methods=['POST'])
def payment():

	customer=stripe.customer.create(email=request.form['stripeEmail'],source=request.form['stripeToken'])
	charge=stripe.charge.create(customer=customer.id,amount=1000,curreny='usd',desciption='Donation')
	return redirect(url_for(thankyou))



if __name__=='__main__':
	app.run(debug=True)