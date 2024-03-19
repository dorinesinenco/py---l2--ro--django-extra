









## Django DRF + ( frontend ? ) / E-SHOP
   > idea
     1. main page -> product
      1.1. discount + countdown
      1.2. order product
      1.3. auth
      1.4. send automatic emails
      1.5. stripe payment link
      1.6. subscription 
      1.7. admin
      1.8. api Chat GPT (bot support) ?

   > tech
     1. DRF
        > urls   
        > views
        > serializers
        > models

        > auth
        > pagination
     
     2. ORM   
        > ?

     3. DB
        > postgresql  

     4. DOCKER
        > containers  

     5. FRONTEND
        > html + css + js     

     6. GIT
        > cli   












REST (REpresentational State Transfer), API (Application Programming Interface), JSON


                                              APP


     GET, POST          /admin/products <--> ProductAdminView 
                           |                             ^       + actions
                           |                             |       + model
                           |   endpoint (urls)           |       + fields: id, name, image, description
                           |   /                         +---+      |
                           |  /                              v      V
     GET req            /products   <--> ProductView <--> ProductSerializer <--> Product (resource)
                           |                   ^                    ^                ^
                           |                   |                    |                |
                           |              ListAPIView (views)  ModelSerializer       +---> Money 
                           |
                           |
          






                                                                 image: postgres:15.4-alpine3.18    
                                                                            |
                                                                            |
                                                            e_shop_pg       | 
                                                               |            |
docker-compose up ------> create & run containers  -----> +----+------------v--(container)---+ 
   ^                                                      | 
   |                                                      |   +---------(postgresql)--
   |                                                      |   |
   |                                                      |   |
   |                                                      |   |
   |                             app (django)  <----->  5777:5432 <----->
   |                                                      |   |
   |                                                      |   |
   |                                            /data <----------->    /var/lib/postgresql/data
 config                                                   |   
   |
docker-compose.yml   




app
  |
  +-- models.py
        |
        +--- class Product 
        |
        +--- class Money 






app
  |
  +-- models/
        |
       __init__.py <--- import ----+
        |                          |
        +-- Product.py             | 
        |    |                     | 
        |    +--- class Product ---+
        |
        +--- Money.py                .
             |                       |
             +--- class Money -------+









ERROR:  Reverse accessor 'Money.product'


 

Product
  .
  .
  .                     OneToOneField (bidirectional)
                             v
  price_standard = ... --------------> Money
                                         |
     <--------price_standard_reverse-----+
      
  price_discount = ... --------------> Money
                                         |
     <--------price_discount_reverse-----+








                                                           |
                              +-------------------------  /  <-> indexPage  <-> templates/public/index.html
                              |                            |
                              |                            |
                              v                            |
                  CLIENT (HTML,CSS,JS,...)                 |                      API (drf,postgres,...)
                                                           |                                                                    
                                                           |                                                                    
                                                           |                                                                    
            +-------------------------------+              |           ProductSerializer  
            |                               |              |                  v                                                  
            |                               | <----> GET  /products <-> ProductView <-> Product <-------> pg 
            |                               |              |                               |                               
            |                               |              |                               +-- Money                     
            |            PRODUCT            |              |                                                                    
            |                               |              |                                 
            |          PRESENTATION         |              |                                      
            |                               |              |                                      
            |                               |              |                                                                    
            |   (name, image, description,  |              |                                                                    
            |            price,...)         |              |                                                                    
            |                               |              |                                                                    
            |                               |              |                                                                    
            +-------------------------------+              |                                                                    
                                                           |                                                                    
            +-------------------------------+              |                 OrderSerializer                               
            |                               |              |                          v                                             
            |       PRODUCT ACTIONS         | <----> POST /orders/<uuid:id> <-> CreateOrderView <-> .post(...)      
            |                               |              |       ^                                   v
            |     (order, discount,...)     | product uuid --------+                  +----------      .post(...,**kwargs)
            |                               |              |                          |                .create(...,**kwargs)
            +-------------------------------+              |                          +---------->     .perform_create() 
                                                           |                                           .
                                                           |                                           .                         
                                                           |                                         Order <-> pg
                                                           |                                                                    
                                                           |                                                                    













        BROWSER 
           |
        window  <---- GET / <---- index.html
           |
           +--  <---- GET /static/public.css
           |
           +--- <---- GET /static/public.js
           |
