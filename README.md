Pour ajouter une nouvelle URL RSS au script existant sans modifier sa structure, voici les étapes à suivre :

1. Ouvrez le fichier contenant le script Python.

2. Localisez le dictionnaire `rss_urls` au début du script. Il contient toutes les URLs RSS actuelles.

3. Ajoutez une nouvelle paire clé-valeur à ce dictionnaire. La clé sera un identifiant unique pour le nouveau flux, et la valeur sera l'URL du flux RSS. Par exemple :
   ```python
   "nouveau_flux": "https://exemple.com/rss-feed",
   ```

4. Trouvez le dictionnaire des titres dans la boucle qui génère les fichiers HTML. Il ressemble à ceci :
   ```python
   title = {
       "cert": "CERT-FR",
       "developpez": "Developpez.com",
       # ... autres entrées ...
   }[key]
   ```

5. Ajoutez une nouvelle paire clé-valeur à ce dictionnaire pour votre nouveau flux. La clé doit correspondre à celle que vous avez ajoutée dans `rss_urls`, et la valeur sera le titre affiché pour ce flux. Par exemple :
   ```python
   "nouveau_flux": "Titre du Nouveau Flux",
   ```

6. Enfin, ajoutez un nouveau bloc `<div>` pour le lien vers votre nouveau flux dans la chaîne `index_html`. Cela se trouve vers la fin du script. Ajoutez une ligne comme celle-ci :
   ```html
   <div class="link">
       <a href="nouveau_flux.html">Flux RSS Titre du Nouveau Flux</a>
   </div>
   ```

7. Sauvegardez le fichier.

Après ces modifications, lorsque vous exécuterez le script, il générera automatiquement une nouvelle page HTML pour votre nouveau flux RSS et l'inclura dans l'index.
