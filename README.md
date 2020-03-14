# desafio_troco

<p> A api recebe uma request POST com 2 parametros: preço e pagameneto em formato json. Exemplo {"preco": 34.56, "pgto: 50"}</p>

<p>Enviado uma request POST na url: http://127.0.0.1:8000/troco/</p>
<p>A url http://127.0.0.1:8000/lista_detalhes/  retona uma response GET listando os trocos. *O troco é fornecido com o menor número de notas e moedas possiveis</p>
<p>http://127.0.0.1:8000/troco_detalhe/4/ retorna um response GET com um troco especifico.</p>
<p>Formato dos dados de troco</p>

<p>  
  <li>{"_id": 4,</li>
  <li>"troco": 96.41,</li>
  <li>"nota_50_reais": 1,</li>
  <li>"nota_10_reais": 4,</li> 
  <li>"nota_5_reais": 1,</li> 
  <li>"nota_1_real": 1,</li>
  <li>"moeda_10_centavos": 4,</li> 
  <li>"moeda_1_centavo": 1}</li>  
</p>


<h4>Instalação das seguintes dependencias:<h4>
<p>asgiref==3.2.5<p>
<p>bson==0.5.8<p>
<p>dataclasses==0.6<p>
<p>Django==2.2.11<p>
<p>djangorestframework==3.11.0<p>
<p>djongo==1.3.1<p>
<p>pymongo==3.10.1<p>
<p>python-dateutil==2.8.1<p>
<p>pytz==2019.3<p>
<p>six==1.14.0<p>
<p>sqlparse==0.2.4<p>