+------>   +--- function loadProduct () {
|    
|              xhr = new XMLHttpRequest()
|               |
|              xhr.open("GET", "/products") 
|               |  
|              xhr.onload = function () {                  response JSON [...] / string
|                   response = xhr.responseText <-------------------------------------
|                   data = JSON.parse(response)
|                   console.log(data)                                                 API
|              }
|               |
|              xhr.send()  ------------------------------------> GET /products --->...
|          }
|    
+--------  loadProduct () 



























HW1: get to this point, draw diagrams: 
     1. call stack 
     2. database relationships: Order, OrderItem, Product
  



# APIView OOP logic





GenericAPIView     CreateModelMixin 
     |                 |     |
     |                 |     +-- create()
     |    +------------+     +-- post()
     v    v
CreateAPIView
     |
     v
CreateOrderView     










Order
  |
  +--- OrderItem #1
  |        |
  |        +--- id
  |        |
  |        +--- product -> Product 
  |        |
  |        +--- quantity
  |        |
  |        +--- order -> Order
  |
  +--- OrderItem #2
  .
  .












HW1:
   add +created field to order  
        ^
        |
      auto completed  











PUBLIC BUSINESS LOGIC (chain)      

  

 client 
   |
  1. views
   v
+-------+                        4. inputs data 
|       |                           |
|       |                           v
|<order> ---------> 3. show modal form -----> 5. order data post ----> API
+--^----+
   |
  2. clicks
   |
  client  











# REST API & relationships

  > separation of concerns


   SOLUTIONS:
      1. separate each request for each relationship

           a. GET /products
               Product {}

           b. GET /prices/{price_id}
               Money {}   

      2. use GRAPHQL queries  

               QUERY {
                   Product {
                      Price: {}
                   }
               }   

      3. refactor the API backend to get the compound

               GET /products
                     < Product {
                        Money {}
                     }











loadProduct ()
     |
     +--> GET /products ----> req ----> |
                                        |  <--> ...
                 res (JSON)             |
                +---------------------+ | 
                |
                v
            xhr.onload = function ()  {
               ...
               data = JSON.parse(response)
                 |
                 +----------------+
               ...                v
               +---> GET /money/{...} ----> req ----> | 
            }                                         |  <--> ...
                                                      |
                xhr.onload = function ()  { <-------- |
                   ...
                   data = JSON.parse(response)
                   ...
                }














# SPLITTING THE CODE / MODULARITY

- sub applications
- sub modules
- flat








app/
 |
 +--- urls.py 'admin/' <------+ include()
 |                            |
 +--- admin/                  |
 |     |                      |
 |     +- urls.py ------------+
 |     |     |
 |     |     +-- 'products/' < BREAD 
 |     |
 |     +- views.py
 |          |
 |          +-- ProductView
 |
 +--- client/ 
       |
       +- urls.py
       |
       +- views_api.py
       |        |
       |        +-- ...
       |
       +- views_pages.py
                |
                +-- ...


# MODELS

Payment
 + id
 + amount -------> Money
 + client -------> Client
 + order ------> Order
 + completed (ts)

Client
 + id 
 + name
 + email
 + password
 + phone
 + created (ts)
 + last_online (ts)

Order <----+
 + id      |
 + total -----------> Money
 + client ----------> Client 
 + state -------> "placed", "processed", ...
 + created (ts)
 + updated (ts)
           |
OrderItem  |
 + id      | 
 + order --+
 + product ---+
 + quantity   |
 + cost ------------> Money
              |
Product <-----+
 + id
 + name
 + image
 + description
 + available_quantity
 + created
 + updated

 + price_standard ----+
 + price_discount --+ |
                    | |
Money <-------------+<+
 + id 
 + amount
 + currency







------------------------------------+----+
                                    | x ------> deleteProduct(1)  
