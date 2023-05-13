/*
    Stripe core logic here comes from:
    https://stripe.com/docs/checkout/quickstart?lang=python
    https://stripe.com/docs/elements/appearance-api

    CSS from:
    
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
const appearance = {
    theme: 'stripe',
  
    variables: {
      colorPrimary: '#0570de',
      colorBackground: '#ffffff',
      colorText: '#30313d',
      colorDanger: '#df1b41',
      fontFamily: 'Ideal Sans, system-ui, sans-serif',
      spacingUnit: '3px',
      borderRadius: '5px',
    }
  };
  var card = elements.create('card', {appearance});
card.mount('#card-element');