# api-project-2
 ---
Over dit project.
Ik heb bij dit project gekozen voor een user die een product heeft met een manufactor. Dit houdt in dat elke user meerdere producten kan hebben met elk zijn eigen manufacotr. 
## Back-end API
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211388304-b800d7af-846e-4bb4-ba61-72be0c1bab48.png)

Dit is de pagina van de back-end van de API. Dit is een interactieve pagina die de API documentatie voorziet door Swagger UI. Deze pagina laat toe om alle POST, GET, PUT en DELETE te grbuiken.
## Authorize back-end
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211388710-187759ed-5b30-4082-8a9b-59a86c12444e.png)

Voor bepaalde dingen in de API moet je machteging hebben, omdat we niet willen dat jan en alleman van alles zouden kunnen aanpassen waar ze niet aan mogen komen.

![afbeelding](https://user-images.githubusercontent.com/91123119/211388913-1f30a71f-e4d9-4b5e-a341-e15b43f7e45b.png)
![afbeelding](https://user-images.githubusercontent.com/91123119/211388957-c425fcbc-4d1e-40c1-b2ac-aac6fae99cf6.png)
![afbeelding](https://user-images.githubusercontent.com/91123119/211388999-16d772e7-b2bd-482d-a7f0-4dac29ad9bdf.png)

Maar deze wekrt jammergenoeg niet. 
## Post token 
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211389184-1c9d443f-9088-4ffe-81d2-53d26cb5945b.png)
![afbeelding](https://user-images.githubusercontent.com/91123119/211389321-71ea0c08-f3e0-4049-83fe-2f005de0c552.png)

Zoals u ziet geeft dit een error. Maar de bedoeling is dat het een OAuth2 token terug geeft. Deze token zou gebruikt worden op de achtergrond om te controleren of de uitgevoerde actie van een grbuiker mag uitgevoerd worden of niet.
## Post  create user
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211389683-dbe80ef8-93bc-4c9d-ba5c-f47811bc5edb.png)
![afbeelding](https://user-images.githubusercontent.com/91123119/211389721-59d2d4f7-d147-4363-8c96-338a1b157610.png)

Via deze post kan er een nieuwe gebruik aangemaakt worden. De gebruiker moet een email addres en een paswoord opgeven. De API zal de user van een ID voorzien in de database.
## Get alle users
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211390048-2d450126-bff9-4741-ba55-d89f4098c7ca.png)

Via deze functie kunnen alle gebruikers in de database worden opgevraagd.
## Get user me
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211403380-203b5191-97d7-40f7-b3e9-f6eb532ba919.png)

Geeft de gebruik die op dit moment is ingelogd.
## Get user via user id
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211403584-a4fffb5b-a95c-4f90-b59f-9aa4a2527d19.png)

Hiermee kan je info over elke gebruiker opvragen aan de hand van de user id.
## Create products user
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211403888-159b10c5-3cc4-487b-aae7-c06170b8bb9a.png)

Hiermee kan je aan elke user producten toekennen. Door de user id te gebruiken.
## Create manufactors products
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211404168-9c4bd5e4-a3a4-49cf-8e41-ba9a3c4520a2.png)

Hiermee kan je aan elk product een manufactor naam toekennen. Dit door middel van de product id.
## Read products
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211404422-6f029e1f-33e1-4f88-9ea3-1a1d09a07400.png)

Hier kan je alle producten die in de database zit opvragen en weergeven.
## Read manufactors
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211404632-031aa000-2938-40ac-9a09-d319c5a26799.png)

Hier kan je alle manufactors die in de database zit opvragen en weergeven.
## update last manufactor
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211404792-9027a967-2936-43bc-9f2d-f1d6cde6a98b.png)

Hier kan je de laats toegevoegde manufactor aanpassen.
## delete manufactors
---
![afbeelding](https://user-images.githubusercontent.com/91123119/211404927-b23c039c-f7c7-49ac-abe2-bead6f16eadd.png)

Hier kan je de volledege database van manufactors leegmaken (alle data verwijderen).

# Postman request
---
Hier geef ik een korte demonstratie van de verschillende endpoints via postman.

## Post token 
![afbeelding](https://user-images.githubusercontent.com/91123119/211405710-14002403-af44-4f8b-9b04-ea76b0317823.png)

## Post create user
![afbeelding](https://user-images.githubusercontent.com/91123119/211406157-f773fbc0-d6e0-4e8f-b9c9-766693861828.png)
![afbeelding](https://user-images.githubusercontent.com/91123119/211406181-9b7e7561-dca3-410b-ad43-33c84ada72b9.png)

## Get alle users
![afbeelding](https://user-images.githubusercontent.com/91123119/211406233-6dd34a06-9367-473a-95e1-b5ddcdefeb6f.png)

## Get user me
![afbeelding](https://user-images.githubusercontent.com/91123119/211406443-a80fc1f8-5011-4c4a-aa9a-fc3144874a63.png)

## Get user via user id
![afbeelding](https://user-images.githubusercontent.com/91123119/211406776-4d007729-3958-4583-a69c-20a9e6d56566.png)

## Create products user
![afbeelding](https://user-images.githubusercontent.com/91123119/211406870-1f01454e-302b-4265-988b-0aa8d8b9f9b2.png)

## Create manufactors products
![afbeelding](https://user-images.githubusercontent.com/91123119/211406955-e7997108-fd7a-4291-896e-79f5ee73f255.png)

## Read products
![afbeelding](https://user-images.githubusercontent.com/91123119/211407015-363991b2-98f9-4cee-abc4-9f6223f492df.png)

## Read manufactors
![afbeelding](https://user-images.githubusercontent.com/91123119/211407161-a3f43e51-3257-4fa9-9ca0-1238ba3aa61f.png)

## update last manufactor
![afbeelding](https://user-images.githubusercontent.com/91123119/211407245-94d2c559-0c9e-49bf-86cc-bbc7adb8ea24.png)

## delete manufactors
![afbeelding](https://user-images.githubusercontent.com/91123119/211407311-886f89f7-4aab-439c-bd60-53366a101bc0.png)

# links 
---
Front-end link: [https://silly-tanuki-b187c7.netlify.app/]
Hosted API link: https://system-service-rubenpinxten.cloud.okteto.net/docs
