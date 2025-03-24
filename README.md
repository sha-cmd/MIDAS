Bienvenue sur le projet MIDAS !

Un exemple de pipeline moderne utilisant GCloud, Data Build Tools, Kubernetes, Docker et Terraform.

### Prérequis pour l'installation 
1. Un compte Google Cloud avec facturation activée :
   - Créer un projet dbtk8s
   - Activer les API Kubernetes Engine, Compute Engine, Container Registry
   - Créer une clé service account pour les credentials terraform et dbt
   - Lui donner les droits BigQuery Data Editor et Job User
   - Créer un registre de conteneur dbtk8sregistry
2. Les outils CLI suivant installés :
   - wsl ubuntu
   - gcloud
   - kubectl
   - terraform
   - docker
   - helm
3. Python 3.9 ou supérieur 
   - Créer un environnement virtuel 
   - Installer les dépendances requises dbt
   - Initialiser le projet dbt

4. Déployer l'infrastructure

```bash
terraform init
terraform apply
```

5. Configurez kubectl pour accéder à votre cluster :
```bash
gcloud container clusters get-credentials dbt-k8s-cluster  --region europe-west1 --project dbtk8s
```

6. Installer dbt Core pour BigQuery et tester la connexion :
```bash
pip install -r requirements
dbt debug
dbt run
```

7. Construction et Publication de l'Images :

Construisez et publiez votre image Docker dans Container Registry :

```bash
# Installer une dépendance gcloud
sudo apt install gke-gcloud-auth-plugin
# Se connecter au registre  
gcloud auth configure-docker europe-west1-docker.pkg.dev
# Créer l'image locale
docker build -t europe-west1-docker.pkg.dev/dbtk8s/dbtk8sregistry/dbt-core:latest .  
# Publier l'image sur le cloud
docker push europe-west1-docker.pkg.dev/dbtk8s/dbtk8sregistry/dbt-core:latest
```

8. Déploiement sur Kubernetes
```bash
# Créer un secret Kubernetes
kubectl create secret generic dbt-service-account --from-file=/home/romain/git/keys/dbtk8s.json
# Créer une ConfigMap pour la configuration de dbt
kubectl create configmap dbt-profiles --from-file=dbtk8s/profiles.yml
# Appliquer cette configuration de cronjob
kubectl apply -f dbt-cronjob.yml
```

9. Intégration CI/CD pour l'Automatisation

Pour automatiser CI/CD, nous configurons GitHub Actions.

Configurez les secrets GitHub nécessaires :
   - GCP_SA_KEY : Contenu de votre fichier de clé de compte de service
   - GCP_PROJECT_ID : ID de votre projet GCP

Ou bien par OIDC :
```bash
gcloud iam workload-identity-pools create "github" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --display-name="GitHub Actions Pool"
  
 
gcloud iam workload-identity-pools providers create-oidc "my-repo" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --workload-identity-pool="github" \
  --display-name="My GitHub repo Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository,attribute.repository_owner=assertion.repository_owner" \
  --attribute-condition="assertion.repository_owner == '${GITHUB_ORG}'" \
  --issuer-uri="https://token.actions.githubusercontent.com"
```

Pour obtenir la chaîne de workload_identity_provider :
```bash
gcloud iam workload-identity-pools providers describe "my-repo" \
--project="${PROJECT_ID}" \
--location="global" \
--workload-identity-pool="github" \
--format="value(name)"
```
La sortie doit ressembler à 'projects/123456789/locations/global/workloadIdentityPools/github/providers/my-repo'