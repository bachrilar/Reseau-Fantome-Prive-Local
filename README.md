#RESEAU FANTOME PRIVE LOCAL


Réseau Fantôme Privé Local 

🎯 Contexte :
Dans un monde où la surveillance numérique est omniprésente, la nécessité de créer des réseaux de communication privés, discrets et éphémères devient cruciale. Votre mission est de concevoir un système de messagerie locale sécurisé entre deux stations Python. Ce système doit garantir la confidentialité des échanges, la suppression automatique des messages après lecture ou expiration, et intégrer des mécanismes de défense contre les tentatives d'accès non autorisées.

🛠️ Objectifs du projet :
Développer deux stations Python capables de :


Envoyer des messages chiffrés.


Recevoir et déchiffrer les messages.


Supprimer les messages après lecture ou après un délai défini.


Implémenter un protocole de communication local sécurisé (via fichiers partagés ou sockets).


Concevoir un système de gestion des erreurs et des tentatives d'accès échouées.


Option : intégrer une alerte en cas d'intrusion (par exemple via Telegram).



📂 Contraintes techniques :
Le projet doit être développé en Python 3.


L'échange des messages doit être local (pas de réseau Internet).


Les messages doivent être chiffrés avec une clé symétrique (utilisation de la bibliothèque cryptography).


Chaque station doit disposer d'un système de journalisation des tentatives d'accès.


Les messages doivent être supprimés après lecture ou après un délai d'expiration.


🔐 Critères de réussite :
Fonctionnalité complète de transmission et de suppression des messages.


Mise en place d'un chiffrement fiable.


Système de journalisation opérationnel.


Collaboration efficace entre les deux membres du binôme (répartition claire des tâches).


🎓 Livrables :
Scripts Python fonctionnels (station A et station B).


Documentation technique (format Markdown ou PDF) expliquant :


Le protocole de communication.


Le système de chiffrement.


Les mécanismes de suppression et de sécurité.


Journal des tentatives d'accès.


Présentation finale (optionnelle) expliquant le fonctionnement du projet et les choix techniques.




