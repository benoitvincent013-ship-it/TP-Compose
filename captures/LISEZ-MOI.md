# Captures d'écran — TP Compose

C'est ici que vous déposez vos preuves pour la remise.

> Les quatre captures ci-dessous sont **déjà fournies** (elles sont affichées
> dans le `README.md`). Vous pouvez les remplacer par les vôtres : gardez les
> mêmes noms de fichiers.

## Transparence sur les captures fournies

Les trois captures « terminal » (`1-docker-compose-ps.png`, `3-curl.png` et
`4-logs.png`) ont été générées à partir des **sorties réelles** des commandes,
recopiées dans une image (fond sombre, police monospace). Ce ne sont donc pas
des copies d'écran d'une fenêtre de terminal. Si votre enseignant exige une
capture native, refaites-la avec l'outil de capture de votre système et
écrasez le fichier en gardant le même nom.

La capture `2-navigateur.png` est, elle, une vraie capture du navigateur.

## Noms de fichiers attendus

| Fichier | Ce qu'il doit montrer |
| --- | --- |
| `1-docker-compose-ps.png` | La sortie de `docker compose ps` avec les 3 services |
| `2-navigateur.png` | La page du navigateur avec le message et le compteur |
| `3-curl.png` | La réponse de `curl` sur `/api/hello` |
| `4-logs.png` | Les logs de l'API (`docker compose logs api`) |

## Comment faire une capture

- **Windows** : `Windows + Maj + S` puis coller dans un fichier (Paint) et
  enregistrer en PNG dans ce dossier.
- **macOS** : `Cmd + Maj + 4`.
- **Linux** : l'outil « Capture d'écran » de votre bureau.

Ensuite, ajoutez les images dans le `README.md` à l'endroit prévu, par exemple :

```markdown
![docker compose ps](captures/1-docker-compose-ps.png)
```

> Astuce : gardez des images de moins de 1600 pixels de large, c'est plus
> confortable à lire sur GitHub.
