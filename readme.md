# PFE - Site web pour le magasin [L'Autre Monde](https://www.facebook.com/Magasin.L.Autre.Monde/)

## Le contexte
Actuellement, et depuis plusieurs années, son [site web](http://www.autre-monde.be/) est en travaux.
> Votre boutique spécialisée en jeux de société, jeux de cartes, jeux de figurines et jeux de rôle. Venez également partager votre passion dans notre salle de jeux.

Le magasin dispose d'une arrière-salle pour organiser des évènements tels que des tournois et découvertes de jeu, ou encore pour du jeu libre par les clients.

*L'Autre Monde* est une petite boutique située rue Hors Château, à Liège, tenue par seul son gérant, Joffrey Collard.
Étant seul, il est important de noter qu'il n'a pas beaucoup de temps pour maintenir un site. Avec cet aspect en tête, il sera important de réaliser une interface instinctive qui n'amènera pas à devoir entrer plusieurs fois les mêmes informations.

Le projet du site web de l'Autre Monde doit être séparé en deux parties, chacune avec ses objectifs :
- (La plus grande) Plateforme commercial : inventaire, précommande, compte client et paiement
- (La petite) Plateforme communautaire : compte client, calendrier, newsletter et réseaux sociaux (facebook, twitter)
Le site aura d'abord et avant tout un caractère commercial.

Le site web ne proposera pas directement d'achat de produits en ligne. Il sera plutôt une vitrine du catalogue de produits disponibles en magasin, avec une indication sur leurs disponibilités.

La seule partie qui comptera du paiement en ligne sera celle des précommandes.

Bien que le site ne présentera pas un panier d'achat, il sera important de garder en tête une possible futur implémentation d'achat en ligne dans la structure de base de données (liens entre les produits et clients, par exemple).

## Les rôles
Deux rôles différents utiliseront le site web : l'administrateur et le client.

### L'administrateur
L'administrateur sera toujours seul, et ne disposera de personne pour l'aider dans ses tâches.

Le catalogue du magasin ne peut objectivement pas être entièrement en ligne avec une seule personne qui y travaille à temps libre. Les différents produits seront ajoutés petit à petit, quand l'administrateur aura le temps de le faire.

#### Les produits du catalogue
L'administrateur devra pouvoir ajouter de nouveaux produits à son catalogue via une interface d'administration (décrite plus tard dans ce cahier des charges).

Lorsqu'il consultera son catalogue, il devra pouvoir indiquer un quantité de produits disponibles, et facilement pouvoir la modifier. Ces changements ne seront pas chiffrés pour les clients, mais plutôt donnés avec des indicatifs :
En stock / en rupture / épuisé / sur commande uniquement.

Les prix des produits ne seront pas visibles par les clients qui visitent le site, mais administrables par l'administrateur.

Une fiche technique de produit comptera plusieurs éléments administrables :
- Son nom
- Une / plusieurs images
- Descriptif
- Information sur le nombre de joueurs
- Catégories
- Sa disponibilité (non chiffré sur le frontend)
- Son prix (non affiché sur le frontend)
- Possibilité d'avoir une vidéo provenant de youtube
- Avis de clients

#### Types de produits
- Produit classique du catalogue
- Nouveauté du catalogue (mise en avant sur le site)
    - L'administrateur devra pouvoir indiquer une durée pendant laquelle le produit est considéré comme nouveauté
- Produit à venir (mise en avant sur le site)
- Précommande
    - Certains produits pourront être ajoutés comme *précommande*
    - Ces produits auront un prix, avec une indication de % de remise (comme il s'agit d'une précommande)
    - L'administrateur devra pouvoir voir en tout temps les produits qui ont été payés pour les précommandes. Ce système est indispensable pour que l'administrateur puisse connaître les quantités qu'il aura à commander
- Produit sur commande
    - Certains produits ne sont pas constamment en stock en magasin, mais disponibles sur demande uniquement. [Effectuer cette demande en ligne ? À revoir]

Lors de l'ajout de nouveautés, l'administrateur souhaite que son résumé soit automatiquement publiée sur Facebook et Twitter.

#### Le Calendrier
L'administrateur devra pouvoir gérer un calendrier d'évènements (journées découvertes, sorties de nouveautés, tournois, jeu libre, etc.). Ce calendrier sera consultable par les clients.

L'administrateur souhaiterait une création d'évènement automatisée avec Facebook.

L'administrateur aura la possibilité de créer des *semaines spéciales*, à thème, avec des produits mis de l'avant. Des réductions seront faites sur ces produits en magasin pour une durée déterminée par l'administrateur.

### Le client
Le client qui visite le site pourra être un habitué du magasin, tout comme une personne inconnue au milieu.

Le client pourra consulter les fiches de produits et les partager sur Facebook/Twitter.

Le client pourra parcourir les différents produits par plusieurs moyens :
- Champ de recherche
- Par catégories de produits
- Par nouveautés / à venir
- Par produits similaires (lors de la consultation d'une fiche de produit)

La client, inscrit ou pas, pourra s'inscrire à une newsletter générale.

Le client pourra se créer un compte sur le site, via lequel plusieurs options lui seront alors proposées :
- Il pourra faire des précommandes de produits, avec leurs paiement en ligne
- Commenter des produits
- Définir les catégories de newsletter auxquelles il est inscrit
- Définir son anniversaire (permettra de recevoir une remise en magasin notifiée par mail)
- Surveiller un produit pour être notifié par mail lors de son retour en stock.

Le client pourra consulter le calendrier des évènements à venir (et des évènements passé). Il pourra exporter le calendrier à son agenda.

## Aspects graphiques / visuels
Le site devra être sobre, et miser sur le visuel des produits. Il devra reprendre l'identité visuelle existante de L'Autre Monde.
Les nouveautés, produits à venir et précommandes devront être mis de l'avant sur le site.

### Sites web déjà existants, inspirations
Plusieurs magasins existants ont des sites web duquel il faudra s'inspirer, pour la forme (et la logique des catégorie) :
- [La Case Départ](https://www.casedepart.be/)
- [Philibert](https://www.philibertnet.com/)
- [Ludocortex](https://www.ludocortex.fr/index.cfm)

### Éléments essentiels
- Barre de recherche
    - Avec suggestions lors des entrées de l'utilisateur
- Implémentation de vidéo dans une fiche produit
- Possibilité d'avoir les avis des clients (connectés) sur les produits.

## Aspects techniques

### Langages et framework
*Front-End :* HTML, CSS, Javascript (*possible utilisation d'une library, à déterminer*)
*Back-End :* Python & Django.
J'aimerais réaliser le back-end avec Python pour plusieurs raisons. D'abord, par envie d'apprendre autre chose que ce qui a été vu en cours (PHP). Ensuite, cela posera un certain challenge technique que je souhaite réaliser. Finalement, après avoir survolé à quoi pouvait ressembler du templating avec Django, j'ai été conquise.

### La newsletter
La newsletter en place actuellement est à chaque fois créé de toutes pièces et envoyer manuellement à plusieurs *mailing lists* par le gérant (avec l'outil *Thunderbird*).
Ce qui sera à faire est une newsletter avec *MailChimp*, qui pourra procurer des statistiques au client ainsi qu'un système de doubles vérifications pour ceux qui s'y enregistrent.
Il sera intéressant de proposer aux utilisateurs plusieurs catégories de newsletter (par exemple: nouveauté / jeux de plateau / évènements et tournoi / etc.).

### Base de données
Une base de données est déjà existante pour une partie de l'inventaire du magasin, mais sa structure sera sans doute à revoir. J'en ajouterai plus ici quand j'aurai un retour par rapport à ce qui existe déjà.

### Les précommandes
Les précommandes devront être payables (au prix entier) en ligne, à venir chercher en magasin à partir de leur date de sortie. (Notification par mail)
*Renseignements à prendre sur les outils suivants :*
- [Mollie](https://www.mollie.com/en/)
- [Stripe](https://stripe.com/be)

### Autre
L'administrateur souhaite que les liens externes soient ouverts dans un nouvel onglet.

## Aspects logiques

### Panneau d'administration
Le panneau d'administration devra être sobre, clair, instinctif. Il doit rendre l'ajout de produit (tâche rébarbative) plus agréable et rapide.

### La logique des catégories
L'inventaire du magasin étant vaste, il sera important de créer des catégories de produits instinctives, logiques, et liées. Cela permettra aux utilisateurs de s'y retrouver, peu importe ce qu'ils cherchent.
*Les catégories sont en cours de réflexion, par moi, et par le gérant de L'Autre Monde. Un schéma sera créer quand une première version sera disponible*

### Le catalogue
Possibilité de surveiller un produit pour recevoir une notification par mail lorsqu'il est de nouveau en stock.
