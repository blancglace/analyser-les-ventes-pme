SELECT SUM(qte * prix) AS chiffre_affaires_total FROM ventes;

SELECT produit, 
       SUM(qte) AS total_quantite,
       SUM(qte * prix) AS chiffre_affaires_produit
FROM ventes 
GROUP BY produit;

SELECT region, 
       SUM(qte * prix) AS chiffre_affaires_region
FROM ventes 
GROUP BY region;