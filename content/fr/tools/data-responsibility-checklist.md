# Liste de contrôle sur la responsabilité des données pour les outils d'IA

Utiliser avant d'entrer des données dans un outil d'IA. S'aligne sur les [Orientations opérationnelles du CPI sur la responsabilité des données (2023)](https://centre.humdata.org/revised-iasc-operational-guidance-on-data-responsibility-in-humanitarian-action/) et les [Lignes directrices OCHA sur la responsabilité des données (janvier 2025)](https://centre.humdata.org/data-responsibility-guidelines-2025/).

![Cycle de vie de la responsabilité des données : planifier, évaluer, collecter, partager, analyser, stocker, clôturer](/assets/images/data-responsibility-lifecycle.svg)

**Équivalent textuel :** Planifier, évaluer, collecter, partager, analyser, stocker, clôturer. Appliquer à chaque étape avant d'utiliser l'IA sur des données opérationnelles. Voir les [aides visuelles](visual-aids.md).

## Avant de taper

- [ ] Je sais quelle classification de données s'applique (public, interne, confidentiel, opérationnel sensible, personnel).
- [ ] J'ai confirmé que cet outil est approuvé pour ce type de données dans mon organisation.
- [ ] J'utilise seulement le minimum de données nécessaire à la tâche.
- [ ] J'ai retiré les noms, coordonnées, numéros de dossier et emplacements précis lorsque ces éléments ne sont pas requis.
- [ ] J'ai vérifié si le fournisseur peut utiliser mon entrée pour l'entraînement du modèle ou la partager avec des tiers.
- [ ] Je sais où les données sont traitées et stockées (pays/région).

## Sauvegarde et protection

- [ ] Je ne saisis pas de notes de cas de protection de l'enfance, de dossiers de survivantes de VBG ou d'autres renseignements de protection très sensibles sauf approbation explicite pour cet outil et ce rôle.
- [ ] Je connais les points focaux de sauvegarde, PSEA et protection de mon organisation avant de gérer des divulgations ou des incidents.
- [ ] Si quelqu'un divulgue un préjudice en réunion ou dans le clavardage, je ferai une pause, éviterai les détails en plénière et référerai à ces points focaux (je ne enquêterai pas moi-même).
- [ ] Je prends au sérieux le risque de réidentification : des champs combinés peuvent identifier des personnes même sans noms complets.

Sources principales : [Manuel du CICR sur la protection des données (3e éd.)](../references.md); [Norme humanitaire fondamentale (2024)](../references.md) (Engagement 5). Ce document ne constitue pas un avis juridique.

## Pendant la tâche

- [ ] Je ne combine pas des ensembles de données de manière à réidentifier des personnes.
- [ ] Je ne téléverse pas de listes de bénéficiaires, de notes de cas de protection ou de dossiers médicaux sauf approbation explicite.
- [ ] J'ai conservé un registre de ce que j'ai entré et quand (sans copier le contenu sensible dans des notes non sécurisées).

## Après la sortie

- [ ] J'ai vérifié les affirmations importantes contre une source autorisée.
- [ ] J'ai vérifié les traductions pour des négations omises, des chiffres erronés ou un sens modifié.
- [ ] J'ai nommé qui approuvera avant toute utilisation opérationnelle.
- [ ] J'ai supprimé les copies inutiles de l'outil si la plateforme le permet.
- [ ] J'ai signalé un incident de données au contact de mon organisation si des données sensibles ont été entrées par erreur.

## Signaux d'alerte : ne procédez pas

| Signal d'alerte | Pourquoi c'est important |
|-----------------|--------------------------|
| Numéros de téléphone de bénéficiaires dans un clavardage IA public | Réidentification et atteinte à la vie privée |
| Emplacements d'abris liés à des personnes nommées | Risque pour la sécurité |
| Détails financiers des donateurs | Risque de confidentialité et de fraude |
| Fournisseur non vérifié avec rétention des données floue | Perte de contrôle sur les données sensibles |
| Détails VBG ou protection de l'enfance dans des outils non approuvés | Préjudice grave et violation de politique |

## Besoin d'aide?

Escalader vers votre responsable de la vie privée, conseiller en protection, point focal de sauvegarde ou PSEA, ou équipe de sécurité informatique. Les décisions ambre et rouge ne reposent pas seulement sur le jugement individuel; elles nécessitent un examen organisationnel.

Voir le [module de sauvegarde de la séance 3](../sessions/session-03-governance/safeguarding-module.md) et le [guide d'animation](facilitator-guide.md) pour l'escalade en salle de formation.
