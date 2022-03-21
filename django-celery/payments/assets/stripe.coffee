$processing_popup = $ '.payment-processing-popup'

$.fn.stripe = () ->
  this.each () ->
    $this = $ this
    handler = StripeCheckout.configure
      key: Project.helpers.stripe_pk()  # defined in base.html
      image: 'https://stripe.com/img/documentation/checkout/marketplace.png'  # please change
      locale: 'auto'
      token: (token) ->  # POST server with token and payment params when stripe allowed the transaction
        $processing_popup.modal 'show'
        $.post '/payments/process/',
          stripeToken: token.id
          amount: $this.data 'amount'
          product_type: $this.data 'product-type'
          product_id: $this.data 'product-id'
          currency: $this.data 'currency'
        , (response) ->
          $processing_popup.modal 'hide'
          window.location.href = response.result

      $this.on 'click', (e) ->  # open stripe form and request a payment
        handler.open
          name: $this.data 'name'
          email: $this.data 'email'
          amount: $this.data 'stripe-amount'
          currency: $this.data 'currency'
          description: $this.data 'description'
          locale: 'auto'
          zipCode: false

        e.preventDefault()

$.getScript 'https://checkout.stripe.com/checkout.js', () ->
  $('.btn-stripe').stripe()
