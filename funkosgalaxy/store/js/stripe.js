// stripe.js

<script src="https://js.stripe.com/v3/"></script>
<script>
  // Configure o Stripe com sua chave pública
  var stripe = Stripe('pk_test_51NalRtA60iQHN3CgZCsz52cwwNRJdfREiHy9aIG76bM31on6eAXPXJVancVNIVfbk6wNfBRu66sjV5TrGX5eEZfO00OCMCjIpA');

  // Crie um elemento do cartão de crédito
  var elements = stripe.elements();
  var cardElement = elements.create('card');

  // Adicione o elemento do cartão de crédito ao formulário
  cardElement.mount('#card-element');

  // Lide com a submissão do formulário
  var form = document.getElementById('payment-form');
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    stripe.createPaymentMethod({
      type: 'card',
      card: cardElement
    }).then(function(result) {
      if (result.error) {
        // Lidar com erros do Stripe
        var errorElement = document.getElementById('card-errors');
        errorElement.textContent = result.error.message;
      } else {
        // Envie o ID do pagamento ao seu servidor Django para processar o pagamento
        fetch('/process_payment/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
          },
          body: JSON.stringify({ payment_method_id: result.paymentMethod.id })
        }).then(function(response) {
          // Lidar com a resposta do servidor após o processamento do pagamento
        });
      }
    });
  });
</script>
