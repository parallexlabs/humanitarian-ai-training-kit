# Étude de cas 5 : Réponse du clavardbot aux bénéficiaires

<div class="synthetic-label"><strong>SYNTHETIC</strong> Transcription de clavardbot fictive pour la formation seulement.</div>

## Scénario

Votre organisation pilote un clavardbot destiné aux bénéficiaires pour les FAQ sur les heures d'inscription et les documents requis.

**Source FAQ approuvée F1 :** « L'inscription au site Sud est les mardis de 09 h 00 à 14 h 00. Apportez une pièce d'identité nationale ou une lettre de référence du partenaire Gamma. »

**Question du bénéficiaire :** « Puis-je m'inscrire lundi au site Nord? »

**Réponse du clavardbot :** « Oui. L'inscription au site Nord est ouverte du lundi au vendredi de 08 h 00 à 17 h 00. Apportez toute pièce d'identité avec photo. »

## Votre tâche (10 minutes)

1. Comparez la réponse à F1.
2. Qui pourrait être blessé?
3. La réponse du clavardbot doit-elle circuler sans examen humain obligatoire?
4. Quel suivi ou quelle règle d'arrêt recommanderiez-vous?

## Réponse modèle

| Élément | F1 | Clavardbot | Problème |
|---------|-----|------------|----------|
| Site | Sud seulement dans F1 | Nord | Mauvais emplacement |
| Jour | Mardi | Lundi-vendredi | Mauvais horaire |
| Documents | Pièce d'identité ou référence Gamma | Toute pièce avec photo | Mauvaises exigences |

**Préjudice :** Exclusion (voyage vers le mauvais site), refus de service (mauvais documents), perte de confiance.

**Décision :** Rouge pour envoi automatique. Examen humain requis pour toute réponse hors correspondance exacte avec la FAQ. Arrêter le pilote si les réponses de mauvais site dépassent le seuil convenu (p. ex. tout emplacement erroné confirmé).

## Erreurs courantes

- Supposer que le clavardbot utilise seulement le fichier FAQ sans tester les questions limites
- Mesurer la réussite par le volume de clavardages plutôt que par l'exactitude
- Voie d'escalade vers un travailleur social humain absente

## Principe enseigné

**Clavardbots humanitaires :** Les bénéficiaires peuvent traiter les réponses comme faisant autorité. De fausses informations logistiques causent de vrais préjudices. Tester et surveiller en continu.
