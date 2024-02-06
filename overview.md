









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
       |                      |
       +- urls.py ------------+
       |     |
       |     +-- 'products/' < BREAD 
       |
       +- views.py
            |
            +-- ProductView


 