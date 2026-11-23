# TP COMPOSE — image du front (Nginx + une page HTML)
FROM nginx:alpine

# La configuration de Nginx : servir la page et transmettre /api/ à l'API.
COPY nginx.conf /etc/nginx/conf.d/default.conf

# La page affichée dans le navigateur.
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
