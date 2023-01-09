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