------------------------------------+----+ 
                                    | x ------> deleteProduct(2)
------------------------------------+----+ 
                                    | x ------> deleteProduct(3)
------------------------------------+----+ 


x---------------x---------------x---------------x----------------->
      click_0                        click_1  


------------------------------------+----+ 
                                    | x ------ 
------------------------------------+----+     \
                                    | x ---------> #deleteProductModal > confirm > deleteProduct(?)
------------------------------------+----+     /
                                    | x ------ 
------------------------------------+----+ 








REST API



/products ------------> Product



/money ------------> Money














                       +-----------------------------------+
                       |                                   |
GET /money/multi/<str:pks> ----------> MoneyBCustomView    |
                                           |               v
                                           +--> get(..., pks)
                                                           |
                                                           v
                                                     Custom QuerySet -------------- > db
                                                           |
                                                           v
                                                      Serialization(data)            
                                                           | 
                                                           |
                                                           v
                                          return
                                           | 
    <--------------------------------------+ 













QuerySet API

.action(field__operation, value)










## Auth 



                                 AUTH SCHEMES 
                                  |
                                  +-- basic
                                  |
                                  +-- session
                                  |
                                  +-- token  --+
                                  |            |
                                  .            | 
                                              /                        +---------- permitted ----------->
                         authentication      /                        / 
                        /                   /                        /
                                           v                        /
--------------------- req ------------->  req -> has permission? --+
                       ^                   |                        \
                       |                   +-- user                  \ 
                   credentials             +-- auth                   \
                                                                       +------------- forbidden -------->










               +----- templated based views
              /        |
             /         +-- session
--------->  + 
             \ 
              \
               +----- API views
                       |
                       +-- token









                    +----- admin -------->
                   /
                  /
                 /
----- req ----> + -------- client -------> 
                 \
                  \
                   \
                    +----- public ------->

















                      +--- retrieve order ----->
                     /
                    +---- auth <---- validate JWT
   credentials?    /                  1. order_Id
       V          /                   2. user_id
----- req -----> +                    3. expires
       |          \
       v           \
      [H]           +--- create order ------>
       |
     Authorization   
    'Token xyz......'








    req
------------>  /client/token --------+
                                     |
<------------------------------------+   







# JWT

1. Extend standard user MODEL

User 
  ^ 
  |
 inheritances (OOP, django) 
  |
Client <---- rel ---- Order 













User (auth_user)       Client (app_client)               
id  <-------+------------ user_ptr_id
name        |             phone
...         | 
            |
            +---------------+
                            |   Order (app_order)
                            |    id
                            |    ...
                            +--  client_id















Model (fields) <--------- token <------ verify --------- auth
         |
       1. custom: User/Client:  email or phone, uuid   ---> larger scope
       2. custom: Order: client_id and order.id        ---> narrower scope



















# User authentication strategy
       
      Client
       v
  CONFIRM ORDER 
       |
       +------------ req (AJAX) --------------> /orders/{product_id}
                     client_email                  |
                     client_phone                  |
                     ...                           |
                                                  view (CreateOrderView)
                                                   |
                                                   +---> find by email/number or create account  
                                                   |
                                                   +---> create Order and link it to this account
                                                   |
                                                   .
                                                   <---- here
                                                   .
        <------------- res ------------------------+                                            
                     1. order data
                     2. JWT (client_id) <--- Access Token






       payload = {
         'user_id': ....,
         'expires': ...,
       }
         |
         |
       encode <----- HS256  
         | ^
         | +----- SECRET_KEY
         v
        code
















JWT (with tokens)


  > Access Token
  > Refresh Token












# PAYMENT (gateway)

  > offsite (redirect)
  > onsite 











PAYMENT LINK


USER
 v
click
 v                    (key)   
PAY ------/pay ---------- python ---------------->  API stripe
                                                     |
                                                     v
                                                   price 
                                                     |
                                                     v
redirect <-------------------------------------------+ payment link     
   |
   +-------------------------------------------------+
                                                     |
                                                     v
                                                   form   
   +-------------------------------------------------+
   |                      redirect success
   v
 HW*: /api/confirm  